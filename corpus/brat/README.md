# BRAT Corpus

Corpus annotated in the BRAT standoff format, where only the tokens are marked: the annotations are stored separately 
(in an `.ann` file) from the document text, which is never modified by the tool. 

These two files are associated by their base name; their file name without suffix is the same: 
`es-S0004-06142005000200009-1.ann` contains the annotations for the file `es-S0004-06142005000200009-1.txt`. 
These two files have to be placed in the same folder in order to visualize the annotations with web-based tool.  

See http://brat.nlplab.org/standoff.html for further details on the brat standoff format and 
http://brat.nlplab.org/index.html for the tool.

This annotation format is produced by running an script that converts the output of SPACC_POS-TAGGER.

## Directory structure

* `ann`: annotation files.
* `txt`: text files.
* `README.md`: this file.
