import http.client
def get_pb():
   conn = http.client.HTTPSConnection("developer.chargenow.top")
   payload = ''
   headers = {
      'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
      'Authorization': 'Basic aXZhbl9rcmlrdW5vdjpJSzEyMzQ='
   }
   conn.request("POST", "/cdb-open-api/v1/rent/order/create?deviceId=BJW04969&callbackURL=https://example.com/cdb-open-api/v1/callback", payload, headers)
   res = conn.getresponse()
   data = res.read()
   print(data.decode("utf-8"))
