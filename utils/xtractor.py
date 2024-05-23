from blackjack import *
import multiprocessing
import sys

f = open("/dev/null", "w")
sys.stdout = f

def generate_game(i):
    """plays a game and return the highest number of cards in a player's hand
    """

    data = []

    croupier = Croupier(Hand(0, []), 0)
    hector = Player(Hand(0, []), 1)
    gabriel = Player(Hand(0, []), 2)

    players = [croupier, hector, gabriel]

    deck = make_deck(1)
    deck.shuffle(100)
    game = Game(players, deck)
    while (
        len(
            [player for player in players if (not player.stopped and not player.is_out)]
        )
        > 1
    ):
        for player in players:
            if player.is_croupier:
                player.play(game)
            else:
                player.rand_play(game) # method has been removed
    max = len(players[0].hand.l_cards)
    for player in players:
        if len(player.hand.l_cards) > max:
            max = len(player.hand.l_cards)
    data.append(max)
    return data


def write_data(file, data):
    with open(file, "w") as f:
        for i in data:
            f.write(str(i[0]) + "\n")



def run():
    with multiprocessing.Pool() as pool:
        # count the max number of process
        maxproc = multiprocessing.cpu_count()
        data = pool.map(generate_game, [i for i in range(maxproc)])
        write_data("blackjack.csv", data)


run()
