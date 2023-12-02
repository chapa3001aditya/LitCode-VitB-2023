class egyptionfraction:
    '''Contains all the functions required to perform an egyption fraction'''

    def __init__(self) -> None:
        '''constructor that takes the input of the denominator and numerator'''
        self.numerator = int(input().strip())
        self.denominator = int(input().strip())


    def fractioncal(self) -> list:
        '''representing the fraction as a sum of unique unit fractions'''
        result = list()
        while self.numerator != 0:
            unit_denominator = -(-self.denominator//self.numerator)
            self.numerator = self.numerator * unit_denominator - self.denominator
            self.denominator = self.denominator * unit_denominator
            result.append(unit_denominator)
        return result



def main() -> None:
    '''main driver code'''
    fraction = egyptionfraction()
    output = fraction.fractioncal()
    [print(x) for x in output]

if __name__ == "__main__":
    main()
                                                                                                                            
