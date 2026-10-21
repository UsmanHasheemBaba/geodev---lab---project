import csv


def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw in ("", "NA", "N/A", "-"):
            continue
        values.append(float(raw))
    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
    }


lat_result = inspect_column("bosso.csv", "latitude")
lon_result = inspect_column("bosso.csv", "longitude")

print("Latitude:", lat_result)
print("Longitude:", lon_result)