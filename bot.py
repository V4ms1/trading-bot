import krakenex
import json
import time

api = krakenex.API()
api.load_key('kraken.key')
pair = 'XETHZUSD'
since = str(int(time.time() - 3600))
print (api.query_public('OHLC', data = {'pair' : pair, 'since' : since})['result'][pair])