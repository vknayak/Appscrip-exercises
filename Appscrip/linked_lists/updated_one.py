class node:
	def __init__(self,value):
		self.info=value
		self.link=None

class SingleLinkedlist:
	def __init__(self):
		self.start=None


	def displayNodes(self): 
		if self.start is None:                                             #checking whther first element has velue or not
			print("linked list is empty")
		else:
			print("list is : ")
			p=self.start
			while p is not None:
				print(p.info," ",end="")
				p=p.link                                                    #p=p.link is for traversing through linked list


	def numberOfNodes(self):
		p=self.start
		count=0
		while p is not None:                                                # running the loop upto the p's node is none because to get count of nodes
			count+=1
			p=p.link
		return count


	def get_middle_element(self):
		p=self.start
		count=list1.numberOfNodes()                                         #using numberofNodes function to get the count and after finding middile number position
		if count%2==0:
			middle_number=count//2
		else:
			middle_number=(count//2)+1
		n=0
		while p is not None:
			n+=1
			
			if n==middle_number:
				print("the middle element is: ",p.info)
				break
			p=p.link


	def third_ele_from_end(self):
		p=self.start
		count=list1.numberOfNodes()

		third_element=count-2
		n=0
		while p is not None:
			n+=1
			if n==third_element:
				print("the third element from end is: ",p.info)
				break
			p=p.link

	def insert_at_end(self,data):
		temp=node(data)                                                        #taking a temporary variable for empty linked list and after that we are linking them by traversing
		if self.start is None:
			self.start=temp
			return
		p=self.start
		while p.link is not None:
			p=p.link
		p.link=temp

	def create_list(self):
		n=int(input("enter number of nodes:"))
		if n==0:
			return
		for i in range(n):
			data=int(input("enter the element that u want to insert:"))
			self.insert_at_end(data)


list1=SingleLinkedlist()

list1.create_list()
list1.displayNodes()
list1.numberOfNodes()
list1.get_middle_element()
list1.third_ele_from_end()