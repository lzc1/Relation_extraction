from multiprocessing import Process
import os

def run_porc(name):
    print('I am the child process %s,my process id is %s'%(name,os.getpid()))

if __name__ == '__main__':
    print('parent process is running ,id is %d'%os.getpid())
    p = Process(target=run_porc,args=('test',))
    print('the child process is going to run')
    p.start()
    #等待子进程运行完成
    p.join()
    print('process end')