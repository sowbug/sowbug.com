+++
date = "2013-08-31T20:11:00-07:00"
title = "paSSSphrase: safely store secrets for your successors"
+++



My latest GitHub project,
[paSSSphrase](https://github.com/sowbug/paSSSphrase), was inspired by a recent
[Instructable about electroetching digital
assets](http://www.instructables.com/id/A-Stainless-Steel-Bitcoin-Wallet/).

![image](http://66.media.tumblr.com/6800db9909caa2d59e75b187e3489eed/tumblr_inline_msffak5w7X1qz4rgp.jpg)

The basic idea is to split a strong passphrase among multiple shares according
to [Shamir's Secret Sharing
algorithm](http://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing), then
generate an inverted/mirrored image of the shares as QR codes. The image
transformations make for an easy
[electroetching](http://en.wikipedia.org/wiki/Electroetching) stencil.

So far I haven't actually done this process for a secret I care about. But I
thought electroetching was interesting enough to want to spend a few evenings
working on it. I wrote up what I learned from my experience in the project
README.

If you try this, let me know! (But don't send me pictures, please, unless you
want to share your secrets with me.)

_Update: The poor man's version is **lines=( $( LC_CTYPE=C &lt;/dev/urandom tr
-dc '[:alnum:]' | head -c32 | ssss-split -t3 -n5 -Q ) ) ; for line in
"${lines[@]}"; do qrencode -o share-${line:0:1}.png $line; done**. This
version just spits out the shares as individual PNGs that you can print on
regular paper. You can verify the results even if you don't have a QR-code
scanner with __**zbarimg -raw share-*.png | ssss-combine -t3 -q**._

