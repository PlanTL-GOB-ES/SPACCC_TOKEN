#!/usr/bin/env python
# -*- coding: utf-8 -*
import os
import sys
import time
import argparse
from shutil import copyfile


class FreelingToBrat(object):

    def main(self):
        # Read directory with files with Freeling annotations
        for freeling_filename in os.listdir(args.tagged_dir):
            if args.verbose:
                print("Proccessing '" + freeling_filename + "'...")
            try:
                self.start = 0
                self.end = 0
                self.tag_id = 0

                # Split filename
                name_splitted = freeling_filename.split(".")

                # Copy original text file to output directory for comfort
                input_original = name_splitted[0] + ".txt"
                copyfile(args.input_dir + "/" + input_original, args.output_dir + "/" + input_original)

                # Output Brat annotations file with same name but '.ann' suffix
                output_ann = name_splitted[0] + ".ann"

                # Process file and write
                self.convert_text(os.path.join(args.input_dir, input_original),
                                  os.path.join(args.tagged_dir, freeling_filename),
                                  os.path.join(args.output_dir, output_ann))

            except Exception as e:
                if not args.quiet:
                    print("[ERROR] Error while converting Freeling annotation file '%s' to Brat" % freeling_filename)
                    print(e)

    def convert_text(self, original_filename, freeling_filename, output_filename):
        output_ann = open(output_filename, "w")
        text, lines = self.read_file(freeling_filename)
        original_file = open(original_filename, "r").read()
        # Take the different component of Freeling lines: form, lemma, tag, percentage (not used)
        for row in text:
            form = row[0]
            lemma = row[1]
            tag = row[2]
            tag_simple = tag if (tag[0] == 'F' or tag[0] == 'Z') else tag[:2]

            # Find the start and end offset of the form in the text
            try:
                self.start = original_file.find(form, self.end)
            except ValueError:
                if not args.quiet:
                    print("[ERROR] Form '%s' not found in file '%s'." % (form, original_filename))

            # If form is not in the original text check if we are searching a multiword
            if self.start == -1:
                if args.verbose:
                    print("WARNING: '" + form + "' not found in original text: Searching it as multiword...")
                form_trimmed = form.split('_')[0]
                if form_trimmed:
                    self.start = original_file.find(form_trimmed, self.end)
                else:
                    self.start = self.end + 1
            self.end = self.start + len(form)

            # Check if we are searching an abbreviation
            control = form.split('_')
            if len(control) > 1:
                if control[1] == '.':
                    if args.verbose:
                        print("WARNING: '" + form + "' may be an abbreviation: Adjusting offset...")
                    self.end = self.start + len(form) - 1

            self.tag_id += 1

            if args.level == "FULL":
                # Writing line in Brat format (Tx   tag_simple start end    form)
                output_ann.write("T" + str(self.tag_id) + "\t" + tag_simple + " " + str(self.start)
                                 + " " + str(self.end) + "\t" + original_file[self.start:self.end] + "\n")
                # Writing line as Brat comment (#x    Norm Tx    lemma tag)
                output_ann.write("#" + str(self.tag_id) + "\t" + "Norm " + "T" + str(self.tag_id) + "\t" + lemma
                                 + " " + tag + "\n")
            elif args.level == "SENTENCES":
                if form == '.':  # Comprobamos si es un punto
                    # Writing line in Brat format (Tx   tag_simple start end    form)
                    output_ann.write("T" + str(self.tag_id) + "\t" + tag + " " + str(self.start) + " "
                                     + str(self.end) + "\t" + form + "\n")
            elif args.level == "TOKENS":
                # Writing line in Brat format (Tx   tag_simple start end    form)
                output_ann.write("T" + str(self.tag_id) + "\t" + "token" + " " + str(self.start) + " " + str(self.end)
                                 + "\t" + original_file[self.start:self.end] + "\n")

    def read_file(self, filename):
        # Read the file
        input_file = open(filename, "r")
        lines = input_file.readlines()
        text = []
        line_number = 0

        for row in lines:
            # If row is not empty store it
            if len(row) > 1:
                text.append(row.split())
                line_number += 1

        input_file.close()

        return text, line_number


def readable_dir(prospective_dir):
    if not os.path.isdir(prospective_dir):
        raise argparse.ArgumentTypeError("readable_dir:{0} is not a valid path".format(prospective_dir))
    if os.access(prospective_dir, os.R_OK):
        return prospective_dir
    else:
        raise argparse.ArgumentTypeError("readable_dir:{0} is not a readable dir".format(prospective_dir))


if __name__ == "__main__":

    start_time = time.time()
    # Read command line parameters
    parser = argparse.ArgumentParser(description="Script to convert FreeLing3.1 tabular output format into "
                                                 "BRAT standoff format, where only the Sentence Boundary Symbols "
                                                 "are marked.")

    parser.add_argument("-i", "--input_dir",
                        type=readable_dir,
                        help="Folder with the original text files",
                        default='example_input')
    parser.add_argument("-t", "--tagged_dir",
                        type=readable_dir,
                        help="Folder with the files annotated by Freeling",
                        default='example_tagged')
    parser.add_argument("-o", "--output_dir",
                        type=readable_dir,
                        help="Folder to store the output files in BRAT standoff format",
                        default='example_output')
    parser.add_argument("-l", "--level",
                        help="Annotation level",
                        required=True,
                        choices={"FULL", "SENTENCES", "TOKENS"})
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose",
                       help="Increase output verbosity",
                       action="store_true")
    group.add_argument("-q", "--quiet",
                       help="Do not print anything",
                       action="store_true")
    args = parser.parse_args()
    # Load files and process corpus
    if not args.quiet:
        print("Converting your corpus...\n")

    FreelingToBrat().main()

    if not args.quiet:
        print("Processing time: %.2f seconds.\n" % (time.time() - start_time))
