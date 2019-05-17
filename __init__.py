import time
from functools import wraps
from TimerMain import TimerMain
# 设置阻塞器内核
TimerMainSleeper = time.sleep


class Breakobj:
    _break = False


def run_timer(days=None, hours=None, minutes=None, seconds=None, loop=None, stop=Breakobj):

    _sleeper = TimerMain(TimerMainSleeper).sleep

    import TimeCallmethod
    TimeCallmethod.set_day = days
    TimeCallmethod.set_hour = hours
    TimeCallmethod.set_minute = minutes
    TimeCallmethod.set_second = seconds

    # method = TimeCallMethod()
    # run_count = method.run_count
    get_sleep = TimeCallmethod.GetSleepSec()
    get_time = get_sleep.get

    def _warpper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            _sleep_time = get_time()
            print(_sleep_time)
            while True:
                _sleeper(_sleep_time)
                func(*args, **kwargs)
                if stop._break or not loop:
                    break
                # 循环的时候使用的计数方法
                _sleep_time = get_time()
                print(time.time())
        return inner
    return _warpper


if __name__ == '__main__':
    @run_timer(minutes=24, seconds=2, loop=True)
    def test():
        print('test正在执行')
        import datetime
        print(datetime.datetime.now())

    test()
