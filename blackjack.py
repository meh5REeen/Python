import random
from art import logo
#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
is_playing = True
def score(list):
    scores = 0
    for i in list:
        scores += i
        if (i == 11) & scores > 21:
            list.remove(i)
            list.append(1)
    if (len(list) == 2) and scores == 21:
        return 0
    return scores

def deal():
    card = int(random.choice(cards))
    return card



def compare(comp , user):
    if user == 0:
        print("User won")
    elif comp == 0:
        print("Computer won")
    elif user == 21:
        print("User won")
    elif comp == 21:
        print("Computer won")
    elif user > 21:
        print("BUST! Computer Won")
    elif comp > 21:
        print(" BUST! User Won")
    elif user == comp:
        print("Draw! ")
    elif user > comp:
        print("User Won")
    elif comp > user:
        print("Computer Won")


    print(f"User Score: {user}\nComputer Score: {comp}")

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
while is_playing:
    print(logo)
    user_cards = []
    user_cards.append(deal())
    user_cards.append(deal())

    user_sum = score(user_cards)


    print(f"You have the cards: {user_cards}.\nIt sums up to {user_sum}")


    computer_cards = []
    computer_cards.append(deal())
    computer_cards.append(deal())
    comp_sum = score(computer_cards)



    print(f"Computer has the card: {computer_cards[0]}.\nIt sums up to {comp_sum}")



    #Hint 6: Create a function called calculate_score() that takes a List of cards as input
    #and returns the score.


        #Look up the sum() function to help you do this.


    if user_sum == 21:
        print("User won")
    elif comp_sum == 21 :
        print("Computer  won")
    else:
        play = input("Do you wanna draw another card? 'y ' or 'n'")
        if play == 'y':
            user_cards.append(deal())
            user_sum = score(user_cards)
            while comp_sum <17:
                computer_cards.append(deal())
                comp_sum = score(computer_cards)

    compare(comp_sum,user_sum)

    play = input("Do you wanna keep  playing? 'y' or 'n'")
    if play == 'n':
        is_playing = False

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

