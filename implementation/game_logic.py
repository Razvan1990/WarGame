import random

from implementation.list_creator import ListCreation
from implementation import constants
import time


class GameLogic:

    def __init__(self):
        self.creator = ListCreation()

    def run_game(self):
        player1_name, player2_name = self.creator.introduce_player_names()
        player1_list, player2_list = self.creator.split_cards()
        print(player1_list)
        print(player2_list)
        print("___________________________________________________________")
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
            # make check here again
            is_player1_list_empty = self.check_player_list_length(player1_list)
            is_player2_list_empty = self.check_player_list_length(player2_list)
            if is_player1_list_empty:
                return f"{player2_name} has won the game"
            if is_player2_list_empty:
                return f"{player1_name} has won the game"
            # need to use insert for addition to specify index
            if index_player1 >= len(player1_list) - 1 or (index_player1 == 0 and len(player1_list) == 0):
                index_player1 = 0
            if index_player2 >= len(player2_list) - 1 or (index_player2 == 0 and len(player2_list) == 0):
                index_player2 = 0
            print("Index player1", index_player1)
            print("Index player2", index_player2)
            print(player1_list)
            print(player2_list)
            value_player1 = self.get_card_value(player1_list[index_player1])
            value_player2 = self.get_card_value(player2_list[index_player2])
            value_player1_copy = value_player1
            value_player2_copy = value_player2
            print("_____________________________________________________")
            print("{} card is {}".format(player1_name, player1_list[index_player1]))
            print("{} card is {}".format(player2_name, player2_list[index_player2]))
            winner = self.compute_game(value_player1, value_player2)
            if winner == 1:
                print("{} has won the hand".format(player1_name))
                time.sleep(1.5)
                player1_list.insert(0, player2_list[index_player2])
                player2_list.remove(player2_list[index_player2])
                is_player2_list_empty = self.check_player_list_length(player2_list)
                if is_player2_list_empty:
                    return f"{player1_name} has won the game"
                if index_player1 >= len(player1_list) - 2:
                    index_player1 = 0
                else:
                    index_player1 += 2
                continue
            elif winner == 2:
                print("{} has won the hand".format(player2_name))
                time.sleep(1.5)
                player2_list.insert(0, player1_list[index_player1])
                player1_list.remove(player1_list[index_player1])
                # make here another check before the update
                is_player1_list_empty = self.check_player_list_length(player1_list)
                if is_player1_list_empty:
                    return f"{player2_name} has won the game"
                if index_player2 >= len(player2_list) - 2:
                    index_player2 = 0
                else:
                    index_player2 += 2
                continue
            elif winner == 0:
                print("We have war at cards {} and {}".format(player1_list[index_player1], player2_list[index_player2]))
                time.sleep(1.5)
                time.sleep(1.5)
                list_cards_added_player1 = []
                list_cards_added_player2 = []
                # 1. first it is the ok part to check if both lists have a value in range and we have sufficent cards to number till the end
                if len(player1_list) - index_player1 - 1 >= value_player1 and len(
                        player2_list) - index_player2 - 1 >= value_player2:
                    # a.add in the lists the cards
                    for i in range(index_player1, index_player1 + value_player1 + 1):
                        list_cards_added_player1.append(player1_list[i])
                    for i in range(index_player2, index_player2 + value_player2 + 1):
                        list_cards_added_player2.append(player2_list[i])
                    value_player1 = self.get_card_value(list_cards_added_player1[len(list_cards_added_player1) - 1])
                    value_player2 = self.get_card_value(list_cards_added_player2[len(list_cards_added_player2) - 1])

                    # b. now we get the result and see what happens
                    score = self.compute_game(value_player1, value_player2)
                    if score == 1:
                        print("{} has won with {} versus {}".format(player1_name, value_player1, value_player2))
                        time.sleep(1.5)
                        for card in list_cards_added_player2:
                            player1_list.insert(0, card)
                        index_player1 += value_player1_copy + 1
                        if index_player1 >= len(player1_list) - 1:
                            index_player1 = 0
                        for card in list_cards_added_player2:
                            player2_list.remove(card)
                            # we need to check if index_player2 is too big now
                        is_player2_list_empty = self.check_player_list_length(player2_list)
                        if is_player2_list_empty:
                            return f"{player1_name} has won the game"
                        if index_player2 > len(player2_list) - 1:
                            index_player2 = abs(len(player2_list) - index_player2)
                        elif index_player2 == len(player2_list) - 1:
                            index_player2 = 0
                        else:
                            index_player2 -= value_player2 + 1
                        continue
                    if score == 2:
                        print("{} has won with {} versus {}".format(player2_name, value_player2, value_player1))
                        time.sleep(1.5)
                        for card in list_cards_added_player1:
                            player1_list.remove(card)
                            # we need to check if index_player1 is too big now
                        is_player1_list_empty = self.check_player_list_length(player1_list)
                        if is_player1_list_empty:
                            return f"{player2_name} has won the game"
                        if index_player1 > len(player1_list) - 1:
                            index_player1 = abs(len(player1_list) - index_player1)
                        elif index_player1 == len(player1_list) - 1:
                            index_player1 = 0
                        for card in list_cards_added_player1:
                            player2_list.insert(0, card)
                        index_player2 += value_player2_copy + 1
                        if index_player2 >= len(player2_list) - 1:
                            index_player2 = 0
                        continue
                    else:
                        # if we have a new war, we just give the cards back for simplicity
                        print("Equality again with {}-{}".format(value_player1, value_player2))
                        time.sleep(1.5)
                        # no need to do anything with the cards
                        if index_player1 == len(player1_list) - 1:
                            index_player1 = 0
                        else:
                            index_player1 += 1
                        if index_player2 == len(player2_list) - 1:
                            index_player2 = 0
                        else:
                            index_player2 += 1
                        continue
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
                    for i in range(index_player1, index_player1 + value_player1 + 1):
                        list_cards_added_player1.append(player1_list[i])
                    value_player1 = self.get_card_value(list_cards_added_player1[len(list_cards_added_player1) - 1])
                    value_player2 = self.get_card_value(list_cards_added_player2[len(list_cards_added_player2) - 1])
                    score = self.compute_game(value_player1, value_player2)
                    if score == 1:
                        print("{} has won with {} versus {}".format(player1_name, value_player1, value_player2))
                        time.sleep(1.5)
                        for card in list_cards_added_player2:
                            player1_list.insert(0, card)
                        index_player1 += value_player1_copy + 1
                        if index_player1 >= len(player1_list) - 1:
                            index_player1 = 0
                        for card in list_cards_added_player2:
                            player2_list.remove(card)
                        is_player2_list_empty = self.check_player_list_length(player2_list)
                        if is_player2_list_empty:
                            return f"{player1_name} has won the game"
                            # we need to check if index_player2 is too big now
                        if index_player2 > len(player2_list) - 1:
                            index_player2 = abs(len(player2_list) - index_player2)
                        elif index_player2 == len(player2_list) - 1:
                            index_player2 = 0
                        continue
                    if score == 2:
                        print("{} has won with {} versus {}".format(player2_name, value_player2, value_player1))
                        time.sleep(1.5)
                        for card in list_cards_added_player1:
                            player2_list.insert(0, card)
                        index_player2 += value_player2_copy + 1
                        if index_player2 >= len(player2_list) + 1:
                            index_player2 = 0
                        for card in list_cards_added_player1:
                            player1_list.remove(card)
                            # we need to check if index_player1 is too big now
                        is_player1_list_empty = self.check_player_list_length(player1_list)
                        if is_player1_list_empty:
                            return f"{player2_name} has won the game"
                        if index_player1 > len(player1_list) - 1:
                            index_player1 = abs(len(player1_list) - index_player1)
                        elif index_player1 == len(player1_list) - 1:
                            index_player1 = 0
                        continue
                    else:
                        # if we have a new war, we just give the cards back for simplicity
                        print("Equality again with {}-{}".format(value_player1, value_player2))
                        time.sleep(1.5)
                        if index_player1 == len(player1_list) - 1:
                            index_player1 = 0
                        else:
                            index_player1 += 1
                        if index_player2 == len(player2_list) - 1:
                            index_player2 = 0
                        else:
                            index_player2 += 1
                        continue
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
                        time.sleep(1.5)
                        for card in list_cards_added_player2:
                            player1_list.insert(0, card)
                        index_player1 += value_player1_copy + 1
                        if index_player1 >= len(player1_list) - 1:
                            index_player1 = 0
                        for card in list_cards_added_player2:
                            player2_list.remove(card)
                            # we need to check if index_player2 is too big now
                        is_player2_list_empty = self.check_player_list_length(player2_list)
                        if is_player2_list_empty:
                            return f"{player1_name} has won the game"
                        if index_player2 > len(player2_list) - 1:
                            index_player2 = abs(len(player2_list) - index_player2)
                        elif index_player2 == len(player2_list) - 1:
                            index_player2 = 0
                        continue
                    if score == 2:
                        print("{} has won with {} versus {}".format(player2_name, value_player2, value_player1))
                        time.sleep(1.5)
                        for card in list_cards_added_player1:
                            player2_list.insert(card)
                        index_player2 += value_player2_copy + 1
                        if index_player2 >= len(player2_list):
                            index_player2 = 0
                        for card in list_cards_added_player1:
                            player1_list.remove(card)
                        is_player1_list_empty = self.check_player_list_length(player1_list)
                        if is_player1_list_empty:
                            return f"{player2_name} has won the game"
                        # we need to check if index_player1 is too big now
                        if index_player1 > len(player1_list) - 1:
                            index_player1 = abs(len(player1_list) - index_player1)
                        elif index_player1 == len(player1_list) - 1:
                            index_player1 = 0
                        else:
                            index_player1 -= value_player1_copy + 1
                        continue
                    else:
                        print("Equality again with {}-{}".format(value_player1, value_player2))
                        time.sleep(1.5)
                        # if we have a new war, we just give the cards back for simplicity - do nothing
                        if index_player1 == len(player1_list) - 1:
                            index_player1 = 0
                        else:
                            index_player1 += 1
                        if index_player2 == len(player2_list) - 1:
                            index_player2 = 0
                        else:
                            index_player2 += 1
                        continue
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
                        time.sleep(1.5)
                        for card in list_cards_added_player2:
                            player1_list.insert(0, card)
                        index_player1 += value_player1_copy + 1
                        if index_player1 >= len(player1_list) - 1:
                            index_player1 = 0
                        for card in list_cards_added_player2:
                            player2_list.remove(card)
                        is_player2_list_empty = self.check_player_list_length(player2_list)
                        if is_player2_list_empty:
                            return f"{player1_name} has won the game"
                            # we need to check if index_player2 is too big now
                        if index_player2 > len(player2_list) - 1:
                            index_player2 = abs(len(player2_list) - index_player2)
                        elif index_player2 == len(player2_list) - 1:
                            index_player2 = 0
                        continue
                    if score == 2:
                        print("{} has won with {} versus {}".format(player2_name, value_player2, value_player1))
                        time.sleep(1.5)
                        for card in list_cards_added_player1:
                            player2_list.insert(0, card)
                        index_player2 += value_player2_copy + 1
                        if index_player2 >= len(player2_list) - 1:
                            index_player2 = 0
                        for card in list_cards_added_player1:
                            player1_list.remove(card)
                        is_player1_list_empty = self.check_player_list_length(player1_list)
                        if is_player1_list_empty:
                            return f"{player2_name} has won the game"
                            # we need to check if index_player1 is too big now
                        if index_player1 > len(player1_list) - 1:
                            index_player1 = abs(len(player1_list) - index_player1)
                        elif index_player1 == len(player1_list) - 1:
                            index_player1 = 0

                        continue
                    else:
                        print("Equality again with {}-{}".format(value_player1, value_player2))
                        time.sleep(1.5)
                        # if we have a new war, we just give the cards back for simplicity
                        if index_player1 == len(player1_list) - 1:
                            index_player1 = 0
                        else:
                            index_player1 += 1
                        if index_player2 == len(player2_list) - 1:
                            index_player2 = 0
                        else:
                            index_player2 += 1
                        continue
                # TODO CHECK HERE
                elif len(player1_list) - index_player1 - 1 < value_player1 > len(player1_list) or len(
                        player2_list) - index_player2 - 1 < value_player2 > len(player2_list):
                    if len(player1_list) > len(player2_list):
                        if index_player1 + len(player2_list) - 1 > len(player1_list):
                            value_player1_temp = len(player2_list)
                            for i in range(index_player1, index_player1 + len(player2_list)):
                                if i >= len(player1_list) - 1:
                                    i = 0
                                list_cards_added_player1.append(player1_list[i])
                                value_player1_temp -= 1
                                index_player1 += 1
                                if index_player1 >= len(player1_list) - 1:
                                    index_player1 = 0
                        elif index_player1 + len(player2_list) - 1 < len(player1_list):
                            value_player1_temp = len(player2_list)
                            for i in range(index_player1, len(player1_list)):
                                list_cards_added_player1.append(player1_list[i])
                                value_player1_temp -= 1
                            index_player1 = 0
                            if value_player1_temp < len(player2_list) - len(list_cards_added_player1):
                                for i in range(0, value_player1_temp):
                                    list_cards_added_player1.append(player1_list[i])
                            else:
                                for i in range(0, len(player2_list) - len(list_cards_added_player1)):
                                    list_cards_added_player1.append(player1_list[i])
                        value_player1 = self.get_card_value(list_cards_added_player1[len(player2_list) - 1])
                        value_player2 = self.get_card_value(player2_list[index_player2 - 1])
                        value_player1_copy = value_player1
                        value_player2_copy = value_player2
                        if value_player1_copy > value_player2_copy:
                            for i in range(0, len(list_cards_added_player1)):
                                player1_list.insert(0, player2_list[i])
                            for i in range(len(player2_list) - 1, -1, -1):
                                player2_list.remove(player2_list[i])
                            continue
                        if value_player1_copy < value_player2_copy:
                            for i in range(0, len(list_cards_added_player1)):
                                player2_list.insert(0, list_cards_added_player1[i])
                            for i in range(len(list_cards_added_player1) - 1, -1, -1):
                                player1_list.remove(list_cards_added_player1[i])
                            continue
                        else:
                            if index_player1 == len(player1_list) - 1:
                                index_player1 = 0
                            else:
                                index_player1 += 1
                            if index_player2 == len(player2_list) - 1:
                                index_player2 = 0
                            else:
                                index_player2 += 1
                            continue
                    if len(player1_list) < len(player2_list):
                        if index_player2 + len(player1_list) - 1 > len(player2_list):
                            value_player2_temp = len(player1_list)
                            for i in range(index_player2, index_player2 + len(player1_list)):
                                if i >= len(player2_list) - 1:
                                    i = 0
                                list_cards_added_player2.append(player2_list[i])
                                value_player2_temp -= 1
                                index_player2 += 1
                                if index_player2 >= len(player2_list) - 1:
                                    index_player2 = 0
                        elif index_player2 + len(player1_list) - 1 < len(player2_list):
                            value_player2_temp = len(player1_list)
                            for i in range(index_player2, len(player2_list)):
                                list_cards_added_player2.append(player2_list[i])
                                value_player2_temp -= 1
                            index_player2 = 0
                            if value_player2_temp < len(player1_list) - len(list_cards_added_player2):
                                for i in range(0, value_player2_temp):
                                    list_cards_added_player2.append(player1_list[i])
                            else:
                                for i in range(0, len(player1_list) - len(list_cards_added_player2)):
                                    list_cards_added_player2.append(player2_list[i])
                        value_player2 = self.get_card_value(list_cards_added_player2[len(player1_list) - 1])
                        value_player1 = self.get_card_value(player1_list[index_player1 - 1])
                        value_player1_copy = value_player1
                        value_player2_copy = value_player2
                        if value_player2_copy > value_player1_copy:
                            for i in range(0, len(list_cards_added_player2)):
                                player2_list.insert(0, player1_list[i])
                            for i in range(len(player1_list) - 1, -1, -1):
                                player1_list.remove(player1_list[i])
                            continue
                        if value_player2_copy < value_player1_copy:
                            for i in range(0, len(list_cards_added_player2)):
                                player1_list.insert(0, list_cards_added_player2[i])
                            for i in range(len(list_cards_added_player1) - 1, -1, -1):
                                player2_list.remove(list_cards_added_player2[i])
                            continue
                        else:
                            if index_player2 == len(player2_list) - 1:
                                index_player2 = 0
                            else:
                                index_player2 += 1
                            if index_player1 == len(player1_list) - 1:
                                index_player1 = 0
                            else:
                                index_player1 += 1
                            continue
                else:
                    # get a random card from every list
                    player1_card_index = random.randint(1, len(player1_list) - 1)
                    player2_card_index = random.randint(1, len(player2_list) - 1)
                    score = self.compute_game(player1_list[player1_card_index], player2_list[player2_card_index])
                    list_cards_added_player1 = []
                    list_cards_added_player2 = []
                    if score == 1:
                        # here we will pick a number of random cards to add or remove to the list based on the list with less elements
                        if len(player1_list) > len(player2_list):
                            random_card_number = random.randint(0, len(player2_list) - 1)
                            for i in range(0, random_card_number):
                                list_cards_added_player2.append(player2_list[i])
                            for i in range(0, random_card_number):
                                player1_list.insert(0, player2_list[i])
                                index_player1 += 1
                            index_player1 += 1
                            for i in range(0, random_card_number):
                                player2_list.remove(list_cards_added_player2[i])
                            # put the index to 0 to start over again
                            index_player2 = 0
                        if len(player2_list) > len(player1_list):
                            random_card_number = random.randint(0, len(player1_list) - 1)
                            for i in range(0, random_card_number):
                                list_cards_added_player2.append(player2_list[i])
                            for i in range(0, random_card_number):
                                player1_list.insert(0, player2_list[i])
                                index_player1 += 1
                            index_player1 += 1
                            for i in range(0, random_card_number):
                                player2_list.remove(list_cards_added_player2[i])
                            index_player2 = 0
                        if score == 2:
                            # here we will pick a number of random cards to add or remove to the list based on the list with less elements
                            if len(player1_list) > len(player2_list):
                                random_card_number = random.randint(0, len(player2_list) - 1)
                                for i in range(0, random_card_number):
                                    list_cards_added_player1.append(player1_list[i])
                                for i in range(0, random_card_number):
                                    player1_list.remove(list_cards_added_player1[i])
                                index_player1 = 0
                                for i in range(0, random_card_number):
                                    player2_list.insert(player1_list[i])
                                    index_player2 += 1
                                index_player2 += 1
                            if len(player2_list) > len(player1_list):
                                random_card_number = random.randint(0, len(player2_list) - 1)
                                for i in range(0, random_card_number):
                                    player2_list.insert(0, player1_list[i])
                                    index_player2 += 1
                                index_player2 += 1
                                for i in range(0, random_card_number):
                                    list_cards_added_player1.append(player1_list[i])
                                for i in range(0, random_card_number):
                                    player1_list.remove(list_cards_added_player1[i])
                                index_player1 = 0
                        else:
                            if index_player2 == len(player2_list) - 1:
                                index_player2 = 0
                            else:
                                index_player2 += 1
                            if index_player1 == len(player1_list) - 1:
                                index_player1 = 0
                            else:
                                index_player1 += 1
                            continue

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
