class arraymanipulation:
    def __init__(self) -> None:
        '''This constructor takes the input of the length of the 1 indexed array,
        the number of operations to be performed and list of operation that have
        to be performed'''
        self.n ,self.m= int(input().strip()),int(input().strip())
        self.matrix = list()
        for i in range(self.m):
            self.matrix.extend(list(map(int,input().strip().split())))

    def maxval(self) -> int:
        '''This function performs the operations on the 1 indexed array filled
        with zeros. It performs each operation ny adding a value to each element 
        of the array between two given indicies (inclusive)'''
        manipulated_matrix = [0]*int(self.n)
        for i in range(0,int(self.m)*3,3):
            manipulated_matrix[self.matrix[i]-1:(self.matrix[i+1])]=(list(map(lambda x: x+self.matrix[i+2],manipulated_matrix[self.matrix[i]-1:(self.matrix[i+1])])))
        return max(manipulated_matrix)
        
        
def main() -> None:
    '''Main driver code'''
    arrayinput = arraymanipulation()
    max_val = arrayinput.maxval()
    print(max_val)

if __name__ == '__main__':
    main()
                                                                                                                            
