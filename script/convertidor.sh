#!/bin/bash

######################################################################
#
# convertidor.sh
#
# Prepara a partir de un fichero de etiquetas freeling y otro de texto
# plano, distribuidos en carpetas especificadas en la documentacion,
# ficheros .ann para ser visualizados en Brat.
#
# Parametros:
#    $1 : accion
#
# Autor:
#    José Luis Suárez Fueyo, Junio 2018
#
######################################################################

HELP="
USO: \$> bash $0  ACCION
  ACTION : < COMPLETO | PUNTOS | TOKENS >
  {COMPLETO} Prepara ficheros .ann con todas las etiquetas de freeling
  {PUNTOS} Prepara ficheros .ann señalizando los puntos que separan frases.
  {TOKENS} Prepara ficheros .ann con los tokens.
"

cd "$(dirname $0)"

function analisis_completo () 
{
  #Sirve para convertir del formato freeling al formato brat
  python convertidorFreelingBrat.py
  exit 0
}

function analisis_puntos () 
{
  #Sirve para convertir del formato freeling al formato brat para puntos
  python convertidorFreelingBrat_puntos.py
  exit 0
}

function analisis_tokens () 
{
  #Sirve para convertir del formato freeling al formato brat para tokens
  python convertidorFreelingBrat_tokens.py
  exit 0
}

########
#      #
# MAIN #
#      #
########

# Sin argumentos -> ayuda
if [ "$#" -lt 1 ]
then 
  echo "$HELP"
  exit 0

# ANALISIS_COMPLETO
elif [ "$1" == "COMPLETO" ]
then
  shift
  analisis_completo
  exit $?

# ANALISIS_SENTENCES
elif [ "$1" == "PUNTOS" ]
then
  shift
  analisis_puntos
  exit $?

# ANALISIS_TOKENS
elif [ "$1" == "TOKENS" ]
then
  shift
  analisis_tokens
  exit $?


# Si el argumento no es correcto
else
  echo "No se reconoce la accion $1"
  echo "$HELP"
  exit 0

fi

