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

def round(bet):
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
		print(f"Dealer cards: [{dealer_cards[0]}{f', {dealer_cards[1]}' if dealer_score == 21 or player_score == 21 else ', ?' if len(dealer_cards) > 1 else ''}]")
		if player_score == dealer_score == 21:
			print("Push!")
			return 0
		if player_score == 21:
			print("Player has blackjack!")
			print(f"Player wins {bet * 1.5} tokens!")
			return bet * 1.5
		if dealer_score == 21:
			print("Dealer has blackjack!")
			print("Dealer wins!")
			print(f"Player loses {bet} tokens!")
			return -bet
	while player_score < 21:
		print()
		if player_cards[0].rank == player_cards[1].rank and len(player_cards) == 2:
			choice = input("What do you want to do? (h for hit, s for split, d for double down, or q for stand) ")
		elif len(player_cards) == 2:
			choice = input("What do you want to do? (h for hit, d for double down, or q for stand) ")
		else:
			choice = input("What do you want to do? (h for hit or q for stand) ")
		if len(choice) != 1 or choice.upper() not in ('HDQS' if player_cards[0].rank == player_cards[1].rank and len(player_cards) == 2 else 'HDQ' if len(player_cards) == 2 else 'HQ'):
			print("Invalid input!")
			continue
		if choice.upper() == 'H':
			player_cards = hit(player_cards, deck)
			player_score = sum(c.value for c in player_cards)
			print("Player cards:", player_cards)
			if player_score > 21:
				print("Player has busted!")
				print("Dealer wins!")
				print(f"Player loses {bet} tokens!")
				return -bet
			elif player_score == 21: break
		elif choice.upper() == 'D':
			if len(player_cards) != 2:
				print("You can only double down on your first turn!")
				continue
			bet = bet * 2
			print("You double your bet to", bet)
			player_cards = hit(player_cards, deck)
			player_score = sum(c.value for c in player_cards)
			print("Player cards:", player_cards)
			if player_score > 21:
				print("Player has busted!")
				print("Dealer wins!")
				print(f"Player loses {bet} tokens!")
				return -bet
			break
		elif choice.upper() == 'S':
			if len(player_cards) != 2 or player_cards[0].rank != player_cards[1].rank:
				print("You can only split on your first turn if you have two cards of the same rank!")
				continue
			print("You split your hand into two hands.")
			player_cards = [[player_cards[0]], [player_cards[1]]]
			bet = [bet, bet]
			player_cards[0] = hit(player_cards[0], deck)
			player_cards[1] = hit(player_cards[1], deck)
			player_score = [sum(c.value for c in player_cards[0]), sum(c.value for c in player_cards[1])]
			print("Player cards:", player_cards)
			if player_score[0] == 21:
				print("Player has blackjack in first hand!")
				bet[0] = bet[0] * 1.5
			else:
				print("You play your first hand.")
				while player_score[0] < 21:
					if len(player_cards[0]) == 2:
						choice = input("What do you want to do? (h for hit, d for double down, or q for stand) ")
					else:
						choice = input("What do you want to do? (h for hit or q for stand) ")
					if len(choice) != 1 or choice.upper() not in ('HDQ' if len(player_cards[0]) == 2 else 'HQ'):
						print("Invalid input!")
						continue
					if choice.upper() == 'H':
						player_cards[0] = hit(player_cards[0], deck)
						player_score[0] = sum(c.value for c in player_cards[0])
						print("Player cards:", player_cards)
						if player_score[0] > 21:
							print("Player has busted!")
							print("Dealer wins!")
							bet[0] = -bet[0]
							break
						elif player_score[0] == 21: break
					elif choice.upper() == 'D':
						if len(player_cards[0]) != 2:
							print("You can only double down on your first turn!")
							continue
						bet[0] = bet[0] * 2
						print("You double your bet to", bet[0])
						player_cards[0] = hit(player_cards[0], deck)
						player_score[0] = sum(c.value for c in player_cards[0])
						print("Player cards:", player_cards)
						if player_score[0] > 21:
							print("Player has busted!")
							print("Dealer wins!")
							bet[0] = -bet[0]
							break
						break
					elif choice.upper() == 'Q':
						break
			if player_score[1] == 21:
				print("Player has blackjack in second hand!")
				bet[1] = bet[1] * 1.5
			else:
				print("You play your second hand.")
				while player_score[1] < 21:
					choice = input("What do you want to do? (h for hit or q for stand) ")
					if len(choice) != 1 or choice.upper() not in 'HQ':
						print("Invalid input!")
						continue
					if choice.upper() == 'H':
						player_cards[1] = hit(player_cards[1], deck)
						player_score[1] = sum(c.value for c in player_cards[1])
						print("Player cards:", player_cards)
						if player_score[1] > 21:
							print("Player has busted!")
							print("Dealer wins!")
							bet[1] = -bet[1]
							break
						elif player_score[1] == 21: break
					elif choice.upper() == 'Q':
						break
				break
		elif choice.upper() == 'Q':
			break
	print("Dealer cards:", dealer_cards)
	while dealer_score < 17:
		print()
		dealer_cards = hit(dealer_cards, deck)
		dealer_score = sum(c.value for c in dealer_cards)
		print("Dealer cards:", dealer_cards)
		if dealer_score > 21:
			print("Dealer has busted!")
			if type(bet) is list:
				print(f"Player wins {sum(bet)} tokens!")
				return sum(bet)
			else:
				print(f"Player wins {bet} tokens!")
				return bet
		elif dealer_score == 21: break
	if type(player_score) is list:
		if player_score[0] > dealer_score:
			print("Player wins first hand!")
		else:
			print("Dealer wins first hand!")
			bet[0] = -bet[0]
		if player_score[1] > dealer_score:
			print("Player wins second hand!")
		else:
			print("Dealer wins second hand!")
			bet[1] = -bet[1]
		if sum(bet) > 0:
			print(f"Player wins {sum(bet)} tokens!")
		elif sum(bet) < 0:
			print(f"Player loses {sum(bet)} tokens!")
		else:
			print("Push!")
		return sum(bet)
	else:
		if player_score > dealer_score:
			print(f"Player wins {bet} tokens!")
			return bet
		elif player_score < dealer_score:
			print("Dealer wins!")
			print(f"Player loses {bet} tokens!")
			return -bet
		else:
			print("Push!")
			return 0

def main():
	print("Welcome to Blackjack!")
	print("The goal of the game is to get as close to 21 as possible without going over.")
	print("Aces can be worth 1 or 11.")
	print("Jacks, Queens, and Kings are worth 10.")
	print("Have fun!")
	print()
	tokens = 100
	while tokens > 0:
		print(f'You now have {tokens} tokens.')
		print()
		bet = input("How much do you want to bet? (q to quit) ")
		if bet == 'q':
			print(f"You leave the table with {tokens} tokens.")
			print("Goodbye!")
			return
		if not bet.isdigit():
			print("Invalid input!")
			continue
		bet = int(bet)
		if bet > tokens:
			print("You don't have enough tokens!")
			continue
		tokens += round(bet)

if __name__ == '__main__':
	main()