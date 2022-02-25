import requests
from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth('username','password')
q=requests.get('http:link',auth=basic)
url_content =q.content
csv_file = open('downloaded.csv','wb')
csv_file.write(url_content)
csv_file.close()
