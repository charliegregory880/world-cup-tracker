import streamlit as st
import json
from scoring import calculate_leaderboard

# Load data
with open("data/players.json") as f:
    players = json.load(f)

with open("data/teams.json") as f:
    teams = json.load(f)

with open("data/results.json") as f:
    results = json.load(f)

# Calculate leaderboard
leaderboard = calculate_leaderboard(players, teams, results)

# UI
st.title("🏆 World Cup Tracker")

st.subheader("Leaderboard")

# Sort and display
sorted_board = sorted(
    leaderboard.items(),
    key=lambda x: x[1],
    reverse=True
)

for player, score in sorted_board:
    st.write(f"**{player}**: {score} pts")

st.subheader("Results so far")
st.json(results)