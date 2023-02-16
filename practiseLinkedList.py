# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def printz(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
#             itr = itr.next
#         print(llstr)

#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count+=1
#             itr = itr.next

#         return count

#     def insert_at_begining(self, data):
#         node = Node(data, self.head)
#         self.head = node

#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return

#         itr = self.head

#         while itr.next:
#             itr = itr.next

#         itr.next = Node(data, None)

#     def insert_at(self, index, data):
#         if index<0 or index>self.get_length():
#             raise Exception("Invalid Index")

#         if index==0:
#             self.insert_at_begining(data)
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 node = Node(data, itr.next)
#                 itr.next = node
#                 break

#             itr = itr.next
#             count += 1

#     def remove_at(self, index):
#         if index<0 or index>=self.get_length():
#             raise Exception("Invalid Index")

#         if index==0:
#             self.head = self.head.next
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 break

#             itr = itr.next
#             count+=1

            
#     def insert_values(self,data_list):
#         print("1")
#         self.head=None
#         for data in data_list:
#             self.insert_at_end(data)
            
#     def insert_after_value(self, data_after, data_to_insert):
#     # Search for first occurance of data_after value in linked list
#     # Now insert data_to_insert after data_after node  
#         print("11") 
#         if self.head is None:
#             return
#         itr=self.head
#         if itr.data==Node(data_to_insert,self.head.next):
#             self.head=self.head.next
#             return    
#         while itr:
#             if itr.data==data_after:
#                 node=Node(data_to_insert,itr.next)  
#                 itr.next=node
#             itr=itr.next
            
#     def remove_by_value(self, data):
#     # Remove first node that contains data
#         if self.head is None:
#             return
#         itr=self.head
#         if itr.data==data:
#             self.head=self.head.next
#             return
           
#         while itr.next:
#             if itr.next.data==data:
#                 itr.next=itr.next.next  
#                 break     
#             itr=itr.next 
       
class Node:
    def __init__(self,data=None,next=None,prev=None) :
        self.data=data
        self.next=next
        self.prev=prev
        
class DoubleLinkedList:
    def __init__(self):
        self.head=None
    def print_forward(self):
    # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Double link list is empty")
            return
        itr= self.head
        str=""
        while itr:
            str+=itr.data+"-->" 
            itr=itr.next
        return str
            
        
        # print("111")
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def print_backward(self):
        if self.head is None:
            print("Double link list is empty")
            return
        last_node=self.get_last_node()
        itr=last_node
        str=""
        while itr:
            str+=itr.data+"-->"
            itr=itr.prev
        return str
            
    # Print linked list in reverse direction. Use node.prev for this.
        
     
        

if __name__ =='__main__':
    # ll=LinkedList()
    # ll.insert_at_begining(16)
    # ll.insert_at_begining(20)
    # ll.insert_at_end(33)
    # ll.insert_at(1,1)
    # print('length',ll.get_length(),ll.printz(),"xxxxxxx")
    # ll.insert_at(3,36)
    # ll.printz()
    # # ll.remove_at(1)
    # # ll.insert_values(["anitha","michitha","suchi"])
    # ll.insert_after_value(36,37)
    # ll.insert_after_value(33,37)
    # ll.remove_by_value(37)
    # ll.printz()
    dll= DoubleLinkedList()
    dll.print_forward()




    

    