# Validation corpus

The procedure to annotate the validation corpus was the following: 10% of the corpus was randomly selected to 
assess SPACCC_POS-TAGGER and it was annotated by both SPACCC_POS-TAGGER and one of the annotators. 
Using an ad-hoc script, the interagreement between them was measured and, if the required minimum 
levels --99% (sentence splitting), 98% (tokenizing), 96% (POS tagging)-- were not reached, 
SPACCC_POS-TAGGER was tunned until they are reached. 

## Directory structure

* `anotador1/`: texts manually annotated by annotator 1.
* `corpus10porcientovalidacion/`: original texts used to validate SPACCC_POS-TAGGER.
* `corpus10porcientovalidacion_etiquetado/`: texts automatically annotated by SPACCC_POS-TAGGER.
* `README.md`: this file.
