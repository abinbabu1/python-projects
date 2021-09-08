#Implementing Linked List

class Node():

	def __init__(self, data, nextb):
		self.data = data
		self.nextb = nextb

class LinkedList():

	def __init__(self):
		self.head = None

	def insert_at_beginning(self, data):
		node = Node(data, self.head)
		self.head = node
		return f"Data {data} inserted at beginning"

	def insert_at_end(self, data):
		if self.head is None:
			node = Node(data, None)
			self.head = node
		else:
			itr = self.head
			while itr.nextb:

				itr = itr.nextb
			node = Node(data, None)
			itr.nextb = node
		return f"Data {data} inserted at end"

	def insert_set_values(self, datalist):
		for item in datalist:
			self.insert_at_end(item)
		return f"Items {datalist} inserted!"

	def insert_at_index(self, index, data):
		if index < 0 or index > self.__len__():
			return f"Error! LL length is {self.__len__()}"
		elif index == 0:
			result = self.insert_at_beginning(data)
			return result
		else:
			count = 0
			itr = self.head
			while itr:
				if count == (index -1):
					node = Node(data, itr.nextb)
					itr.nextb = node
					break
				itr = itr.nextb
				count += 1
			return f"Inserted {data}!"

	def insert_after_value(self, data_after, data_to_insert):
		if self.head is None:
			return f"Error! Linked List is empty!"
		else:
			count = 0
			itr = self.head
			while itr:
				if itr.data == data_after:
					node = Node(data_to_insert, itr.nextb)
					itr.nextb = node
					return f"{data_after} found at index {count}"
				itr = itr.nextb
				count += 1
			return f"{data_after} not found in LL!"


	def delete_from_beginning(self):
		if self.head is None:
			return f"Error! Linked List is empty!"
		else:
			del_item = self.head.data
			self.head = self.head.nextb
			return del_item
	
	def delete_from_end(self):
		if self.head is None:
			return f"Error! Linked List is empty!"
		else:
			itr = self.head
			while itr.nextb.nextb:
				itr = itr.nextb
			del_item = itr.nextb.data
			itr.nextb = None
			return del_item		

	def delete_at_index(self, index):
		if self.head is None:
			return f"Error! Linked List is empty!"
		elif index < 0 or index >= self.__len__():
			return f"Error! LL length is {self.__len__()}"
		elif index == 0:
			result = self.delete_from_beginning()
			return result
		elif index == (self.__len__() - 1):
			result = self.delete_from_end()
			#result = f"Item {del_item} deleted!"
			return result
		else:
			count = 0
			itr = self.head
			while itr:
				if count == (index-1):
					del_item = itr.nextb.data
					itr.nextb = itr.nextb.nextb
					break
				itr = itr.nextb
				count += 1
			return f"Item {del_item} deleted!"

	def remove_by_value(self, data):
		if self.head is None:
			return f"Error! Linked List is empty!"
		elif self.head.data == data:
			result = self.delete_from_beginning()
			return str(result)+' found at index 0'
		else:
			count = 1
			itr = self.head
			while itr:
				if itr.nextb.data == data:
					itr.nextb = itr.nextb.nextb
					return f"{data} found at index {count}"
				itr = itr.nextb
				count += 1
			return f"{data} not found in LL!"


	#Print function
	def __str__(self):
		if self.head is None:
			return "Linked List is empty!"
		else:
			itr = self.head
			llstr = ''
			while itr:

				llstr += str(itr.data) + '-->'
				itr = itr.nextb
			return llstr

	#Length of Linked List
	def __len__(self):
		count = 0
		itr = self.head
		while itr:
			itr = itr.nextb
			count += 1
		return count
