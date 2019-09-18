## Program #5 written by Ariadna Ayala


def main():
    score1=float(input('Enter your Test 1 score: '))    ## Collect test scores
    score2=float(input('Enter your Test 2 score: '))    ## from user
    score3=float(input('Enter your Test 3 score: '))    
    average=(score1+score2+score3)/3                    ## Formula for average grade


    
    def calc_average(score1,score2,score3):             ## Calculate the average.
        return average
    
    print('Your average is: ',                          ## Print the average
        format(calc_average(score1,score2,score3),      ## formatted to two
            ',.2f'))                                    ## decimal units.

    def determine_grade():
        
        if average >=90:                                ## Using 'if','else', and
            return 'A'                                  ## 'elif' to determine which
        elif average >=80:                              ## grade to print
            return 'B'
        elif average >=70:
            return 'C'
        elif average >=60:
            return 'D'
        else:
            return 'F'

    
    print ('Your grade is: ',determine_grade())         ## Print grade letter.
main()                                                  ## Call main function.
print ('This program is written by Ariadna Ayala')


