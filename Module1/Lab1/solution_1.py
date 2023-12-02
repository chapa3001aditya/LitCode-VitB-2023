import sys 
import string 
from string import ascii_lowercase, ascii_uppercase, punctuation, digits

def composition(input_string:str):
    total_len = len(input_string)
    lower_case = 0
    upper_case = 0
    digits_count = 0
    symbols = 0
    for i in input_string:
        if i in ascii_lowercase:
            lower_case += 1
        elif i in ascii_uppercase:
            upper_case += 1
        elif i in digits :
            digits_count += 1 
        else:
            symbols += 1
    print(f"{round((upper_case/total_len)*100,3)}% \n{round((lower_case/total_len)*100,3)}% \n{round((digits_count/total_len)*100,3)}% \n{round((symbols/total_len)*100,3)}")
    


def main():
    input_string = str(input())
    composition(input_string)
    
if __name__=="__main__":
    main()
                                                                                                                            
