import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#上面第二个参数制定了这个连接是UDP类型
s.bind(('127.0.0.1',9995))
#UDP不需要调用listen方法，而是直接接受来自任何客户端的数据
print('Bind UDP on 9995...')
while True:
    #接受数据
    data,addr = s.recvfrom(1024)
    #revcfrom()方法返回数据和客户端的地址与端口号，这样，服务器接收到数据后，直接调用sendto就可以把数据用UDP
    #发给客户端
    print('Recieve from %s:%s'%addr)
    s.sendto(b'Hello,%s'%data,addr)