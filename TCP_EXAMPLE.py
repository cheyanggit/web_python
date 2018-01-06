#首先是服务端，先是适用bind方法赋予socket以固定的地址和接口，并且使用listen方法来被动
#监听该端口，当有客户尝试用connect方法连接的时候，服务器使用accept接受连接，从而建立起
#一个socket
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
name = socket.gethostname()
port = 1234
s.bind((name,port))
s.listen(5)
while True:
    conn,addr = s.accept()
    print("已经接收到",addr)
    conn.send("欢迎访问".encode('utf-8'))
    conn.close()



