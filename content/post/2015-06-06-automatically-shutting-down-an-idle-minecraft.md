+++
date = "2015-06-06T08:39:40-07:00"
title = "Automatically shutting down an idle Minecraft server"
+++



Put this in /etc/cron.hourly/check_minecraft_server or maybe cron.daily
depending on how much you care about paying extra server-rental charges:

> #!/usr/bin/python

>

> # <https://github.com/Dinnerbone/mcstatus>  
> # pip install mcstatus

>

> from mcstatus import MinecraftServer  
> import os

>

> server = MinecraftServer.lookup("your-minecraft-server.com:12345")

>

> status = server.status()

>

> if status and not status.players.online:  
>     print "Server is empty."  
>     os.system("shutdown now -h")

