+++
date = "2005-06-01T08:31:48+00:00"
title = "pushd &amp; popd"
+++



Yesterday I discovered the shell commands pushd and popd. For some reason
every time I read the man pages I didn't grok what they were for, but this
time it clicked.

Suppose you're in some directory somewhere like
~/src/main/project/module/test/data/, and you need to work with a file in your
~/scraps directory. Without pushd and popd, you have three choices: open a new
shell, cd to ~/scraps and then cd back again when you're done, or use path
completion to type the full path to the file in ~/scraps.

But what you really want is the hyperspace button, where you jump to the other
directory, do your work, then jump back wherever you were before. This is what
pushd/popd does:

    
    
    [~/src/main/project/module/test/data] $ pushd ~/scraps
    [~/scraps] $ (work with the file)
    [~/scraps] $ popd
    [~/src/main/project/module/test/data] $ (I'm back here again!)

As you can guess from the command names, it's a stack. So you can push all the
locations you want and then get back where you were when you're done.

A belated thanks to my friend and partner in entrepreneurial endeavors, [ Erik
Kay](http://www.eak.com/), who mentioned these commands to me two years ago.

