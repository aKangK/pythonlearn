import threading
def ShowOK():
    print(OK)
    
if __name__=='__main__':
    print('test开始！')
    t1=threading.Thread(target=ShowOK)
    lock=threading.Lock()
    lock.acquire()
    lock.acquire()
    t1.start()
    lock.release()
    lock.release()
    print('锁死了吗？')