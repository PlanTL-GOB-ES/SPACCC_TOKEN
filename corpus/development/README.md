# Development corpus

The procedure to annotate the development corpus was the following: First, 10% of the corpus was annotated by 
SPACCC_POS-TAGGER. Next, this annotation was corrected manually and individually by two annotators. 
Finally, using an ad hoc script, the interagreement was measured between them and, if the required minimum levels 
 --99% (sentence splitting), 98% (tokenizing), 96% (POS tagging)-- were not reached, the criteria were revised and the two 
annotators annotated the corpus again. This process was repeated until the required interagreement was obtained, which indicated 
that the annotator had the necessary annotation quality to validate the accuracy of SPACCC_POS-TAGGER.


## Directory structure

* `anotador1/`: texts manually annotated by annotator 1.
* `anotador2/`: texts manually annotated by annotator 2.
* `armonizada/`: gold standard corpus.
* `corpus10porcientodesarrollo/`: original texts used for development. 
* `corpus10porcientodesarrollo_etiquetado/`: texts automatically annotated by SPACCC_POS-TAGGER.
* `README.md`: this file.
