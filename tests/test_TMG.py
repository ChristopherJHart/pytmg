import pytest
from pytmg import TMG


def test_tmg_init():
    tmg = TMG.TMG()
    assert tmg is not None


class TestDeviceSearching:
    # def test_tmg_search_for_n9k_93180yc_ex(self):
    #     tmg = TMG.TMG()
    #     res = tmg.search_device("N9K-C93180YC-EX")
    #     assert res is not None
    #     assert res.network_devices[0].product_id == "N9K-C93180YC-EX"

    # def test_tmg_search_for_n9k_9372px(self):
    #     tmg = TMG.TMG()
    #     res = tmg.search_device("N9K-C9372PX")
    #     assert res is not None
    #     assert res.network_devices[0].product_id == "N9K-C9372PX"

    # def test_tmg_search_for_ws_c3750_24ps(self):
    #     tmg = TMG.TMG()
    #     res = tmg.search_device("WS-C3750-24PS")
    #     assert res is not None
    #     assert res.network_devices[0].product_id == "WS-C3750-24PS"

    # def test_tmg_search_all_3750s(self):
    #     tmg = TMG.TMG()
    #     res = tmg.search_device("WS-C3750")
    #     assert res is not None
    #     assert len(res.network_devices) > 1
    #     # Verify expected products are in returned list
    #     product_list = [dev.product_id for dev in res.network_devices]
    #     assert "WS-C3750G-16TD" in product_list
    #     assert "WS-C3750-24PS" in product_list
    #     assert "WS-C3750-24TS" in product_list
    #     assert "WS-C3750-48PS" in product_list
    #     assert "WS-C3750-48TS" in product_list
    #     assert "WS-C3750G-12S" in product_list
    #     assert "WS-C3750G-24PS" in product_list
    #     assert "WS-C3750G-24TS" in product_list
    #     assert "WS-C3750G-24TS-E1U" in product_list
    #     assert "WS-C3750G-24TS-S1U" in product_list
    #     assert "WS-C3750G-48PS" in product_list
    #     assert "WS-C3750G-48TS" in product_list
    #     assert "WS-C3750-24FS-S" in product_list
    #     assert "WS-C3750V2-24PS" in product_list
    #     assert "WS-C3750V2-24TS" in product_list
    #     assert "WS-C3750V2-48PS" in product_list
    #     assert "WS-C3750V2-48TS" in product_list
    #     assert "WS-C3750V2-24FS-S" in product_list
    #     assert "WS-C3750E-24TD" in product_list
    #     assert "WS-C3750E-24PD" in product_list
    #     assert "WS-C3750E-48TD" in product_list
    #     assert "WS-C3750E-48PD" in product_list
    #     assert "WS-C3750E-48PDF" in product_list
    #     assert "WS-C3750X-12S" in product_list
    #     assert "WS-C3750X-24S" in product_list
    #     assert "WS-C3750-24WFS" in product_list
    #     assert "WS-C3750V2-24FS" in product_list
    #     assert "WS-C3750X-24T" in product_list
    #     assert "WS-C3750X-48T" in product_list
    #     assert "WS-C3750X-24P" in product_list
    #     assert "WS-C3750X-48P" in product_list
    #     assert "WS-C3750X-48PF" in product_list
    #     assert "WS-C3750X-12S" in product_list
    #     assert "WS-C3750X-24S" in product_list

    # def test_tmg_search_multiple_devices(self):
    #     device_list = [
    #         "N9K-C93180YC-FX",  # Nexus 93180YC-FX
    #         "C9300-48S",  # Catalyst 9300-48S
    #         "2951",  # ISR 2951
    #     ]
    #     tmg = TMG.TMG()
    #     res_list = tmg.search_devices(device_list)
    #     assert res_list is not None
    #     assert len(res_list) == 3
    #     for result in res_list:
    #         for result_device in result.network_devices:
    #             assert result_device.product_id in device_list
