import json

file_name = './unigram.json'
with open(file_name, encoding="utf-8") as f:
    text = json.load(f)

for key, value in sorted(mydict.items(), key=lambda (k, v): (v, k)):
    print "%s: %s" % (key, value)


f = open(file_name, 'w', encoding='utf-8')
f.write(json.dumps(text, ensure_ascii=False))
