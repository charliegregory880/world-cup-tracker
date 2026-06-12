import json

with open("data/results.json", "r") as f:
    results = json.load(f)

for result in results:
    result["home_goals"] = None
    result["away_goals"] = None

with open("data/results.json", "w") as f:
    json.dump(results, f, indent=4)

print("Converted all scores to null")