# SPACCC_TOKEN: Spanish Clinical Case Corpus - Tokenization

## Digital Object Identifier (DOI) and access to source files

https://doi.org/10.5281/zenodo.1494869


## Introduction

This repository contains the tokenization annotations in the Spanish Clinical Case Corpus that have been 
carried out by means of the Spanish Clinical Case Corpus Part-of-Speech Tagger based on FreeLing3.1 
(SPACCC_POS-TAGGER, https://github.com/PlanTL/SPACCC_POS-TAGGER).


## Repository structure

<pre>
corpus/
Original, development, validation and automatically annotated corpus, both in tabular format and BRAT 
standoff format.

guidelines/
Annotation guidelines.

IAA/
Onter-annotator agreement report, along with the data and the scripts used to calculate it. 

script/
Script to convert FreeLing3.1 tabular output format into BRAT standoff format.
</pre>


## Document selection

The SPACCC corpus was created after collecting 1,000 clinical cases from SciELO (Scientific Electronic Library Online), 
an electronic library that gathers electronic publications of complete full text articles from scientific journals of 
Latin America, South Africa and Spain (http://www.scielo.org).

A clinician classified those cases into those that were similar to real clinical texts in terms of structure and content
and those that were not suitable for this task. Figure legends were automatically removed and in case multiple clinical 
cases were listed, these were split into single clinical cases.


## Annotation format

Annotations created in SPACCC_TOKEN are provided in BRAT standoff format; i.e. the annotations are stored separately 
(in an `.ann` file) from the document text, which is never modified by the tool. 
These two files are associated by their base name; their file name without suffix is the same: 
`es-S0004-06142005000200009-1.ann` contains the annotations for the file `es-S0004-06142005000200009-1.txt`. 
See http://brat.nlplab.org/standoff.html for further details on the brat standoff format. 

This annotation format is produced by running an script that converts the output of SPACC_POS-TAGGER, a 
CoNLL-like column format where columns are:

* `FORM`: word form.
* `LEMMA`: word lemma.
* `TAG`: complete POS tag.
* `PROBABILITY`: probability of the chosen tag.


## Annotation guidelines

The annotation guidelines describe the criteria that have been followed to annotate the corpus, along with illustrative examples. They describe FreeLing default resources, the criteria that have been followed in the manual annotation and the implementations that solve these criteria in automatic annotation. The guidelines also compare the criteria followed in this project with those followed by the Apache CTAKES NLP system (http://ctakes.apache.org/) as well as the criteria followed in the development of the GENIA corpus (https://github.com/spyysalo/genia-pos).

Guidelines have been written and developed in Spanish and are only available in Spanish.


## Corpus consistency

The following three tables show the interagreement results measured on both the development and the validation corpus. See the inter-annotator agreement report (Informe_interagreement_CNIO_PlanTL_SEAD.pdf) included in folder `IAA`in this repository for further details. The required minimum level was 98%.

|                        | Token  | 
| ---------------------- | ------ |
| A1 vs A2               | 99,97% | 
| A1 vs FL               | 99,95% | 
| A2 vs FL               | 99,96% | 

Table 1: Interagreement betwen the two human annotators and SPACCC_POS_TAGGER on the development corpus.


|                        | Token  | 
| ---------------------- | ------ |
| GS vs FL               | 99,95% | 

Table 2: Interagreement between the gold standard corpus and SPACCC_POS-TAGGER on the development corpus.


|                        |  Token |
| ---------------------- | ------ |
| GS vs FL               | 99,97% |

Table 3: Interagreement between the gold standard corpus and SPACCC_POS-TAGGER on the validation corpus.


## Contact

Montserrat Marimon (montserrat.marimon@bsc.es)


## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

Copyright (c) 2018 Secretaría de Estado para el Avance Digital (SEAD)
