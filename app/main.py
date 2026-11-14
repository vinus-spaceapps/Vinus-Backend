"""Vinus API — 와인 기후 추세 탐정.

실행:  uvicorn app.main:app --reload --port 8000
문서:  http://localhost:8000/docs
"""

from __future__ import annotations

import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

load_dotenv()

from . import catalog  # noqa: E402
from .ai import insight_agent, llm, variable_agent  # noqa: E402
from .analysis import AnalysisError, AnalyzeRequest, run_analysis  # noqa: E402

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Vinus API", version="0.1.0", description="와인 기후 추세 탐정 — NASA Space Apps 2026")

origins = [o.strip() for o in os.getenv("VINUS_CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(",") if o.strip()]
# 지표 목록이 커서(약 1MB) 압축해서 보냅니다.
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health() -> dict:
    return {"ok": True, "ai": llm.status()}


@app.get("/api/variables")
def variables() -> dict:
    return {
        "categories": catalog.CATEGORIES,
        "families": catalog.FAMILIES,
        "variables": [catalog.public_indicator(m) for m in catalog.indicators().values()],
    }


@app.get("/api/regions")
def regions() -> list:
    return catalog.regions()


@app.post("/api/analyze")
def analyze(req: AnalyzeRequest) -> dict:
    try:
        return run_analysis(req)
    except AnalysisError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@app.post("/api/ai/variables")
def ai_variables(req: variable_agent.VariableChatRequest) -> dict:
    return variable_agent.reply(req)


@app.get("/api/ai/decisions")
def ai_decisions() -> list:
    return insight_agent.DECISIONS


@app.post("/api/ai/insight")
def ai_insight(req: insight_agent.InsightRequest) -> dict:
    try:
        return insight_agent.respond(req)
    except AnalysisError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
