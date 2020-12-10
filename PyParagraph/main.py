# Keeping in folder to show attempt at code without regular expressions.
# While practicing on sample paragraph 2 in Gitlab (about Jackie Chan),
# hint code re.split("(?<=[.!?]) +", paragraph), did not seem to work well
# and researching re's also wasn't yielding good solutions.

# Since labels are "Approximate" word count, sentence count, etc. messed
# with code without re's in order to complete extra assignment.

# Collaborated with Kate Spitzer for solution using re's, turns out the
# hint code works much better with sample paragraph 1 in Gitlab.  Collab
# code in other .py file.

# Code practiced on paragraph_2.txt provided in Gitlab.

# Paragraph used for assignment from:
# https://www.britannica.com/animal/Dimetrodon
# written by The Editors of Encyclopedia Britannica


import re

Letter_Count = 0
Sent_Length = 0

my_paragraph = "C:\\Python-Challenge\\PyParagraph\\Resources\\Dimetrodon.txt"

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(my_paragraph, 'r') as text:

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    Sentence_Split = lines.split(".")
    Sentence_Count = len(Sentence_Split)

    for sent in Sentence_Split:
        Sent_Length = Sent_Length + len(sent.split())

    Ave_Sent_Length = round(Sent_Length/Sentence_Count,2)

    # Found on https://codeburst.io/python-basics-11-word-count-filter-out-punctuation-dictionary-manipulation-and-sorting-lists-3f6c55420855
    # by Michael Galarnyk

    for char in '-.,\n':
        lines = lines.replace(char, '')
    
        Word_Split = lines.split()
    Word_Count = len(Word_Split)
    

    for word in Word_Split:
        Letter_Count = Letter_Count + len(word)
        
    Average_Letter = round(Letter_Count/Word_Count, 2)



print("\nParagraph Analysis")
print("--------------------------")
print(f"Approximate Word Count : {Word_Count}")
print(f"Approximate Sentence Count : {Sentence_Count}")
print(f"Average Letter Count : {Average_Letter}")
print(f"Average Sentence Length : {Ave_Sent_Length}")


# Set variable for output file

output_file = "C:\\Python-Challenge\\PyParagraph\\Analysis\\paragraph_analysis.txt"

#  Open the output file in the same format as printed in terminal

with open(output_file, "w") as text_file:
    text_file.write("Paragraph Analysis\n")
    text_file.write("--------------------------\n")
    text_file.write(f'Approxiate Word Count : {Word_Count}\n')
    text_file.write(f'Approximate Sentence Count : {Sentence_Count}\n')
    text_file.write(f'Average Letter Count : {Average_Letter}\n')
    text_file.write(f'Average Sentence Length : {Ave_Sent_Length}\n')
    


