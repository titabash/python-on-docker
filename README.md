※こちらのリポジトリを流用させていただいております。
https://github.com/yyuuiikk/cloud_functions_python

# Cloud Functions, AWS Lambda Python実行環境

ローカル環境でCloud Functionsを実行するための環境。

HTTPトリガーにのみ対応。

# コンテナの作成と起動

```
$ docker-compose up -d
```

# コンテナの終了と削除
```
$ docker-compose down --rmi all --volumes --remove-orphans
```

## サンプルプログラムの実行
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

## デプロイ

GCP
```
$ docker exec -it gcp_function_python
$ gcloud app create --project=[YOUR_PROJECT_ID] # まだプロジェクトを作成していない場合は実行
$ gcloud app deploy --project [YOUR_PROJECT_ID]
```

# その他
- Lambdaに関しては今後Zappaに対応するかもしれません。

## How to Develop
1. Fork this repository to your github project
2. clone your repository<br>
   ```git clone <your repo>```<br>
3. add this repository to your remote upstream<br>
   ```git remote add upstream git@github.com:titabash/multicloud-python-batch.git```<br>
   You are ready to develop your batch.
## How to merge upstream change
4. fetch the upstream repo<br>
   ```git fetch upstream```<br>
5. merge the upstream change<br>
   ```git merge upstream/main```<br>
