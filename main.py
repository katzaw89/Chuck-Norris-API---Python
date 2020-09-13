import requests

url = 'https://api.chucknorris.io/jokes/random'

print("10 Joke about Chuck Norris: \n")
for i in range(10):
    RES = requests.get(url)
    data = RES.json()
    joke = data['value']
    print(i+1,joke)
