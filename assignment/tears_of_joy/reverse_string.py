"""
13. Reverse a string with a loop
Without using string slicing, use a loop to build and print the reverse of a user-entered string.
Expected output: Enter: hello / Reversed: olleh
"""

reversed_str = ""
user_string = input("Enter a string: ")
for letters in user_string:
    reversed_str = letters + reversed_str
print(reversed_str)
