import random
from implementation import constants


class ListCreation:

    def __init__(self):
        self.player1_name = ""
        self.player2_name = ""
        self.list_player1 = []
        self.list_player2 = []

    def introduce_player_names(self):
        self.player1_name = input("Player 1 name: ").upper()
        self.player2_name = input("Player 2 name: ").upper()

        return self.player1_name, self.player2_name

    def split_cards(self):
        copy_list_constants = constants.list_cards.copy()
        for i in range(0, len(copy_list_constants)):
            random_card = random.randint(0, len(constants.list_cards) - 1)
            while constants.list_cards[random_card] not in constants.list_cards:
                random_card = random.randint(0, len(constants.list_cards) - 1)
            if i % 2 == 0:
                self.list_player1.append(constants.list_cards[random_card])
                constants.list_cards.remove(constants.list_cards[random_card])
            else:
                self.list_player2.append(constants.list_cards[random_card])
                constants.list_cards.remove(constants.list_cards[random_card])
            if len(constants.list_cards) == 0:
                break

        return self.list_player1, self.list_player2