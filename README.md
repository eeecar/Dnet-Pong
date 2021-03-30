# Pong Game

## Configuration 
First go to  /PongGame/Server/server.py

Change the TCP port and UDP port for broadcast in 
>[line 39](https://gitlab.lrz.de/ge56jow/lkn-class-project/-/blob/master/PongGame/Server/server.py#L39) `self.tcpport = 54001`
>
>[line 328](https://gitlab.lrz.de/ge56jow/lkn-class-project/-/blob/master/PongGame/Server/server.py#L328)`port0 = 54000`

Then go to /PongGame/Client/Braodcast.py

Change the broadcast address to the broadcast server in 
>[line 9](https://gitlab.lrz.de/ge56jow/lkn-class-project/-/blob/master/PongGame/Game/Braodcast.py#L9) `self.addr = ("129.187.223.130", 54333)`


## Play
To open the server without GUI, please run /PongGame/Server/server.py

To open the client GUI, please run /gui_lobby.py

