class kthsmallesttrimmednum:
    '''This class consists of functions that are required to perform 
    Query Kth Smallest Trimmed'''
    def __init__(self) -> None:
        '''This is a constructor that takes imput of the nums,queries count
        and the query pair'''
        self.nums = input().strip().split()
        self.n = int(input().strip())
        self.query = list(list(map(int,input().strip().split())) for i in range(self.n))

    def kthsmallestnum(self)->list:
        '''Trim each number in nums to its right most trimi digits by 
        removing the left most digits until only trimi digits remain.
Determine the index of the kth smallest trimmed number in the modified
nums. If two trimmed numbers are equal, consider the number with the lower 
index to be smaller.Reset each number in nums to its original length.
Store the answers to each query in an array answer, where answer[i] is the 
answer to the ith query. '''
        trimmed_list = list()
        new_trimmed = list()

        for query in self.query:
            trimmed_list.append(list(map(lambda x: x[-query[1]:],self.nums)))
            new_trimmed.append(list(map(lambda x: x[-query[1]:],self.nums)))
        
        for sub_list in new_trimmed:
            sub_list.sort()
          
        for i in range(len(self.query)):
            self.query[i] = trimmed_list[i].index(new_trimmed[i][(self.query[i][0])-1])
        
        return self.query

def main() -> None:
    '''main driver code'''
    query = kthsmallesttrimmednum()
    output = query.kthsmallestnum()
    print(*output)

if __name__ =='__main__':
    main()
                                                                                                                            
