import wikipedia
import os
import re

wikipedia.set_lang("sw")
titles = []
home = os.path.expanduser("~")
with open(home + "/Downloads/swwiki-20180901-all-titles", "r") as f:
    lines = f.readlines()
    for l in lines:
        titles.append(l.split("\t")[1])
with open(home + "/Downloads/wikipedia_swahili_texts.txt", "w") as f:
    for title in titles:
        print("page {} of {}, {:0.02f} %".format(titles.index(title), len(titles), (100* titles.index(title)/len(titles))))
        try:
            wiki_page = wikipedia.page(title)
            raw_text = wiki_page.content
            clean_text = re.sub(r'([^\s\w]|_)+',"",raw_text)
            text = re.sub(r'\n\n.',"",clean_text)
            f.write(text.lower() + '\n')
        except :
            print(title)
            continue