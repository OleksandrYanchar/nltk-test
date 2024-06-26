import pytest
from schemas.nltk import (
    EntitiesRecognizeOutputSchema,
    EntitySchema,
    TaggingOutputSchema,
    TextDataInputSchema,
    TokenizeOutputSchema,
)
from services.nlp import NLPService


@pytest.mark.asyncio
async def test_tokenize():
    input_data = TextDataInputSchema(
        text="#Bitcoin exchange balances are hitting six-year lows, but some analysts argue this metric is overrated."
    )
    result = await NLPService.tokenize(input_data)
    assert result == TokenizeOutputSchema(
        result=[
            "#",
            "Bitcoin",
            "exchange",
            "balances",
            "are",
            "hitting",
            "six-year",
            "lows",
            ",",
            "but",
            "some",
            "analysts",
            "argue",
            "this",
            "metric",
            "is",
            "overrated",
            ".",
        ]
    )


@pytest.mark.asyncio
async def test_pos_tagging():
    input_data = TextDataInputSchema(
        text="""
Coinbase CEO says 'owning #Bitcoin is pro-America.'
'It may extend the American 🇺🇸 experiment, and western civilization along with it.'
"""
    )
    result = await NLPService.pos_tagging(input_data)
    assert result == TaggingOutputSchema(
        result=[
            ["Coinbase", "NNP"],
            ["CEO", "NNP"],
            ["says", "VBZ"],
            ["'owning", "VBG"],
            ["#", "#"],
            ["Bitcoin", "NNP"],
            ["is", "VBZ"],
            ["pro-America", "JJ"],
            [".", "."],
            ["'", "''"],
            ["'It", "POS"],
            ["may", "MD"],
            ["extend", "VB"],
            ["the", "DT"],
            ["American", "JJ"],
            ["🇺🇸", "NNP"],
            ["experiment", "NN"],
            [",", ","],
            ["and", "CC"],
            ["western", "JJ"],
            ["civilization", "NN"],
            ["along", "IN"],
            ["with", "IN"],
            ["it", "PRP"],
            [".", "."],
            ["'", "''"],
        ]
    )


@pytest.mark.asyncio
async def test_named_entity_recognition():
    input_data = TextDataInputSchema(text="Barack Obama was born in Hawaii.")
    result = await NLPService.named_entity_recognition(input_data)

    expected_entities = [
        EntitySchema(entity="Barack", type="PERSON"),
        EntitySchema(entity="Obama", type="PERSON"),
        EntitySchema(entity="Hawaii", type="GPE"),
    ]
    expected_result = EntitiesRecognizeOutputSchema(entities=expected_entities)

    # Detailed comparison
    assert len(result.entities) == len(expected_result.entities)
    for res_entity, exp_entity in zip(result.entities, expected_result.entities):
        assert res_entity.entity == exp_entity.entity
        assert res_entity.type == exp_entity.type
