from typing import Dict

SupportedLanguage = str


MESSAGES: Dict[SupportedLanguage, Dict[str, str]] = {
    "ru": {
        "start": "Пожалуйста, пришлите фото для конвертации в PDF!",
        "processing_error": "Произошла ошибка при обработке фото: {error}",
        "unsupported_content": (
            "Я умею конвертировать только изображения в PDF. "
            "Отправьте одно фото или альбом из нескольких фото в одном сообщении."
        ),
    },
    "en": {
        "start": "Please send a photo to convert it to PDF!",
        "processing_error": "An error occurred while processing the photo: {error}",
        "unsupported_content": (
            "I can convert only images to PDF. "
            "Send one photo or an album with several photos in one message."
        ),
    },
}


def resolve_language(language_code: str | None) -> SupportedLanguage:
    if language_code and language_code.lower().startswith("ru"):
        return "ru"
    return "en"


def get_message(key: str, language_code: str | None) -> str:
    lang = resolve_language(language_code)
    return MESSAGES.get(lang, MESSAGES["en"]).get(key, key)
