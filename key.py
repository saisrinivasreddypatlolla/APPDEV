import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"ImhheMRQdRO86xKSDl4rFA": "KEY", "isbns": "9781632168146"})
print(res.json())