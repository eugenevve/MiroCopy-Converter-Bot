from bot.locales import en, ru


def get_texts(language_code: str | None):
    if language_code and language_code.lower().startswith("ru"):
        return ru
    return en
