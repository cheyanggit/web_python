#在服务器端，需要先绑定一个端口并且监听来自其他客户端的连接，如果某个客户端连接过来了，服务器就与该客户端建立socket连接
#随后的通信就靠这个socket连接起来了
#服务器会打开固定的端口监听，没来一个客户端连接，就创建该socket连接
#由于服务器会接受多个客户端发送过来的请求连接，所以，服务器就要区分一个socket连接是和哪个客户端绑定的，
#一个socket以来4个项目，服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个socket
#同时呢，服务器还要响应多个客户端的请求，所以每个连接都需要一个新的进程或者新的线程来处理，否则的话，一个服务器就只能跟一个客户端连接了

#下面的任务是接受客户端的请求，把客户端发过来的字符串加上Hello再发回去
import socket
import threading
import time

def tcplink(sock,addr):
    print('Accept new connection from %s:%s...'%addr)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s!'%data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s close.'%addr)




#先创建一个基于IPv4和TCP协议的Socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#然后绑定监听的地址和端口，服务器或许有多块网卡，可以绑定到某一块网卡的IP地址上，可以用127.0.0.1绑定到本机的地址
#如果绑定了这个地址，客户端就必须同时在本机运行才能连接，外部的计算机是无法连接进来的
#端口是需要预先绑定的，因为不是标准服务，所以用9999这个端口号，小于1024的端口号需要管理员权限才能进行绑定
#监听端口
s.bind(('127.0.0.1',9996))
#接着调用listen方法开始监听端口，传入的参数制定等待连接的最大数量
s.listen(5)
print('Waiting for connection...')
#接下来通过一个永久循环来接受来自呵护短的连接，accept会等待并且返回一个客户端的连接
while True:
    #接受一个新的连接
    sock,addr = s.accept()
    #创建新县城来处理TCP连接
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()



