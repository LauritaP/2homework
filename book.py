import certifi
import ssl
import re

from urllib.request import urlopen

url = "https://www.gutenberg.org/files/11/11-h/11-h.htm"
local_name = "Alice’s Adventures in Wonderland.txt"


def save_locally():
    """
    Save the book locally, so we can use it faster and no need to load every time
    :return: None
    """
    # The downloaded book had many other characters that normally were not supposed to be in the book so i dedcided to imporve our html file
    # To do this i serched on google possible solutions and used code from website https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
    CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    with open(local_name, "w") as local_fp:
        with urlopen(url, context=ssl.create_default_context(cafile=certifi.where())) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")
                line= re.sub(CLEANR, '', line)
                local_fp.write(line)

punctuation = ",;!.?-()"
def get_unique_words():
    """
    Get the dictionary of unique words and their frequency
    :return: dict
    """
    unique_words = {}
    with open(local_name) as fp:
        for line in fp:
            # remove punctuation
            for p in punctuation:
                line = line.replace(p, " ")
            line = line.lower()
            # get the words:
            for word in line.split():
                unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words

#Step 1: save book in project
#save_locally()

#Step 2: we creat a dicionary of unique words in our book with their frequency
dict_alice = get_unique_words()
print("here is the dictionary for the book Alice : ")
print('dict_alice')

#Step 3: Get the total number of words
print("here is the total number of words in book Alice : ")
total_number_of_unique_words_in_Alice = len(dict_alice)
print(total_number_of_unique_words_in_Alice)

#Step 4: repeat all the previous steps for the new book

url = "https://www.gutenberg.org/files/730/730-h/730-h.htm"
local_name = "Oliver.txt"

save_locally()
print("here is the dictionary for the book Oliver : ")
dict_oliver = get_unique_words()
print('dict_oliver')
print("here is the total number of words in book oliver : ")
total_number_of_unique_words_in_Oliver = len(dict_oliver)
print(total_number_of_unique_words_in_Oliver)

#Step 5: Which book has weider vocab

if total_number_of_unique_words_in_Oliver>total_number_of_unique_words_in_Alice:
    print('Oliver has more words than Alice')
else:
    print('Alice has more words than Oliver')
#Olivar has more vocab than Alice

#Step 6 which book has more words over 7 letters
Alice_words_higher_7=0

for elem in dict_alice.keys():
    if len(elem)>7:
        Alice_words_higher_7+=1

print('Words in Alice over 7 letters')
print(Alice_words_higher_7)

#Step 7
Oliver_words_higher_7=0

for elem in dict_oliver.keys():
    if len(elem)>7:
      Oliver_words_higher_7+=1

print('Words in Oliver over 7 letters')
print(Oliver_words_higher_7)

#Step 8
if Oliver_words_higher_7>Alice_words_higher_7:
    print('Oliver has more words longer than 7 characters than Alice')
else:
    print('Alice has more words longer than 7 characters than Oliver')