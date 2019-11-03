import pytest
import responses
import json
from pytmg import TMG
from pytmg import TMGResult


def test_tmg_init():
    tmg = TMG.TMG()
    assert tmg is not None


class TestPrivateSearchMethod:
    @responses.activate
    def test_tmg_private_search_for_n9k_93180yc_ex(self):
        resp_json = {
            "totalCount": 1,
            "itemPerPage": None,
            "page": None,
            "networkDevices": [
                {
                    "productFamily": "N9300",
                    "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/datasheet-c78-742282.html",
                    "networkAndTransceiverCompatibility": [
                        {"productId": "N9K-C93180YC-EX", "transceivers": []}
                    ],
                }
            ],
        }
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg._search(search_input=["N9K-C93180YC-EX"])
        assert res is not None
        assert (
            res["networkDevices"][0]["networkAndTransceiverCompatibility"][0][
                "productId"
            ]
            == "N9K-C93180YC-EX"
        )

    @responses.activate
    def test_tmg_private_search_for_n9k_9372px(self):
        resp_json = {
            "totalCount": 1,
            "itemPerPage": None,
            "page": None,
            "networkDevices": [
                {
                    "productFamily": "N9300",
                    "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/datasheet-c78-742282.html",
                    "networkAndTransceiverCompatibility": [
                        {"productId": "N9K-C9372PX", "transceivers": []},
                        {"productId": "N9K-C9372PX-E", "transceivers": []},
                    ],
                }
            ],
        }
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg._search(search_input=["N9K-C9372PX"])
        assert res is not None
        assert (
            res["networkDevices"][0]["networkAndTransceiverCompatibility"][0][
                "productId"
            ]
            == "N9K-C9372PX"
        )
        assert (
            res["networkDevices"][0]["networkAndTransceiverCompatibility"][1][
                "productId"
            ]
            == "N9K-C9372PX-E"
        )

    @responses.activate
    def test_tmg_private_search_for_ws_c3750_24ps(self):
        resp_json = {
            "totalCount": 1,
            "itemPerPage": None,
            "page": None,
            "networkDevices": [
                {
                    "productFamily": "C3750",
                    "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/support/switches/catalyst-3750-metro-series-switches/products-release-notes-list.html",
                    "networkAndTransceiverCompatibility": [
                        {"productId": "WS-C3750-24PS", "transceivers": []}
                    ],
                }
            ],
        }
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg._search(search_input=["WS-C3750-24PS"])
        assert res is not None
        assert (
            res["networkDevices"][0]["networkAndTransceiverCompatibility"][0][
                "productId"
            ]
            == "WS-C3750-24PS"
        )

    @responses.activate
    def test_tmg_private_search_for_all_3750s(self):
        resp_json = {
            "totalCount": 2,
            "itemPerPage": None,
            "page": None,
            "networkDevices": [
                {
                    "productFamily": "C3750",
                    "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/support/switches/catalyst-3750-metro-series-switches/products-release-notes-list.html",
                    "networkAndTransceiverCompatibility": [
                        {"productId": "WS-C3750G-16TD", "transceivers": []},
                        {"productId": "WS-C3750-24PS", "transceivers": []},
                        {"productId": "WS-C3750-24TS", "transceivers": []},
                        {"productId": "WS-C3750-48PS", "transceivers": []},
                        {"productId": "WS-C3750-48TS", "transceivers": []},
                        {"productId": "WS-C3750G-12S", "transceivers": []},
                        {"productId": "WS-C3750G-24PS", "transceivers": []},
                        {"productId": "WS-C3750G-24TS", "transceivers": []},
                        {"productId": "WS-C3750G-24TS-E1U", "transceivers": []},
                        {"productId": "WS-C3750G-24TS-S1U", "transceivers": []},
                        {"productId": "WS-C3750G-48PS", "transceivers": []},
                        {"productId": "WS-C3750G-48TS", "transceivers": []},
                        {"productId": "WS-C3750-24FS-S", "transceivers": []},
                        {"productId": "WS-C3750V2-24PS", "transceivers": []},
                        {"productId": "WS-C3750V2-24TS", "transceivers": []},
                        {"productId": "WS-C3750V2-48PS", "transceivers": []},
                        {"productId": "WS-C3750V2-48TS", "transceivers": []},
                        {"productId": "WS-C3750V2-24FS-S", "transceivers": []},
                        {"productId": "WS-C3750E-24TD", "transceivers": []},
                        {"productId": "WS-C3750E-24PD", "transceivers": []},
                        {"productId": "WS-C3750E-48TD", "transceivers": []},
                        {"productId": "WS-C3750E-48PD", "transceivers": []},
                        {"productId": "WS-C3750E-48PDF", "transceivers": []},
                        {"productId": "WS-C3750X-12S", "transceivers": []},
                        {"productId": "WS-C3750X-24S", "transceivers": []},
                        {"productId": "WS-C3750-24WFS", "transceivers": []},
                        {"productId": "WS-C3750V2-24FS", "transceivers": []},
                    ],
                },
                {
                    "productFamily": "C3750X",
                    "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/support/switches/catalyst-3750-x-series-switches/tsd-products-support-series-home.html",
                    "networkAndTransceiverCompatibility": [
                        {"productId": "WS-C3750X-24T", "transceivers": []},
                        {"productId": "WS-C3750X-48T", "transceivers": []},
                        {"productId": "WS-C3750X-24P", "transceivers": []},
                        {"productId": "WS-C3750X-48P", "transceivers": []},
                        {"productId": "WS-C3750X-48PF", "transceivers": []},
                        {"productId": "WS-C3750X-12S", "transceivers": []},
                        {"productId": "WS-C3750X-24S", "transceivers": []},
                    ],
                },
            ],
        }
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg._search(search_input=["WS-C3750"])
        assert res is not None
        product_list = [
            dev["productId"]
            for dev in res["networkDevices"][0]["networkAndTransceiverCompatibility"]
        ]
        product_list += [
            dev["productId"]
            for dev in res["networkDevices"][1]["networkAndTransceiverCompatibility"]
        ]
        assert "WS-C3750G-16TD" in product_list
        assert "WS-C3750-24PS" in product_list
        assert "WS-C3750-24TS" in product_list
        assert "WS-C3750-48PS" in product_list
        assert "WS-C3750-48TS" in product_list
        assert "WS-C3750G-12S" in product_list
        assert "WS-C3750G-24PS" in product_list
        assert "WS-C3750G-24TS" in product_list
        assert "WS-C3750G-24TS-E1U" in product_list
        assert "WS-C3750G-24TS-S1U" in product_list
        assert "WS-C3750G-48PS" in product_list
        assert "WS-C3750G-48TS" in product_list
        assert "WS-C3750-24FS-S" in product_list
        assert "WS-C3750V2-24PS" in product_list
        assert "WS-C3750V2-24TS" in product_list
        assert "WS-C3750V2-48PS" in product_list
        assert "WS-C3750V2-48TS" in product_list
        assert "WS-C3750V2-24FS-S" in product_list
        assert "WS-C3750E-24TD" in product_list
        assert "WS-C3750E-24PD" in product_list
        assert "WS-C3750E-48TD" in product_list
        assert "WS-C3750E-48PD" in product_list
        assert "WS-C3750E-48PDF" in product_list
        assert "WS-C3750X-12S" in product_list
        assert "WS-C3750X-24S" in product_list
        assert "WS-C3750-24WFS" in product_list
        assert "WS-C3750V2-24FS" in product_list
        assert "WS-C3750X-24T" in product_list
        assert "WS-C3750X-48T" in product_list
        assert "WS-C3750X-24P" in product_list
        assert "WS-C3750X-48P" in product_list
        assert "WS-C3750X-48PF" in product_list
        assert "WS-C3750X-12S" in product_list
        assert "WS-C3750X-24S" in product_list


class TestDeviceSearching:
    @responses.activate
    def test_tmg_search_for_n9k_93180yc_ex(self):
        resp_json = {
            "totalCount": 1,
            "itemPerPage": None,
            "page": None,
            "networkDevices": [
                {
                    "productFamily": "N9300",
                    "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/datasheet-c78-742282.html",
                    "networkAndTransceiverCompatibility": [
                        {"productId": "N9K-C93180YC-EX", "transceivers": []}
                    ],
                }
            ],
        }
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg.search_device("N9K-C93180YC-EX")
        assert res is not None
        assert res.network_devices[0].product_id == "N9K-C93180YC-EX"

    @responses.activate
    def test_tmg_search_for_n9k_9372px(self):
        resp_json = {
            "totalCount": 1,
            "itemPerPage": None,
            "page": None,
            "networkDevices": [
                {
                    "productFamily": "N9300",
                    "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/datasheet-c78-742282.html",
                    "networkAndTransceiverCompatibility": [
                        {"productId": "N9K-C9372PX", "transceivers": []},
                        {"productId": "N9K-C9372PX-E", "transceivers": []},
                    ],
                }
            ],
        }
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg.search_device("N9K-C9372PX")
        assert res is not None
        assert res.network_devices[0].product_id == "N9K-C9372PX"

    @responses.activate
    def test_tmg_search_for_ws_c3750_24ps(self):
        resp_json = {
            "totalCount": 1,
            "itemPerPage": None,
            "page": None,
            "networkDevices": [
                {
                    "productFamily": "C3750",
                    "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/support/switches/catalyst-3750-metro-series-switches/products-release-notes-list.html",
                    "networkAndTransceiverCompatibility": [
                        {"productId": "WS-C3750-24PS", "transceivers": []}
                    ],
                }
            ],
        }
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg.search_device("WS-C3750-24PS")
        assert res is not None
        assert res.network_devices[0].product_id == "WS-C3750-24PS"

    @responses.activate
    def test_tmg_search_all_3750s(self):
        resp_json = {
            "totalCount": 2,
            "itemPerPage": None,
            "page": None,
            "networkDevices": [
                {
                    "productFamily": "C3750",
                    "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/support/switches/catalyst-3750-metro-series-switches/products-release-notes-list.html",
                    "networkAndTransceiverCompatibility": [
                        {"productId": "WS-C3750G-16TD", "transceivers": []},
                        {"productId": "WS-C3750-24PS", "transceivers": []},
                        {"productId": "WS-C3750-24TS", "transceivers": []},
                        {"productId": "WS-C3750-48PS", "transceivers": []},
                        {"productId": "WS-C3750-48TS", "transceivers": []},
                        {"productId": "WS-C3750G-12S", "transceivers": []},
                        {"productId": "WS-C3750G-24PS", "transceivers": []},
                        {"productId": "WS-C3750G-24TS", "transceivers": []},
                        {"productId": "WS-C3750G-24TS-E1U", "transceivers": []},
                        {"productId": "WS-C3750G-24TS-S1U", "transceivers": []},
                        {"productId": "WS-C3750G-48PS", "transceivers": []},
                        {"productId": "WS-C3750G-48TS", "transceivers": []},
                        {"productId": "WS-C3750-24FS-S", "transceivers": []},
                        {"productId": "WS-C3750V2-24PS", "transceivers": []},
                        {"productId": "WS-C3750V2-24TS", "transceivers": []},
                        {"productId": "WS-C3750V2-48PS", "transceivers": []},
                        {"productId": "WS-C3750V2-48TS", "transceivers": []},
                        {"productId": "WS-C3750V2-24FS-S", "transceivers": []},
                        {"productId": "WS-C3750E-24TD", "transceivers": []},
                        {"productId": "WS-C3750E-24PD", "transceivers": []},
                        {"productId": "WS-C3750E-48TD", "transceivers": []},
                        {"productId": "WS-C3750E-48PD", "transceivers": []},
                        {"productId": "WS-C3750E-48PDF", "transceivers": []},
                        {"productId": "WS-C3750X-12S", "transceivers": []},
                        {"productId": "WS-C3750X-24S", "transceivers": []},
                        {"productId": "WS-C3750-24WFS", "transceivers": []},
                        {"productId": "WS-C3750V2-24FS", "transceivers": []},
                    ],
                },
                {
                    "productFamily": "C3750X",
                    "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/support/switches/catalyst-3750-x-series-switches/tsd-products-support-series-home.html",
                    "networkAndTransceiverCompatibility": [
                        {"productId": "WS-C3750X-24T", "transceivers": []},
                        {"productId": "WS-C3750X-48T", "transceivers": []},
                        {"productId": "WS-C3750X-24P", "transceivers": []},
                        {"productId": "WS-C3750X-48P", "transceivers": []},
                        {"productId": "WS-C3750X-48PF", "transceivers": []},
                        {"productId": "WS-C3750X-12S", "transceivers": []},
                        {"productId": "WS-C3750X-24S", "transceivers": []},
                    ],
                },
            ],
        }
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg.search_device("WS-C3750")
        assert res is not None
        assert len(res.network_devices) > 1
        # Verify expected products are in returned list
        product_list = [dev.product_id for dev in res.network_devices]
        assert "WS-C3750G-16TD" in product_list
        assert "WS-C3750-24PS" in product_list
        assert "WS-C3750-24TS" in product_list
        assert "WS-C3750-48PS" in product_list
        assert "WS-C3750-48TS" in product_list
        assert "WS-C3750G-12S" in product_list
        assert "WS-C3750G-24PS" in product_list
        assert "WS-C3750G-24TS" in product_list
        assert "WS-C3750G-24TS-E1U" in product_list
        assert "WS-C3750G-24TS-S1U" in product_list
        assert "WS-C3750G-48PS" in product_list
        assert "WS-C3750G-48TS" in product_list
        assert "WS-C3750-24FS-S" in product_list
        assert "WS-C3750V2-24PS" in product_list
        assert "WS-C3750V2-24TS" in product_list
        assert "WS-C3750V2-48PS" in product_list
        assert "WS-C3750V2-48TS" in product_list
        assert "WS-C3750V2-24FS-S" in product_list
        assert "WS-C3750E-24TD" in product_list
        assert "WS-C3750E-24PD" in product_list
        assert "WS-C3750E-48TD" in product_list
        assert "WS-C3750E-48PD" in product_list
        assert "WS-C3750E-48PDF" in product_list
        assert "WS-C3750X-12S" in product_list
        assert "WS-C3750X-24S" in product_list
        assert "WS-C3750-24WFS" in product_list
        assert "WS-C3750V2-24FS" in product_list
        assert "WS-C3750X-24T" in product_list
        assert "WS-C3750X-48T" in product_list
        assert "WS-C3750X-24P" in product_list
        assert "WS-C3750X-48P" in product_list
        assert "WS-C3750X-48PF" in product_list
        assert "WS-C3750X-12S" in product_list
        assert "WS-C3750X-24S" in product_list

    @responses.activate
    def test_tmg_search_multiple_devices(self):
        def tmg_callback(request):
            payload = json.loads(request.body)
            if payload["searchInput"][0] == "N9K-C93180YC-FX":
                resp_json = {
                    "totalCount": 1,
                    "itemPerPage": None,
                    "page": None,
                    "networkDevices": [
                        {
                            "productFamily": "N9300",
                            "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/datasheet-c78-742282.html",
                            "networkAndTransceiverCompatibility": [
                                {"productId": "N9K-C93180YC-FX", "transceivers": []}
                            ],
                        }
                    ],
                }
                return (
                    200,
                    {"content-type": "application/json"},
                    json.dumps(resp_json),
                )
            elif payload["searchInput"][0] == "C9300-48S":
                resp_json = {
                    "totalCount": 1,
                    "itemPerPage": None,
                    "page": None,
                    "networkDevices": [
                        {
                            "productFamily": "C9300",
                            "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/products/switches/catalyst-9300-series-switches/index.html",
                            "networkAndTransceiverCompatibility": [
                                {"productId": "C9300-48S", "transceivers": []}
                            ],
                        }
                    ],
                }
                return (
                    200,
                    {"content-type": "application/json"},
                    json.dumps(resp_json),
                )
            elif payload["searchInput"][0] == "2951":
                resp_json = {
                    "totalCount": 1,
                    "itemPerPage": None,
                    "page": None,
                    "networkDevices": [
                        {
                            "productFamily": "ISR2900",
                            "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/support/routers/2900-series-integrated-services-routers-isr/tsd-products-support-series-home.html",
                            "networkAndTransceiverCompatibility": [
                                {"productId": "2951", "transceivers": []}
                            ],
                        }
                    ],
                }
                return (
                    200,
                    {"content-type": "application/json"},
                    json.dumps(resp_json),
                )
            else:
                return (503, {}, None)

        responses.add_callback(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            callback=tmg_callback,
            content_type="application/json",
        )

        device_list = [
            "N9K-C93180YC-FX",  # Nexus 93180YC-FX
            "C9300-48S",  # Catalyst 9300-48S
            "2951",  # ISR 2951
        ]
        tmg = TMG.TMG()
        res_list = tmg.search_devices(device_list)
        assert res_list is not None
        assert len(res_list) == 3
        for result in res_list:
            for result_device in result.network_devices:
                assert result_device.product_id in device_list
