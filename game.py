import csv, os
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
		else:
			card.answered(False)
			print('Incorrect!')
			print('The correct answer was %s') % card.answer
		self.save()

	def save(self):
		with open('temp.csv', 'w') as tempfile:
			fieldnames = ['question', 'answer', 'category', 'correct', 'answered']
			writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
			writer.writeheader()
			for card in self.cards:
				writer.writerow({
					'question': card.question,
					'answer': card.answer,
					'category': card.category,
					'correct': card.num_correct,
					'answered': card.num_answered
				})
		os.rename('temp.csv', 'problems.csv')

game = Game()
game.play()
