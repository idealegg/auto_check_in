from threading import Timer

cnt = 0


class MyTimer:
    def __init__(self):
        self._timer = None
        self._tm = None
        self._fn = None

    def _do_func(self):
        if self._fn:
            self._fn()
        self._do_start()

    def _do_start(self):
        self._timer = Timer(self._tm, self._do_func)
        self._timer.start()

    def start(self, tm, fn):
        global cnt
        cnt = 0
        self._fn = fn
        self._tm = tm
        self._do_start()

    def stop(self):
        try:
            self._timer.cancel()
            print "cnt:[%d]" %cnt
        except:
            pass


def hello():
    import sys
    global cnt
    cnt += 1
    from datetime import datetime
    #sys.stdout.write("hello world![%d] %s\r" % (cnt, datetime.now()))
    sys.stdout.write("hello world![%d] %s\n" % (cnt, datetime.now()))
    sys.stdout.flush()


if __name__ == '__main__':
    mt = MyTimer()
    mt.start(2, hello)
    for i in range(10):
        import time
        time.sleep(1)
    mt.stop()
