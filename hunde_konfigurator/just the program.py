from flask import Flask
from flask import render_template
from random import randrange
from json import loads, dumps
import json


with open("fragen1.json", encoding="utf-8") as json_file:
    fragen = json.load(json_file)

nummer = 1

frage = fragen[str(nummer)]["Frage"]
antwort = fragen[str(nummer)]["Antwort"]


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
