from enum import Enum, StrEnum


class Command(str, Enum):
    START = "start"


class Locales(str, Enum):
    EN = "en"
    RU = "ru"
    ES = "es"
    PT = "pt"
    ID = "id"
    AR = "ar"


class FileDocumentsExtensions(str, Enum):
    PDF = "pdf"
    TXT = "txt"


class FileImageExtensions(str, Enum):
    PNG = "png"
    JPG = "jpg"
    JPEG = "jpeg"

    HEIC = "heic"
    TIF = "tif"
    TIFF = "tiff"

    BMP = "bmp"
    ICO = "ico"
    PSD = "psd"

    JP2 = "jp2"
    AVIF = "avif"
    APNG = "apng"

    @classmethod
    def image_extensions(cls):
        return [
            cls.PNG, cls.JPG, cls.JPEG,
            cls.HEIC, cls.TIF, cls.TIFF,
            cls.BMP, cls.ICO, cls.PSD,
            cls.JP2, cls.AVIF, cls.APNG,
        ]


class FileImageExtensionsUppercase(str, Enum):
    JPEG = "JPEG"


class CommandArgs(StrEnum):
    MAIN = "main"
    IMAGE = "image"
    TXT = "txt"
