#3.6
"""
(Turing Test) The great British mathematician Alan Turing proposed a simple test
to determine whether machines could exhibit intelligent behavior. A user sits at a comput-
er and does the same text chat with a human sitting at a computer and a computer oper-
ating by itself. The user doesn’t know if the responses are coming back from the human
or the independent computer. If the user can’t distinguish which responses are coming
from the human and which are coming from the computer, then it’s reasonable to say that
the computer is exhibiting intelligence.
Create a script that plays the part of the independent computer, giving its user a sim-
ple medical diagnosis. The script should prompt the user with 'What is your problem?'
When the user answers and presses Enter, the script should simply ignore the user’s input,
then prompt the user again with 'Have you had this problem before (yes or no)?' If
the user enters 'yes', print 'Well, you have it again.' If the user answers 'no', print
'Well, you have it now.'
"""

response1 = input("What is your problem?")
response2 = input("Have you had this problem before (yes or no)?")
if response2 == "yes":
    print("Well, you have it again.")
if response2 == "no":
    print("Well, you have it now.")
    
