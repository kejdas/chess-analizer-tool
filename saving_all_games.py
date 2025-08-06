import requests
from pathlib import Path

def fetch_and_save_games(username, base_path="/root/chess-api/games"):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}
    archive_url = f"https://api.chess.com/pub/player/{username}/games/archives"

    res = requests.get(archive_url, headers=headers)
    if res.status_code != 200:
        print(f"[{username}] Failed to fetch archives: {res.status_code}")
        return

    archives = res.json().get("archives", [])
    if not archives:
        print(f"[{username}] No archives found.")
        return

    for url in archives:
        print(f"[{username}] Fetching: {url}")
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            print(f"[{username}] Failed to fetch games from {url}")
            continue

        games = r.json().get("games", [])
        print(f"[{username}] Found {len(games)} games in {url}")

        parts = url.strip("/").split("/")
        folder_name = f"{parts[-2]}-{parts[-1]}"
        folder_path = Path(base_path) / username / folder_name
        folder_path.mkdir(parents=True, exist_ok=True)

        for i, game in enumerate(games, 1):
            pgn = game.get("pgn")
            if pgn:
                file_path = folder_path / f"{username}_game_{i}.pgn"
                with open(file_path, "w") as f:
                    f.write(pgn)

fetch_and_save_games("keejdi")
fetch_and_save_games("orzelmocnygaz")
