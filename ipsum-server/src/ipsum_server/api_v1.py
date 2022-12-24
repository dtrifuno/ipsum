from typing import Any, Optional

import fastapi
from ipsum import LanguageModel
from ipsum import load_all_models
from ipsum import SupportedLanguage

from ipsum_server.limiter import limit
from ipsum_server.limiter import limiter

api_v1 = fastapi.FastAPI(
    title="Ipsum",
    version="1.0",
    contact={
        "name": "Darko Trifunovski",
        "url": "https://trifunovski.me/",
        "email": "darko@trifunovski.me",
    },
    license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
)

models = load_all_models()


def _get_models() -> dict[SupportedLanguage, LanguageModel]:
    return models


@api_v1.get("/health_check")
@limiter.exempt
async def health_check() -> Optional[str]:
    """Returns a 200 OK response with no content in the body."""
    return None


@api_v1.get("/supported_languages")
@limiter.exempt
async def supported_languages() -> dict[str, Any]:
    """Returns a list of objects describing languages currently supported by Ipsum."""
    return {
        "supported_languages": [
            {"name": lang.name, "code": lang.value} for lang in SupportedLanguage
        ]
    }


@api_v1.get("/generate_words/{lang}")
@limiter.limit(limit)
async def generate_words(
    request: fastapi.Request,
    lang: SupportedLanguage = fastapi.Path(
        description="ISO 639-1 code of the language."
    ),
    count: int = fastapi.Query(
        description="Number of words to generate.", ge=1, le=500, default=20
    ),
    models: dict = fastapi.Depends(_get_models),
) -> list[str]:
    """Returns a number of randomly generated words resembling target language."""
    model: LanguageModel = models[lang]
    return model.generate_words(count)


@api_v1.get("/generate_sentences/{lang}")
@limiter.limit(limit)
async def generate_sentences(
    request: fastapi.Request,
    lang: SupportedLanguage = fastapi.Path(
        description="ISO 639-1 code of the language."
    ),
    count: int = fastapi.Query(
        description="Number of sentences to generate.", ge=1, le=150, default=5
    ),
    models: dict = fastapi.Depends(_get_models),
) -> list[str]:
    """Returns a number of randomly generated sentences resembling target language."""
    model: LanguageModel = models[lang]
    return model.generate_sentences(count)


@api_v1.get("/generate_paragraphs/{lang}")
@limiter.limit(limit)
async def generate_paragraphs(
    request: fastapi.Request,
    lang: SupportedLanguage = fastapi.Path(
        description="ISO 639-1 code of the language."
    ),
    count: int = fastapi.Query(
        description="Number of paragraphs to generate.", ge=1, le=50, default=5
    ),
    models: dict = fastapi.Depends(_get_models),
) -> list[str]:
    """Returns a number of randomly generated paragraphs resembling target language."""
    model: LanguageModel = models[lang]
    return model.generate_paragraphs(count)
