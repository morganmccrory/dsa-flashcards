import csv, os, pprint
from options import options
from card import Card

class Game:
	def __init__(self):
		self.cards = []
		with open('problems.csv') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				self.cards.append(Card(row))

	def play(self):
		print('Let\'s go over some data structures and algorithms!')
		category = self.choose_category()
		category_cards = self.get_category_cards(category)
		for card in category_cards:
			self.ask_question(card)
		self.end_game(category, category_cards)

	def choose_category(self):
		print('Choose a category:')
		pprint.pprint(options)
		try:
			user_choice = int(raw_input())
			return options.get(user_choice)
		except:
			print("Oops! You must enter a number. Exiting game.")

	def get_category_cards(self, category):
		if category == 'All':
			return self.cards
		elif category == 'Cards Answered Wrong Last Time':
			return self.get_cards_answered_wrong()

		cards = []
		for card in self.cards:
			if card.category == category:
				cards.append(card)

		return cards

	def ask_question(self, card):
		print(card.question)
		answer = raw_input()
		self.submit_answer(answer, card)

	def submit_answer(self, answer, card):
		if answer == card.answer:
			card.answered(True)
			print('Correct!')
		else:
			card.answered(False)
			print('Incorrect!')
			print('The correct answer was %s') % card.answer
		self.save()

	def get_cards_answered_wrong(self):
		cards = []
		for card in self.cards:
			if card.previous_answer == 'False':
				cards.append(card)

		return cards

	def save(self):
		with open('temp.csv', 'w') as tempfile:
			fieldnames = ['question', 'answer', 'category', 'correct', 'answered', 'previous_answer']
			writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
			writer.writeheader()
			for card in self.cards:
				writer.writerow({
					'question': card.question,
					'answer': card.answer,
					'category': card.category,
					'correct': card.num_correct,
					'answered': card.num_answered,
					'previous_answer': card.previous_answer
				})
		os.rename('temp.csv', 'problems.csv')

	def end_game(self, category, cards):
		if not category:
			return None

		print('That\'s all of the questions in %s! Would you like to play again? Type "yes" or "no".' % category) 
		response = raw_input()
		if response == 'yes':
			game.play()
		else:
			print('Thanks for playing!')

game = Game()
game.play()
