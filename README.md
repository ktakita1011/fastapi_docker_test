# これは？
文字列情報のjsonを受け取って、画像や数値を含んだjsonを返すAPIサーバーの基礎

# docker起動コマンド
```bash
$ docker build -t myapi:latest .
$ docker run -p 8000:8000 myapi:latest
```

# 確認方法
dockerの外からを実行すると、文字列を含んだjsonをPOSTします。
受け取った画像は保存して数値はprintします。
```bash
$ python get_request_json.py
```