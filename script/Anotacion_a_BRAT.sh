#!/bin/bash

HELP="
USO: \$> bash $0  <input originales> <input anotados> <output> ACCION
  <input originales> : Carpeta con los ficheros en texto plano.
  <input anotados> : Carpeta con los ficheros ya anotados.
  <output> : Carpeta para guardar los ficheros anotados con el texto plano.
  ACTION : < COMPLETO | PUNTOS | TOKENS >
  {COMPLETO} Transforma todas las etiquetas a BRAT.
  {PUNTOS} Transforma los puntos a BRAT.
  {TOKENS} Transforma los tokens a BRAT.
"

# Sin argumentos -> ayuda
if [ "$#" -lt 4 ]
then 
	echo "$HELP"
	exit 1
# Comprobacion de directorios de entrada y salida
elif [ ! -d "$1" ]
then
	echo "No se encuentra el directorio $1"
	exit 2
elif [ ! -d "$2" ]
then
	echo "No se encuentra el directorio $2"
	exit 3
elif [ ! -d "$3" ]
then
	echo "No se encuentra el directorio $3"
	exit 4
# Si el argumento es correcto guardamos el tipo de analisis a realizar
elif [ "$4" == "COMPLETO" ] || [ "$4" == "PUNTOS" ] || [ "$4" == "TOKENS" ]
then
	INPUT_TXT=$(readlink -m "$1")
	INPUT_TAGGED=$(readlink -m "$2")
	OUTPUT=$(readlink -m "$3")
	TIPO="$4"
# Si el argumento no es correcto
else
	echo "No se reconoce la accion $4"
	echo "$HELP"
	exit 5
fi

# Para cada entrada se realiza la copia de los archivos para transformarlos a formato brat
for i in $(find "$INPUT_TXT" -name '*.txt' -exec basename \{\} .txt \;)
do
	#cp "$INPUT_TAGGED/$i.txt_tagged" "$(dirname $0)/entrada/$i.txt_tagged"
	#cp "$INPUT_TXT/$i.txt" "$(dirname $0)/originales/$i.txt"
        cat "$INPUT_TAGGED/$i.txt_tagged" | sed "s/$(echo -n "&nbsp;" | html2text)/ẍ/g" > "$(dirname $0)/entrada/$i.txt_tagged"
        cat "$INPUT_TXT/$i.txt" | sed "s/$(echo -n "&nbsp;" | html2text)/ẍ/g" > "$(dirname $0)/originales/$i.txt"
done
# Se hace una llamada al script de paso de Freeling a BRAT
bash "$(dirname $0)/convertidor.sh" $TIPO

# Se copia el texto en plano y la anotacion de BRAT (.ann) en la carpeta output y se limpian las carpetas intermedias
for i in $(find "$INPUT_TXT" -name '*.txt' -exec basename \{\} .txt \;)
do
	#cp $(dirname $0)/ann/$i.ann "$OUTPUT"
	#cp $(dirname $0)/originales/$i.txt "$OUTPUT"
	cat $(dirname $0)/ann/$i.ann | sed "s/ẍ/$(echo -n "&nbsp;" | html2text)/g" > "$OUTPUT/$i.ann"
	cat $(dirname $0)/originales/$i.txt | sed "s/ẍ/$(echo -n "&nbsp;" | html2text)/g" > "$OUTPUT/$i.txt"
	rm $(dirname $0)/ann/$i.ann
	rm $(dirname $0)/originales/$i.txt
	rm $(dirname $0)/entrada/$i.txt_tagged
done

