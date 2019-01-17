# Script

Script to convert FreeLing3.1 tabular output format into BRAT standoff format, where only the Sentence Boundary Symbols are marked.

## Directory structure
* `ann/`: folder for temporary use of the script `Anotacion_a_BRAT.sh`
* `Anotacion_a_BRAT.sh`: main script.
* `convertidorFreelingBrat_tokens.py`: auxiliary script to convert the tokenization.
* `convertidor.sh`: auxiliary script to call the suitable conversor.
* `ejemplo_anotados/`: annotated sample text folder.
* `ejemplo_originales/`: original sample text folder. 
* `ejemplo_resultados_ann_BRAT/`: sample text folder as they result from the execution of the script `Anotacion_a_BRAT.sh`.
* `entrada/`: folder for temporary use of the script` Anotacion_a_BRAT.sh`.
* `generadorFicherosBrat.py`: script with auxiliary functionality common to all converters.
* `originales/`: folder for temporary use of the script `Anotacion_a_BRAT.sh`.
* `README.md`: this file.

### Prerequisites

The script requires Python 3 and html2text module installed on your system. You can install html2text module using the following command 
with the right privileges:

<pre>
apt install html2text
</pre>

NOTE: `ann/`, `entrada/`, `originales/` and output folders must be created manually before running this script.

### Troubleshooting

If Python 3 is not called by default in your enviromentment, please change the call to `python` by `python3` in the 
`convertidorFreelingBrat_tokens.py` script or create an alias.

If you get an error similar to `'ascii' codec can't decode byte 0xc3 in position 67: ordinal not in range(128)` you can correct
your locale configuration executing these commands:

<pre>
apt-get install -y --no-install-recommends locales && locale-gen en_US.UTF-8
export LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8
</pre>


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

