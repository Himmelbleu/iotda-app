import time


class Device:
    def __init__(self, device_id, device_name=None, device_desc=None):
        self.device_id = device_id
        self.device_name = device_name
        self.device_desc = device_desc


class Cover:
    def __init__(self, temp, accel_x, accel_y, accel_z, cover_status):
        self.temp = temp
        self.accel_x = accel_x
        self.accel_y = accel_y
        self.accel_z = accel_z
        self.cover_status = cover_status
        self.date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.name = 'Himmelbleu'
        self.sno = '42020xxx'

    # 通过定义 __iter__() 方法将其转换为元组或其他可迭代对象。
    def __iter__(self):
        yield self.temp
        yield self.accel_x
        yield self.accel_y
        yield self.accel_z
        yield self.cover_status
        yield self.date
        yield self.name
        yield self.sno


class Smoke:
    def __init__(self, smoke_value, beep_status):
        self.smoke_value = smoke_value
        self.beep_status = beep_status
        self.date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.name = 'Himmelbleu'
        self.sno = '42020xxx'

    # 通过定义 __iter__() 方法将其转换为元组或其他可迭代对象。
    def __iter__(self):
        yield self.smoke_value
        yield self.beep_status
        yield self.date
        yield self.name
        yield self.sno
