import os
import img2pdf
from PIL import Image
from pillow_heif import register_heif_opener

from bot.utils.enums import FileImageExtensions, FileImageExtensionsUppercase


register_heif_opener()


def images_to_pdf(image_paths: list[str], output_path: str) -> None:
    if not image_paths:
        raise ValueError("image_paths is empty")

    processed_paths = []
    converted_suffix = f"_converted.{FileImageExtensions.JPG.value}"

    try:
        for path in image_paths:
            ext_str = path.lower().split('.')[-1]
            try:
                ext = FileImageExtensions(ext_str)
            except ValueError:
                ext = None

            if ext in FileImageExtensions.image_extensions():
                img = Image.open(path)
                rgb_img = img.convert('RGB')
                new_path = path.rsplit('.', 1)[0] + converted_suffix
                rgb_img.save(new_path, FileImageExtensionsUppercase.JPEG)
                processed_paths.append(new_path)
            else:
                processed_paths.append(path)

        pdf_bytes = img2pdf.convert(processed_paths)
        with open(output_path, "wb") as f:
            f.write(pdf_bytes)

    finally:
        for p in processed_paths:
            if converted_suffix in p and os.path.exists(p):
                os.remove(p)
