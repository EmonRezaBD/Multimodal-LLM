import re

print("Start!\n")

# Read the text file : short story for tokenizing : Comment 01
with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read() 

# print("Total number of character:", len(raw_text))
# print(raw_text[:99])

# Tokenizing the text : From raw text to list of words : Comment 02

# Testtext = "Hello, world. This, is a test."
# Tokenizetext01 = re.split(r'(\s)',Testtext)
# print(Tokenizetext01)

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(len(preprocessed))
print(preprocessed[:30])



print("\nEnd!\n")
