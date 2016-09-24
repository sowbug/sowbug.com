+++
date = "2013-09-03T12:56:00-07:00"
title = "Generating elliptic-curve keys in OpenSSL"
+++



  * Generate a key: openssl ecparam -name prime256v1 -out new-ecdsa-key.pem -genkey -noout
  * Show the key just generated: openssl asn1parse -in new-ecdsa-key.pem
  * Generate the public key corresponding to the given private one: openssl ec -in new-ecdsa-key.pem -pubout -text -noout

