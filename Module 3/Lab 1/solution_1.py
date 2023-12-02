class maxsubstr:
    def __init__(self) -> None:
        '''This function is a constructor that takes input 
        while creating an object of this class'''
        self.string = str(input())
        self.pattern = str(input())
        
    def maximumSubsequenceCount(self) -> int:
        '''this function calculates the maximum number of subsequences'''
        cnt1 = cnt2 = 0
        ttl = 0

        for ch in self.string:
            if ch == self.pattern[1]:
                cnt2 += 1
                ttl += cnt1
            if ch == self.pattern[0]:
                cnt1 += 1
        return ttl + max(cnt1,cnt2)

def main() -> None:
    '''Main driver code'''
    string = maxsubstr()
    print(string.maximumSubsequencwCount())
    
if __name__ == '__main__':
    main()
                                                                                                                            
