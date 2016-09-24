+++
date = "2015-06-27T10:44:18-07:00"
title = "How to generate a BIP0039 mnemonic in CLI Python"
+++



`>>> import hashlib, mnemonic  
>>> b = hashlib.sha256("secret source of entropy").digest()  
>>> mnemonic.Mnemonic("english").to_mnemonic(b)  
'slogan achieve entire maze regular crunch stem vivid fluid month ceiling
penalty absurd love sort clarify absorb company drink dance excess know
uncover eagle'`

That 24-word phrase is your BIP0039 recovery mnemonic. Substitute your own
string for the secret source of entropy. Don’t be a goof and make it something
cute or memorable that someone else will guess. I recommend the output of `<
/dev/random head -c 256 | shasum -a 512` with a bunch of keyboard mashing
added on the end for good measure. And you don't need to save the entropy
string; the 24 words are all that matter.

