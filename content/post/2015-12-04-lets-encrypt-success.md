+++
date = "2015-12-04T13:52:13-08:00"
title = "Let’s encrypt: success!"
+++



Here’s what I did to get [z.sowbug.com](https://z.sowbug.com/) running with a
Let’s Encrypt cert.

  * `git clone <https://github.com/letsencrypt/letsencrypt>`
  * `cd letsencrypt/`
  * `./letsencrypt-auto certonly --standalone -d z.sowbug.com`
  * `sudo tar cf etc-letsencrypt.tar.gz /etc/letsencrypt`
  * `gpg -c etc-letsencrypt.tar.gz`
  * (scp etc-letsencrypt.tar.gz somewhere safe)
  * `sudo su -`
  * `apt-get install nginx`
  * `cd /etc/nginx/`
  * `emacs sites-enabled/default`
  * Shove in results of [Mozilla SSL Configuration Generator](https://mozilla.github.io/server-side-tls/ssl-config-generator/), with nginx/modern/1.4.6 selected.
  * Delete `ssl_trusted_certificate` line (not sure what that is)
  * Change to `ssl_certificate /etc/letsencrypt/live/z.sowbug.com/fullchain.pem;`
  * Change to `ssl_certificate_key /etc/letsencrypt/keys/0000_key-letsencrypt.pem;`
  * exit Emacs
  * `sudo /etc/init.d/nginx reload`

Looks like a lot of steps, but it was actually pretty easy.

