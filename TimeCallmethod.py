import datetime
import time

Hours = 24 * 60 * 60
Minutes = 60 * 60
Seconds = 60

set_day = None
set_hour = None
set_minute = None
set_second = 3

# after_time = True
__all__ = ['GetSleepSec']


class GetSleepSec:

    def __init__(self):
        self.run_count = 0  # 执行几次
        # self.cal_method = True    # 是否使用短间断循环

    def __cal_after_times(self):
        # 没100s执行一次
        _now = datetime.datetime.now()
        _t = _now
        if set_hour:
            _now += datetime.timedelta(hours=set_hour)
        if set_minute:
            _now += datetime.timedelta(minutes=set_minute)
        if set_second:
            _now += datetime.timedelta(seconds=set_second)
        return time.mktime(_now.timetuple()) - time.mktime(_t.timetuple())

    def __cal_first(self):
        # tm_min是不能被操作的   所以转换成时间戳
        _now = datetime.datetime.now()
        _t = _now.timetuple()
        _c = time.mktime(_t)

        if set_minute:
            if _t.tm_min < set_minute:
                # _c1 = 设定时间 - 当前时间  （获取剩下要执行的秒数）
                _c1 = set_minute - _t.tm_min

            if _t.tm_sec == set_minute:
                _c1 = 0

            if _t.tm_sec > set_minute:
                _c1 = 60 - _t.tm_min + set_minute
            print(_c1)
            _now += datetime.timedelta(minutes=_c1)

        if set_second:
            if _t.tm_sec < set_second:
                _c1 = set_second - _t.tm_sec

            if _t.tm_sec == set_second:
                _c1 = 0

            if _t.tm_sec > set_second:
                _c1 = 60 - _t.tm_sec + set_second
            print(_c1)
            _now += datetime.timedelta(seconds=_c1)

        if set_hour:
            if _t.tm_hour < set_hour:
                _c1 = set_hour - _t.tm_hour

            if _t.tm_hour == set_hour:
                _c1 = 0

            if _t.tm_hour > set_hour:
                _c1 = 24 - _t.tm_min + set_hour     #########此处c1未转换
            _now += datetime.timedelta(hours=_c1)

        _c2 = time.mktime(_now.timetuple()) - _c

        return _c2

    def __setup(self):
        _now = datetime.datetime.now()
        _t = time.mktime(_now.timetuple())
        return _now, _t

    def __cal_loop_sec(self):
        _now, _t = self.__setup()
        if set_second:
            _now += datetime.timedelta(minutes=1)

        _c = time.mktime(_now.timetuple()) - _t
        return _c

    def __cal_loop_min(self):
        _now, _t = self.__setup()
        if set_minute:
            _now += datetime.timedelta(hours=1)

        _c = time.mktime(_now.timetuple()) - _t
        return _c

    def __cal_loop_hours(self):
        _now, _t = self.__setup()
        if set_hour:
            _now += datetime.timedelta(days=1)

        # elif set_day:
        #     _now += datetime.timedelta(days=set_day)
        _c = time.mktime(_now.timetuple()) - _t
        return _c

    # def __cal_loop(self):
    #     # tm_min是不能被操作的   所以转换成时间戳
    #     _now = datetime.datetime.now()
    #     _t = time.mktime(_now.timetuple())
    #
    #     if set_second:
    #         _now += datetime.timedelta(minutes=1)
    #
    #     if set_minute:
    #         _now += datetime.timedelta(hours=1)
    #
    #     if set_hour:
    #         _now += datetime.timedelta(days=1)
    #
    #     _c = time.mktime(_now.timetuple()) - _t
    #     return _c

    def get(self):
        # 将传入的时间值带入到时间计算方法中进行计算
        m = None
        if self.run_count == 0:
            m = self.__cal_first()
            self.run_count += 1
        else:
            if set_hour or set_day:
                m = self.__cal_loop_hours()
            elif set_minute:
                m = self.__cal_loop_min()
            elif set_second:
                m = self.__cal_loop_sec()

        if m < 0:
            m = 0
        return m


if __name__ == '__main__':
    def test():
        i = 20
        while True:
            get_sleep = GetSleepSec()
            m = get_sleep.get()
            time.sleep(m)
            print('test正在执行')
            i -= 1
            if i == 0:
                break

    test()