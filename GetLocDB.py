'''
Created on 2020/06/10

'''

import google.cloud.bigquery as bq

class GetLocDB:

    user = None; locid = None ;

    # コンストラクタ
    def __init__(self, p_user,p_locid):
        # どのユーザーの、どのロケーションIDを地図に表示するか(開始～終了までの統一番号)
        self.user    = p_user
        self.locid = p_locid

    # BigQueryから対象データ取得
    def getLocForMap(self):
        client = bq.Client()
#        query = """
#            select latitude as lat,longitude as lng from `location.loc_data` where dt >= '2020-06-14' order by dt
#        """
        query = """
            with a as (select latitude as lat,longitude as lng from `location.loc_data` where id={} order by dt)
            select string_agg(to_json_string(a,true),',') as loc from a limit 1
        """.format(self.locid)

        query_job = client.query(query)

        for row in query_job:
            # Row values can be accessed by field name or index.
            locdata = row["loc"]

        return locdata

    def getLocLast(self):
        client = bq.Client()
#        query = """
#            select latitude as lat,longitude as lng from `location.loc_data` where dt >= '2020-06-14' order by dt
#        """
        query = """
            select string_agg(to_json_string(x,true),',') as loc from  (select latitude as lat,longitude as lng,row_number() over (order by dt desc) as rank from `location.loc_data` where id = {}) as x where x.rank = 1
        """.format(self.locid)

        query_job = client.query(query)

        for row in query_job:
            # Row values can be accessed by field name or index.
            locdata = row["loc"]

        return locdata


