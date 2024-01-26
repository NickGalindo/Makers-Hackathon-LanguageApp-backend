from typing import Dict, List
from fastapi import APIRouter, Request

from endpoints.models import FrCard, EnCard
from endpoints import service

router = APIRouter()

@router.post("/frError")
async def frError(request: Request, card: FrCard) -> Dict:
    service.frError(card, request.app.state.mongoConnection)

    return {"status": "success"}

@router.post("/frCorrect")
async def frCorrect(request: Request, card: FrCard) -> Dict:
    service.frCorrect(card, request.app.state.mongoConnection)

    return {"status": "success"}


@router.post("/enError")
async def enError(request: Request, card: EnCard) -> Dict:
    service.enError(card, request.app.state.mongoConnection)

    return {"status": "success"}

@router.post("/enCorrect")
async def enCorrect(request: Request, card: EnCard) -> Dict:
    service.enCorrect(card, request.app.state.mongoConnection)

    return {"status": "success"}


@router.post("/enRecommend")
async def enRecommend(request: Request) -> List:
    return service.enRecommend(request.app.state.mongoConnection)

@router.post("/frRecommend")
async def frRecommend(request: Request) -> List:
    return service.frRecommend(request.app.state.mongoConnection)

