# python-on-docker

## 環境構築
1. Install docker, docker-compose
2. Install tmux

## コンテナの作成と起動

```
$ make init
$ make start
```

## コンテナの停止
```
$ make stop
```

## コンテナの終了と削除
```
$ make remove
```

## サンプルプログラムの実行
### バックエンドAPI
webサーバが起動するので、ターミナルの別ウインドウを開きcurlを実行する。
ローカル
```
$ curl http://127.0.0.1:8000/
```

GCP(Cloud Functions)
```
$ curl http://127.0.0.1:8010/
```

AWS Lambda (API Gatewayを経由すること想定している)
```
$ curl -XPOST "http://localhost:8020/2015-03-31/functions/function/invocations" -d '{"resource": "/",
    "path": "/",
    "httpMethod": "GET",
    "headers": {},
    "multiValueHeaders": {},
    "queryStringParameters": {
    },
    "multiValueQueryStringParameters": {},
    "pathParameters": {
        "bar": "barbar",
        "foo": "foofoo"
    },
    "stageVariables": null,
    "requestContext": {},
    "body": null,
    "isBase64Encoded": false}'
```

### バッチ
Run batch on local<br>
```docker exec -it local_batch_python python src/batch.py -o '{"hoge": "fuga"}'```<br>
Run batch on local AWS<br>
```curl -XPOST "http://localhost:8020/2015-03-31/functions/function/invocations" -d '{"hoge": "fuga"}'```<br>
Run batch on local GCP(Cloud Functions)<br>
```curl -XPOST http://localhost:8010/ -H 'Content-Type:application/json; charset=utf-8' -d '{"data": {"hoge": "fuga"}}'```<br>


## デプロイ

GCP
```
$ docker exec -it gcp_function_python
$ gcloud app create --project=[YOUR_PROJECT_ID] # まだプロジェクトを作成していない場合は実行
$ gcloud app deploy --project [YOUR_PROJECT_ID]
```

# その他
- Lambdaに関しては今後Zappaに対応するかもしれません。
