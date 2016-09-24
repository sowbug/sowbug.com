#!/usr/bin/python

import datetime
import frontmatter
import html2text
import os
import re

DIR="./original/jekyll/"

for filename in os.listdir(DIR):
    if filename.endswith(".html"):
        f = open(DIR + filename)
        contents = f.read()
        f.close()
        contents = re.sub(r"---", r"---\n\n", contents, re.M)
        md = html2text.html2text(contents)
        fm = frontmatter.loads(contents)
        fout = open("content/post/" +
                    os.path.splitext(filename)[0] + ".md", "w")
        fout.write("+++\n")
        if len(fm.keys()) == 0:
            print filename
            fout.write("%s = \"%s\"\n" % ("draft", "true"))
        else:
            for k in fm.keys():
                if k == "title":
                    fout.write("%s = \"%s\"\n" % (k, fm[k]))
                if k == "date":
                    fout.write("%s = \"%s\"\n" % (k, fm[k].strftime("%Y-%m-%dT%H:%M:%S+00:00")))
        fout.write("+++\n\n")
        fout.write(md)
        fout.close()
