import json
import csv
from os import mkdir
from typing import final

from bs4 import BeautifulSoup
import requests

OUTPUT_DIR = "src/data"

def fetch_doc(url):
    try:
        res = requests.get(url)
        if(res.status_code == 200):
            return BeautifulSoup(res.text , features = "html.parser")
        else:
            return err_code(res.status_code , res.reason)
    except Exception as e:
        return err_code("INTERNAL" , str(type(e)))

def save(file , data):
    try:
        f = None

        try:
            open("{}/{}".format(OUTPUT_DIR,file) , "w")
        except FileNotFoundError:
            mkdir(OUTPUT_DIR)
        finally:
            f = open("{}/{}".format(OUTPUT_DIR,file) , "w")
            

        _format = file.split(".")[1]
        if _format == "json":
            f.write(json.dumps(data , indent=4 , sort_keys=True))

        elif _format == "csv":
            
            csv.register_dialect("custom" , quoting = csv.QUOTE_MINIMAL)

            w = csv.DictWriter(f , ["url" , "data"] , dialect="custom")
            w.writeheader()

            for url in data:
                w.writerow({"url" : url , "data" : str(data[url])})

        f.close()
    except FileNotFoundError:
        print("[FATAL]Save directory({}/{}) was not found.".format(OUTPUT_DIR,file))
    except Exception as e:
        print("[FATAL] {}".format(e))

def err_code(code , reason):
    return "[{}] [{}]".format(code , reason)