"""Clean raw order records and compute revenue per store."""
from collections import defaultdict


def clean_orders(rows):
    """Keep valid orders only, and add a total_amount to each."""
    cleaned = []
    for row in rows:
        if row.get("qty", 0) <= 0 or row.get("price", 0) <= 0:
            continue
        cleaned.append({**row, "total_amount": row["qty"] * row["price"]})
    return cleaned


def revenue_by_store(orders):
    """Total revenue per store, highest first."""
    totals = defaultdict(int)
    for order in orders:
        totals[order["store"]] += order["total_amount"]
    return dict(sorted(totals.items(), key=lambda item: -item[1]))
