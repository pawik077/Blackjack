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

def main():
	deck = create_deck()
	player_cards = []
	dealer_cards = []
	player_score = 0
	dealer_score = 0
	while len(player_cards) < 2:
		player_cards.append(deck.pop(rd.randint(0, len(deck))))
		player_score += player_cards[-1].value
		if len(player_cards) == 2:
			if player_cards[0].rank == player_cards[1].rank == 'A':
				player_cards[0].value = 1
				player_score -= 10
		dealer_cards.append(deck.pop(rd.randint(0, len(deck))))
		dealer_score += dealer_cards[-1].value
		if len(dealer_cards) == 2:
			if dealer_cards[0].rank == dealer_cards[1].rank == 'A':
				dealer_cards[0].value = 1
				dealer_score -= 10
		print("Player cards:", player_cards)
		print("Dealer cards:", dealer_cards)
		print("Player score:", player_score)
		print("Dealer score:", dealer_score)

	

if __name__ == '__main__':
	main()