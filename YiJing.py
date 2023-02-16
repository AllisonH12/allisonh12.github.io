from flask import Flask, render_template
import random

app = Flask(__name__)

class YiJing:
    HEXAGRAMS = { 
    # ... rest of the class code ...
    }

    @staticmethod
    def get_binary_code(word):
        # ... rest of the class code ...

def get_luck():
    word = input("Enter a word: ")
    word += str(random.randint(0, 65))
    binary_code = YiJing.get_binary_code(word)
    fragments = YiJing.get_fragments(binary_code)
    luck = {}
    for fragment in fragments:
        if YiJing.lookup_hexagram(fragment) in luck:
            luck[YiJing.lookup_hexagram(fragment)] += 1
        else:
            luck[YiJing.lookup_hexagram(fragment)] = 1

    sorted_dict = {k: v for k, v in sorted(luck.items(), key=lambda item: item[1], reverse=True)}
    ct = 0
    out = ""
    for key, value in sorted_dict.items():
        ct += 1 
        if ct < 4 and key is not None:
            out += key + "<br>"
    return out

@app.route('/')
def home():
    luck = get_luck()
    return render_template('home.html', luck=luck)

if __name__ == '__main__':
    app.run(debug=True)
