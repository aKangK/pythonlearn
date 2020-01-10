from multiprocessing import Process,Pipe
from datetime import datetime
def do_send(conn_s,j):
    conn_s.send({'发送序号':j,'鲫鱼':[18,10.5],'鲤鱼':[8,6.2]})
    conn_s.close()

if __name__=='__main__':
    receive_conn,send_conn=Pipe()
    i=0
    while i<2:
        i=i+1
        pp=Process(target=do_send,args=(send_conn,i,))
        pp.start()
        print(datetime.now())
        print('接受数据%s成功！'%(receive_conn.recv()))
        pp.join