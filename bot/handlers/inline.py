from aiogram import Router
from aiogram.utils.deep_linking import create_start_link
from aiogram.types import InlineQuery, InlineQueryResultArticle, InlineQueryResultsButton, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
from bot.locales.index import get_texts
from bot.utils.enums import CommandArgs


router = Router()


@router.inline_query()
async def show_modes(query: InlineQuery):
    lang = query.from_user.language_code
    texts = get_texts(lang)

    public_image = "https://raw.githubusercontent.com/eugeneviktorov/MiroCopy-Converter-Bot/main/assets/images"
    image_link = await create_start_link(query.bot, CommandArgs.IMAGE, encode=False)
    txt_link = await create_start_link(query.bot, CommandArgs.TXT, encode=False)

    switch_button = InlineQueryResultsButton(
        text=texts.INLINE_MAIN_BUTTON,
        start_parameter=CommandArgs.MAIN
    )

    results = [
        InlineQueryResultArticle(
            id=CommandArgs.IMAGE,
            title=texts.BTN_IMAGE_TO_PDF,
            description=texts.INLINE_DESCRIPTION_IMAGE,
            thumbnail_url=f"{public_image}/inline-image.png",

            input_message_content=InputTextMessageContent(
                message_text=f"<b>{texts.BTN_IMAGE_TO_PDF}</b>\n\n{texts.INLINE_MESSAGE_IMAGE}"
            ),
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(
                    text=texts.INLINE_BUTTON_CONVERT,
                    url=image_link
                )]
            ])
        ),

        InlineQueryResultArticle(
            id=CommandArgs.TXT,
            title=texts.BTN_TXT_TO_PDF,
            description=texts.INLINE_DESCRIPTION_TXT,
            thumbnail_url=f"{public_image}/inline-txt.png",

            input_message_content=InputTextMessageContent(
                message_text=f"<b>{texts.BTN_TXT_TO_PDF}</b>\n\n{texts.INLINE_MESSAGE_TXT}"
            ),
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(
                    text=texts.INLINE_BUTTON_CONVERT,
                    url=txt_link
                )]
            ])
        )
    ]

    await query.answer(
        results=results,
        button=switch_button,
        cache_time=0,
        is_personal=True
    )
