# APIサーバー

## はじめに

このREADMEでは、「APIサーバー」の概要を説明させていただきます。</br>各機能のコード説明等は下記リンクをご覧いただけると幸いです。現在開発済みの範囲はセンサーとRestAPIとなっております。Webアプリケーションに関しても随時更新していく予定です。

- [全体概要](./../README.md)

- [センサー](./Sensor.md)

## 概要

### 機能

- 利用者情報管理機能とトークン認証
  - 利用者の登録機能
  - 利用者のログイン機能とトークン割り当て機能
  - トークンの状態確認機能・リフレッシュ機能
  - 利用者登録情報の取得機能・更新機能・削除機能
- 施設情報管理機能
  - 施設情報の登録機能
  - 施設登録情報の取得機能・更新機能
- ソーシャルディスタンス計測管理機能
  - 施設ごとのソーシャルディスタンス計測記録のアップロード機能
  - 施設ごとのソーシャルディスタンス計測記録の取得機能

### 注力した機能・工夫した点

- RESTを利用した認証機能付きのAPI
  - 利用者登録機能とトークン認証機能をつけることで、施設管理者のみデータの追加を可能にした。
  - 利用者は認証なしでデータへのアクセスが可能である。
  - 施設管理者の利用者登録情報を呼び出す際に、他者の登録情報を呼び出せないよう実装した。
  - RESTで情報を呼び出すときに情報を絞り込めるように、フィルター機能を実装した。

## スタートガイド

プロジェクトを複製してローカル端末で実行し、開発や検証ができるまでの手順を説明する。実際のシステムにプロジェクトをデプロイする方法については、デプロイの項目に記載する。

### 必要条件

本システムは以下の環境で構築されている。開発や検証を行うためには**Doker-compose,pyenv,pipenv**のインストールが必要となる。

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

### 認証機能のデモ

認証機能の登録・ログイン・ユーザー情報の取得の三つのデモを行います。他の機能も認証機能と同様にrestでリクエストを送ることで情報をユーザーに返します。

#### 登録

![登録](/Users/ryoto/Development/Private/Distance-measurement/doc/img/api_demo1.gif)

#### ログイン

![ログイン](/Users/ryoto/Development/Private/Distance-measurement/doc/img/api_demo2.gif)

#### ユーザー情報の取得

![ユーザー情報の取得](/Users/ryoto/Development/Private/Distance-measurement/doc/img/api_demo3.gif)

## デプロイ

本番環境（サーバー）上で上記インストール手順を行う。

