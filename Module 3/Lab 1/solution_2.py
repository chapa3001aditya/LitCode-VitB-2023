class candies:
    '''This class contains the functions for calculating the number of steps for
    reaching the goal'''
    def __init__(self) -> None:
        '''This is a constructor that will take input of the 
        target sweetness and the sweetness of individual candies'''
        self.target = input().strip()
        self.candies = input().strip().split(" ")
    def stepstotarget(self) -> int:
        '''This function counts the steps taken to reach the 
        candie sweetness target'''
        count = 0
        while len(self.candies) > 2:
            count += 1
            if self.target not in self.candies:
                self.candies = sorted(self.candies)
                self.candies.append(self.candies[0] + self.candies[1])
                del self.candies[:2]
            else:
                return count
        return count
def main() -> None:
    ''' Main driver code'''
    sweet_candies = candies()
    print(sweet_candies.stepstotarget())

if __name__ == "__main__":
    main()
                                                                                                                            
