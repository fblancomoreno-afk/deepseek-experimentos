import json
import logging

from models import Game

logger = logging.getLogger(__name__)


def _game_to_dict(game):
    return {
        "fecha": game.fecha,
        "rival": game.rival,
        "resultado": game.resultado,
        "rating_rival": game.rating_rival,
        "color": game.color,
        "pgn": game.pgn,
    }


def _dict_to_game(d):
    return Game(
        fecha=d["fecha"],
        rival=d["rival"],
        resultado=d["resultado"],
        rating_rival=d["rating_rival"],
        color=d["color"],
        pgn=d["pgn"],
    )


def save_games(games, filename="data/games.json"):
    data = [_game_to_dict(g) for g in games]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    logger.info("Guardadas %d partidas en %s", len(games), filename)


def load_games(filename="data/games.json"):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    games = [_dict_to_game(d) for d in data]
    logger.info("Cargadas %d partidas desde %s", len(games), filename)
    return games
