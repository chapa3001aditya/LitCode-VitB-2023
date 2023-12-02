class CustomStack():
    ''' This class supports various operations such as inserting a value
    into class, deleting a value, getting the index, and reverting back
    to the last change made.'''
    def __init__(self) ->None:
        self.text =""
        self.stack = list()

    def UpdateStack(self,command:str) -> None:
        '''This function will keep an update of all the recent changes made'''
        if len(self.stack) < 2:
            self.stack.append(command)
        else:
            self.stack.pop(0)
            self.stack.append(command)

# 1

    def Insert(self,text:str) -> str:
        '''Inserts the text provided at the cursor position.'''
        self.text += text
        return self.text
        
# 2  

    def Delete(self,value:int) -> None:
        '''Deletes the last value characters from the text starting 
        from the current cursor position.'''
        self.text = self.text[:-value]
        return self.text 
# 3

    def GetValue(self,IndexVal:int) -> str:
        '''This fucntion retrives the charector present at the mentioned index value'''
        if IndexVal <= len(self.text) :
           return self.text[IndexVal-1]
# 4

    def Undo(self) -> None:
        '''Reverts the last executed command on the text'''
        self.text = self.stack[0]
         

    def CommandExecuter(self,command:str)-> None:
        '''This function checks which operation has to be carried out and performs the same'''
        operator= command.split()
        
        if int(operator[0]) == 1 :
            _, val = command.split()
            self.UpdateStack(self.Insert(val))
            
        elif int(operator[0]) == 2:
            _, val = command.split()
            self.UpdateStack(self.Delete(int(val)))
            
        elif int(operator[0]) == 3:
            _, val = command.split()
            print(self.GetValue(int(val)))
            
        else:
            self.Undo()


def main():
    '''Main driver code'''
    InputCommand = input().strip().split(',')
    TextEditor = CustomStack()
    [TextEditor.CommandExecuter(i) for i in InputCommand]
         

if __name__=='__main__':
    main()
                                                                                                                            
