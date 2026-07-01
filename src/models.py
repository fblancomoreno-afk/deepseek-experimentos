import chess.pgn
import logging
import io

logger = logging.getLogger(__name__)


class Game:
    def __init__(self, fecha, rival, resultado, rating_rival, color, pgn):
        self.fecha = fecha
        self.rival = rival
        self.resultado = resultado
        self.rating_rival = rating_rival
        self.color = color
        self.pgn = pgn


def parse_pgn_to_game(pgn_text):
    pgn_io = io.StringIO(pgn_text)
    game = chess.pgn.read_game(pgn_io)
    if game is None:
        raise ValueError("No se pudo parsear el PGN")

    headers = game.headers

    fecha = headers.get("Date", "")
    rival_white = headers.get("White", "")
    rival_black = headers.get("Black", "")
    resultado = headers.get("Result", "*")
    white_elo = headers.get("WhiteElo", "0")
    black_elo = headers.get("BlackElo", "0")

    white_rating = int(white_elo) if white_elo.isdigit() else 0
    black_rating = int(black_elo) if black_elo.isdigit() else 0

    juego = headers.get("White", "").lower()

    if "fblan" in juego:
        color = "white"
        rival = rival_black
        rating_rival = black_rating
    else:
        color = "black"
        rival = rival_white
        rating_rival = white_rating

    logger.debug(
        "Partida parseada: %s vs %s (%s) [%s]", rival, color, resultado, fecha
    )

    return Game(
        fecha=fecha,
        rival=rival,
        resultado=resultado,
        rating_rival=rating_rival,
        color=color,
        pgn=pgn_text,
    )
