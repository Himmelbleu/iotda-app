import json
import sys

from qt_threads import ListDevicesThread, QueryDeviceThread, UpdateDeviceThread, GetSmokeDeviceShadowThread, \
    GetCoverDeviceShadowThread, SmokeCommandThread, CoverCommandThread
from apis import Device

from Ui_Designer import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox


def waring_dialog(title, msg, on_ok=None, on_cancel=None):
    box = QMessageBox()
    box.setIcon(QMessageBox.Warning)
    box.setText(msg)
    box.setWindowTitle(title)
    box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    if box.exec() == QMessageBox.Ok:
        on_ok and on_ok()
    else:
        on_cancel and on_cancel()


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.smoke_thread = None
        self.cover_thread = None
        self.query_device_thread = None
        self.update_device_thread = None
        self.setupUi(self)

        # 获取设备列表
        self.list_shadow_thread = ListDevicesThread()
        self.list_shadow_thread.signal.connect(self.after_list_devices)
        self.list_shadow_thread.start()

        # 获取井盖影子数据
        self.list_cover_shadow_thread = GetCoverDeviceShadowThread()
        self.list_cover_shadow_thread.set_device(Device(device_id=""))
        self.list_cover_shadow_thread.signal.connect(self.after_get_cover_shadow)
        self.list_cover_shadow_thread.start()

        # 获取烟感影子数据
        self.list_smoke_shadow_thread = GetSmokeDeviceShadowThread()
        self.list_smoke_shadow_thread.set_device(Device(device_id=""))
        self.list_smoke_shadow_thread.signal.connect(self.after_get_smoke_shadow)
        self.list_smoke_shadow_thread.start()

        # 绑定按钮
        self.query_device_button.clicked.connect(self.query_device)
        self.update_device_button.clicked.connect(self.update_device)

        self.cover_command_button.clicked.connect(self.put_cover_command)
        self.smoke_command_button.clicked.connect(self.put_smoke_command)

    def setTableItem(self, row, col, data):
        item = QTableWidgetItem(data)
        self.tableWidget.setItem(row, col, item)

    def after_list_devices(self, data):
        row = 0
        self.tableWidget.setRowCount(data['page']['count'])
        for item in data['devices']:
            self.setTableItem(row, 0, item['device_id'])
            self.setTableItem(row, 1, item['device_name'])
            self.setTableItem(row, 2, item['product_name'])
            self.setTableItem(row, 3, item['status'])
            self.setTableItem(row, 4, item['description'])
            row += 1

    def after_query_device(self, data):
        self.query_device_text.setText(json.dumps(data, indent=2))

    def query_device(self):
        self.query_device_thread = QueryDeviceThread()
        self.query_device_thread.set_device_id(self.input_query_device_id.text())
        self.query_device_thread.signal.connect(self.after_query_device)
        self.query_device_thread.start()

    def update_device(self):
        self.update_device_thread = UpdateDeviceThread()
        device_id = self.update_device_id_input.text()
        device_name = self.update_device_name_input.text()
        device_desc = self.update_device_desc_input.text()
        self.update_device_thread.set_data(Device(device_id, device_name, device_desc))
        self.update_device_thread.signal.connect(self.after_update_device)
        self.update_device_thread.start()

    def after_update_device(self, data):
        waring_dialog('操作成功', '更新设备成功！！！')

    # 获取井盖之后更新界面并插入数据库
    def after_get_cover_shadow(self, data):
        self.temp_lcd.display(data['temp'])
        self.accel_x_lcd.display(data['x'])
        self.accel_y_lcd.display(data['y'])
        self.accel_z_lcd.display(data['z'])
        self.cover_status_text.setText(data['c'])
        if data['x'] > 10:
            self.cover_state_text.setText("井盖倾斜")
            self.cover_state_text.setStyleSheet("color: red;")
        else:
            self.cover_state_text.setText("井盖正常")
            self.cover_state_text.setStyleSheet("color: black;")

    def after_get_smoke_shadow(self, data):
        self.smoke_value_lcd.display(data['s'])
        self.beep_status_text.setText(data['b'])

        if data['s'] > 200:
            self.smoke_state_text.setText("烟雾超标")
            self.smoke_state_text.setStyleSheet("color: red;")

        else:
            self.smoke_state_text.setText("烟雾正常")
            self.smoke_state_text.setStyleSheet("color: black;")

    # 下发井盖指令
    def put_cover_command(self):
        self.cover_thread = CoverCommandThread()
        self.cover_command_input.setReadOnly(True)
        self.cover_command_button.setEnabled(False)
        self.cover_thread.set_status(self.cover_command_input.text())
        self.cover_thread.signal.connect(self.after_put_cover_command)
        self.cover_thread.start()

    def after_put_cover_command(self, data):
        if data['response'] is None:
            waring_dialog('井盖指令失败', '下发井盖指令失败！！！')

        self.cover_command_input.setReadOnly(False)
        self.cover_command_button.setEnabled(True)

    # 下发烟感指令
    def put_smoke_command(self):
        self.smoke_thread = SmokeCommandThread()
        self.smoke_command_input.setReadOnly(True)
        self.smoke_command_button.setEnabled(False)
        self.smoke_thread.set_status(self.smoke_command_input.text())
        self.smoke_thread.signal.connect(self.after_put_smoke_command)
        self.smoke_thread.start()

    def after_put_smoke_command(self, data):
        if data['response'] is None:
            waring_dialog('烟感指令失败', '下发烟感指令失败！！！')

        self.smoke_command_input.setReadOnly(False)
        self.smoke_command_button.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()
