import requests
import logging

from models import parse_pgn_to_game

logger = logging.getLogger(__name__)


def fetch_games(username, max=100):
    url = f"https://lichess.org/api/games/user/{username}?max={max}"
    logger.info("Solicitando partidas a %s", url)

    response = requests.get(url, headers={"Accept": "application/x-chess-pgn"})
    response.raise_for_status()

    raw_games = [g.strip() for g in response.text.strip().split("\n\n\n") if g.strip()]
    logger.info("Descargadas %d partidas de %s", len(raw_games), username)

    games = []
    for raw in raw_games:
        try:
            game = parse_pgn_to_game(raw)
            games.append(game)
        except Exception as e:
            logger.warning("Partida omitida por error: %s", e)

    logger.info("%d partidas convertidas correctamente", len(games))
    return games
