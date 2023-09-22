import base64
from io import BytesIO
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image

app = FastAPI()

def open_image2base64(path):
    with open(path, "rb") as img_file:
        image_str = base64.b64encode(img_file.read()).decode()
    return image_str

def base64_to_pillow_image(base64_image_string: str) -> Image:
    """
    Convert a base64 encoded image string to a Pillow Image object.

    :param base64_image_string: The base64 encoded image string.
    :return: A Pillow Image object.
    """
    image_bytes = base64.b64decode(base64_image_string)
    return Image.open(BytesIO(image_bytes))

@app.post("/generate_image/")
async def generate_image(data: dict):
    # この部分に、jsonまたは辞書データをもとに画像を生成するコードを書きます。
    # 今回は仮の例として、BytesIOを使ってダミーの画像を返します。
    print(data['key1'])
    print(data['key2'])

    probability = 0.5
    image_dog = open_image2base64(Path("/app/sample_dog.png"))
    image_cat = open_image2base64(Path("/app/sample_cat.png"))

    response_json = {
        'probability':probability, 
        'image_dog':image_dog, 
        'image_cat':image_cat
    }

    return JSONResponse(content=response_json)
