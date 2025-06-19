# import random

# def create_deck():
#   suits = ["♥", "♦", "♣", "♠"]

#   ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

#   deck = []

#   for suit in suits: 
#     for rank in ranks: 
#       deck.append((suit, rank))

#   for card in deck:
#     rank, suit = card

#   random.shuffle(deck)
#   return deck

# def draw_card(deck, num_cards):
#   if len(deck) < num_cards: 
#     print("we don't have enough cards")
#     return [], deck 
#   else:
#     hand = []
#     for _ in range(num_cards):
#       if deck:
#         hand.append(deck.pop())
#       else:
#         break
#     return hand, deck

# deck = create_deck()
# while len(deck) > 0:
#   num_cards = int(input("How many cards do you want to draw? "))
#   hand, deck = draw_card(deck, num_cards)
#   print(hand[0])

# print("We are out of cards")

import random

def draw_card(deck, num_cards):
  hand = []
  for _ in range(num_cards):
    if deck:
      hand.append(deck.pop())
    else:
      break
  return hand, deck

def create_deck():
  suits = ["♥", "♦", "♣", "♠"]
  ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  deck = []

  for suit in suits:
    for rank in ranks:
      deck.append((suit, rank))

  return deck

deck = create_deck()
while len(deck) > 0:
  num_cards = int(input("How many cards do you want to draw? "))
  hand, deck = draw_card(deck, num_cards)
  print(hand[0])

print("We are out of cards")