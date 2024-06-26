from configs.logger import init_logger
from fastapi import APIRouter, HTTPException
from schemas.nltk import (
    EntitiesRecognizeOutputSchema,
    TaggingOutputSchema,
    TextDataInputSchema,
    TokenizeOutputSchema,
)
from services.nlp import NLPService

logger = init_logger(__file__)
router = APIRouter(prefix="/nltk", tags=["nltk"])


@router.post("/tokenize", response_model=TokenizeOutputSchema)
async def tokenize(text_data: TextDataInputSchema) -> TokenizeOutputSchema:
    try:

        return await NLPService.tokenize(text_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/pos_tag", response_model=TaggingOutputSchema)
async def pos_tagging(data: TextDataInputSchema) -> TaggingOutputSchema:
    try:
        return await NLPService.pos_tagging(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/ner", response_model=EntitiesRecognizeOutputSchema)
async def named_entity_recognition(
    data: TextDataInputSchema,
) -> EntitiesRecognizeOutputSchema:
    try:

        return await NLPService.named_entity_recognition(data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
