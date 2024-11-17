# Author:   Rafael D. Coss <rdcoss@icloud.com>
# Language: Python 3.9.x
# Creation: Sun Oct 20 11:08:34 PDT 2024
# Filename: max_grade.py
# Descr:    A simple program that outputs the single maximum value from an
#           input list (at the command line) of total points earned over an
#           academic term during a community college course. Rounds the output
#           value to a single decimal place. 
#           An exercise in completing an existing program, by writing the code
#           for a user-defined function implementing a well-known algorithm.
# 
#         
# Task:     Complete the body of the following function:
#           • get_maximum()
#           ...to make the program output the desired result.
# 
# Ex: If the total earned points were entered at the command line as:
#   python3 maxgrade.py 98.75 78.25 76 61.5 88 87.5
#   
#  the output would be:
#   Largest total course score was: 98.8
# 
# 
import sys

# 
course_points = []

def get_course_scores():
    """
    Sets the elements of the list course_points with values retrieved from the
    command line. Returns 'True' if one or more values was successfully read.
    Returns 'False' otherwise.

    Postcondition: course_results is a list of floats. 
    
    """
    num_arguments = len(sys.argv)
    if (num_arguments < 2):
        results = False
    else:
        results = True
        for itr in range(1, num_arguments):
            # print(f'Value: {float(sys.argv[itr])}')
            course_points.append( float(sys.argv[itr]) )
        
    return(results)



def get_maximum(course_results):
    """
    Returns the single largest number from the list of test scores passed as a
    parameter.
        
    Parameter course_results: numerical scores representing the total number of 
                              course points earned by each student.
    Precondition: course_results is a list of floats
        
    """
    curr_value = 0
    max_value = 0


    for i in course_results:
        # print(i)
        if i < max_value:
            max_value = max_value
        else:
            # want to set maximum value to the current number in the list that 
            # we know is either equal to or bigger that max_value 
            max_value = i
            # print(max_value)
    return max_value

# 'main' part of the program follows...
if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} val1, val2, val3...')
    sys.exit(1) # 1 indicates an error
else:
    #
    # Retrieve the highest total course score...
    if ( get_course_scores() ):
        best_total_score = get_maximum(course_points)
        print(f'Largest total course score was: {best_total_score:.1f}')
    else:
        print('There was a problem reading the values. Confirm that they are numbers.')