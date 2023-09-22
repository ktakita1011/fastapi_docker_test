import base64

import requests

# APIエンドポイントのURL
url = "http://127.0.0.1:8000/generate_image/"

# テストデータの準備
data_to_send = {
    "key1": "value1",
    "key2": "value2"
}

# POSTリクエストの実行
response = requests.post(url, json=data_to_send, proxies={"http": None, "https": None})

# レスポンスを確認
if response.status_code == 200:
    response_data = response.json()

    # 犬の画像を保存
    dog_image_data = base64.b64decode(response_data['image_dog'])
    with open("output_dog.jpg", "wb") as f:
        f.write(dog_image_data)
    print("画像を output_dog.jpg として保存しました。")
    
    # 猫の画像を保存
    cat_image_data = base64.b64decode(response_data['image_cat'])
    with open("output_cat.jpg", "wb") as f:
        f.write(cat_image_data)
    print("画像を output_cat.jpg として保存しました。")
    print('prob',response_data['probability'] )

else:
    print(f"エラーが発生しました。HTTPステータスコード: {response.status_code}")
    print(f"エラーメッセージ: {response.text}")
