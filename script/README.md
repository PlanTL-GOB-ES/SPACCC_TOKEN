# Script

Script to convert FreeLing3.1 tabular output format into BRAT standoff format, where only the tokens are marked.

## Directory structure
* `ann/`: folder for temporary use of the script `Anotacion_a_BRAT.sh`
* `Anotacion_a_BRAT.sh`: main script.
* `convertidorFreelingBrat_puntos.py`: auxiliary script to convert the sentence splitting. 
* `convertidorFreelingBrat.py`: auxiliary script to complete the conversion.
* `convertidorFreelingBrat_tokens.py`: auxiliary script to convert the tokenization.
* `convertidor.sh`: auxiliary script to call the suitable conversor.
* `ejemplo_anotados/`: annotated sample text folder.
* `ejemplo_originales/`: original sample text folder. 
* `ejemplo_resultados_ann_BRAT/`: sample text folder as they result from the execution of the script `Anotacion_a_BRAT.sh`.
* `entrada/`: folder for temporary use of the script` Anotacion_a_BRAT.sh`.
* `generadorFicherosBrat.py`: script with auxiliary functionality common to all converters.
* `originales/`: folder for temporary use of the script `Anotacion_a_BRAT.sh`.
* `README.md`: this file.

## Usage

### Prerequisites

The script requires Python 3 installed on your system.

### Convertir de formato FreeLing a BRAT

To convert a set of files labeled by SPACCC_POS-TAGGER into BRAT standoff format, follow the following steps:
* Put all original files (with extension `.txt`) in a folder
* Put all of their corresponding annotated files (with extension `.txt_tagged`) in another folder
* Create an output folder
* Run the `Anotacion_a_BRAT.sh` script by choosing the TOKENS annotation level

### Example:

Assuming that we have:
- the original files are in folder `ejemplo_originales/`
- the annotated files are in folder `ejemplo_anotados/`
- the destination folder is `ejemplo_resultados_ann_BRAT/` (it has to be created)

<pre>
Anotacion_a_BRAT.sh ejemplo_originales/ ejemplo_anotados/ ejemplo_resultados_ann_BRAT/ TOKENS 
</pre>
