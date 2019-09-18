##*************************************************************************
##  File Import / Driving test results
##  Programmer: Ariadna Ayala
##  Status: Completed 
##  This program uses a list of correct answers to the question to compare them
##  to an external file and determine whether user passed the test.
##*************************************************************************


## NOTES: 1) I used a new file import method shown in the previous class.
##        2) Having main function in the beginning of the code did not quite
##           work for me in this case, displaying various function and
##           value undifined errors.


def correct_answers():
    correct_list = ['A','C','A','A','D','B','C','A',    ## A list of correct answers
                    'C','B','A','D','C','A','D','C',
                    'B','B','D','A']
    return correct_list
def open_file():                                        ## Opening a file w./ Examinee's answers
                                                        ## and create a list
    import tkinter as tk                                ## Using new method of file import
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename()
    
    driver_answers = []                                 ## Creating a list for Examinee's answers
    object_file = open(filepath,'r')                    ## Opening a file w./ Examinee's answers
    for i in object_file:
        i=i.strip('\n')                                 ## Making sure the values are lined up 
        driver_answers.append(i)                        ## Inserting the answers to the driver_answers list
    return driver_answers
def check_answers(correct_list, driver_answers):        ## Checking the answers
    count=0
    wrong_list = []                                     ## Creating a list of wrong answers
    for i in range(20):
        if correct_list[i] == driver_answers[i]:        ## Comparing each Examinee's answers 
            count+=1                                    ## to the correct answers.
        else:
            wrong_list.append(i)                        ## Adding wrongly answered questions
            count+=0                                    ## to the wrong_list
    if count < 15:                                      ## Output, if failed
        print ('Sorry, you failed. Maybe next time.')
    else:
        print ('Congratulations, you passed!')          ## Output, if passed
    print('Your score is: ', count/0.2 , '%')           ## Calculating & displaying the score
    print('Correct answers: ',count,sep=' ')            ## Displaying amount of correct answers
    print('Incorrect answers: ',20-count)               ## Displaying amount of incorrect answers
    print('The questions you answered incorrectly: ',   ## Displaying the list of incorrectly
          wrong_list, sep=' ')                          ## answered questions
        
def main():
    name = (input('Examinee\'s name: ').strip())        ## Using .strip function to remove any white space
    correct_list = correct_answers()
    driver_answers = open_file()
    check_answers (correct_list, driver_answers)

main()
print ('\n')
print ('This program is written by Ariadna Ayala')
