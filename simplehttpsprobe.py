import requests
import sys

headers = {'User-agent':'Mozilla//5.0',}

url = sys.argv[1]
addhttps = "https://"
if not "https://" in url:
        url = addhttps + url
pedido = requests.get(url, headers=headers)
estado = pedido.status_code

print(estado, url)
