+++
date = "2005-07-01T13:20:00+00:00"
title = "xterm & backspace key"
+++



If you're using xterm and hitting the backspace key doesn't do what you
expect, add this to your .Xdefaults file:

    
    
    xterm.*.backarrowKey: false

(Thanks, [Kelly Felkins](http://kellyfelkins.org/?c=emacs).) Another solution
specific to Emacs is to add this to your .emacs file:

    
    
    (define-key global-map "\010" 'backward-delete-char-untabify)

(Thanks, Ehud Karni.)

