
import re

my_paragraph = "C:\\Python-Challenge\\PyParagraph\\Resources\\paragraph_2.txt"

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(my_paragraph, 'r') as text:

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    # Print the contents of the text file
    #print(lines)

    Word_Split = lines.split()
    Word_Count = len(Word_Split)
    
    Sentence_Count = len(re.findall(r'\.', lines))
    #Sentence_Split = lines.split(".")
    #Sentence_Count = len(Sentence_Split)
    print(Sentence_Count)
    


