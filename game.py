import csv
from card import Card

class Game:
	def __init__(self):
		self.cards = []
		with open('problems.csv') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				self.cards.append(Card(row))

	def play(self):
		for card in self.cards:
			print(card.question)
			answer = raw_input()
			self.submit_answer(answer, card)

	def submit_answer(self, answer, card):
		if answer == card.answer:
			card.answered(True)
			print('Correct!')
			print(card.num_correct)
		else:
			card.answered(False)
			print('Incorrect!')
			print('The correct answer was %s') % card.answer

game = Game()
game.play()
