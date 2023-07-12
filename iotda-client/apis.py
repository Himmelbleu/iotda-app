from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkiotda.v5 import *
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.auth.credentials import DerivedCredentials
from huaweicloudsdkcore.exceptions import exceptions

AK = ""
SK = ""
PROJECT_ID = ""
REGION_ID = "cn-north-4"
ENDPOINT = ""


def create_client():
    region = Region(REGION_ID, ENDPOINT)
    credentials = BasicCredentials(AK, SK, PROJECT_ID)
    credentials.with_derived_predicate(DerivedCredentials.get_default_derived_predicate())

    return IoTDAClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(region) \
        .build()


def list_devices() -> dict:
    try:
        client = create_client()
        request = ListDevicesRequest()
        response = client.list_devices(request)
        print("[获取的设备列表] >>> %s" % response)
        return response.to_dict()
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def query_device(device_id) -> dict:
    try:
        client = create_client()
        request = ShowDeviceRequest()
        request.device_id = device_id
        response = client.show_device(request)
        print("[查询的设备列表] >>> %s" % response)
        return response.to_dict()
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


class Device:
    def __init__(self, device_id, device_name=None, device_desc=None):
        self.device_id = device_id
        self.device_name = device_name
        self.device_desc = device_desc


def update_device(data: Device) -> dict:
    try:
        client = create_client()
        request = UpdateDeviceRequest()
        request.device_id = data.device_id
        request.body = UpdateDevice(
            device_name=data.device_name,
            description=data.device_desc or "",
        )
        response = client.update_device(request)
        return response.to_dict()
    except exceptions.ClientRequestException as e:
        return e.status_code


def list_device_shadow(data: Device) -> dict:
    try:
        client = create_client()
        request = ShowDeviceShadowRequest()
        request.device_id = data.device_id
        response = client.show_device_shadow(request)
        print("[设备影子数据] >>> %s" % response)
        return response.to_dict()
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def cover_command(cover_status):
    try:
        client = create_client()
        request = CreateCommandRequest()
        request.device_id = ""
        request.body = DeviceCommandRequest(
            paras=f"{{\"Status\":\"{cover_status}\"}}",
            command_name="Open_Alert",
            service_id="Manhole_Cover"
        )
        response = client.create_command(request)
        return response.to_dict()
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def smoke_command(beep_status):
    try:
        client = create_client()
        request = CreateCommandRequest()
        request.device_id = ""
        request.body = DeviceCommandRequest(
            paras=f"{{\"Beep\":\"{beep_status}\"}}",
            command_name="Smoke_Control_Beep",
            service_id="Smoke"
        )
        response = client.create_command(request)
        return response.to_dict()
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
