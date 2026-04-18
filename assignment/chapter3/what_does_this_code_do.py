"""
(What Does This Code Do?) What does the following program print?
for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
    print()

ANSWER: It prints 10 rows of > and <, both alternating for each row.
Each row contains 10 signs of < or > accordingly.
"""


for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
    print()
