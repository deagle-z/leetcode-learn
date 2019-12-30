# 顺序打印
import threading


class Foo_1:
    def __init__(self):
        self.t=0;
    
    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        # printFirst() outputs "first". Do not change or remove this line.
        self.t=1
       
        

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.t!=1:
            pass
        printSecond()
        self.t=2
        # printSecond() outputs "second". Do not change or remove this line.
       


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.t!=2:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


class Foo_2:
    def __init__(self):
        self.c=threading.Condition();
        self.t=0

    def first(self,printFirst: 'Callable[[], None]'):
        refs()

    def second(self,printFirst: 'Callable[[], None]'):
        refs()

    def third(self,printFirst: 'Callable[[], None]'):
        refs()
    
    def refs(self,val:int,func: 'Callable[[], None]'):
        while self.t:
            self.c.wait_for(lambda : val==self.t)
        func()
        self.t +=1
        self.c.notify_all() 


    

    