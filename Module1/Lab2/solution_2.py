class Queue:
    def __init__(self) -> None:
        self.stack1 = list()
        self.stack2 = list()

    def enqueue(self,data:str)-> None:
        ''' this function is used to enqueue the elememts into the queue'''
        self.stack1.append(data)

    def dequeue(self) -> str:
        ''' This function will dequeue the element on the basis of FIFO '''
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    
    def printTop(self) ->str:
        '''This function will print the element on the top'''
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
        
def main():
    q = Queue()
    queries = input().strip().split(",")
    for query in queries:
        if "1 " in query:
            q.enqueue(query[2:])
                
        elif "2" in query:
            q.dequeue()
        else:    
            print(q.printTop())
if __name__ == "__main__":
    main()
                                                                                                                            
