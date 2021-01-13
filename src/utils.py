import json
import csv

from bs4 import BeautifulSoup
import requests

def fetch_doc(url):
    res = requests.get(url)
        
    if(res.status_code == 200):
        return BeautifulSoup(res.text , features = "html.parser")
    else:
        return err_code(res.status_code , res.reason)
def save(file , data):
    try:
        f = open("src/data/{}".format(file) , "w")

        _format = file.split(".")[1]
        if _format == "json":
            f.write(json.dumps(data))

        elif _format == "csv":

            w = csv.DictWriter(f , ["url" , "data"] , dialect=csv.excel)
            w.writeheader()

            for url in data:
                w.writerow({"url" : url , "data" : str(json.dumps(data[url]))})

        f.close()
    except FileNotFoundError:
        print("[FATAL]Save directory(src/data/{}) was not found.".format(file))
    except Exception as e:
        print("[FATAL] {}".format(e))

def err_code(code , reason):
    return "[{}] [{}]".format(code , reason)