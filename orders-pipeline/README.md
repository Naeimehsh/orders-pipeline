# orders-pipeline (CI/CD Day 1 starter project)

A tiny data pipeline: `pipeline/transform.py` cleans raw orders and computes revenue per store; `pipeline/report.py` formats a report
(it imports the `requests` library).

You do NOT need to read or run this code.

**It starts with one deliberate flaw:** `requirements.txt` (the project's list of packages) is missing `requests`.
That is the bug from the story: it works on a laptop that happens to have `requests` installed, and fails on a clean machine.


With the flaw in place, `pytest -q` stops with `ModuleNotFoundError: No module named 'requests'`.
The fix is one line: add `requests` to `requirements.txt` and install again.

The `integration/` folder holds a MongoDB test used in a deep dive (it needs `pymongo` and a running MongoDB). It is not run by default.


>Nb; this is AI generated and verified to demo how one can use actions in context
