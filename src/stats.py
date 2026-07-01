def calculate_stats(games):
    total = len(games)
    wins = 0
    losses = 0
    draws = 0
    ratings = []

    for g in games:
        if g.rating_rival:
            ratings.append(g.rating_rival)

        if g.resultado == "1-0" and g.color == "white":
            wins += 1
        elif g.resultado == "0-1" and g.color == "black":
            wins += 1
        elif g.resultado == "1/2-1/2":
            draws += 1
        else:
            losses += 1

    win_rate = (wins / total * 100) if total > 0 else 0.0
    avg_rating = round(sum(ratings) / len(ratings)) if ratings else 0
    highest = max(ratings) if ratings else 0
    lowest = min(ratings) if ratings else 0

    return {
        "total_games": total,
        "wins": wins,
        "losses": losses,
        "draws": draws,
        "win_rate": round(win_rate, 1),
        "avg_rating_rival": avg_rating,
        "highest_rating": highest,
        "lowest_rating": lowest,
    }


def print_stats(stats):
    print("=" * 36)
    print(f"{'Estadísticas de partidas':^36}")
    print("=" * 36)
    print(f"  Partidas totales:      {stats['total_games']}")
    print(f"  Victorias:             {stats['wins']}")
    print(f"  Derrotas:              {stats['losses']}")
    print(f"  Tablas:                {stats['draws']}")
    print(f"  Win rate:              {stats['win_rate']}%")
    print(f"  Rating rival promedio: {stats['avg_rating_rival']}")
    print(f"  Rating rival más alto: {stats['highest_rating']}")
    print(f"  Rating rival más bajo: {stats['lowest_rating']}")
    print("=" * 36)
