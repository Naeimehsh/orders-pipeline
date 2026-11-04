import os

import pytest
from pymongo import MongoClient

from pipeline.transform import clean_orders, revenue_by_store

RAW = [
    {"product": "laptop", "price": 25000, "qty": 1, "store": "Mumbai"},
    {"product": "mouse", "price": 1500, "qty": 4, "store": "Delhi"},
]



@pytest.mark.skipif(not os.environ.get("MONGO_URL"), reason="needs a MongoDB (set MONGO_URL)")
def test_orders_round_trip_through_mongodb():
    with MongoClient(os.environ["MONGO_URL"]) as client:
        collection = client["ci_demo"]["orders"]
        collection.drop()
        collection.insert_many(clean_orders(RAW))
        stored = list(collection.find({}, {"_id": 0}))
        assert revenue_by_store(stored) == {"Mumbai": 25000, "Delhi": 6000}
        collection.drop()
