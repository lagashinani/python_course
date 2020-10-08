import requests
import time


time_2_days_ago = int(time.time() - 2 * 24 * 60 * 60)

response = requests\
            .get("https://api.stackexchange.com/2.2/search/advanced",
                params={"fromdate":time_2_days_ago, 
                "order":"desc",
                "sort":"creation","tagged":"python","site":"stackoverflow"}
                )\
            .json()

for item in response["items"]:
    print(item["tags"], ":", item["title"])
