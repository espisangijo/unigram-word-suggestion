from nltk.corpus import gutenberg
import json
text = gutenberg.fileids()

file_name = './unigram.json'
f = open(file_name, 'w', encoding='utf-8')

# print(' '.join(gutenberg.words(text[0])))
ngram_dict = {}
previous = ''
for i in text:
    print(i)
    # x.append(gutenberg.words(i))
    for j in gutenberg.words(i):
        if previous not in ngram_dict:
            ngram_dict[previous] = {}
        if j in ngram_dict[previous]:
            ngram_dict[previous][j] = ngram_dict[previous][j] + 1
        else:
            ngram_dict[previous][j] = 1
        previous = j
    # print(gutenberg.words(i))

f.write(json.dumps(ngram_dict, ensure_ascii=False))
