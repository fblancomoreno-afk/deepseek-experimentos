import logging
from pathlib import Path

import yaml

from lichess_client import fetch_games
from stats import calculate_stats, print_stats
from storage import save_games

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "config.yaml"
DATA_DIR = BASE_DIR / "data"


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)


def main():
    cfg = load_config()
    default_user = cfg["lichess_username"]
    default_max = cfg["max_games"]

    username = input(f"Nombre de usuario (default: {default_user}): ").strip()
    if not username:
        username = default_user

    max_games = input(f"Número de partidas (default: {default_max}): ").strip()
    if not max_games:
        max_games = default_max
    else:
        max_games = int(max_games)

    games = fetch_games(username, max=max_games)

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    pgn_path = DATA_DIR / "partidas.pgn"
    with open(pgn_path, "w", encoding="utf-8") as f:
        for g in games:
            f.write(g.pgn + "\n\n\n")
    logger.info("PGN bruto guardado en %s", pgn_path)

    json_path = DATA_DIR / "games.json"
    save_games(games, filename=str(json_path))

    print(f"✅ {len(games)} partidas guardadas en {json_path}")

    stats = calculate_stats(games)
    print_stats(stats)


if __name__ == "__main__":
    main()
