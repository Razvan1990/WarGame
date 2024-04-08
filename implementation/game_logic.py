from implementation.list_creator import ListCreation
from implementation import constants
import time


class GameLogic:

    def __init__(self):
        self.creator = ListCreation()

    def run_game(self):
        player1_name, player2_name = self.creator.introduce_player_names()
        player1_list, player2_list = self.creator.split_cards()
        '''
        implement here logic to define war
        1. basically we will play until one list player is empty
        2. we will play and check which card is bigger
        3. in this case we will add both cards in the winning list and remove the card from the losing list
        4. for razboi we need to add exact the number of cards we have but to check if we have enough cards
        5. if we don't have enough cards in the list, then we put the last card in the list which is smaller and count how much till we have till the last card
        '''
        time.sleep(1.5)
        index_player1 = 0
        index_player2 = 0
        while True:
            is_player1_list_empty = self.check_player_list_length(player1_list)
            is_player2_list_empty = self.check_player_list_length(player2_list)
            if is_player1_list_empty:
                return f"{player2_name} has won the game"
            if is_player2_list_empty:
                return f"{player1_name} has won the game"
            # need to use insert for addition to specify index
            value_player1 = self.get_card_value(player1_list[index_player1])
            value_player2 = self.get_card_value(player2_list[index_player2])
            print("{} card is {}".format(player1_name, player1_list[index_player1]))
            print("{} card is {}".format(player2_name, player2_list[index_player2]))
            winner = self.compute_game(value_player1, value_player2)
            if winner == 1:
                print("{} has won the hand".format(player1_name))
                player1_list.insert(0, player1_list[index_player1])
                player1_list.insert(0, player2_list[index_player2])
                player2_list.remove(player2_list[index_player2])
                if index_player1 == len(player1_list) - 1:
                    index_player1 = 0
                else:
                    index_player1 += 2
            elif winner == 2:
                print("{} has won the hand".format(player2_name))
                player2_list.insert(0, player2_list[index_player2])
                player2_list.insert(0, player1_list[index_player1])
                player2_list.remove(player2_list[index_player2])
                if index_player2 == len(player2_list) - 1:
                    index_player2 = 0
                else:
                    index_player2 += 2
            elif winner == 0:
                print("We have war at cards {} and {}".format(player1_list[index_player1], player2_list[index_player2]))
                time.sleep(1)
                list_cards_added_player1 = []
                list_cards_added_player2 = []
                # 1. first it is the ok part to check if both lists have a value in range and we have sufficent cards to number till the end
                if len(player1_list) - index_player1 - 1 >= value_player1 and len(
                        player2_list) - index_player2 - 1 >= value_player2:
                    # a.add in the lists the cards
                    for i in range(index_player1, index_player1 + value_player1):
                        list_cards_added_player1.append(player1_list[i])
                    for i in range(index_player2, index_player2 + value_player2):
                        list_cards_added_player2.append(player2_list[i])
                    value_player1 = self.get_card_value(list_cards_added_player1[len(list_cards_added_player1) - 1])
                    value_player2 = self.get_card_value(list_cards_added_player2[len(list_cards_added_player2) - 1])
                    # b. now we get the result and see what happens
                    score = self.compute_game(value_player1, value_player2)
                    if score == 1:
                        print("{} has won with {} versus {}".format(player1_name, value_player1, value_player2))
                        for i in range(index_player1, index_player1 + value_player1):
                            player1_list.insert(0, list_cards_added_player1[i])
                            player1_list.insert(0, list_cards_added_player2[i])
                            index_player1 += value_player1 + 1
                        for i in range(index_player2, index_player2 + value_player2):
                            player2_list.remove(list_cards_added_player2[i])
                            # we need to check if index_player2 is too big now
                            if index_player2 > len(player2_list) - 1:
                                index_player2 = abs(player2_list - index_player2)
                            elif index_player2 == len(player2_list) - 1:
                                index_player2 = 0
                            else:
                                index_player2 -= value_player2 + 1
                    if score == 2:
                        print("{} has won with {} versus {}".format(player2_name, value_player2, value_player1))
                        for i in range(index_player1, index_player1 + value_player1):
                            player1_list.remove(list_cards_added_player1[i])
                            # we need to check if index_player1 is too big now
                            if index_player1 > len(player1_list) - 1:
                                index_player1 = abs(player1_list - index_player1)
                            elif index_player1 == len(player1_list) - 1:
                                index_player1 = 0
                            else:
                                index_player1 -= value_player1 + 1
                        for i in range(index_player2, index_player2 + value_player2):
                            player2_list.insert(0, list_cards_added_player2[i])
                            player2_list.insert(0, list_cards_added_player1[i])
                            index_player2 += value_player2 + 1
                    else:
                        # if we have a new war, we just give the cards back for simplicity
                        print("Equality again with {}-{}".format(value_player1, value_player2))
                        for i in range(index_player1, index_player1 + value_player1):
                            player1_list.append(list_cards_added_player1[i])
                        for i in range(index_player2, index_player2 + value_player2):
                            player2_list.append(list_cards_added_player2[i])
                        if index_player1 == len(player1_list) - 1:
                            index_player1 = 0
                        else:
                            index_player1 += 1
                        if index_player2 == len(player2_list) - 1:
                            index_player2 = 0
                        else:
                            index_player2 += 1
                elif len(player1_list) - index_player1 - 1 >= value_player1 and len(
                        player2_list) - index_player2 - 1 < value_player2 < len(player2_list):
                    # first add in the cards till the final for player2
                    value_player2_temp = value_player2
                    for i in range(index_player2, len(player2_list)):
                        list_cards_added_player2.append(player2_list[i])
                        value_player2_temp -= 1
                    index_player2 = 0
                    for i in range(index_player2, value_player2_temp):
                        list_cards_added_player2.append((player2_list[i]))
                        index_player2 += 1
                    # add cards for player1
                    for i in range(index_player1, index_player1 + value_player1):
                        list_cards_added_player1.append(player1_list[i])
                    value_player1 = self.get_card_value(list_cards_added_player1[len(list_cards_added_player1) - 1])
                    value_player2 = self.get_card_value(list_cards_added_player2[len(list_cards_added_player2) - 1])
                    score = self.compute_game(value_player1, value_player2)
                    if score == 1:
                        print("{} has won with {} versus {}".format(player1_name, value_player1, value_player2))
                        for i in range(index_player1, index_player1 + value_player1):
                            player1_list.insert(0, list_cards_added_player1[i])
                            player1_list.insert(0, list_cards_added_player2[i])
                            index_player1 += value_player1 + 1
                        for i in range(index_player2, index_player2 + value_player2):
                            player2_list.remove(list_cards_added_player2[i])
                            # we need to check if index_player2 is too big now
                            if index_player2 > len(player2_list) - 1:
                                index_player2 = abs(player2_list - index_player2)
                            elif index_player2 == len(player2_list) - 1:
                                index_player2 = 0
                            else:
                                index_player2 -= value_player2 + 1
                    if score == 2:
                        print("{} has won with {} versus {}".format(player2_name, value_player2, value_player1))
                        for i in range(index_player1, index_player1 + value_player1):
                            player1_list.remove(list_cards_added_player1[i])
                            # we need to check if index_player1 is too big now
                            if index_player1 > len(player1_list) - 1:
                                index_player1 = abs(player1_list - index_player1)
                            elif index_player1 == len(player1_list) - 1:
                                index_player1 = 0
                            else:
                                index_player1 -= value_player1 + 1
                        for i in range(index_player2, index_player2 + value_player2):
                            player2_list.insert(0, list_cards_added_player2[i])
                            player2_list.insert(0, list_cards_added_player1[i])
                            index_player2 += value_player2 + 1
                    else:
                        # if we have a new war, we just give the cards back for simplicity
                        print("Equality again with {}-{}".format(value_player1, value_player2))
                        for i in range(index_player1, index_player1 + value_player1):
                            player1_list.append(list_cards_added_player1[i])
                        for i in range(index_player2, index_player2 + value_player2):
                            player2_list.append(list_cards_added_player2[i])
                        if index_player1 == len(player1_list) - 1:
                            index_player1 = 0
                        else:
                            index_player1 += 1
                        if index_player2 == len(player2_list) - 1:
                            index_player2 = 0
                        else:
                            index_player2 += 1
                elif len(player1_list) - index_player1 - 1 < value_player1 < len(player1_list) and len(
                        player2_list) - index_player2 - 1 >= len(player2_list):
                    # first add in the cards till the final for player2
                    value_player1_temp = value_player1
                    for i in range(index_player1, len(player1_list)):
                        list_cards_added_player1.append(player1_list[i])
                        value_player1_temp -= 1
                    index_player1 = 0
                    for i in range(index_player1, value_player1_temp):
                        list_cards_added_player1.append((player1_list[i]))
                        index_player1 += 1
                    # add cards for player1
                    for i in range(index_player2, index_player2 + value_player2):
                        list_cards_added_player2.append(player2_list[i])
                    value_player1 = self.get_card_value(list_cards_added_player1[len(list_cards_added_player1) - 1])
                    value_player2 = self.get_card_value(list_cards_added_player2[len(list_cards_added_player2) - 1])
                    score = self.compute_game(value_player1, value_player2)
                    if score == 1:
                        print("{} has won with {} versus {}".format(player1_name, value_player1, value_player2))
                        for i in range(index_player1, index_player1 + value_player1):
                            player1_list.insert(0, list_cards_added_player1[i])
                            player1_list.insert(0, list_cards_added_player2[i])
                            index_player1 += value_player1 + 1
                        for i in range(index_player2, index_player2 + value_player2):
                            player2_list.remove(list_cards_added_player2[i])
                            # we need to check if index_player2 is too big now
                            if index_player2 > len(player2_list) - 1:
                                index_player2 = abs(player2_list - index_player2)
                            elif index_player2 == len(player2_list) - 1:
                                index_player2 = 0
                            else:
                                index_player2 -= value_player2 + 1
                    if score == 2:
                        print("{} has won with {} versus {}".format(player2_name, value_player2, value_player1))
                        for i in range(index_player1, index_player1 + value_player1):
                            player1_list.remove(list_cards_added_player1[i])
                            # we need to check if index_player1 is too big now
                            if index_player1 > len(player1_list) - 1:
                                index_player1 = abs(player1_list - index_player1)
                            elif index_player1 == len(player1_list) - 1:
                                index_player1 = 0
                            else:
                                index_player1 -= value_player1 + 1
                        for i in range(index_player2, index_player2 + value_player2):
                            player2_list.insert(0, list_cards_added_player2[i])
                            player2_list.insert(0, list_cards_added_player1[i])
                            index_player2 += value_player2 + 1
                    else:
                        print("Equality again with {}-{}".format(value_player1, value_player2))
                        # if we have a new war, we just give the cards back for simplicity
                        for i in range(index_player1, index_player1 + value_player1):
                            player1_list.append(list_cards_added_player1[i])
                        for i in range(index_player2, index_player2 + value_player2):
                            player2_list.append(list_cards_added_player2[i])
                        if index_player1 == len(player1_list) - 1:
                            index_player1 = 0
                        else:
                            index_player1 += 1
                        if index_player2 == len(player2_list) - 1:
                            index_player2 = 0
                        else:
                            index_player2 += 1
                elif len(player1_list) - index_player1 - 1 < value_player1 < len(player1_list) and len(
                        player2_list) - index_player2 - 1 < value_player2 < len(player2_list):
                    # first add in the cards till the final for player2
                    value_player1_temp = value_player1
                    value_player2_temp = value_player2
                    for i in range(index_player1, len(player1_list)):
                        list_cards_added_player1.append(player1_list[i])
                        value_player1_temp -= 1
                    index_player1 = 0
                    for i in range(index_player1, value_player1_temp):
                        list_cards_added_player1.append((player1_list[i]))
                        index_player1 += 1
                    # add cards for player1
                    for i in range(index_player2, len(player2_list)):
                        list_cards_added_player2.append(player2_list[i])
                        value_player2_temp -= 1
                    index_player2 = 0
                    for i in range(index_player2, value_player2_temp):
                        list_cards_added_player2.append((player2_list[i]))
                        index_player2 += 1
                    value_player1 = self.get_card_value(list_cards_added_player1[len(list_cards_added_player1) - 1])
                    value_player2 = self.get_card_value(list_cards_added_player2[len(list_cards_added_player2) - 1])
                    score = self.compute_game(value_player1, value_player2)
                    if score == 1:
                        print("{} has won with {} versus {}".format(player1_name, value_player1, value_player2))
                        for i in range(index_player1, index_player1 + value_player1):
                            player1_list.insert(0, list_cards_added_player1[i])
                            player1_list.insert(0, list_cards_added_player2[i])
                            index_player1 += value_player1 + 1
                        for i in range(index_player2, index_player2 + value_player2):
                            player2_list.remove(list_cards_added_player2[i])
                            # we need to check if index_player2 is too big now
                            if index_player2 > len(player2_list) - 1:
                                index_player2 = abs(player2_list - index_player2)
                            elif index_player2 == len(player2_list) - 1:
                                index_player2 = 0
                            else:
                                index_player2 -= value_player2 + 1
                    if score == 2:
                        print("{} has won with {} versus {}".format(player1_name, value_player1, value_player2))
                        for i in range(index_player1, index_player1 + value_player1):
                            player1_list.remove(list_cards_added_player1[i])
                            # we need to check if index_player1 is too big now
                            if index_player1 > len(player1_list) - 1:
                                index_player1 = abs(player1_list - index_player1)
                            elif index_player1 == len(player1_list) - 1:
                                index_player1 = 0
                            else:
                                index_player1 -= value_player1 + 1
                        for i in range(index_player2, index_player2 + value_player2):
                            player2_list.insert(0, list_cards_added_player2[i])
                            player2_list.insert(0, list_cards_added_player1[i])
                            index_player2 += value_player2 + 1
                    else:
                        print("Equality again with {}-{}".format(value_player1, value_player2))
                        # if we have a new war, we just give the cards back for simplicity
                        for i in range(index_player1, index_player1 + value_player1):
                            player1_list.append(list_cards_added_player1[i])
                        for i in range(index_player2, index_player2 + value_player2):
                            player2_list.append(list_cards_added_player2[i])
                        if index_player1 == len(player1_list) - 1:
                            index_player1 = 0
                        else:
                            index_player1 += 1
                        if index_player2 == len(player2_list) - 1:
                            index_player2 = 0
                        else:
                            index_player2 += 1
                elif len(player1_list) - index_player1 - 1 < value_player1 > len(player1_list) or len(
                        player2_list) - index_player2 - 1 < value_player2 > len(player2_list):
                    if len(player1_list) > len(player2_list):
                        if index_player1 + len(player2_list) - 1 > len(player1_list):
                            value_player1_temp = len(player2_list)
                            for i in range(index_player1, len(player1_list)):
                                list_cards_added_player1.append(player1_list[i])
                                value_player1_temp -= 1
                            index_player1 = 0
                            for i in range(index_player1, value_player1_temp):
                                list_cards_added_player1.append((player1_list[i]))
                                index_player1 += 1
                        value_player1 = self.get_card_value(list_cards_added_player1[len(player2_list) - 1])
                        value_player2 = self.get_card_value(player2_list[index_player2 - 1])
                        if value_player1 > value_player2:
                            for i in range(0, len(list_cards_added_player1)):
                                player1_list.insert(0, list_cards_added_player1[i])
                                player1_list.insert(0, player2_list[i])
                            for i in range(len(player2_list) - 1, -1, -1):
                                player2_list.remove(player2_list[i])
                        if value_player1 < value_player2:
                            for i in range(0, len(list_cards_added_player1)):
                                player2_list.insert(0, list_cards_added_player1[i])
                                player2_list.insert(0, player2_list[i])
                            for i in range(len(list_cards_added_player1) - 1, -1, -1):
                                player1_list.remove(list_cards_added_player1[i])
                        else:
                            if index_player1 == len(player1_list) - 1:
                                index_player1 = 0
                            else:
                                index_player1 += 1
                            if index_player2 == len(player2_list) - 1:
                                index_player2 = 0
                            else:
                                index_player2 += 1
                    if len(player1_list) < len(player2_list):
                        if index_player2 + len(player1_list) - 1 > len(player2_list):
                            value_player2_temp = len(player1_list)
                            for i in range(index_player2, len(player2_list)):
                                list_cards_added_player2.append(player2_list[i])
                                value_player2_temp -= 1
                            index_player2 = 0
                            for i in range(index_player2, value_player2_temp):
                                list_cards_added_player2.append((player2_list[i]))
                                index_player2 += 1
                        value_player2 = self.get_card_value(list_cards_added_player2[len(player1_list) - 1])
                        value_player1 = self.get_card_value(player1_list[index_player1 - 1])
                        if value_player2 > value_player1:
                            for i in range(0, len(list_cards_added_player2)):
                                player2_list.insert(0, list_cards_added_player2[i])
                                player2_list.insert(0, player1_list[i])
                            for i in range(len(player1_list) - 1, -1, -1):
                                player1_list.remove(player1_list[i])
                        if value_player2 < value_player1:
                            for i in range(0, len(list_cards_added_player2)):
                                player1_list.insert(0, list_cards_added_player2[i])
                                player1_list.insert(0, player2_list[i])
                            for i in range(len(list_cards_added_player1) - 1, -1, -1):
                                player2_list.remove(list_cards_added_player2[i])
                        else:
                            if index_player2 == len(player2_list) - 1:
                                index_player2 = 0
                            else:
                                index_player2 += 1
                            if index_player1 == len(player1_list) - 1:
                                index_player1 = 0
                            else:
                                index_player1 += 1

    def get_card_value(self, card):
        card_value = card.split(" ")[0]
        if card_value in constants.dictionary_figures:
            card_value_number = constants.dictionary_figures[card_value]
            return card_value_number
        return int(card_value)

    def check_player_list_length(self, player_list):
        if len(player_list) == 0:
            return True
        return False

    def compute_game(self, value_player1, value_player2):
        if value_player1 > value_player2:
            return 1
        if value_player1 < value_player2:
            return 2
        else:
            return 0  # 0 logic should be done at the step
