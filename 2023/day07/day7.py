import re 
from collections import Counter
import copy

file = open('7ex.in', 'r')
file = open('7.in', 'r')
lines = file.readlines()
ans1 = 0
ans2 = 0
# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
#   Five of a kind, where all five cards have the same label: AAAAA
#   Four of a kind, where four cards have the same label and one card has a different label: AA8AA
#   Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
#   Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
#   Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
#   One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
#   High card, where all cards' labels are distinct: 23456

def check_four_of_a_kind(hand):
    for c in hand:
        if hand.count(c) == 4:
            return True 
    return False

def check_full_house(hand):
    c = Counter(hand)
    if(len(c) == 2):
        return True
    return False

def check_three_of_a_kind(hand):
    c = Counter(hand)
    for x in c:
        if c[x] == 3:
            return True 
    return False

def check_two_pairs(hand):
    c = Counter(hand)
    pairCnt = 0
    for x in c:
        if c[x] == 2:
            pairCnt += 1
        if pairCnt == 2:
            return True 
    return False    

def check_one_pairs(hand):
    c = Counter(hand)
    for x in c:
        if c[x] == 2:
            return True
    return False 

def replaceMax(hand):
    for i in range(len(hand)):
        if hand[i] == -1:
            hand[i] = max(hand)
    return hand

def replaceMaxCnt(hand):
    c = Counter(hand)
    repWith = ("",0)
    for xx in c:
        if xx != -1:
            if c[xx] > repWith[1]:
                repWith = (xx,c[xx])
    for i in range(len(hand)):
        if hand[i] == -1:
            hand[i] = repWith[0]
    return hand

def replaceJoker(hand):
    handOld = copy.deepcopy(hand)
    for i in range(len(hand)):
        if(hand[i] == 1):
            hand[i] = -1
    if hand.count(-1) == 5:
        hand = [14 for x in range(5)]
    elif check_four_of_a_kind(hand) or check_full_house(hand):
        # jjjj+x // xxxx+j
        # jj + xxx // xx + jjj
        hand = replaceMax(hand)
    elif check_three_of_a_kind(hand):
        # jjj + x + y // xxx + 
        if(hand.count(-1) == 3):
            hand = replaceMax(hand)
        else:
            hand = replaceMaxCnt(hand)
    elif check_two_pairs(hand):
        # jj + xx + y // xx + yy + j 
        if hand.count(-1) == 2:
            hand = replaceMaxCnt(hand)
        else:
            hand = replaceMax(hand)
    elif check_one_pairs(hand):
        # jj + x + y + z // 
        if(hand.count(-1) == 2):
            hand = replaceMax(hand)
        else:
            hand = replaceMaxCnt(hand)
    else: 
        hand = replaceMax(hand)

    return hand 

def solve(prt):
    ans = 0
    handsSor = {"five" : [], "four" : [], "fullHouse" : [], "three" : [], "twoPair" : [],"onePair" : [], "high" : []}
    cnt = 0
    card_order_dict1 = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}
    card_order_dict2 = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":1, "Q":12, "K":13, "A":14}
    for l in lines:
        cnt += 1
        l = l.strip()
        hand,bid = l.split()
        # hand = sorted(hand,reverse=True)
        # hand = [card_order_dict[c] for c in hand]
        if(prt == 1):
            hand = [card_order_dict1[c] for c in hand]
        else:
            hand = [card_order_dict2[c] for c in hand]

        handOld2 = copy.deepcopy(hand)
        if(1 in hand):
            hand = replaceJoker(hand)


        if( len(list(set(hand))) == 1):
            handsSor["five"].append((handOld2,hand,bid))
        elif check_four_of_a_kind(hand):
            handsSor["four"].append((handOld2,hand,bid))
        elif check_full_house(hand):
            handsSor["fullHouse"].append((handOld2,hand,bid))
        elif check_three_of_a_kind(hand):
            handsSor["three"].append((handOld2,hand,bid))
        elif check_two_pairs(hand):
            handsSor["twoPair"].append((handOld2,hand,bid))
        elif check_one_pairs(hand):
            handsSor["onePair"].append((handOld2,hand,bid))
        else:
            handsSor["high"].append((handOld2,hand,bid))




    for h in handsSor:
        # for x in range(len(handsSor[h])):
        #     asdf = [card_order_dict[c] for c in handsSor[h][x][0]]
        #     handsSor[h][x] = (asdf,handsSor[h][x][1])
        sor = sorted(handsSor[h],reverse=True)
            
        # print(h,handsSor[h])
        for xx in sor:
            handold,hand,y = xx 
            y = int(y)
            ans += cnt*y 
            # if 11 in handold:
            #     print(h,xx)
            cnt -= 1
    return ans


#ans2 != 253704057
#ans2 != 253282553
#ans2 != 253277450
#ans2 != 253265670
#ans2 != 253270807
#ans2 != 253791366
#ans2 != 253200817
#ans2 != 253553070
#ans2 != 253824930
#ans2 != 253231362
#ans2 != 253157581

print("----------")
print("ans1:",solve(1))
print("ans2:",solve(2))

