
import re

Letter_Count = 0

my_paragraph = "C:\\Python-Challenge\\PyParagraph\\Resources\\paragraph_2.txt"

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(my_paragraph, 'r') as text:

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    Sentence_Count = len(re.findall(r'\.', lines))

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
#print(f"Average Sentence Length : {}")


# Set variable for output file

output_file = "C:\\Python-Challenge\\PyParagraph\\Analysis\\paragraph_analysis.txt"

#  Open the output file in the same format as printed in terminal

with open(output_file, "w") as text_file:
    text_file.write("Paragraph Analysis\n")
    text_file.write("--------------------------\n")
    text_file.write(f'Approxiate Word Count : {Word_Count}\n')
    text_file.write(f'Approximate Sentence Count : {Sentence_Count}\n')
    text_file.write(f'Average Letter Count : {Average_Letter}\n')
    #text_file.write(f'Average Sentence Length : {}\n')
    


