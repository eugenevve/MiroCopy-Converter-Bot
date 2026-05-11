from aiogram.fsm.state import StatesGroup, State


class ConvertStates(StatesGroup):
    main_menu = State()
    convert_for_images = State()
    convert_for_txt = State()
