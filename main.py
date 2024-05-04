from game import Game


def main():
    game = Game(5)
    game.start()
    game.display()
    winner = game.show(0)
    print("\nWINNER:")
    winner.display()


if __name__ == "__main__":
    main()
