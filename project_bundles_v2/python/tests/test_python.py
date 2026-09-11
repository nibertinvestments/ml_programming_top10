import csv
from pathlib import Path

bundle_root = Path(__file__).resolve().parents[1]
data_path = bundle_root / 'data' / 'sample.csv'

with data_path.open(newline='', encoding='utf-8') as fh:
    rows = list(csv.DictReader(fh))

revenue = sum(float(r['amount']) for r in rows)
print(f'Revenue: {revenue:.2f}')
