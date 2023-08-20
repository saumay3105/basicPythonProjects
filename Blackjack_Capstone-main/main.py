# Blackjack_Capstone_Project
from numpy import random
from art import logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    """Returns a random card from deck"""
    card = random.choice(cards)
    return card
def calc_score(card_list):
    """Take a list of cards and calculate the score"""
    if sum(card_list)==21 and len(card_list) == 2:
        return 0
    if 11 in card_list and sum(card_list)>21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)
def compare_score(user_score, computer_score):
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "Lose, Dealer has Blackjack"
    elif user_score==0:
        return "Win, with a blackjack"
    elif user_score>21:
        return "Bust! Dealer Wins"
    elif computer_score>21:
        return "Dealer Busts, You Win"
    elif user_score>computer_score:
        return "You Win"
    else:
        return " You Lose"
def play_game():
    user_card = []
    computer_card = []
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    is_game_over = False
    while not is_game_over:
        user_score = calc_score(user_card)
        computer_score = calc_score(computer_card)
        print(f"Your cards are {user_card} and score is {user_score}")
        print(f"Dealer's first card is {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score>21:
            is_game_over = True
        else:
            user_should_deal = input("Enter y to deal another card and n to pass:").lower()
            if user_should_deal=="y":
                user_card.append(deal_card())
            else:
                is_game_over= True
    while computer_score!=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score = calc_score(computer_card)
    print(f"Your final hand is {user_card} and score is {user_score}")
    print(f"Dealer's final hand is {computer_card} and final score is {computer_score}")
    print(compare_score(user_score,computer_score))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()