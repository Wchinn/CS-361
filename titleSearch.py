import requests, json

url = "https://streaming-availability.p.rapidapi.com/shows/search/title"

querystring = {"country":"us","title":"Harry Potter","output_language":"en","show_type":"movie","series_granularity":"show"}

headers = {
	"X-RapidAPI-Key": "f83e32ba4dmsh9e258aa66e87ac5p1cedb2jsn6d976f8f26bc",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)


print((response.json()[0]["title"]))