import base64
import random
import time
from os import getenv

import msgpack
import requests
import xxtea


REQUEST_KEY = "H#ufB@O1G5Rxnkm#hd@k76"
RESPONSE_KEY = "0C9FEBHwd*qsd@k128l"
PARSE_URL = "https://api.xiaoxiaobite.com/api/v3/parse/web/single-source?app_key=web_token"


def make_parse_payload(url: str):
    return {
        "lan": "zh_Hans",
        "platform": "web",
        "package": "longmao_web",
        "nonce": str(random.random()),
        "time_zone": -480,
        "time_stamp": int(time.time()),
        "logined": True,
        "token": getenv("LONGMAO_TOKEN"),
        "debug": False,
        "content": url,
    }


def encrypt_data(data) -> str:
    packed = msgpack.packb(data)
    encrypted = xxtea.encrypt(packed, REQUEST_KEY.encode("utf-8"))
    return base64.b64encode(encrypted).decode("utf-8")


def decrypt_response(text: str):
    binary = base64.b64decode(text)
    decrypted = xxtea.decrypt(binary, RESPONSE_KEY.encode("utf-8"))
    return msgpack.unpackb(decrypted, raw=False)


def parse_content(url: str):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
        ),
        "Content-Type": "text/plain;charset=UTF-8",
    }

    payload = make_parse_payload(url)

    response = requests.post(
        PARSE_URL,
        data=encrypt_data(payload),
        headers=headers,
        timeout=30,
    )

    return decrypt_response(response.text)
