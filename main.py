# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import *
import PutGps

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!!!'

@app.route('/test2',methods=["POST"])
def test2():

    # POST送信されたフォームデータを取得
    myid = escape(request.form["id"])
    longitude = escape(request.form["longitude"])
    latitude = escape(request.form["latitude"])
    altitude = escape(request.form["altitude"])
    dt = escape(request.form["dt"])

    msg="{},{},{},{},{}".format(myid,latitude,longitude,altitude,dt)
    pt = PutGps.PutGps(p_gpsdata=msg,
                       p_pjid="<YOUR GCP PROJECT_ID>",
                       p_topic_name="locationdata")
    pt.putTopic()

    return 'ok'

@app.route('/showmap',methods=["GET"])
def showmap():
    import GetLocDB as gl

    # GET params
    myid = escape(request.args.get('id', ''))

    gldata = gl.GetLocDB("potato!", myid)
    locdata = gldata.getLocForMap()
    lastdata = gldata.getLocLast()

    return render_template('showmap.html',locdata=locdata,lastdata=lastdata)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True, threaded=True)
# [END gae_python37_app]
