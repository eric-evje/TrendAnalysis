from pytrends.request import TrendReq


# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()
search_list = ['bitcoin']

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()

pytrend.build_payload(kw_list=search_list, timeframe='now 4-H')

# Interest Over Time
interest_over_time_df = pytrend.interest_over_time()
print(interest_over_time_df)


