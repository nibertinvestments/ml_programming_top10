import csv

with open('input.csv', newline='', encoding='utf-8') as fh:
    rows = list(csv.DictReader(fh))

revenue = sum(float(r['amount']) for r in rows)
print(f'Revenue: {revenue:.2f}')
