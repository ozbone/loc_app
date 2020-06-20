## loc_app

位置情報取得アプリのAppEngine側ソース(Flask)

**前提:Python3。Google SDKがインストールされていること。

## ローカルで試す場合(Windows)

keyを環境変数に指定

```
set GOOGLE_APPLICATION_CREDENTIALS=C:/xxxxx/xxxxxx.json
```

Python仮想環境を作成

```
python -m virtualenv c:\temp\loc_app
```

Python仮想環境をactivate(Linux系の場合はsource xxxx/bin/activateを実行)

```
c:\temp\loc_app\Scripts\activate
```

requirements.txtで必要なライブラリをインストール

```
pip install -r requirements.txt --no-cache-dir
```

main.pyを実行

```
python main.py
```

localhostのURLが表示されるので、ブラウザからアクセスしてhelloworldと表示されればOK。

```
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 260-818-480
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
```

## AppEngineにデプロイする方法

keyを環境変数に指定

```
set GOOGLE_APPLICATION_CREDENTIALS=C:/xxxxx/xxxxxx.json
```

deployを実行

```
cd <app.ymlが存在するパス>
gcloud app deploy
```

↓のようにDeploy先のURLが表示されるので、ブラウザで確認する。helloworldが表示されればOK。

```
Services to deploy:

descriptor:      [C:\xxxx\locapp\app.yaml]
source:          [C:\xxxx\locapp\locapp]
target project:  [xxxxxxxxxx]
target service:  [default]
target version:  [20200620t095441]
target url:      [https://xxxxxxxxxxx.appspot.com]


Do you want to continue (Y/n)?  Y

Beginning deployment of service [default]...
Created .gcloudignore file. See `gcloud topic gcloudignore` for details.
#============================================================#
#= Uploading 5 files to Google Cloud Storage                =#
#============================================================#
File upload done.
Updating service [default]...done.
Setting traffic split for service [default]...done.
Deployed service [default] to [https://xxxxxxxxxxx.appspot.com]]

You can stream logs from the command line by running:
  $ gcloud app logs tail -s default

To view your application in the web browser run:
  $ gcloud app browse


Updates are available for some Cloud SDK components.  To install them,
please run:
  $ gcloud components update
```
