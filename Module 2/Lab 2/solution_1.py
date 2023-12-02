class sumwithuk:
    '''To find the minimum possible size of a set of positive integers with the following properties:
        Each integer in the set has the unit digit equal to k.
        The sum of all the integers in the set equals num.
        If such a set exists, return its minimum size. Otherwise, if no set satisfies the conditions, return -1.'''
    def __init__(self) ->None:
        self.num = int(input())
        self.k = int(input())

    def minimumNumbers(self) -> int:
        '''This funtion is created to return the least number of elements required for making the sum '''
        if self.num == 0:
            return 0
        
        elif self.num < self.k:
            return -1
        
        elif self.num == self.k:
            return 1
        
        ans = -1
        i = 1

        while i <= 10:
            if (self.num - i * self.k) % 10 == 0 and i * self.k <= self.num:
                return i
            i += 1

        return ans
    
def main():
    '''Main Driver Code'''
    num = sumwithuk()
    print(num.minimumNumbers())

if __name__=="__main__":
    main()
                                                                                                                            
