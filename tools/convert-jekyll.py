#!/usr/bin/python

import codecs
import datetime
import frontmatter
import html2text
import os
import re
import sys

DIR="./original/tumblr/"

for filename in os.listdir(DIR):
    if filename.endswith(".html"):
        f = open(DIR + filename)
        contents = f.read()
        f.close()
        contents = contents.decode('utf8')
        contents = re.sub(r"---", r"---\n\n", contents, re.M)
        try:
            contents = unicode(contents)
        except UnicodeDecodeError, e:
            print "---------", contents
        try:
            md = html2text.html2text(contents)
        except UnicodeDecodeError, e:
            print "problem", e, contents
        md = re.sub(r"^\\---[\s\S]*\\---", r"", md, re.M)

        fm = frontmatter.loads(contents)
        fout = codecs.open("content/post/" +
                           os.path.splitext(filename)[0] + ".md",
                           "w", "utf-8-sig")
        fout.write("+++\n")
        if len(fm.keys()) == 0:
            print filename
            fout.write("%s = \"%s\"\n" % ("draft", "true"))
        else:
            for k in fm.keys():
                if k == "title":
                    fout.write("%s = \"%s\"\n" % (k, fm[k].replace('"','\\"')))
                if k == "date":
                    if "tumblr_url" in fm.keys():
                        fout.write("%s = \"%s\"\n" % (k, fm[k]))
                    else:
                        fout.write("%s = \"%s\"\n" % (k, fm[k].strftime("%Y-%m-%dT%H:%M:%S+00:00")))
            fout.write("+++\n\n")
        fout.write(md)
        fout.close()
