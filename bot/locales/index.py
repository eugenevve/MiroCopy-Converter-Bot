from bot.locales import en, ru, es, pt, id, ar


def get_texts(language_code: str | None):
    if not language_code:
        return en

    code = language_code.lower()

    if code.startswith("ru"):
        return ru
    if code.startswith("es"):
        return es
    if code.startswith("pt"):
        return pt
    if code.startswith("id"):
        return id
    if code.startswith("ar"):
        return ar
    return en
