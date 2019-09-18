##*************************************************************************
##  Temperature Converter
##  Programmer: Ariadna Ayala
##  Status: Completed 
##*************************************************************************
//  Account Balancing Program
print ('Welcome to Temperature Converter 1.0!')
#Getting the value from user, used variable temp_c for Celsius. 
#Using float in case user inputs a number with a decimal place
temp_c=float(input('Please, enter your temperature in Celsius:')) 
## Calculating temperature in Fahrenheits (variable temp_f) using formula F=(9/5)C+32.
temp_f=(9.0/5.0)*temp_c+32
print (' ')    ## I prefer distance between parts of text
print ('Your result is:')
## The data must be formatted to one decimal point, used '.1f' as learned in class
## Removing comma as a separator of parts of the code in line below using "sep=' '"
print (temp_c, "°C =", (format (temp_f, '.1f')), "°F.", sep=' ')
print (' ')     
print ('Thank you for using my program! Have a Good Day!')
print (' ')
print (' ')
print ('This program is written by Ariadna Ayala')       
