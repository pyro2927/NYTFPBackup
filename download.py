from datetime import date
from datetime import datetime, timedelta
import os
import pathlib
import requests
import sys

def download(root, d):
    folder = os.path.join(root, d.strftime("%Y/%m"))
    dest = os.path.join(folder, d.strftime("%d.pdf"))
    pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
    if os.path.exists(dest):
        return
    url = "https://static01.nyt.com/images/{}/nytfrontpage/scan.pdf".format(d.strftime("%Y/%m/%d"))
    r = requests.get(url, allow_redirects=True)
    if r.status_code == 200:
        open(dest, 'wb').write(r.content)

if __name__ == '__main__':
    d = date.today()
    if len(sys.argv) >= 1:
        root = sys.argv[1] 
        print("Using custom download directory: {}".format(root))
    else:
        root = os.getcwd()
    while True:
        download(root, d)
        d = d - timedelta(days=1)