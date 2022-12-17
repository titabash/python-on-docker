# python-on-docker

Use this template から新しいリポジトリを作成してください。

## 環境構築

1. Install docker, docker-compose
2. Install tmux

## コンテナの作成と起動

1. git clone --recursive {Template Repositoryから作成したリポジトリ}

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

# その他
