import sys
import time
import itertools

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))


value = { '2':  0, '3':  1, '4':  2, '5':  3, '6':  4, 
          '7':  5, '8':  6, '9':  7, 'T':  8, 'J':  9, 
          'Q': 10, 'K': 11, 'A': 12 }

value_joker = { '2':  0, '3':  1, '4':  2, '5':  3, '6':  4, 
                '7':  5, '8':  6, '9':  7, 'T':  8, 'J':  -1, 
                'Q': 10, 'K': 11, 'A': 12 }


def five_of_a_kind(cards):
    card_set = set(cards)
    if len(card_set) == 1:
        return 6
    return 0


def four_of_a_kind(cards):
    card_set = set(cards)
    if len(card_set) == 2:
        for card in card_set:
            if cards.count(card) == 4:
                return 5
    return 0


def three_of_a_kind(cards):
    card_set = set(cards)
    for card in card_set:
        if cards.count(card) == 3:
            return 3
    return 0
    
    
def two_pair(cards):
    card_set = set(cards)
    if len(card_set) == 3:
        for card in card_set:
            if cards.count(card) == 2:
                return 2
    return 0


def full_house(cards):
    card_set = set(cards)
    if three_of_a_kind(cards):
        if len(set(cards)) == 2:
            return 4
    return 0


def pair(cards):
    card_set = set(cards)
    if len(card_set) != len(cards):
        return 1
    return 0


def joker_transform(cards):
    joker_count = cards.count('J')
    if joker_count == 0:
        return cards

    transform_cards = []

    cards_set = set(cards)
    cards_set.remove('J')
    
    if len(cards_set) == 0:
        return "AAAAA"

    for card in cards_set:
        transform = cards.replace('J', card, joker_count)
        transform_cards.append((transform, 0, evaluate_cards(transform)))

    transform_cards = sorted(transform_cards, key=compare_cards, reverse=True)

    return transform_cards[0][0]

def evaluate_cards(cards, joker=False):
    if joker:
        cards = joker_transform(cards)
    
    score = 0
    
    score = five_of_a_kind(cards)
    if score != 0:
        return score

    score = four_of_a_kind(cards)
    if score != 0:
        return score

    score = full_house(cards)
    if score != 0:
        return score
    
    score = three_of_a_kind(cards)
    if score != 0:
        return score
    
    score = two_pair(cards)
    if score != 0:
        return score
    
    score = pair(cards)
    if score != 0:
        return score

    return score


def compare_cards(hand):
    cards, strength = hand[0], hand[2]
    return strength, value[cards[0]], value[cards[1]], value[cards[2]], value[cards[3]], value[cards[4]]

def compare_cards_p2(hand):
    cards, strength = hand[0], hand[2]
    return strength, value_joker[cards[0]], value_joker[cards[1]], value_joker[cards[2]], value_joker[cards[3]], value_joker[cards[4]]



def part_1(data):
    hands = []
    for hand in data:
        cards, score = hand.split()
        strength = evaluate_cards(cards)
        hands.append((cards, int(score), strength))


    sorted_hands = sorted(hands, key=compare_cards, reverse=True)
    hand_count = len(sorted_hands)
    sum = 0

    for idx, hand in enumerate(sorted_hands):
        cards, score = hand[0], hand[1]
        factor = hand_count - idx
        sum += factor * int(score)

    return sum

def part_2(data):
    hands = []
    for hand in data:
        cards, score = hand.split()
        strength = evaluate_cards(cards, True)
        hands.append((cards, int(score), strength))

    sorted_hands = sorted(hands, key=compare_cards_p2, reverse=True)
    hand_count = len(sorted_hands)
    sum = 0


    for idx, hand in enumerate(sorted_hands):
        cards, score = hand[0], hand[1]
        factor = hand_count - idx
        sum += factor * int(score)

    return sum

input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")