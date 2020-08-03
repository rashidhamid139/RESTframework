from  requests import Request, Session


import json

s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = req.prepare()