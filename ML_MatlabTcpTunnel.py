import socket

class ML_MatlabTcpTunnel():
    def __init__(self, Address, Port, BuffSize, Terminator, TimeOut): 
        self.Address = Address
        self.Port = Port 
        self.BuffSize = BuffSize
        self.Terminator = Terminator
        self.TimeOut = TimeOut
        self.Socket = None
        
    def Connect(self):
        socket.setdefaulttimeout(self.TimeOut)
        self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Connects to server
        connectError = self.Socket.connect_ex((self.Address, self.Port))
        if (connectError==0):
            return True
        else:
            return False


    def SendMessage(self, Message):
        #Message = Message + self.Terminator
        sent = self.Socket.send(Message.encode('utf-8'))
        return True

    def ReceiveMessage(self):
        tempMessage = self.Socket.recv(self.BuffSize)
        Message = tempMessage.decode('utf-8')
        return Message

    def Close(self):
        self.Socket.close()



