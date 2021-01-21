# APIサーバー

## はじめに

このREADMEでは、「APIサーバー」の概要を説明させていただきます。</br>各機能のコード説明等は下記リンクをご覧いただけると幸いです。現在開発済みの範囲はセンサーとRestAPIとなっております。Webアプリケーションに関しても随時更新していく予定です。

- [全体概要](./../README.md)

- [センサー](./Sensor.md)

## 概要



## スタートガイド

プロジェクトを複製してローカル端末で実行し、開発や検証ができるまでの手順を説明する。実際のシステムにプロジェクトをデプロイする方法については、デプロイの項目に記載する。

### 必要条件

本システムは以下の環境で構築されている。**Doker-compose,pyenv,pipenv**のインストールが必要となる。

- データベース
  - Docker-compose
    - MySQL
- APIサーバー
  - Python
    - pyenv 
      - python version 3.7.9
    - パッケージ
      - pipenv
        - Django
        - Django rest framework
        - Django filter
        - pymysql
        - crypyography
        - Django rest framework jwt

### Installing / インストール

開発環境の構築方法を以下で説明する。

#### Docker上のMySQLデータベースの起動

```
docker-compose up -d
```

#### Pyenvの設定

```
pyenv local 3.7.9
pyenv rehash
```

 #### pipenvの設定

```
* pipfileからのパッケージインストールの場合
pipenv install
pipenv shell

* pipfile.lockからのパッケージインストールの場合
pipenv sync
pipenv shell
```

#### APIサーバーの起動

```
cd ./server/restapi/
python manage.py runserver
```

#### APIの動作確認

```
localhost:8000/<上記、機能一覧に記載された機能ごとのURL>
```

## デモ



## デプロイ

本番環境（サーバー）上で上記インストール手順を行う。

