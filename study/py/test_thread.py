'''
我们提供了一个类：

public class Foo {
  public void one() { print("one"); }
  public void two() { print("two"); }
  public void three() { print("three"); }
}
三个不同的线程将会共用一个 Foo 实例。

线程 A 将会调用 one() 方法
线程 B 将会调用 two() 方法
线程 C 将会调用 three() 方法
请设计修改程序，以确保 two() 方法在 one() 方法之后被执行，three() 方法在 two() 方法之后被执行。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/print-in-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from threading import *


class Foo:
    def __init__(self):
        self.s1 = Semaphore(1)
        self.s2 = Semaphore(0)
        self.s3 = Semaphore(0)

    def first(self, printFirst):
    # 每调用一次acquire()，计数器减1；每调用一次release()，计数器加1,当计数器为0时，acquire()调用被阻塞。
    # printFirst() outputs "first". Do not change or remove this line.
        self.s1.acquire()
        printFirst()
        self.s2.release()


    def second(self, printSecond):

# printSecond() outputs "second". Do not change or remove this line.
        self.s2.acquire()
        printSecond()
        self.s3.release()


    def third(self, printThird):

# printThird() outputs "third". Do not change or remove this line.
        self.s3.acquire()
        printThird()