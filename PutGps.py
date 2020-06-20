'''
Created on 2020/06/10

@author: kojima
'''

import os
from google.cloud import pubsub
from datetime import datetime, timedelta, timezone

class PutGps:

    gpsdata = "" ; topic_name = "" ; pjid = ""

    # コンストラクタ
    def __init__(self, p_gpsdata,p_pjid, p_topic_name):
        self.gpsdata    = p_gpsdata
        self.topic_name = p_topic_name
        self.pjid       = p_pjid

    # pubsubにput
    def putTopic(self):

        # pubsubクライアント作成
        publisher = pubsub.PublisherClient()

        # Topic定義
        topic = publisher.topic_path(self.pjid, self.topic_name)

        # 取得できない場合は作成
        try:
            publisher.get_topic(topic)
        except:
            publisher.create_topic(topic)

        # pubsubに位置情報を送るー
        JST = timezone(timedelta(hours=+9), 'JST')
        dt_now = datetime.now(JST).strftime('%Y-%m-%d %H:%M:%S')
        publisher.publish(topic, self.gpsdata.encode(), EventTimeStamp=dt_now)

        print("finish")


