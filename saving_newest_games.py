import requests
from pathlib import Path
from datetime import datetime

def fetch_and_save_games(username, base_path="/root/chess-api/games"):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}

    # Get current year/month
    now = datetime.now()
    year = now.year
    month = f"{now.month:02}"
    url = f"https://api.chess.com/pub/player/{username}/games/{year}/{month}"

    print(f"[{username}] Fetching: {url}")
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print(f"[{username}] Failed to fetch games from {url}")
        return

    games = r.json().get("games", [])
    print(f"[{username}] Found {len(games)} games in {url}")

    folder_name = f"{year}-{month}"
    folder_path = Path(base_path) / username / folder_name
    folder_path.mkdir(parents=True, exist_ok=True)

    # Save only if not already saved
    for i, game in enumerate(games, 1):
        pgn = game.get("pgn")
        if pgn:
            file_path = folder_path / f"{username}_game_{i}.pgn"
            if not file_path.exists():  # Skip if already exists
                with open(file_path, "w") as f:
                    f.write(pgn)

fetch_and_save_games("keejdi")
fetch_and_save_games("orzelmocnygaz")

