import http.client
def get_pb(id):
   conn = http.client.HTTPSConnection("developer.chargenow.top")
   payload = ''
   headers = {
      'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
      'Authorization': 'Basic aXZhbl9rcmlrdW5vdjpJSzEyMzQ='
   }
   conn.request("POST", f"/cdb-open-api/v1/rent/order/create?deviceId={id}&callbackURL=https://example.com/cdb-open-api/v1/callback", payload, headers)
   res = conn.getresponse()
   data = res.read()
   print(data.decode("utf-8"))


def check_pbs(id):
   #проверить какие айди возвращает и дальше наладить работу с этими айди в функциях ниже.
   conn = http.client.HTTPSConnection("developer.chargenow.top")
   payload = ''
   headers = {
      'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
      'Authorization': 'Basic aXZhbl9rcmlrdW5vdjpJSzEyMzQ='
   }
   conn.request("GET", f"/cdb-open-api/v1/rent/cabinet/query?deviceId={id}", payload, headers)
   res = conn.getresponse()
   data = res.read()
   return data.decode("utf-8")
