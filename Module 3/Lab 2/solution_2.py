class passwordanalyser:
    '''This class contains the functions required for the declaring the given set of passwords as GOOD PASSWORDS or BAD PASSWORDS'''
    def __init__(self) -> None:
        '''This is an constructor that get initialized when an object created and takes an input of set of passwords. '''
        self.passwordinput = input().strip().lower().split(" ")
    def prefixchecker(self) -> str:
        '''This function is to check if no password is a prefix of another password in the set, except for identical passwords'''
        self.passwordinput.sort()
        for i in range(len(self.passwordinput)-1):
            if not self.passwordinput[i+1].startswith(self.passwordinput[i]):
                pass
            else:
                if self.passwordinput[i+1] == self.passwordinput[i]:
                    pass
                else:
                    return "BAD PASSWORD"
        return "GOOD PASSWORD"

def main() -> None:
    '''Main driver code'''
    passwordlist = passwordanalyser()
    print(passwordlist.prefixchecker())

if __name__ == '__main__':
    main()
                                                                                                                            
