from typing import List
from aiogram import Bot


async def download_images(
    bot: Bot,
    file_ids: List[str],
    user_id: int,
    operation_id: str,
) -> List[str]:
    paths: List[str] = []

    for index, file_id in enumerate(file_ids, start=1):
        path = f"temp_{user_id}_{operation_id}_{index}.jpg"

        file = await bot.get_file(file_id)
        await bot.download_file(file.file_path, path)

        paths.append(path)

    return paths
