#Doubly Linked List
class Node:
    def __init__(self,prev,data):
        self.next = None
        self.data = data
        self.prev = prev
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, data):
        new_node = Node(self.tail,data)
        print("Pushing.."+data)
        self.length +=1
        if(self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def printList(self):
        print(">>Doubly Linked List:")
        temp = self.head
        while(temp):
            print(temp.data+" ",end =" ")
            temp = temp.next
        print("\n")
            
    def printRev(self):
        print("Doubly Linked List in reverse:")
        temp = self.head
        #Reaching from head to tail
        while(temp.next):
            temp = temp.next
        #Iterating from tail to head till temp == head
        while(temp.prev != None):
            print(temp.data+" ",end =" ")
            temp = temp.prev
        print(temp.data)

    def printSummary(self):
        temp = self.head
        print("------------------------------------------------------------------------------------------")
        print("\t\t\t\t\tSUMMARY DOUBLE LINKED LIST\n")
        print("\t\t\t\t\tLength :"+str(self.length)+"\n")
        print("Node Data\t\t\tPrev Node\t\t\t\t\t\t\tCurrent Node\t\t\t\t\tNext Node\n")
        print(str(temp.data) + "\t" +"\t\t\t"+ str(temp.prev) +"\t\t\t\t\t\t\t"+ str(temp) +"\t\t\t"+ str(temp.next))
        temp = temp.next
        while(temp):            
            print(str(temp.data) + "\t" +"\t\t\t"+ str(temp.prev) +"\t\t\t"+ str(temp) +"\t\t\t"+ str(temp.next))
            temp = temp.next
        print("------------------------------------------------------------------------------------------")
            
    def pop(self):
        temp = self.head
        #Reaching from head to tail
        while(temp.next):
            last = temp
            print(last.data)
            temp = temp.next
        print("Popped last element "+temp.data)
        last.next = None
        self.tail = last
        self.length -= 1
        
    def search(self, key):
        temp = self.head
        counter  = 0
        while(temp):
            if(temp.data != key):
                counter += 1
            else:
                break
            last = temp
            temp = temp.next
        if(counter == self.length):
            print(str(key)+ " not found")
        else:
            print(str(key)+" is present at index: "+str(counter))
        return last
    
    def removeEle(self, key):
        temp = self.head
        counter  = 0
        while(temp):
            if(temp.data != key):
                counter += 1
            else:
                break
            last = temp
            temp = temp.next
            print(counter)
        if(counter == self.length):
            print(str(key)+ " not found")
        elif(counter == self.length - 1):
            print(str(key)+" is present at index: "+str(counter))
            last.next = None
            self.length -= 1
        elif(counter == 0):
            print(str(key)+" is present at index: "+str(counter))
            self.head = temp.next
            self.head.prev = None
            self.length -= 1
        else:
            print(str(key)+" is present at index: "+str(counter))
            next = temp.next
            print("temp is " + str(temp.data))
            prev = temp.prev
            print("prev is " + str(prev.data))
            next.prev = prev
            prev.next = next
            self.length -= 1
    def help(self):
        print("Commmands Available for Doubly linked list:-\n")
        print("1)push [value]\t\tpushes value to list\n2)remove [value]\tremove value from list\n3)summary\t\tprints summary of the list\n4)print\t\t\tprints the list\n5)printrev\t\tprints the list in reverse\n6)pop\t\t\tpops the last element\n7)search [value]\tsearches for value\n8)end\t\t\tquits the interface")
    def ui(self):
        while True:
            raw = list(input("Enter the Command: (h for help)").split())
            if(raw[0] == 'h'):
                print("Under Construction\n")
                self.help()
            elif(raw[0] == "push"):
                self.push(raw[1])
            elif(raw[0] == "remove"):
                self.removeEle(raw[1])
            elif(raw[0] == "summary"):
                self.printSummary()
            elif(raw[0] == "print"):
                self.printList()
            elif(raw[0] == "printrev"):
                self.printRev()
            elif(raw[0] == "pop"):
                self.pop()
            elif(raw[0] == "search"):
                self.search(raw[1])
            elif(raw[0] == 'end'):
                return 0
            
new = LinkedList()
new.ui()
