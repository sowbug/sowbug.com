+++
date = "2005-03-21T16:38:57+00:00"
title = "SMTP sample exchange"
+++



Because I always forget, here's how to manually send a mail given a telnet
client and an SMTP server in order to test and make sure the server's working:

`$ telnet mail.example.com 25  
Trying 12.34.56.78...  
Connected to mail.example.com (12.34.56.78).  
Escape character is '^]'.  
220 mail.example.com ESMTP Ready on Mon, 21 Mar 2005 16:29:31 -0800 [a.mail]  
HELO mail.somewhere.com  
250 a.mail.somewhere.com Hello 98.76.54.32.somewhere.com [98.76.54.32],
pleased to meet you  
MAIL FROM:<mike@somewhere.com>  
250 2.1.0 <mike@somewhere.com>... Sender ok  
RCPT TO:<someone@example.com>  
250 2.1.5 <someone@example.com>... Recipient ok  
DATA  
354 Enter mail, end with "." on a line by itself  
Hello there!  
OK, bye!  
.  
250 2.0.0 0987654321 Message accepted for delivery  
QUIT  
221 2.0.0 a.mail.example.com closing connection  
Connection closed by foreign host.  
$  
 `

