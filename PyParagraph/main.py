
import re

my_paragraph = "C:\\Python-Challenge\\PyParagraph\\Resources\\paragraph_2.txt"

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(my_paragraph, 'r') as text:

    # This stores a reference to a file stream
    print(text)

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    # Print the contents of the text file
    print(lines)
