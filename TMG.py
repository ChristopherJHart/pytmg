import json
import requests


class TMG():
    def __init__(self):
        self.search_url = "https://tmgmatrix.cisco.com/public/api/networkdevice/search"

    def _search(self, cable_type=[], data_rate=[], form_factor=[],
                reach=[], search_input=[], os_type=[],
                transceiver_product_family=[],
                transceiver_product_id=[],
                network_device_product_family=[],
                network_device_product_id=[]):
        body  = {
            "cableType": cable_type,
            "dataRate": data_rate,
            "formFactor": form_factor,
            "reach": reach,
            "searchInput": search_input,
            "osType": os_type,
            "transceiverProductFamily": transceiver_product_family,
            "transceiverProductID": transceiver_product_id,
            "networkDeviceProductFamily": network_device_product_family,
            "networkDeviceProductID": network_device_product_id
        }
        headers = {
            "content-type": "application/json"
        }

        res = requests.post(self.search_url,
                            json=body,
                            headers=headers)
        res.raise_for_status()
        return res.json()

    def search_device(self, search_device):
        return self._search(search_input=[search_device])

    def search_devices(self, search_devices):
        return self._search(search_input=search_devices)

