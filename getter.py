import requests

url = "https://imdb8.p.rapidapi.com/auto-complete"

querystring = {"q":"game of thr"}

headers = {
	"X-RapidAPI-Key": "e83578d430mshd7df5e6711568c3p1db3b8jsncf718f5d3db2",
	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)