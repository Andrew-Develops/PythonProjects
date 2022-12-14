############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
import random
from replit import clear
from art import logo

def deal_card():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated by the cards"""
#  if 11 in cards and 10 in cards and len(cards)==2:
  if sum(cards) == 21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)==21:
    cards.remove(11)
    cards.append(1)
    
  return sum(cards)

def compare(user_score,computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0 :
    return "Lose, opponent has Blackjack"
  elif user_score == 0 :
    return "You win with a Blackjack"
  elif user_score > 21 :
    return "You went over. You lose"
  elif computer_score > 21 :
    return "Opponent went over. You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"

def blackjack_game():
  print(logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  my_cards = []
  computer_cards = []
  is_game_over = False
  #Pick my cards and computer cards
  for _ in range (2):
    my_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(my_cards)
    computer_score = calculate_score(computer_cards)
  
    #Print first set of cards
    print(f"   Your cards: {my_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")
  
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      deal_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if deal_another_card == 'y':
        my_cards.append(deal_card())
      elif deal_another_card == 'n':
        is_game_over = True
 
  while computer_score < 17 and computer_score !=0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  
  print(f"  Your final hand: {my_cards}, current score: {user_score}")
  print(f"  Computer final hand: {computer_cards}, current score: {computer_score}")
  print(compare(user_score, computer_score))
   
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  blackjack_game()
print("Thank you for the game. I hope to see you again soon. ")
