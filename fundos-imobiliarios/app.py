# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request, redirect, url_for
import requests                
from bs4 import BeautifulSoup
import sqlite3
import json
# from pymongo import MongoClient


### mongo connection
# cliente = MongoClient('mongodb://localhost:27017/')

def insertAtivoName(name):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ativos
        (name)
        VALUES (?)
    """, (name,))
    conn.commit()
    conn.close()   

def updateAtivo(one, three, six, twelve, name):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE ativos
        SET one = ? ,
        three = ? ,
        six = ? ,
        twelve = ?
        WHERE name = ?
    """, (one, three, six, twelve, name))
    conn.commit()
    conn.close()

def selectAll():
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, one, three, six, twelve FROM ativos ORDER BY one DESC; """)
    return cursor.fetchall()
    conn.close()

def selectAtivos():
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name FROM ativos; """)
    return cursor.fetchall()
    conn.close()

def selectAtivo(name):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM ativos WHERE name=? """, (name,))
    return cursor.fetchall()
    conn.close()

def deleteAtivoName(name):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ativos WHERE name=? ", (name,))
    conn.commit()
    conn.close()

def getAtivo():
    for ativo in selectAtivos():
        url = "https://www.fundsexplorer.com.br/funds/{}"
        # compare = {}
        name = ''.join(ativo[0])
        r = requests.get(url.format(name))  
        print(r)   
        soup = BeautifulSoup(r.text, "html.parser") 
        data = soup.find('td', text="Em relação ao valor de cota atual").parent
        A = [row.text.strip() for row in data.findAll("td")][1:]
        # compare[ativo]  = [A[0], A[1], A[2], A[3]]
        name = ''.join(ativo[0])
        one = A[0]
        three = A[1]
        six = A[2]
        twelve = A[3]
        updateAtivo(one, three, six, twelve, name)



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo='Fundos Imobiliarios')

@app.route('/ativos')
def listaAtivos():
    records = selectAll()
    print(records)
    compare = {}
    for ativo in records:
        compare[ativo[0]]  = [ativo[1], ativo[2], ativo[3], ativo[4]]
    return render_template('ativos.html', titulo='Lista de Ativos', compare=compare)

@app.route('/cadastro', methods=['GET'])
def cadastraAtivos():
    return render_template('cadastro.html', titulo='Cadastro de Ativo')

@app.route('/efetua-cadastro', methods=['POST',])
def efetuaCadastro():
    ativo = request.form['ativo']
    print(ativo)
    data = selectAtivo(ativo)
    if not data:
        insertAtivoName(ativo)
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


@app.route('/atualiza-dados')
def atualizaDados():
    ativo = selectAtivos()
    if ativo:
        getAtivo()
        return render_template('atualiza-dados.html', titulo='Base de dados Atualizada!')
    else:
        return render_template('atualiza-dados.html', titulo='Nenhum item para atualizar')

@app.route('/remover-ativo', methods=['POST','GET'])
def Ativo():
    return render_template('remove-ativo.html', titulo='Remover Ativo')

@app.route('/remover-ativo-db', methods=['POST',])
def removeAtivoDb():
    ativo = request.form['ativo']
    print(ativo)
    data = selectAtivo(ativo)
    print(data)
    if data:
        deleteAtivoName(ativo)
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
    

app.run(port=5000, debug=True, host="0.0.0.0")