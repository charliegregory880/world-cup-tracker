import csv
import json

CSV_FILE = r"C:\Users\CharlieGregory\world_cup\data\fixtures.csv"
OUTPUT_FILE = r"C:\Users\CharlieGregory\world_cup\data\results.json"

results = []

with open(CSV_FILE, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:

        # Stop once we reach Congo DR vs Uzbekistan
        if row["team_a"] == "Congo DR" and row["team_b"] == "Uzbekistan":
            break

        # Only group stage matches
        if row["stage"] != "Group Stage":
            continue

        result = {
    "date": row["date"],
    "home_team": row["team_a"],
    "away_team": row["team_b"],
    "home_goals": None,
    "away_goals": None,
    "penalties_winner": None
}

        results.append(result)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4)

print(f"Created {len(results)} results")