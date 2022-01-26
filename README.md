# python-on-docker

Use this template から新しいリポジトリを作成してください。

## 環境構築

1. Install docker, docker-compose
2. Install tmux

## コンテナの作成と起動

1. 開発するPythonスクリプトのテンプレートを取得する。[python-clean-architecture-template](https://github.com/titabash/python-clean-architecture-template)<br>

```
make init
```

2. コンテナを立ち上げる。BUILD_MODE変数にbatchかapiを指定することでどちらで立ち上げるか指定する。<br>

```
make start BUILD_MODE=batch or api
```

## コンテナの停止

```
make stop BUILD_MODE=batch or api
```

## コンテナの終了と削除

```
make remove BUILD_MODE=batch or api
```

## コンテナの再起動

```
make restart BUILD_MODE=batch or api
```

## サンプルプログラムの実行

### バックエンドAPI

webサーバが起動するので、ターミナルの別ウインドウを開きcurlを実行する。

#### ローカル

```
curl http://127.0.0.1:8000/
```

#### GCP(Cloud Functions)

```
curl http://127.0.0.1:8010/
```

#### AWS Lambda (API Gatewayを経由すること想定している)

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

#### ローカルでバッチを実行

```docker exec -it local_batch_python python src/batch.py -o '{"hoge": "fuga"}'```

#### AWS Lambdaのローカルテストを実行

```curl -XPOST "http://localhost:8020/2015-03-31/functions/function/invocations" -d '{"hoge": "fuga"}'```

#### GCP Cloud Functionのローカルテストを実行

```curl -XPOST http://localhost:8010/ -H 'Content-Type:application/json; charset=utf-8' -d '{"data": {"hoge": "fuga"}}'```

## デプロイ

GCP

```
docker exec -it gcp_batch or gcp_api_be
gcloud app create --project=[YOUR_PROJECT_ID] # まだプロジェクトを作成していない場合は実行
gcloud app deploy --project [YOUR_PROJECT_ID]
```

AWS

```
zappa deploy dev
```

# その他
