# Define Scoring Rules

SCORING = {
    "A": {"win": 2, "goal": 1},
    "B": {"win": 2, "goal": 1},
    "C": {"win": 3, "goal": 2},
    "D": {"win": 3, "goal": 2},
    "E": {"win": 4, "goal": 3},
    "F": {"win": 4, "goal": 3}
}


def calculate_leaderboard(players, teams, results):
    leaderboard = {player: 0 for player in players}

    for player, player_teams in players.items():

        total = 0

        for team in player_teams:

            tier = teams[team]["tier"]

            for result in results:

                # does this team appear in the result?
                if team not in (result["home_team"], result["away_team"]):
                    continue

                # determine goals for / against
                if result["home_team"] == team:
                    goals_for = result["home_goals"]
                    goals_against = result["away_goals"]
                else:
                    goals_for = result["away_goals"]
                    goals_against = result["home_goals"]

                # goal points
                total += goals_for * SCORING[tier]["goal"]

                # win points
                if goals_for > goals_against:
                    total += SCORING[tier]["win"]

                # penalties
                elif goals_for == goals_against:
                    if result.get("penalties_winner") == team:
                        total += SCORING[tier]["win"]


        leaderboard[player] = total

    return leaderboard