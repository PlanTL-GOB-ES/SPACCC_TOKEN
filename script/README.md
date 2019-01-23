# Introduction
------------

Script to convert FreeLing3.1 tabular output format into BRAT standoff format, where only the tokens are marked.


### Prerequisites
------------

The script requires Python 3 installed on your system.

NOTE: Do not remove `example_input/`, `example_tagged/` and `example_output/` folders.


## Directory structure
------------

<pre>
example_input/
	Original sample text files folder. 

example_tagged/
	Annotated sample text files folder.

example_output/
	Sample text files folder as they result from the execution of the script `convertFreelingToBrat.py`.

convertFreelingToBrat.py
	Main script.

generadorFicherosBrat.py
	Script with auxiliary functionality to the converter.

README.md
	This file.
</pre>



## Usage
------------

It is possible to configure the behavior of this software using the different options.

  - The `input_dir`, `tagged_dir`, and `output_dir` options allow to change the default folders.
  
  - `verbose` and `quiet` options allow to control the verbosity level of the software.
  
  - `level` option allows to select the desired level of annotation: `TOKENS`, `SENTENCES` 
or `FULL`.


The user can select the different options using the command line:

	python convertFreelingToBrat.py [options] 

Options:
<pre>
-h, --help            show this help message and exit
-i INPUT_DIR, --input_dir INPUT_DIR	Folder with the original text files
-t TAGGED_DIR, --tagged_dir TAGGED_DIR	Folder with the files annotated by Freeling
-o OUTPUT_DIR, --output_dir OUTPUT_DIR	Folder to store the output files in BRAT standoff format
-l {SENTENCES,FULL,TOKENS}, --level {SENTENCES,FULL,TOKENS}	Annotation level
-v, --verbose         Increase output verbosity (not allowed with argument -q/--quiet)
-q, --quiet           Do not print anything (not allowed with argument -v/--verbose)
</pre>


### Convert from Freeling format to BRAT
------------

To convert a set of files labeled by SPACCC_POS-TAGGER into BRAT standoff format, follow the following steps:
<pre>
- Put all original files (with extension `.txt`) in a folder.
- Put all of their corresponding annotated files (ex: with extension `.txt_tagged`) in another folder.
- Create an output folder.
- Run the `convertFreelingToBrat.py` script by choosing the FULL annotation level.
</pre>


### Example
------------
Assuming that we have the following configuration:

<pre>
- The original files are in folder `example_input/`
- The annotated files are in folder `example_tagged/`
- The destination folder is `example_output/`
</pre>

Run:

<pre>
python convertFreelingToBrat.py -i example_input/ -t example_tagged/ -o example_output/ -l TOKENS
</pre>

Given that those are the default folders, it also works running the following command:

<pre>
python convertFreelingToBrat.py -l TOKENS
</pre>



## Contact
------

Aitor Gonzalez-Agirre (aitor.gonzalez@bsc.es)


## License
-------

Copyright (c) 2017-2018 Secretaría de Estado para el Avance Digital (SEAD)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
