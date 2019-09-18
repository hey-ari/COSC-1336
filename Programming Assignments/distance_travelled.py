## Program #4 --Distance Travelled-- Written by Ariadna Ayala

g = 'y'
while g == 'Y' or g == 'y':
    mph = int(input('Enter speed: '))
    hrs = int(input('Enter hours: '))
    print()
    print('Time\tDistance')
    print('_______________')
    if hrs <= 0 or mph <= 0:      ## Elliminating invalid, or negative, outputs
        print('ERROR: Hours and mph must be greater than 0')
    else:
        for t in range(hrs):
            dist = mph * (t+1)        ## t+1 instead of time
            print(t + 1,'\t', dist) ## Formatting to 2 dec.places

        g = 'n'                   ## Avoiding the "nfinite loop"
        
print('End')
print()
print('*** This program is written by Ariadna Ayala ***')
