import collections
from random import shuffle
import itertools

Card = collections.namedtuple('Card', ['rank', 'suit'])
g_all_combs = []

import collections
from collections import defaultdict

Card = collections.namedtuple('Card', ['rank', 'suit'])

suit_values = dict(joker=5,spades=3, hearts=2, diamonds=1, clubs=0)

"""============================================================== 
 Function Name : get_sliding_windows
 Inputs : chkstr : String for which all combination of Strings need to be extracted.
          Ex : input : spades => 1, 2 ,3,J,Q,K,A
               output : {'123','23J','3JQ','JQK','QKA}
=================================================================="""
def get_sliding_windows(chkstr):

    all_combs = []
    for i in range(3, 14):
        for j in range(0,14):
            if j+i < len(chkstr)+1:
                all_combs.append(''.join(chkstr[j:j+i]))
    return all_combs
"""============================================================== 
 Function Name : is_q_seq_missing
 Inputs : missing : Suits for which 3 Sequence Numbers is missing
          dicts : dict containing cards of Player
=================================================================="""
def is_q_seq_missing(dicts,missing):
    #print("m",missing)
    prev = 0
    curr = 0
    is_seq = 0
    mis_dicts = defaultdict(list)
    for k in dicts:
        #print("V",dicts[k])
        if k in missing:
            #print("k",k)
            for v in dicts[k]:

                try :
                    if (v == 'J'):
                        curr = 11
                    elif (v=='Q'):
                        curr = 12
                    elif (v=='K'):
                        curr = 13
                    elif (v == 'A'):
                        curr = 1
                    else :
                        curr = int(v)

                    if curr-prev == 1 or curr-prev==12:
                        is_seq+=1
                        #print(is_seq)
                        mis_dicts[k].append([curr,prev])
                    prev = curr

                except:
                    #print("v",v)
                    pass
                #print(type(v)==int)

    return is_seq,mis_dicts

"""=============================================== 
 Function Name : check_runs
 Inputs : player : Player Number
          dict : dict containing cards of Player
=================================================="""
def check_runs(player,dicts):
    miss_dicts = {}
    print(dicts)
    hasjoker = 0
    totRuns = 0
    hasRuns = set()
    missing = []
    for k in dicts:
        if k == 'joker':
            hasjoker = len(dicts[k])

        if len(dicts[k]) >= 3:
            all_rank_combs = get_sliding_windows(dicts[k])
            hasRuns = set(all_rank_combs).intersection(g_all_combs)

            if(hasRuns != set()):
                totRuns+=1
                res = max(len(ele) for ele in hasRuns)
                print("Has Runs", hasRuns,res,totRuns,k)
            else:
                missing.append(k)
        elif len(dicts[k]) == 2:
            missing.append(k)
    seq_missed = 0
    if hasjoker>0:
        seq_missed,miss_dicts = is_q_seq_missing(dicts,missing)
    if seq_missed >= hasjoker :
        totRuns = totRuns + hasjoker
    elif seq_missed<hasjoker and seq_missed>0:
        totRuns = totRuns + seq_missed

    print("<==================================>")
    print(f"Player-{player} Has {totRuns} Runs {hasRuns} ")
    print("HasJoker", hasjoker,f" miss_dicts {miss_dicts.keys()} {miss_dicts.values()} ")
    print("<==================================>")



"""=============================================== 
 Inputs : player : Player Number
          dict : dict containing cards of Player
=================================================="""

def check_pure_runs(player,dicts):
    ret = []

    totRuns = 0
    hasPureRuns = set()
    missing = []
    for k in dicts:

        if len(dicts[k]) >= 3:
            all_rank_combs = get_sliding_windows(dicts[k])
            # print("all_rank_combs---->",all_rank_combs)
            hasPureRuns = (set(all_rank_combs).intersection(g_all_combs))
            # print("InterSect",hasRuns)
            if (hasPureRuns != set()):
                totRuns += 1
                res = max(len(ele) for ele in hasPureRuns)
                print("Has Runs", hasPureRuns, res, totRuns)
            else:
                missing.append(k)
        elif len(dicts[k]) == 2:
            missing.append(k)

    print("<==================================>")
    print(f"Player-{player} Has {totRuns} Pure Runs {hasPureRuns}")
    print("<==================================>")
    return hasPureRuns
def get_scores(dicts):

    pass



def check_books(player,dicts):
    for k, values in dicts.items():
        for value in values:
            print(f'{k} - {value}',end = ",")
    print("\n")
    hasBooks = False
    ret = []
    for k in dicts:
        if len(dicts[k])>=3:
            hasBooks = True
            if ret == None:
                ret = [(k,dicts[k])]
            else:
                ret.append((k,dicts[k]))
    if(len(ret)>0):
        print(f'Player {player} Has ->{len(ret)} Books {ret}')
    else:
        print(f"player {player} has no books")

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

def sort_cards(cards):
    cards_sorted = sorted(sorted(cards, key=spades_high), key=lambda x: x[1])
    return cards_sorted
def get_global_assign():
    global g_all_combs
    g_all_combs = []
    chkstr = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    g_all_combs = get_sliding_windows(chkstr)

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA0')
    #print(ranks)
    suits = 'spades diamonds clubs hearts joker'.split()
    jokers = 'J1 J2'.split()

    def __init__(self):
        #print("Inited")
        self._cards = [Card(rank, suit) for suit in self.suits if suit not in 'joker' for rank in self.ranks if rank not in ['0']] + [Card(rank='0',suit='joker'),Card(rank='0',suit='joker')]
        #print(self._cards)
        #self._cards.append(jokers)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def shuffle(self):
        shuffle(self._cards)
        return self._cards


if __name__ == "__main__":
    deck = FrenchDeck()

    player_cards = []
    deck.shuffle()

    player_1_cards = deck[0:13]
    player_2_cards = deck[13:26]
    player_3_cards = deck[26:39]
    player_4_cards = deck[39:52]

    p_1_sorted = sort_cards(player_1_cards)
    p_2_sorted = sort_cards(player_2_cards)
    p_3_sorted = sort_cards(player_3_cards)
    p_4_sorted = sort_cards(player_4_cards)

    #print("player_cards")
    #print(p_1_sorted)
    #print(p_2_sorted)
    #print(p_3_sorted)
    #print(p_4_sorted)

    p_1_dict = defaultdict(list)
    p_2_dict = defaultdict(list)
    p_3_dict = defaultdict(list)
    p_4_dict = defaultdict(list)

    p_r_1_dict= defaultdict(list)
    p_r_2_dict= defaultdict(list)
    p_r_3_dict= defaultdict(list)
    p_r_4_dict= defaultdict(list)

    for p1,p2,p3,p4 in zip(p_1_sorted,p_2_sorted,p_3_sorted,p_4_sorted):
        #print(f'{p1.rank}{p1.suit},{p2.rank}{p2.suit},{p3.rank},{p2.suit},{p4.rank}{p2.suit}')
        p_1_dict[p1.suit].append(p1.rank)
        p_2_dict[p2.suit].append(p2.rank)
        p_3_dict[p3.suit].append(p3.rank)
        p_4_dict[p4.suit].append(p4.rank)

        p_r_1_dict[p1.rank].append(p1.suit)
        p_r_2_dict[p2.rank].append(p2.suit)
        p_r_3_dict[p3.rank].append(p3.suit)
        p_r_4_dict[p4.rank].append(p4.suit)

    """
    print(p_1_dict)
    print(p_2_dict)
    print(p_3_dict)
    print(p_4_dict)
    print(p_r_1_dict)
    print(p_r_2_dict)
    print(p_r_3_dict)
    print(p_r_4_dict)
    """

    check_books(1,p_r_1_dict)
    check_books(2,p_r_2_dict)
    check_books(3,p_r_3_dict)
    check_books(4,p_r_4_dict)
    print("-----!!!!!!!!!!!-----------")

    #check_runs(2, p_2_dict)
    #check_runs(3, p_3_dict)
    #check_runs(4, p_4_dict)
    print("-----!!!!!!!!!!!-----------")
    get_global_assign()
    #global g_all_combs


    check_runs(1, p_1_dict)
    check_pure_runs(1, p_1_dict)
    #print(has_sequence(['8','9', '10'], ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '0']))
