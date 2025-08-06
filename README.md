Here's the requested content in `README.md` format:

````markdown
# ♟️ Chess Analyzer Tool

A lightweight tool to fetch chess.com games for one or more users, store them monthly in PGN format, and soon analyze them using Stockfish via a web interface.

## 🚀 Features

- 🔄 Automatically fetches new games from chess.com
- 📁 Organizes PGN files by username and month
- 🧠 Skips old or already downloaded games
- 🕓 Cron-ready for scheduled automation
- 📈 Planned: Stockfish-powered web UI for interactive analysis

## 🧑‍💻 Usage

Edit `saving_newest_games.py` and set your chess.com usernames:

```python
fetch_and_save_games("keejdi")
fetch_and_save_games("orzelmocnygaz")
````

Then run:

```bash
python3 saving_newest_games.py
```

To automate daily at 10:00 AM, add to your crontab:

```cron
0 10 * * * python3 /root/chess-api/saving_newest_games.py
```

## 📁 Output Structure

Games are stored like this:

```
/root/chess-api/games/
└── keejdi/
    └── 2025-08/
        ├── game_0_keejdi.pgn
        ├── game_1_keejdi.pgn
        └── ...
└── orzelmocnygaz/
    └── 2025-08/
        ├── game_0_orzelmocnygaz.pgn
        └── ...
```

## 🛠️ Roadmap

* ✅ Skip redundant data fetches
* ⏳ Add Stockfish analysis engine
* ⏳ Build Flask web frontend
* ⏳ Display PGN metadata in browser

## 👨‍🔧 Developer Notes

* Git SSH setup required to push changes to GitHub
* Run inside Docker or behind Nginx for production (planned)

## 📄 License

MIT © 2025 kejdas

