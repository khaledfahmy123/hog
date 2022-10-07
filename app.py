from flask import Flask, jsonify, request
import enchant


d = enchant.Dict("en_US") 

app = Flask(__name__)

print(d.check("lo7l"))


def check(word):
    dictionary = PyDictionary()

    if dictionary.meaning(word,True) is None:
       return False
    else:
       return True


ref = {
    "a": "ا",
    "b": "ب",
    "c": "س",
    "d": "د",
    "e": "ي",
    "f": "ف",
    "g": "ج",
    "h": "ه",
    "i": "ي",
    "j": "ج",
    "k": "ك",
    "l": "ل",
    "m": "م",
    "n": "ن",
    "o": "و",
    "p": "ب",
    "q": "ق",
    "r": "ر",
    "s": "س",
    "t": "ت",
    "u": "ي",
    "v": "ف",
    "w": "و",
    "x": "ك",
    "y": "ي",
    "z": "ز",
    "9": "ص",
    "8": "ق",
    "7": "ح",
    "6": "ط",
    "5": "خ",
    "4": "ش",
    "3": "ع",
    "2": "ئ",
  }


@app.route("/")
def home_view():
        return "<h1>Hello World!</h1>"

@app.route('/words')
def get_incomes():
    word = request.get_json()
    res = []
    arr = word["example"].split()
    for i in arr:
        word = ""
        if not d.check(i):
            for j in i:
                try: 
                    word += ref[j]
                except:
                    word += j
        else:
            word = i
        res.append(word)
        
    return jsonify(" ".join(res))




if __name__ == "__main__":
    app.run()