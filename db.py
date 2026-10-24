import streamlit as st
import pymongo
from urllib.parse import quote_plus

@st.cache_resource
def get_collection():
    config = st.secrets["mongo"]

    username = quote_plus(config["username"])
    password = quote_plus(config["password"])
    host = config["host"]

    uri = f"mongodb+srv://{username}:{password}@{host}/"

    client = pymongo.MongoClient(uri)
    db = client[config["db_name"]]
    collection = db[config["collection_name"]]

    return collection
