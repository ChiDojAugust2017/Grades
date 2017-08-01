import random
def scottgrades():
    print "Scores and Grades"
    
    for x in range(10):
        grades = random.randint(60,100)

        
    
        if grades >=90:
            print "Score:", grades,"Your grade is A!"
        elif grades >=80 and grades <90:
            print "Score:", grades,"Your grade is B!"
        elif grades >=70:
            print "Score:", grades,"Your grade is C!"
        else:
            print "Score:", grades, "Work harder and smarter!"
            
    print "End of the program. Bye!"
           


scottgrades() 










