#%%
from farasa.segmenter import FarasaSegmenter
from tqdm import tqdm
import re
import editdistance
import pyarabic.araby as araby
from desegmentors import desegmentword
#%%
fs = FarasaSegmenter(interactive=True)


# %%
with open('data/100ksentences.csv','r',encoding='utf-8') as f:
    text = f.read()

# %%
all_non_arabic_characters = r"[^\u0621-\u063A\u0641-\u064A ]+"

def normalize_alef(s):
    s = s.replace(araby.ALEF_HAMZA_ABOVE,araby.ALEF)
    s = s.replace(araby.ALEF_HAMZA_BELOW,araby.ALEF)
    s = s.replace(araby.ALEF_MADDA,araby.ALEF)
    return s
# %%
#Clean and get original and segmented words
all_words= []
for line in tqdm(text.split('\n')):
    cleaned_line = normalize_alef(line)
    cleaned_line = re.sub(all_non_arabic_characters,"",cleaned_line)
    temp_seg_line = fs.segment(cleaned_line).split()
    cleaned_words= cleaned_line.split()
    for i , word in enumerate(temp_seg_line):
        if "+" in word:
            all_words.append((normalize_alef(word),cleaned_words[i]))
#%%
#remove duplicate word tuples
unique_word_tuple = list(set(all_words))
#%%
#verify that the words in a tuple match
all_edit = []
for word_tuples in unique_word_tuple:
    distance = editdistance.distance(word_tuples[0],word_tuples[1])
    if distance > 5:
        print(word_tuples)
    else:
        all_edit.append(distance)

# %%
#remove obvious typos
#this will result in some words that are tru being removed like لالغاء
cleaned_typos = []
count = 0
for i, word_tuples in enumerate(unique_word_tuple):
    if word_tuples[1].startswith("لال"):
        if "ل+ال+" in word_tuples[0] or "ل+ال" in word_tuples[0]:
            print(word_tuples)
            print(i)
            count+=1
            continue
    cleaned_typos.append(word_tuples)


#%%
count = 0
for i, word_tuples in enumerate(tqdm(cleaned_typos)):
    if desegmentword(word_tuples[0])!=word_tuples[1]:
        print(word_tuples)
        print(desegmentword(word_tuples[0]))
        print(i)
        count +=1
        

print('ERROR rate: ',100*count/len(cleaned_typos))
print('Error Count: ',count)
print('Total Words after Cleaning: ',len(cleaned_typos))
print('Total Cleaned Words: ',len(unique_word_tuple) - len(cleaned_typos))


# %%
