# Collaboration with Kate Spitzer using hint code:
# re.split("(?<=[.!?]) +", paragraph)
# Other .py file is code for assignment without using re's.

# Code practiced on paragraph_1.txt provided in Gitlab.

# Paragraph used for assignment from:
# https://www.britannica.com/animal/Dimetrodon
# written by The Editors of Encyclopedia Britannica

# Import necessary modules

import re

# Setting variables to zero for counting words and letters

Word_Count = 0
Letter_Count = 0


# Setting variable for paragraph txt file for later calculations.

my_paragraph = "C:/Python-Challenge/PyParagraph/Resources/Dimetrodon.txt"

# Open the file in "read" mode ('r') and store the contents in the variable "text

with open(my_paragraph, 'r', encoding='utf-8') as text:


    # Store all of the text inside a variable called "lines"

    lines = text.read()


# Using hint code provided, break paragraph into sentences at various
# kinds of punctuation.

Sents = re.split("(?<=[.!?]) +", lines)

# Loop through each sentence split out from previous code, further splitting
# the sentences into words. Counting up the words in each split sentence.

for sentence in Sents:
    words = sentence.split()

    Word_Count += len(words)

    # Loop through each word in each sentence,
    # Counting up the letters in each word

    for word in words:
        Letter_Count += len(word)



# Calculating and printing the necessary values for the assignment.

print("\nParagraph Analysis")
print("--------------------------")
print(f"\nApproximate Word Count: {Word_Count}")
print(f"Approximate Sentence Count: {len(Sents)}")
print(f"Average Letter Count: {round(Letter_Count/Word_Count, 2)}")
print(f"Average Sentence Length: {round(Word_Count/len(Sents), 2)}")


# Set variable for output file

output_file = "C:/Python-Challenge/PyParagraph/Analysis/paragraph_analysis2.txt"

# Open the output file in the same format as printed in terminal.

with open(output_file, "w") as text_file:
    text_file.write("Paragraph Analysis\n")
    text_file.write("--------------------------\n")
    text_file.write(f"Approximate Word Count: {Word_Count}\n")
    text_file.write(f"Approximate Sentence Count: {len(Sents)}\n")
    text_file.write(f"Average Letter Count: {round(Letter_Count/Word_Count, 2)}\n")
    text_file.write(f"Average Sentence Length: {round(Word_Count/len(Sents), 2)}\n")

