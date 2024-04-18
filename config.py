# TEAM DAXX ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "20136640"
    API_HASH = "32fa482ffd34ceefec26b7ccd73c4fbb"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://DxLEGEND143:DxLEGEND143@dxlegend.oztipqk.mongodb.net/?retryWrites=true&w=majority&appName=DxLEGEND"
    START_PIC = "https://te.legra.ph/file/92f53162869ce9701386e.jpg"
    SUDOERS = filters.user(["6458155947"])
