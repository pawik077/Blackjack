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

def hit(player_cards, player_score, deck):
	player_cards.append(deck.pop(rd.randint(0, len(deck))))
	player_score += player_cards[-1].value
	for card in player_cards:
		while player_score > 21:
			if card.rank == 'A':
				card.value = 1
				player_score -= 10
	return player_cards, player_score

def main():
	deck = create_deck()
	player_cards = []
	dealer_cards = []
	player_score = 0
	dealer_score = 0
	while len(player_cards) < 2:
		player_cards, player_score = hit(player_cards, player_score, deck)
		dealer_cards, dealer_score = hit(dealer_cards, dealer_score, deck)
		print("Player cards:", player_cards)
		print("Dealer cards:", dealer_cards)
		print("Player score:", player_score)
		print("Dealer score:", dealer_score)
		if player_score == dealer_score == 21:
			print("Draw")
			break
		if player_score == 21:
			print("Player has blackjack!")
			print("Player wins!")
			break
		if dealer_score == 21:
			print("Dealer has blackjack!")
			print("Dealer wins!")
			break


	

if __name__ == '__main__':
	main()