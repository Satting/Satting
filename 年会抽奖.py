# import random
# import time
#
# staff = ['张三', '李四', '王五', '赵六']
# list1 = ['泰国5日游+手术费报销', 'iPhone14手机', '三斤苹果']
# for i in range(3, 0, -1):
#     print('路飞科技年会抽奖{}等奖抽奖开始啦！！！'.format(i))
#     for k in range(i, i + 1):
#         num = random.choice(staff)
#         print('抽奖中........................')
#         time.sleep(1)
#         print('恭喜{0}抽到了{1}！！！'.format(num, list1[i - 1]))
#         print('')
#         staff.remove(num)
#         time.sleep(1)
# print('路飞科技年会抽奖结束')


# import random
# from enum import Enum, auto
#
# class Suit(Enum):
#     HEARTS = auto()
#     DIAMONDS = auto()
#     CLUBS = auto()
#     SPADES = auto()
#
# class Rank(Enum):
#     TWO = auto()
#     THREE = auto()
#     FOUR = auto()
#     FIVE = auto()
#     SIX = auto()
#     SEVEN = auto()
#     EIGHT = auto()
#     NINE = auto()
#     TEN = auto()
#     JACK = auto()
#     QUEEN = auto()
#     KING = auto()
#     ACE = auto()
#
# class PlayingCard:
#     def __init__(self, suit, rank):
#         self.suit = suit
#         self.rank = rank
#
# def generate_deck():
#     deck = [PlayingCard(suit, rank) for suit in Suit for rank in Rank]
#     return deck
#
# def distribute_hands(deck, num_players, num_cards_in_hand):
#     random.shuffle(deck)
#     hands = [deck[i*num_cards_in_hand:(i+1)*num_cards_in_hand] for i in range(num_players)]
#     return hands
#
# # Other functions such as sorting, calculating hand type, and comparing hands can be defined here
#
# def main():
#     num_players = 17
#     num_cards_in_hand = 3
#
#     deck = generate_deck()
#     player_hands = distribute_hands(deck, num_players, num_cards_in_hand)
#
#     # Conduct the game logic to determine the winner and print the result...
#
# if __name__ == "__main__":
#     main()