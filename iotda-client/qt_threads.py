import time
import winsound

import apis
import pojos
import db_utils

from PyQt5 import QtCore
from PyQt5.QtCore import *


class ListDevicesThread(QtCore.QThread):
    signal = pyqtSignal(dict, name='list_devices')

    def run(self):
        while True:
            devices_list = apis.list_devices()
            self.signal.emit(devices_list)
            time.sleep(5)


class QueryDeviceThread(QtCore.QThread):
    signal = pyqtSignal(dict, name='query_device')
    device_id = ''

    def set_device_id(self, device_id):
        self.device_id = device_id

    def run(self):
        device = apis.query_device(self.device_id)
        self.signal.emit(device)


class UpdateDeviceThread(QtCore.QThread):
    signal = pyqtSignal(dict, name="update_device")
    device_data = None

    def set_data(self, data: pojos.Device):
        self.device_data = data

    def run(self):
        res = apis.update_device(self.device_data)
        self.signal.emit(res)


class GetSmokeDeviceShadowThread(QtCore.QThread):
    signal = pyqtSignal(dict, name="get_smoke_device_shadow")
    device_data = None

    def set_device(self, data: pojos.Device):
        self.device_data = data

    def run(self):
        while True:
            res = apis.list_device_shadow(self.device_data)
            smoke_value = res['shadow'][0]['reported']['properties']['Smoke_Value']
            beep_status = res['shadow'][0]['reported']['properties']['BeepStatus']

            if smoke_value >= 200:
                winsound.Beep(440, 1000)

            # 插入数据库
            db_utils.insert_smoke(pojos.Smoke(smoke_value, beep_status))

            self.signal.emit({
                's': smoke_value,
                'b': beep_status
            })

            time.sleep(8)


class GetCoverDeviceShadowThread(QtCore.QThread):
    signal = pyqtSignal(dict, name="get_cover_device_shadow")
    device_data = None

    def set_device(self, data: pojos.Device):
        self.device_data = data

    def run(self):
        while True:
            res = apis.list_device_shadow(self.device_data)
            temp = res['shadow'][1]['reported']['properties']['Temperature']
            x = res['shadow'][1]['reported']['properties']['Accel_x']
            y = res['shadow'][1]['reported']['properties']['Accel_y']
            z = res['shadow'][1]['reported']['properties']['Accel_z']
            c = res['shadow'][1]['reported']['properties']['Cover_Status']

            # 插入数据库
            db_utils.insert_cover(pojos.Cover(temp, x, y, z, c))

            if x >= 10:
                winsound.Beep(2000, 1000)

            self.signal.emit({
                'x': x, 'y': y, 'z': z, 'c': c, 'temp': temp
            })

            time.sleep(10)


class CoverCommandThread(QtCore.QThread):
    signal = pyqtSignal(dict, name="cover_command_thread")
    cover_status = ""

    def set_status(self, status):
        self.cover_status = status

    def run(self):
        res = apis.cover_command(self.cover_status)

        self.signal.emit(res)


class SmokeCommandThread(QtCore.QThread):
    signal = pyqtSignal(dict, name="smoke_command_thread")

    smoke_status = ""

    def set_status(self, status):
        self.smoke_status = status

    def run(self):
        res = apis.smoke_command(self.smoke_status)

        self.signal.emit(res)
