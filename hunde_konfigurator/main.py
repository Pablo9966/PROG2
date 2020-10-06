from flask import Flask, render_template
from random import randrange
from json import loads, dumps
import json


"""
Hier importieren wir die Files mit den Fragen. Die Files wurden als json geschrieben
und können daher importiert und wie Dictionaries behandelt werden.
Wenn die Files nicht richtig importiert werden können,
wird durch das Try and Except eine Fehlermeldung ausgegeben.
"""
with open("fragen1.json", encoding="utf-8") as json_file:
    fragen = json.load(json_file)

nummer = 1

frage = fragen[str(nummer)]["Frage"]
antwort = fragen[str(nummer)]["Antwort"]


app = Flask("Hunde Konfigurator")


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/konfigurator')
def konfigurator():
    return render_template('konfigurator.html', frage=frage, antwort=antwort)


if __name__ == "__main__":
    app.run(debug=True, port=5002)


def runde():
    print(fragen[str(nummer)]["Frage"])
    for x in range(0, 4):
        print(fragen[str(nummer)]["Antwort"][x][0],
              fragen[str(nummer)]["Antwort"][x][1])
    antwort = input("\nWie lautet deine Antwort? ")
    antwort = antwort.upper()


while(1):
    runde()
    nummer += 1
