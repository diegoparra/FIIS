# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify
import requests                
from bs4 import BeautifulSoup
import sqlite3
import json

def insertAtivo(name, one, three, six, twelve):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ativos
        (name, one, three, six, twelve)
        VALUES (?,?,?,?,?)
    """, (name, one, three, six, twelve))
    conn.commit()
    conn.close()

def selectAll():
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, one, three, six, twelve FROM ativos ORDER BY id DESC; """)
    return cursor.fetchall()
    conn.close()

def getAtivo():
    ativos = ['BRCR11', 'BCFF11', 'FLMA11', 'KNRI11', 'XPML11', 'MXRF11', 'BCRI11', 'FIGS11', 'IRDM11', 'SPTW11', 'KNIP11', 'RBRR11', 'GGRC11', 'ALZR11']
    url = "https://www.fundsexplorer.com.br/funds/{}"
    compare = {}
    for ativo in ativos:
        r = requests.get(url.format(ativo))           
        soup = BeautifulSoup(r.text, "html.parser") 
        data = soup.find('td', text="Em relação ao valor de cota atual").parent

        A = [row.text.strip() for row in data.findAll("td")][1:]

        compare[ativo]  = [A[0], A[1], A[2], A[3]]
        
        name = ativo
        one = A[0]
        three = A[1]
        six = A[2]
        twelve = A[3]
        insertAtivo(name, one, three, six, twelve)

getAtivo()

compare = {}
for ativo in selectAll():
    compare[ativo[0]]  = [ativo[1], ativo[2], ativo[3], ativo[4]]

print(compare)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo='Fundos Imobiliarios', compare=compare)

app.run(port=5000, debug=True, host="0.0.0.0")