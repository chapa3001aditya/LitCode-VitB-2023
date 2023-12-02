import sys

def max_len(nums):
    count = 0
    max_length = 0
    table = {0: 0}
    for index,value in enumerate(nums,1):
        if value==0:
            count -= 1 
        else:
            count += 1
        if count in table:
            max_length = max(max_length, index - table [count])
        else:
            table[count] = index 
    return max_length 


def main():
    nums = input()
    nums = list(map(int,nums.split(" ")))
    length = max_len(nums)
    print(length)
    
if __name__=="__main__":
    main()
                                                                                                                            
