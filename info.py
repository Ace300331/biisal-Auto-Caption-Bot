# (c) @biisal
from os import getenv
import re

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "929048904"))
API_ID = int(getenv("API_ID", "23790461"))
API_HASH = str(getenv("API_HASH", "2d0a7fb85f06246e93948bf7afc05fb3"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "8140367385:AAEkE6mkxoPwUTRON1XJY4OD9hYG9JMCvwA"))
MONGO_DB = str(
    getenv(
        "MONGO_DB",
        "mongodb+srv://Rax:amit7001@cluster0.cintttk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    )
)
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b><a href='telegram.me/Ace_Files'>{file_name} Telegram : @Ace_Files\n\nForward the file before Downloading.</a></b>",
    )
)
