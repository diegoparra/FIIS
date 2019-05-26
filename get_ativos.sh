#!/bin/bash

function get_atual(){
	echo "Mes Atual:  `curl -s https://www.fundsexplorer.com.br/funds/${i} | grep -A4 "Em relação ao valor de cota atual"| grep -v "Em" | sed -e 's/<td>//g' | sed -e 's/<\/td>//g' | sed -e 's/ //g' | paste -s -d "\n" -  | awk '{if(NR==1) print $0}'` "
}

function get_lastthree(){
	echo "3 Meses:    `curl -s https://www.fundsexplorer.com.br/funds/${i} | grep -A4 "Em relação ao valor de cota atual"| grep -v "Em" | sed -e 's/<td>//g' | sed -e 's/<\/td>//g' | sed -e 's/ //g' | paste -s -d "\n" -  | awk '{if(NR==2) print $0}'` "
}

function get_lastsix(){
	echo "6 Meses:    `curl -s https://www.fundsexplorer.com.br/funds/${i} | grep -A4 "Em relação ao valor de cota atual"| grep -v "Em" | sed -e 's/<td>//g' | sed -e 's/<\/td>//g' | sed -e 's/ //g' | paste -s -d "\n" -  | awk '{if(NR==3) print $0}'` "
}

function get_lasttwelve(){
	echo "12 Meses:   `curl -s https://www.fundsexplorer.com.br/funds/${i} | grep -A4 "Em relação ao valor de cota atual"| grep -v "Em" | sed -e 's/<td>//g' | sed -e 's/<\/td>//g' | sed -e 's/ //g' | paste -s -d "\n" -  | awk '{if(NR==4) print $0}'` "
}

case $1 in
	
	all)
		for i in $(cat ativos.txt) 
		do
			echo "Ativo: ${i}"
			get_atual
			get_lastthree
			get_lastsix
			get_lasttwelve
			echo ""
			echo ""
		done
	;;


	*)
		i=$1
		echo "Ativo: ${i}"
		get_atual
		get_lastthree
		get_lastsix
		get_lasttwelve
		echo ""
		echo ""

	;;
esac


