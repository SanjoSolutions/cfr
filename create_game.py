def create_game(Game, Player, **kwargs):
    game = Game(**kwargs)
    players = tuple(
        Player(player_index, game)
        for player_index
        in range(game.number_of_players)
    )
    game.add_players(players)
    return game
