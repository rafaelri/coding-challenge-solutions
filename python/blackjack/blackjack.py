from functools import reduce

def aces_value(aces, non_aces_total):
    if len(aces) == 0:
        return 0
    missing = 21 - non_aces_total
    with_11 = 11 + len(aces)-1
    without_11 = len(aces)
    if with_11 <= missing:
        return with_11
    else:
        return without_11

def card_value(card):
    if "Q" == card or "J" == card or "K" == card:
        return 10
    else:
        return int(card)

def value(hand):
    count = len(hand)
    aces = filter(lambda x: x == "A", hand)
    non_aces = filter(lambda x: x != "A", hand)
    non_aces_value = map(lambda x: card_value(x), non_aces)
    non_aces_total = reduce(lambda x,y: x+y, non_aces_value, 0)
    aces_total = aces_value(list(aces), non_aces_total)
    return non_aces_total + aces_total
print(value(["2","2", "3"]))
print(value(["A", "A"]))
twenty_one_aces = ["A"] * 21
print(value(twenty_one_aces))

