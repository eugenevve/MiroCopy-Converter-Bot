import img2pdf


def images_to_pdf(image_paths: list[str], output_path: str) -> None:
    if not image_paths:
        raise ValueError("image_paths is empty")

    pdf_bytes = img2pdf.convert(image_paths)

    with open(output_path, "wb") as f:
        f.write(pdf_bytes)
