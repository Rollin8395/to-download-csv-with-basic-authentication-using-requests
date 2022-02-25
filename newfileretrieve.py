import requests
from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth('admin','P@55word')
q=requests.get('http://172.16.0.60/dataloader.cgi?dw=logcsv&maintype=0&subtype=10&starttime=2022-02-25-00:00:00&endtime=2022-02-25-23:59:59',auth=basic)
url_content =q.content
csv_file = open('downloaded.csv','wb')
csv_file.write(url_content)
csv_file.close()