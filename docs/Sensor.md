# センサー

## はじめに

このREADMEでは、「センサー」の概要を説明させていただきます。</br>各機能のコード説明等は下記リンクをご覧いただけると幸いです。開発範囲はセンサーとRestAPIです。

- [全体概要](./../README.md)

- [APIサーバー](./APIServer.md)

## 概要

### 機能

- 人感センサーの制御
- アルコール消毒の使用回数（施設訪問者数）のカウント

### 注力した機能・工夫した点

- 通行人などには反応しないよう改良した。
- 連続使用での誤作動が怒らないように改良した。

## スタートガイド

プロジェクトを複製してローカル端末で実行し、開発や検証ができるまでの手順を説明する。実際のシステムにプロジェクトをデプロイする方法については、デプロイの項目に記載する。

### 必要条件

本システムは以下の環境で構築されている。開発や検証を行うためには**pyenv**のインストールが必要となる。

- センサー
  - Python
    - pyenv 
      - python version 3.7.9

### インストール

開発環境の構築方法を以下で説明する。

#### githubからクローン

```
# sshを使用する場合
git clone git@github.com:Ryoto-128/Distance-measurement.git

# HTTPSを使用する場合
git clone https://github.com/Ryoto-128/Distance-measurement.git
```

#### Pyenvの設定

```
pyenv local 3.7.9
pyenv rehash
```

#### 作業ディレクトリの移動

```
cd ./client/sensor
```

 #### pipenvの設定

```
# pipfileからのパッケージインストールの場合
pipenv install
pipenv shell

# pipfile.lockからのパッケージインストールの場合
pipenv sync
pipenv shell
```

#### 作業ディレクトリの移動

```
cd ./client/sensor
```

#### 実行

```
python main.py
```

## デモ

実際に使用している様子をデモとして示す。

![sensor_demo1](./img/sensor_demo1.gif)

