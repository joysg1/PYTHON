import requests

url = ''
r = requests.get(url, allow_redirects=True)
open('image.png', 'wb').write(r.content)

