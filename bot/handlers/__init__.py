from aiogram import Router
from .common import router as common_router
from .image import router as image_router
from .txt import router as txt_router


def get_handlers_router() -> Router:
    main_router = Router()

    main_router.include_router(common_router)
    main_router.include_router(image_router)
    main_router.include_router(txt_router)
    
    return main_router
