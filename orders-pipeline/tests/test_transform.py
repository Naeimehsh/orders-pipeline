from pipeline.transform import clean_orders, revenue_by_store

RAW = [
    {"product": "laptop", "price": 25000, "qty": 1, "store": "Mumbai"},
    {"product": "mouse", "price": 1500, "qty": 4, "store": "Delhi"},
    {"product": "broken", "price": 100, "qty": 0, "store": "Pune"},   # invalid: quantity 0
]


def test_clean_orders_drops_invalid_rows():
    assert len(clean_orders(RAW)) == 2


def test_clean_orders_adds_total_amount():
    assert clean_orders(RAW)[1]["total_amount"] == 6000


def test_revenue_by_store_is_highest_first():
    assert list(revenue_by_store(clean_orders(RAW))) == ["Mumbai", "Delhi"]
