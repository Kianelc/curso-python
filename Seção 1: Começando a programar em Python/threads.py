from threading import Thread
import time

'''
    Thread é uma forma de um processo dividir a si 
    mesmo em duas ou mais tarefas que podem ser 
    executadas concorrencialmente.
    De modo que essas tarefas possam ser executadas 
    concorrencialmente.
'''
def my_func(i):
    print('Iniciando a thread %d' % i)
    time.sleep(5)
    print('Thread %d finalizada' % i)


for i in range(10):
    t = Thread(target=my_func, args=(i,))
    t.start()