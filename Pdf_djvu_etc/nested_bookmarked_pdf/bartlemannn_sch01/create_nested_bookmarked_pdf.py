#!python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Jan 22, 2017
#
# Imports
import io
import subprocess
import os
from pdfrw import PdfReader, PdfWriter
from natsort import natsorted
import glob


def create_index_file_for_ghostscript(bookmarks_file):
    """Get chapters and page numbers."""
    data = open(bookmarks_file, 'r', encoding='utf-8').readlines()
    fo = open('index.txt', 'w', encoding='utf-8')
    print('Creating: ', 'index.txt')
    chapters = []
    chapter = None
    for line in data:
        if line.startswith('Chapter'):
            if chapter is not None:
                chapters.append(chapter)
            chapter = (line.strip().rsplit(' ', 1), [])
            # chapter is tuple of two lists
            # second list is empty list
            # first list has two elements,
            # second element is separated by white space in end by rsplit.
            # print(line)
            # Chapter 1 Introduction 1
            # print(chapter)
            # (['Chapter 1 Introduction', '1'], [])
            # print("\n")
        else:
            subchapter = line.strip().rsplit(' ', 1)
            chapter[1].append(subchapter)

    if chapter is not None:
        chapters.append(chapter)

    def page_num(page):
        try:
            return int(page) - 290
        except:
            return 5


    fmt_chapter = '[/Count -%d /Page %d /Title (%s) /OUT pdfmark'
    fmt_sub_chapter = '[/Count 0 /Page %d /Title (%s) /OUT pdfmark'

    for chapter in chapters:
        print(fmt_chapter % (
            len(chapter[1]), page_num(chapter[0][1]), chapter[0][0]), file=fo)
        for sub_chapter in chapter[1]:
            print(fmt_sub_chapter % (
                page_num(sub_chapter[1]), sub_chapter[0]), file=fo)
        pass
    fo.close()


def create_bookmarked_pdf(inpdf, outpdf):
    """Create clickable pdf."""
    commands = "gs -sDEVICE=pdfwrite -q -dBATCH -dNOPAUSE -sOutputFile={} -dPDFSETTINGS=/prepress index.txt -f {}".format(outpdf, inpdf)
    subprocess.call(commands, shell=True)
    subprocess.call('pwd', shell=True)
    print('Creating {}'.format(outpdf))


def main():
    """Run main function."""
    bookmarks_file='bookmarks.txt'
    inpdf = 'in.pdf'
    outpdf = 'output.pdf'

    create_index_file_for_ghostscript(bookmarks_file)
    create_bookmarked_pdf(inpdf, outpdf)


if __name__ == "__main__":
    main()
