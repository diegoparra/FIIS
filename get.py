#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests                
from bs4 import BeautifulSoup
import pandas as pd

ativos = ['BRCR11', 'BCFF11', 'FLMA11', 'KNRI11', 'XPML11', 'MXRF11', 'BCRI11', 'FIGS11', 'IRDM11', 'SPTW11', 'KNIP11', 'RBRR11', 'GGRC11', 'ALZR11']
url = "https://www.fundsexplorer.com.br/funds/{}"
compare = {}

def main():
    for ativo in ativos:
        r = requests.get(url.format(ativo))           
        soup = BeautifulSoup(r.text, "html.parser") 
        data = soup.find('td', text="Em relação ao valor de cota atual").parent
    
        A = [row.text.strip() for row in data.findAll("td")][1:]

        new_dic = {'1': A[0],
                  '3': A[1],
                  '6': A[2],
                  '12': A[3]}

        compare[ativo]  = A[0]

        df=pd.DataFrame(new_dic.items(), columns=['MES', 'VALOR'], index=[' ', ' ', ' ', ' '])
        print('\n\n{}\n'.format(ativo))
        print(df)

def comp():
        
        listofTuples = sorted(compare.items() ,  key=lambda x: x[1], reverse=True )
        print('\n\n\n''Principais rendimentos:')
        for elem in listofTuples :
                print(elem[0] , " ::" , elem[1] )


if __name__ == '__main__':
    main()
    comp()