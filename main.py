import random as rd
CARD_SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
CARD_SUIT_SYMBOLS = {'Spades': '♠', 'Hearts': '♥', 'Diamonds': '♦', 'Clubs': '♣'}
CARD_RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = self.get_value()
		self.name = self.get_name()

	def get_value(self):
		if self.rank == 'A':
			return 11
		elif self.rank == 'J' or self.rank == 'Q' or self.rank == 'K':
			return 10
		else:
			return int(self.rank)

	def get_name(self):
		return self.rank + CARD_SUIT_SYMBOLS[self.suit]
	def __repr__(self):
		return self.name

def create_deck():
	deck = []
	for suit in CARD_SUITS:
		for rank in CARD_RANKS:
			deck.append(Card(suit, rank))
	return deck

def hit(cards, deck):
	cards.append(deck.pop(rd.randint(0, len(deck) - 1)))
	c = 0
	while sum(c.value for c in cards) > 21 and c < len(cards):
		if cards[c].rank == 'A':
			cards[c].value = 1
		c += 1
	return cards

def main():
	deck = create_deck()
	player_cards = []
	dealer_cards = []
	player_score = 0
	dealer_score = 0
	while len(player_cards) < 2:
		player_cards = hit(player_cards, deck)
		dealer_cards = hit(dealer_cards, deck)
		player_score = sum(c.value for c in player_cards)
		dealer_score = sum(c.value for c in dealer_cards)
		print("Player cards:", player_cards)
		print("Dealer cards:", dealer_cards)
		print("Player score:", player_score)
		print("Dealer score:", dealer_score)
		if player_score == dealer_score == 21:
			print("Draw")
			quit()
		if player_score == 21:
			print("Player has blackjack!")
			print("Player wins!")
			quit()	
		if dealer_score == 21:
			print("Dealer has blackjack!")
			print("Dealer wins!")
			quit()	
	while player_score < 21:
		choice = input("Hit or stand? (h/s) ")
		if len(choice) != 1 or choice.upper() not in 'HS':
			print("Invalid input!")
			continue
		if choice.upper() == 'H':
			player_cards = hit(player_cards, deck)
			player_score = sum(c.value for c in player_cards)
			print("Player cards:", player_cards)
			print("Player score:", player_score)
			if player_score > 21:
				print("Player has busted!")
				print("Dealer wins!")
				quit()
			elif player_score == 21: break
		elif choice.upper() == 'S':
			break
	while dealer_score < 17:
		dealer_cards = hit(dealer_cards, deck)
		dealer_score = sum(c.value for c in dealer_cards)
		print("Dealer cards:", dealer_cards)
		print("Dealer score:", dealer_score)
		if dealer_score > 21:
			print("Dealer has busted!")
			print("Player wins!")
			quit()
		elif dealer_score == 21: break
	if player_score > dealer_score:
		print("Player wins!")
	elif player_score < dealer_score:
		print("Dealer wins!")
	else:
		print("Draw")

if __name__ == '__main__':
	main()