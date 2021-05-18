import json
from difflib import SequenceMatcher
from difflib import get_close_matches
def translate():
    # print("Enter the word you want to know:\n")
    word = input("Enter the word you want to know:\n")
    data = json.load(open("data.json"))
    if word in data:
        ans = data.get(word.lower())
        for item in ans:
            print(item)
        return
    elif len(get_close_matches(word, data.keys()))>0:
        w= get_close_matches(word, data.keys())[0]
        user_input = input("Did you mean {} please enter yes or no\n".format(w))
        if user_input == 'yes':
            word = w
            if word in data:
                ans = data.get(word.lower())
                for item in ans:
                    print(item)
                return
        else:
            print("We didn't understand your entry ,please check")
    else:
        print("Word not found ,please check")
translate()

