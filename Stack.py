#Implementing a stack using Python

class Stack:
	def __init__(self):
		self.items = []

	#Check whether the stack is empty
	def is_empty(self):
		return self.items == []

	#Get the length of stack
	def get_length(self):
		return len(self.items)

	#Push operation
	def push(self,item):
		self.items.append(item)

	#Pop operation
	def pop(self):
		return self.items.pop()

	#Peek at the top most element in the stack
	def peek(self):
		if not self.is_empty():
			return self.items[-1]
		else:
			return "Stack empty"

	#Return items in the stack
	def get_stack(self):
		return self.items

	#Reverse a string using stack
	def reverse_string(self, text):
		for letter in text:
			self.push(letter)
		print(self.get_stack())
		result = ""
		#for i in range(self.get_length()):
		while not self.is_empty():
			result += self.pop()
		print(result)
		return

	#Convert an decimal number to binary using stack
	def int_to_bin(self,int_num):
		while int_num:
			rem = int_num % 2
			self.push(rem)
			int_num //= 2
			#print(int_num)
		#print()
		#print(int_num)
		print(self.get_stack())
		result = ""
		while not self.is_empty():
			result += str(self.pop())
		print(result)
		return

	#To be used in the next function
	def is_match(self, p1, p2):
		if p1 == "(" and p2 == ")":
			return True
		elif p1 == "[" and p2 == "]":
			return True
		elif p1 == "{" and p2 == "}":
			return True
		else:
			return False

	"""
	Use a stack to check whether or not a string
	has balanced usage of parenthesis.

	Example:
	    (), ()(), (({[]}))  <- Balanced.
	    ((), {{{)}], [][]]] <- Not Balanced.

	Balanced Example: {[]}
	Non-Balanced Example: (()
	Non-Balanced Example: ))
	"""
	def balanced_parenthesis(self,text):
		is_balanced = True
		index = 0

		while index < len(text) and is_balanced:
			paren = text[index]
			if paren in "({[":
				self.push(paren)
			else:
				if self.is_empty():
					#Stack is empty and no opening parenthesis
					#is encountered. Unbalanced
					is_balanced = False
				else:
					top = self.pop()
					if not self.is_match(top, paren):
						is_balanced = False
			index += 1

		if self.is_empty() and is_balanced:
			return True
		else:
			return False
