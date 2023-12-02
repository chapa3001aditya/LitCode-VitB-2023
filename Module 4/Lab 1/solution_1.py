class clumsyfactorial:
    def __init__(self) -> None:
        '''This constructor takes input of an integer when ever a new instance
        of the class created.'''
        self.n = int(input())

    def factorial(self) -> int:
        '''The operations of clumsy factorial are as of follow *,/,+,- and then 
        returns the clumsy factorial of the provided integer'''
        expression = list()
        iteration = 0
        while self.n > 0:
            expression.append(str(self.n))
            if iteration%4 == 0:
                expression.append('*')
            elif iteration%4 == 1:
                expression.append('//')
            elif iteration%4 == 2:
                expression.append('+')
            elif iteration%4 == 3:
                expression.append('-')
            iteration += 1
            self.n -= 1
        expression.pop()
        expression = "".join(expression)
        return eval(expression)

def main() -> None:
    '''Main driver code.'''
    number = clumsyfactorial()
    print(number.factorial())

if __name__ == '__main__':
    main()
                                                                                                                            
