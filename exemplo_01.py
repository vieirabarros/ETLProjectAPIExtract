import requests

url = "https://google.com"

getURL = requests.get(url)
postURL = requests.post(url)

#print(postURL.text)
#print(postURL.headers)


url2 = "https://jsonplaceholder.typicode.com/posts/1"
getURL2 = requests.get(url2)
data=getURL2.json()


url3 = "https://jsonplaceholder.typicode.com/comments"

params = {"postId":1}
response = requests.get(url3, params=params)
comentarios = response.json()

print(f"Foram encontrados {len(comentarios)} comentários")
print(response.status_code)