import Requests
import lxml
import Pandas
import pytrends


kw_list = ['cryptocurrency']
pytrends = TrendReq(hl='en-US', tz=360)
pytrends = build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

