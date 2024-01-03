import random


# 生成一副扑克牌
def playing_cards(number):
    suits = ['♥', '♦', '♣', '♠']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    deck = []
    for suit in suits:
        num = 2
        for rank in ranks:
            deck.append([suit + rank])
            deck[-1].append(num)
            num += 1

    # 给5个玩家随机发牌
    player_hands = []
    for _ in range(number):
        hand = random.sample(deck, 3)
        player_hands.append(hand)
        for card in hand:
            deck.remove(card)

    # 分牌
    ranks = []
    suits = []
    pai = []

    for card in player_hands:
        r = [tile[1] for tile in card]
        s = [tile[0][0] for tile in card]
        p = [tile[0][1:] for tile in card]

        ranks.append(r)
        suits.append(s)
        pai.append(p)
    return ranks, suits, pai


# 冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 计算牌型
def calculate(a, b):
    a = bubble_sort(a)
    if len(set(b)) == 1:  # 同花
        if int(a[2]) - int(a[0]) == 2:
            return '同花顺'
        else:
            return '同花'

    elif len(set(a)) == 2:  # 对子
        return '对子'

    elif int(a[2]) - int(a[0]) == 2:
        return '顺子'

    elif len(set(a)) == 1:  # 豹子
        return '豹子'

    elif len(set(a)) == 3:  # 单张
        return '单张'


# # 比大小
def compare_hands(a, c):
    times = {'豹子': 100000, '同花顺': 10000, '同花': 1000, '顺子': 100, '对子': 10, '单张': 1}
    for k, j in times.items():
        if c == k:
            max_rank = (int(a[0]) * 0.1 + int(a[1]) * 1 + int(a[2]) * 10) * j
            return max_rank


dd = {}
ranks, suits, pai = playing_cards(17)
for i in range(len(suits)):
    qq = calculate(ranks[i], suits[i])
    ss = compare_hands(ranks[i], qq)
    dd[ss] = i + 1
    print('{0}号玩家的牌型是{1}'.format(i + 1, qq),
          suits[i][0] + pai[i][0] + suits[i][1] + pai[i][1] + suits[i][2] + pai[i][2])
ff = max(dd.keys())
print('恭喜{}号玩家获取了胜利！！！！'.format(dd.get(ff)))
