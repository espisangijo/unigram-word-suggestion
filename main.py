import json

file_name = './unigram.json'
with open(file_name, encoding="utf-8") as f:
    text = json.load(f)

print("Autocomplete Program")
print("Enter a word: ")
x = 'Emma'
while True:
    suggestions = []
    for key, value in text[x].items():
        suggestions.append([key, value])
    suggestions = sorted(suggestions, key=lambda suggestions: suggestions[1], reverse=True)
    if len(suggestions) == 1:
        print("suggestion: ", suggestions[0][0])
    elif len(suggestions) == 2:
        print("suggestion: ", suggestions[0][0], suggestions[1][0])
    elif len(suggestions) >= 3:
        print("suggestion: ", suggestions[0][0], suggestions[1][0], suggestions[2][0])
    else:
        print("no suggestion")
    x = input()
    print("text: ", x)
