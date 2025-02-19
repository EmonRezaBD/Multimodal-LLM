import re
import os
os.chdir("F:\GithubRepo\Multimodal-LLM\LLM_from_Scratch\Chapter02") # set the directory to debug the code

print("Start!\n")

class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s, i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [
            item if item in self.str_to_int 
            else "<|unk|>" for item in preprocessed
        ]

        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
        
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        # Replace spaces before the specified punctuations
        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
        return text
    
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
# # print(len(preprocessed))
# # print(preprocessed[:30])

# #Converting tokens into token IDs : Comment 03

all_words = sorted(list(set(preprocessed))) #unique tokens
vocab_size = len(all_words)
# print(vocab_size)

vocab = {token:integer for integer, token in enumerate(all_words)} #unique tokens IDs
# # for i, item in enumerate(vocab.items()):
#     if i < 10:
#         print(item)
#         if(i>50):
#             break


#Using class
tokenizer = SimpleTokenizerV1(vocab)

# text = """"I It's the last he painted, you know," 
#            Mrs. Gisburn said with pardonable pride.""" #old text

# testText = "Hello, Any or Poison?" #new text : it comes error
# ids = tokenizer.encode(testText)
# ids = tokenizer.encode(text)
# print(ids)
# print(tokenizer.decode(ids))

#Modifying the tokenizer to handle unknown words: Comment 04
# all_tokens = sorted(list(set(preprocessed)))
# all_tokens.extend(["<|endoftext|>", "<|unk|>"])
# vocab = {token:integer for integer, token in enumerate(all_tokens)}

# print(len(vocab.items()))
# for i,item in enumerate(list(vocab.items())[-5:]): #end of txt and unk tokens are added
#     print(item)

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((text1, text2))
print(text)

print(tokenizer.encode(text))
print(tokenizer.decode(tokenizer.encode(text)))

print("\nEnd!\n")
