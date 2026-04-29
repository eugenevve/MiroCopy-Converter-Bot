import configparser

# Подключение к конфигурационному файлу
config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8")

API_TOKEN = config["token"]["bot"]
