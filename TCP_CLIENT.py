#socket就是表示打开了一个网络连接，而打卡一个socket需要知道目标计算机的IP地址和端口号，再指定协议类型
import socket
#创建一个socket,AF_INET是指定IPv4协议，如果用IPv6就是AF_INET6，后面的参数指的是使用面向流的TCP协议，这样就建立起了一个socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立连接
#下面是发起连接，须知道IP和端口号，域名会自动转换成IP地址，80端口号是web服务的标准端口，其他服务都有对应的端口号
#小于1024的端口号是internet标准服务端口号，大于1024的，可以任意使用
s.connect(('www.sina.com.cn',80))

#以下是发送数据
s.send(b'GET/HTTP/1.1\r\nConnection:close\r\n\r\n')
#以下是接受数据
buffer = []
while True:
    #以下是每次最多接受1k字节，在while循环中，只要有数据就不停接受，当空数据的时候，就跳出循环
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
print(data)
print(buffer)
header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('sina.html','wb') as f:
    f.write(html)


#当接受完数据之后，用close关闭socket，一次完整的网络通信就结束了
s.close()

