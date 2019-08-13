import socket

class socketCom:

    def __init__(self, host="", port=1234):
        self.h = host
        self.p = port
        self.s = socket.socket()
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    def startServer(self):
        
        try:
            self.s.bind((self.h, self.p))
        except Exception as ex:
            print("error when binding socket")
            template = "An exception of type {0} occured. Arguments: \n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)


            return
        while True: 
            self.s.listen(2)
            conn, addr = self.s.accept()
            conn.send(("Connection accepted").encode('utf-8'))
            print("Connected to ", addr)
       
            while True:
                try: 
                    msg = (conn.recv(1024)).decode('utf-8')
                except ConnectionResetError:
                    print("Connection closed by client")
                    break
                if msg == "close":
                    conn.send(("close").encode('utf-8'))
                    #self.s.shutdown(socket.SHUT_RDWR)
                    #self.s.close()
                    print("connection closed")
                    break 
                elif msg != "":
                    print(msg)
                    conn.send(("Msg recieved").encode('utf-8'))

serv = socketCom()
serv.startServer()
        
