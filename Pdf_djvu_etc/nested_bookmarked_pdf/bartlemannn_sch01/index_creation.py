#!python
# -*- coding: utf-8 -*-
#
# Author      : Stephen Rauch
# Modified by : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Mar 5, 2017
# pastebin link for index.txt: http://pastebin.com/LP8KXAmU
# Imports
from __future__ import print_function, unicode_literals, division, absolute_import

def print_count_page_and_title(data):
    """Get chapters and page numbers."""
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

if __name__ == "__main__":
    test_data = open('bookmarks.txt', 'r', encoding='utf-8').readlines()
    print_count_page_and_title(test_data)
