import re

print("Input file name:")
file_name = input()

# Output file
tidy_file_name = file_name.partition(".")[0]
output_file = f"{tidy_file_name}_SENTENCEANALYSIS.txt"

# Locate input
read_file = f"../resources/{file_name}"

# Read text file
with open(read_file, 'r') as text:
    para_text = text.read()
    print(para_text)

# Drop new line tags
para_text = para_text.replace("\n", " ")

# Create lists of words and sentences
word_list = para_text.split(" ")
sentence_list = re.split("(?<=[.!?]) +", para_text)

# String of letters only
letters = re.sub(r'[^\w\s]','', para_text)
letters = letters.replace(" ", "")

# Stylize and output file
output = (
    f"Paragraph Analysis \n"
    f"-----------------\n"
    f"Approximate Word Count: {str(len(word_list))}\n"
    f"Approximate Sentence Count: {str(len(sentence_list))}\n"
    f"Approximate Average Letter Count: {str(round((len(letters)/len(word_list)),1))}\n"
    f"Average Sentence Length: {str(round((len(word_list)/len(sentence_list)),1))}"
)
print(output)

with open(output_file, "a") as txt_file:
    txt_file.write(output)