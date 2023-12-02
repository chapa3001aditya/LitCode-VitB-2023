class slidingsubarr:
    '''This class contains all the required funtions for retreiving the list of integer array containing n - k + 1 elements '''
    def __init__(self) -> None:
        '''This is an constructor that takes the input of the list of numbers, sub array size, and the value of the postion required'''
        self.numlist = list(map(int,input().strip().split(" ")))
        self.subarrsize = int(input().strip())
        self.nthpos = int(input().strip())

    def findthenum(self) -> list:
        '''This function will return the list of numbers in the sub array and the nth position'''
        subarr = list()
        for i in range(0,len(self.numlist)-self.subarrsize+1):
            subarr.append(self.numlist[i:i+self.subarrsize][self.nthpos - 1])
        print(*subarr)

def main() -> None :
    ''' Main Driver Code'''
    input_list = slidingsubarr()
    input_list.findthenum()   

if __name__ == "__main__":
    main()
                                                                                                                            
