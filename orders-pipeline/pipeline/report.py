"""Format a revenue report and post it to a chat webhook."""
import requests


def format_report(totals):
    lines = [f"{store}: {amount}" for store, amount in totals.items()]
    return "Revenue report\n" + "\n".join(lines)


def post_report(url, text):
    return requests.post(url, json={"text": text}, timeout=10)
