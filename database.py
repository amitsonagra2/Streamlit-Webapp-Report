from deta import Deta
import os
from dotenv import load_dotenv

Deta_Key = os.getenv("Deta_Key")

# Init with project key
load_dotenv(".env")
deta = Deta(Deta_Key)

# connect to db
db = deta.Base("render_appv1_deta")

def insert_data(period,comment,income):
    return db.put({"key":period, "comment":comment, "income":income})

def fetch_all_records():
    res = db.fetch()
    return res.items



