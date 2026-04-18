"""
A college offers a course that prepares students for the state licensing exam for real-
estate brokers. Last year, several of the students who completed this course took the
licensing examination. The college wants to know how well its students did on the exam.
You have been asked to write a program to summarize the results. 
You have been given a list of these 10 students. 
Next to each name is written a 1 if the student passed the exam and a 2 if the student failed.
Your program should analyze the results of the exam as follows:
1. Input each test result (i.e., a 1 or a 2). Display the message “Enter result”
each time the program requests another test result.
2. Count the number of test results of each type.
3. Display a summary of the test results indicating the number of students who
passed and the number of students who failed.
4. If more than eight students passed the exam, display “Bonus to instructor.”

###3.1      (Validating User Input) Modify the script of Fig. 3.3 to validate its inputs.
            For any input, if the value entered is other than 1 or 2,
            keep looping until the user enters a correct value. 
            Use one counter to keep track of the number of passes, 
            then calculate the number of failures after all the user’s inputs have been received.

"""

# fig03_03.py
"""Using nested control statements to analyze examination results."""
# initialize variables
passes = 0 # number of passes
failures = 0 # number of failures
# process 10 students
for student in range(10):
    # get one exam result
    result = int(input('Enter result (1=pass, 2=fail): '))
    if result == 1:
        passes = passes + 1
    else:
        failures = failures + 1
# termination phase
print('Passed:', passes)
print('Failed:', failures)
if passes > 8:
    print('Bonus to instructor')



