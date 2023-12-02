class LongestSubstring():

    def __init__(self) -> None:
        '''This is an constructor that get initialized on the creation of the object'''
        self.string = input().strip()
        self.left, self.right = 0, 0
        self.hash_set = set()
        self.longest_length = 0

    def lengthOfLongestSubstring(self) -> int:
        '''This function is created to find the longest substring'''
        while self.right < len(self.string):
            if self.string[self.right] not in self.hash_set:
                self.hash_set.add(self.string[self.right])
                self.right += 1
                self.longest_length = max(self.longest_length, self.right - self.left)
            else:
                self.hash_set.remove(self.string[self.left])
                self.left += 1
        return self.longest_length

def main():
    '''Main driver code'''
    StringInput = LongestSubstring()
    print(StringInput.lengthOfLongestSubstring())

if __name__ == "__main__":
    main()
                                                                                                                            
