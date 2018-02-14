class Card:
	def __init__(self, obj):
		self.question = obj['question'].lstrip()
		self.answer = obj['answer'].lstrip()
		self.category = obj['category'].lstrip()
		self.num_correct = int(obj['correct'])
		self.num_answered = int(obj['answered'])
		self.previous_answer = obj['previous_answer'].lstrip()

	def answered(self, correct):
		self.num_answered += 1

		if correct is True:
			self.num_correct += 1
			self.previous_answer = 'True'
		else:
			self.previous_answer = 'False'
