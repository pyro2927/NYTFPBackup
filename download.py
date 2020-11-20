from datetime import date
from datetime import datetime, timedelta
import os
import pathlib
import requests

def download(d):
    folder = d.strftime("%Y/%m")
    dest = d.strftime("%Y/%m/%d.pdf")
    pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
    if os.path.exists(dest):
        return
    url = "https://static01.nyt.com/images/{}/nytfrontpage/scan.pdf".format(d.strftime("%Y/%m/%d"))
    r = requests.get(url, allow_redirects=True)
    if r.status_code == 200:
        open(dest, 'wb').write(r.content)

if __name__ == '__main__':
    d = date.today()
    while True:
        download(d)
        d = d - timedelta(days=1)