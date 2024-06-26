from configs.logger import init_logger
from fastapi import HTTPException
from nltk.chunk import ne_chunk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from schemas.nltk import (
    EntitiesRecognizeOutputSchema,
    EntitySchema,
    TaggingOutputSchema,
    TextDataInputSchema,
    TokenizeOutputSchema,
)

logger = init_logger(__file__)


class NLPService:

    @staticmethod
    async def tokenize(text_data: TextDataInputSchema) -> TokenizeOutputSchema:
        try:
            # Tokenize the input text into words
            text = text_data.text
            result = word_tokenize(text)
            return TokenizeOutputSchema(result=result)
        except Exception as e:
            logger.error(f"Error in tokenize: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def pos_tagging(data: TextDataInputSchema) -> TaggingOutputSchema:
        try:
            # Tokenize the input text into words
            tokens = word_tokenize(data.text)
            # Generate POS tags for tokenized words
            tagged_tokens = pos_tag(tokens)
            return TaggingOutputSchema(result=tagged_tokens)
        except Exception as e:
            logger.error(f"Error in pos_tagging: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def named_entity_recognition(
        data: TextDataInputSchema,
    ) -> EntitiesRecognizeOutputSchema:
        try:
            # Tokenize the input text into words
            tokens = word_tokenize(data.text)
            # Tag tokens with their part of speech
            tagged_tokens = pos_tag(tokens)
            # Perform named entity recognition
            named_entities_tree = ne_chunk(tagged_tokens)

            # Extract named entities and their types from the tree
            named_entities = []
            for chunk in named_entities_tree:
                if hasattr(chunk, "label"):
                    entity = " ".join(c[0] for c in chunk)
                    entity_type = chunk.label()
                    named_entities.append(EntitySchema(entity=entity, type=entity_type))

            return EntitiesRecognizeOutputSchema(entities=named_entities)
        except Exception as e:
            logger.error(f"Error in named_entity_recognition: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))
