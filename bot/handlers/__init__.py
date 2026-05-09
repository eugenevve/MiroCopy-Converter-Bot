from aiogram import Router
from .common import router as common_router
from .photo import router as photo_router

def get_handlers_router() -> Router:
    main_router = Router()

    main_router.include_router(common_router)
    main_router.include_router(photo_router)
    
    return main_router
