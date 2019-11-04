import pytest
import responses
import json
from pytmg import TMG
from pytmg import TMGResult


def test_tmg_init():
    tmg = TMG.TMG()
    assert tmg is not None


class TestPrivateSearchMethodSimple:
    @responses.activate
    def test_tmg_private_search_for_n9k_93180yc_ex(self):
        resp_json = {
            "totalCount": "1",
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
            "totalCount": "1",
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
            "totalCount": "1",
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
            "totalCount": "2",
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


class TestDeviceSearchingSimple:
    @responses.activate
    def test_tmg_search_for_n9k_93180yc_ex(self):
        resp_json = {
            "totalCount": "1",
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
            "totalCount": "1",
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
            "totalCount": "1",
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
            "totalCount": "2",
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
                    "totalCount": "1",
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
                    "totalCount": "1",
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
                    "totalCount": "1",
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


class TestPrivateSearchMethodAdvanced:
    @responses.activate
    def test_tmg_private_search_advanced_ios_xe_fet_10g(self):
        resp_json = {
            "totalCount": "2",
            "itemPerPage": None,
            "page": None,
            "networkDevices": [
                {
                    "productFamily": "C9300",
                    "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/products/switches/catalyst-9300-series-switches/index.html",
                    "networkAndTransceiverCompatibility": [
                        {
                            "productId": "C9300-NM-8X",
                            "transceivers": [
                                {
                                    "tmgId": "18751",
                                    "productFamilyId": "12",
                                    "productFamily": "SFP10G",
                                    "productModelId": "99",
                                    "productId": "FET-10G",
                                    "version": " ",
                                    "versionId": None,
                                    "description": None,
                                    "formFactor": "SFP+",
                                    "reach": "100m",
                                    "temperatureRange": "0 to 70C",
                                    "digitalDiagnostic": "N",
                                    "cableType": "Duplex Fiber",
                                    "media": "MMF",
                                    "connectorType": "LC",
                                    "transmissionStandard": " ",
                                    "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.pdf",
                                    "endOfSale": " ",
                                    "dataRate": "10 Gbps",
                                    "transceiverNotes": None,
                                    "noteCount": "1",
                                    "state": None,
                                    "stateMessage": None,
                                    "updatedOn": None,
                                    "updatedBy": None,
                                    "transceiverBusinessUnit": "TMG",
                                    "networkModelId": "670",
                                    "breakoutMode": " ",
                                    "osType": "IOS XE",
                                    "domSupport": " ",
                                    "softReleaseMinVer": "IOS XE 16.5.1",
                                    "networkDeviceNotes": None,
                                    "releaseId": "657",
                                    "softReleaseDOM": "—",
                                    "type": "Optic",
                                }
                            ],
                        }
                    ],
                },
                {
                    "productFamily": "C9300L",
                    "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9500-series-switches/data_sheet-c78-738978.html",
                    "networkAndTransceiverCompatibility": [
                        {
                            "productId": "C9300L-24T-4X",
                            "transceivers": [
                                {
                                    "tmgId": "39519",
                                    "productFamilyId": "12",
                                    "productFamily": "SFP10G",
                                    "productModelId": "99",
                                    "productId": "FET-10G",
                                    "version": " ",
                                    "versionId": None,
                                    "description": None,
                                    "formFactor": "SFP+",
                                    "reach": "100m",
                                    "temperatureRange": "0 to 70C",
                                    "digitalDiagnostic": "N",
                                    "cableType": "Duplex Fiber",
                                    "media": "MMF",
                                    "connectorType": "LC",
                                    "transmissionStandard": " ",
                                    "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.pdf",
                                    "endOfSale": " ",
                                    "dataRate": "10 Gbps",
                                    "transceiverNotes": None,
                                    "noteCount": "0",
                                    "state": None,
                                    "stateMessage": None,
                                    "updatedOn": None,
                                    "updatedBy": None,
                                    "transceiverBusinessUnit": "TMG",
                                    "networkModelId": "1827",
                                    "breakoutMode": " ",
                                    "osType": "IOS XE",
                                    "domSupport": " ",
                                    "softReleaseMinVer": "IOS XE 16.12.1",
                                    "networkDeviceNotes": None,
                                    "releaseId": "1641",
                                    "softReleaseDOM": "—",
                                    "type": "Optic",
                                }
                            ],
                        },
                        {
                            "productId": "C9300L-48T-4X",
                            "transceivers": [
                                {
                                    "tmgId": "39573",
                                    "productFamilyId": "12",
                                    "productFamily": "SFP10G",
                                    "productModelId": "99",
                                    "productId": "FET-10G",
                                    "version": " ",
                                    "versionId": None,
                                    "description": None,
                                    "formFactor": "SFP+",
                                    "reach": "100m",
                                    "temperatureRange": "0 to 70C",
                                    "digitalDiagnostic": "N",
                                    "cableType": "Duplex Fiber",
                                    "media": "MMF",
                                    "connectorType": "LC",
                                    "transmissionStandard": " ",
                                    "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.pdf",
                                    "endOfSale": " ",
                                    "dataRate": "10 Gbps",
                                    "transceiverNotes": None,
                                    "noteCount": "0",
                                    "state": None,
                                    "stateMessage": None,
                                    "updatedOn": None,
                                    "updatedBy": None,
                                    "transceiverBusinessUnit": "TMG",
                                    "networkModelId": "1828",
                                    "breakoutMode": " ",
                                    "osType": "IOS XE",
                                    "domSupport": " ",
                                    "softReleaseMinVer": "IOS XE 16.12.1",
                                    "networkDeviceNotes": None,
                                    "releaseId": "1641",
                                    "softReleaseDOM": "—",
                                    "type": "Optic",
                                }
                            ],
                        },
                        {
                            "productId": "C9300L-24P-4X",
                            "transceivers": [
                                {
                                    "tmgId": "39627",
                                    "productFamilyId": "12",
                                    "productFamily": "SFP10G",
                                    "productModelId": "99",
                                    "productId": "FET-10G",
                                    "version": " ",
                                    "versionId": None,
                                    "description": None,
                                    "formFactor": "SFP+",
                                    "reach": "100m",
                                    "temperatureRange": "0 to 70C",
                                    "digitalDiagnostic": "N",
                                    "cableType": "Duplex Fiber",
                                    "media": "MMF",
                                    "connectorType": "LC",
                                    "transmissionStandard": " ",
                                    "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.pdf",
                                    "endOfSale": " ",
                                    "dataRate": "10 Gbps",
                                    "transceiverNotes": None,
                                    "noteCount": "0",
                                    "state": None,
                                    "stateMessage": None,
                                    "updatedOn": None,
                                    "updatedBy": None,
                                    "transceiverBusinessUnit": "TMG",
                                    "networkModelId": "1829",
                                    "breakoutMode": " ",
                                    "osType": "IOS XE",
                                    "domSupport": " ",
                                    "softReleaseMinVer": "IOS XE 16.12.1",
                                    "networkDeviceNotes": None,
                                    "releaseId": "1641",
                                    "softReleaseDOM": "—",
                                    "type": "Optic",
                                }
                            ],
                        },
                        {
                            "productId": "C9300L-48P-4X",
                            "transceivers": [
                                {
                                    "tmgId": "42136",
                                    "productFamilyId": "12",
                                    "productFamily": "SFP10G",
                                    "productModelId": "99",
                                    "productId": "FET-10G",
                                    "version": " ",
                                    "versionId": None,
                                    "description": None,
                                    "formFactor": "SFP+",
                                    "reach": "100m",
                                    "temperatureRange": "0 to 70C",
                                    "digitalDiagnostic": "N",
                                    "cableType": "Duplex Fiber",
                                    "media": "MMF",
                                    "connectorType": "LC",
                                    "transmissionStandard": " ",
                                    "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.pdf",
                                    "endOfSale": " ",
                                    "dataRate": "10 Gbps",
                                    "transceiverNotes": None,
                                    "noteCount": "0",
                                    "state": None,
                                    "stateMessage": None,
                                    "updatedOn": None,
                                    "updatedBy": None,
                                    "transceiverBusinessUnit": "TMG",
                                    "networkModelId": "1830",
                                    "breakoutMode": " ",
                                    "osType": "IOS XE",
                                    "domSupport": " ",
                                    "softReleaseMinVer": "IOS XE 16.12.1",
                                    "networkDeviceNotes": None,
                                    "releaseId": "1641",
                                    "softReleaseDOM": "—",
                                    "type": "Optic",
                                }
                            ],
                        },
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
        res = tmg._search(
            cable_type=["Duplex Fiber"],
            data_rate=["10 Gbps"],
            form_factor=["SFP+"],
            reach=["100m"],
            os_type=["IOS XE"],
        )
        assert res is not None
        assert int(res["totalCount"]) >= 2
        devices = res["networkDevices"]

        # Verify product families
        assert devices[0]["productFamily"] == "C9300"
        assert devices[1]["productFamily"] == "C9300L"

        # Verify device PIDs
        dev_one = devices[0]["networkAndTransceiverCompatibility"][0]
        dev_two = devices[1]["networkAndTransceiverCompatibility"][0]
        dev_three = devices[1]["networkAndTransceiverCompatibility"][1]
        dev_four = devices[1]["networkAndTransceiverCompatibility"][2]
        dev_five = devices[1]["networkAndTransceiverCompatibility"][3]
        assert dev_one["productId"] == "C9300-NM-8X"
        assert dev_two["productId"] == "C9300L-24T-4X"
        assert dev_three["productId"] == "C9300L-48T-4X"
        assert dev_four["productId"] == "C9300L-24P-4X"
        assert dev_five["productId"] == "C9300L-48P-4X"

        # Verify each device's transceivers
        dev_one["transceivers"][0]["productId"] == "FET-10G"
        dev_two["transceivers"][0]["productId"] == "FET-10G"
        dev_three["transceivers"][0]["productId"] == "FET-10G"
        dev_four["transceivers"][0]["productId"] == "FET-10G"
        dev_five["transceivers"][0]["productId"] == "FET-10G"

    @responses.activate
    def test_tmg_private_search_advanced_ucs_xr_1gbps(self):
        resp_json = {
            "totalCount": "5",
            "itemPerPage": None,
            "page": None,
            "networkDevices": [
                {
                "productFamily": "UCSB",
                "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/datasheet-c78-741116.html",
                "networkAndTransceiverCompatibility": [
                    {
                    "productId": "UCS-FI-M-6324",
                    "transceivers": [
                        {
                        "tmgId": "42449",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "140",
                        "productId": "GLC-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "0 to 70C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "194",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v3.1(1e)",
                        "networkDeviceNotes": None,
                        "releaseId": "1121",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "42450",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "194",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v3.1(1e)",
                        "networkDeviceNotes": None,
                        "releaseId": "1121",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "UCS-FI-6332-U",
                    "transceivers": [
                        {
                        "tmgId": "36102",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "140",
                        "productId": "GLC-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "0 to 70C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "195",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v3.1",
                        "networkDeviceNotes": None,
                        "releaseId": "68",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "UCS-FI-6332-16UP-U",
                    "transceivers": [
                        {
                        "tmgId": "36081",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "140",
                        "productId": "GLC-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "0 to 70C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "196",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v3.0",
                        "networkDeviceNotes": None,
                        "releaseId": "67",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "36083",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "140",
                        "productId": "GLC-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "0 to 70C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "196",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v3.1",
                        "networkDeviceNotes": None,
                        "releaseId": "68",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "39261",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": " ",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "196",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v3.1",
                        "networkDeviceNotes": None,
                        "releaseId": "68",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "N10-S6100",
                    "transceivers": [
                        {
                        "tmgId": "3819",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "140",
                        "productId": "GLC-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "0 to 70C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "905",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v1.3",
                        "networkDeviceNotes": None,
                        "releaseId": "258",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "4340",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "905",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v1.3",
                        "networkDeviceNotes": None,
                        "releaseId": "258",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8300",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "905",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v1.3",
                        "networkDeviceNotes": None,
                        "releaseId": "258",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "N10-S6200",
                    "transceivers": [
                        {
                        "tmgId": "3820",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "140",
                        "productId": "GLC-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "0 to 70C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "906",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v1.3",
                        "networkDeviceNotes": None,
                        "releaseId": "258",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "4341",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "906",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v1.3",
                        "networkDeviceNotes": None,
                        "releaseId": "258",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8301",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "906",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v1.3",
                        "networkDeviceNotes": None,
                        "releaseId": "258",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "N10-E0440",
                    "transceivers": [
                        {
                        "tmgId": "3821",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "140",
                        "productId": "GLC-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "0 to 70C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "907",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v1.3",
                        "networkDeviceNotes": None,
                        "releaseId": "258",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "4342",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "907",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v1.3",
                        "networkDeviceNotes": None,
                        "releaseId": "258",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8302",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "907",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v1.3",
                        "networkDeviceNotes": None,
                        "releaseId": "258",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "N10-E0600",
                    "transceivers": [
                        {
                        "tmgId": "3822",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "140",
                        "productId": "GLC-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "0 to 70C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "908",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v1.3",
                        "networkDeviceNotes": None,
                        "releaseId": "258",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "4343",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "908",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v1.3",
                        "networkDeviceNotes": None,
                        "releaseId": "258",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8303",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "908",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v1.3",
                        "networkDeviceNotes": None,
                        "releaseId": "258",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "N20-I6584",
                    "transceivers": [
                        {
                        "tmgId": "3823",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "140",
                        "productId": "GLC-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "0 to 70C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "909",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v1.3",
                        "networkDeviceNotes": None,
                        "releaseId": "258",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "4344",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "909",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v1.3",
                        "networkDeviceNotes": None,
                        "releaseId": "258",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8304",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "909",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v1.3",
                        "networkDeviceNotes": None,
                        "releaseId": "258",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "UCS-FI-6248UP",
                    "transceivers": [
                        {
                        "tmgId": "3824",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "140",
                        "productId": "GLC-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "0 to 70C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "910",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v2.0(1)",
                        "networkDeviceNotes": None,
                        "releaseId": "259",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "4345",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "910",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v2.0(1)",
                        "networkDeviceNotes": None,
                        "releaseId": "259",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8305",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "910",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v2.0(1)",
                        "networkDeviceNotes": None,
                        "releaseId": "259",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "UCS-FI-E16UP",
                    "transceivers": [
                        {
                        "tmgId": "3825",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "140",
                        "productId": "GLC-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "0 to 70C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "911",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v2.0(1)",
                        "networkDeviceNotes": None,
                        "releaseId": "259",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "4346",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "911",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v2.0(1)",
                        "networkDeviceNotes": None,
                        "releaseId": "259",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8306",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "911",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v2.0(1)",
                        "networkDeviceNotes": None,
                        "releaseId": "259",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "UCS-IOM-2208XP",
                    "transceivers": [
                        {
                        "tmgId": "3826",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "140",
                        "productId": "GLC-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "0 to 70C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "912",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v2.0(1)",
                        "networkDeviceNotes": None,
                        "releaseId": "259",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "4347",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "912",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v2.0(1)",
                        "networkDeviceNotes": None,
                        "releaseId": "259",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8307",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "912",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v2.0(1)",
                        "networkDeviceNotes": None,
                        "releaseId": "259",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "UCS-FI-6454",
                    "transceivers": [
                        {
                        "tmgId": "29789",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "1423",
                        "breakoutMode": " ",
                        "osType": "UCS",
                        "domSupport": " ",
                        "softReleaseMinVer": "UCS Manager v4.0(1a)",
                        "networkDeviceNotes": None,
                        "releaseId": "2361",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    }
                ]
                },
                {
                "productFamily": "NCS5000",
                "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/products/routers/network-convergence-system-5000-series/index.html",
                "networkAndTransceiverCompatibility": [
                    {
                    "productId": "NCS 5001",
                    "transceivers": [
                        {
                        "tmgId": "4440",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "1017",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.0.0",
                        "networkDeviceNotes": None,
                        "releaseId": "329",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "NCS 5002",
                    "transceivers": [
                        {
                        "tmgId": "4441",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "1018",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.0.0",
                        "networkDeviceNotes": None,
                        "releaseId": "329",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    }
                ]
                },
                {
                "productFamily": "NCS5500",
                "networkFamilyDataSheet": "http://www.cisco.com/c/en/us/products/routers/network-convergence-system-5500-series/index.html",
                "networkAndTransceiverCompatibility": [
                    {
                    "productId": "NC55-24H12F-SE",
                    "transceivers": [
                        {
                        "tmgId": "40027",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": " ",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "210",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.3.2",
                        "networkDeviceNotes": None,
                        "releaseId": "359",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "NCS-5501",
                    "transceivers": [
                        {
                        "tmgId": "4442",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "212",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.1.1",
                        "networkDeviceNotes": None,
                        "releaseId": "93",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "NCS-5501-SE",
                    "transceivers": [
                        {
                        "tmgId": "4443",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "213",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.1.1",
                        "networkDeviceNotes": None,
                        "releaseId": "93",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "NC55-MOD-A-S",
                    "transceivers": [
                        {
                        "tmgId": "30334",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "1461",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.5.1",
                        "networkDeviceNotes": None,
                        "releaseId": "782",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "NCS-55A2-MOD-S",
                    "transceivers": [
                        {
                        "tmgId": "30482",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "1481",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.5.1",
                        "networkDeviceNotes": None,
                        "releaseId": "782",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "NC55-MOD-A-SE-S",
                    "transceivers": [
                        {
                        "tmgId": "35275",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "1901",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.6.1",
                        "networkDeviceNotes": None,
                        "releaseId": "1701",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "NCS-55A2-MOD-HD-S",
                    "transceivers": [
                        {
                        "tmgId": "35372",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "1921",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.5.1",
                        "networkDeviceNotes": None,
                        "releaseId": "782",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "NCS-55A2-MOD-SE-S",
                    "transceivers": [
                        {
                        "tmgId": "38120",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "2241",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.6.1",
                        "networkDeviceNotes": None,
                        "releaseId": "1701",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "NCS-55A2-MOD-HX-S",
                    "transceivers": [
                        {
                        "tmgId": "40066",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "2401",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.5.1",
                        "networkDeviceNotes": None,
                        "releaseId": "782",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "NCS-55A2-MOD-SE-H-S",
                    "transceivers": [
                        {
                        "tmgId": "40113",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "2402",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.6.1",
                        "networkDeviceNotes": None,
                        "releaseId": "1701",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    }
                ]
                },
                {
                "productFamily": "ASR9000",
                "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/products/routers/asr-9000-series-aggregation-services-routers/datasheet-listing.html",
                "networkAndTransceiverCompatibility": [
                    {
                    "productId": "A9K-40GE-B",
                    "transceivers": [
                        {
                        "tmgId": "8390",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "251",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 3.9.0",
                        "networkDeviceNotes": None,
                        "releaseId": "673",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9K-40GE-E",
                    "transceivers": [
                        {
                        "tmgId": "8391",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "252",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 3.9.0",
                        "networkDeviceNotes": None,
                        "releaseId": "673",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9K-2T20GE-B",
                    "transceivers": [
                        {
                        "tmgId": "8392",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "253",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 3.9.0",
                        "networkDeviceNotes": None,
                        "releaseId": "673",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9K-2T20GE-E",
                    "transceivers": [
                        {
                        "tmgId": "8393",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "254",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 3.9.0",
                        "networkDeviceNotes": None,
                        "releaseId": "673",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9K-2T20GE-L",
                    "transceivers": [
                        {
                        "tmgId": "8394",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "255",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 3.9.0",
                        "networkDeviceNotes": None,
                        "releaseId": "673",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9K-40GE-L",
                    "transceivers": [
                        {
                        "tmgId": "8395",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "256",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 3.9.0",
                        "networkDeviceNotes": None,
                        "releaseId": "673",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9K-MPA-20X1GE",
                    "transceivers": [
                        {
                        "tmgId": "4473",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "257",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.2.2",
                        "networkDeviceNotes": None,
                        "releaseId": "90",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "36524",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "257",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.0.1",
                        "networkDeviceNotes": None,
                        "releaseId": "92",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8398",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "257",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 4.2.0",
                        "networkDeviceNotes": None,
                        "releaseId": "573",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "36534",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "257",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.0.1",
                        "networkDeviceNotes": None,
                        "releaseId": "92",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9K-40GE-TR",
                    "transceivers": [
                        {
                        "tmgId": "4469",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "511",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.3.4",
                        "networkDeviceNotes": None,
                        "releaseId": "395",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8388",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "511",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.2.2",
                        "networkDeviceNotes": None,
                        "releaseId": "90",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9K-40GE-SE",
                    "transceivers": [
                        {
                        "tmgId": "4470",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "512",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.3.4",
                        "networkDeviceNotes": None,
                        "releaseId": "395",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8389",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "512",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.2.2",
                        "networkDeviceNotes": None,
                        "releaseId": "90",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9K-4T16GE-TR",
                    "transceivers": [
                        {
                        "tmgId": "4471",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "513",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.3.4",
                        "networkDeviceNotes": None,
                        "releaseId": "395",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8396",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "513",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.3.0",
                        "networkDeviceNotes": None,
                        "releaseId": "73",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9K-4T16GE-SE",
                    "transceivers": [
                        {
                        "tmgId": "4472",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "514",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.3.4",
                        "networkDeviceNotes": None,
                        "releaseId": "395",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8397",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "514",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.3.0",
                        "networkDeviceNotes": None,
                        "releaseId": "73",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9K-RSP440-TR",
                    "transceivers": [
                        {
                        "tmgId": "37615",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "515",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.2.2",
                        "networkDeviceNotes": None,
                        "releaseId": "90",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9K-RSP440-SE",
                    "transceivers": [
                        {
                        "tmgId": "4474",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "516",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.2.2",
                        "networkDeviceNotes": None,
                        "releaseId": "90",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "ASR-9000V-AC",
                    "transceivers": [
                        {
                        "tmgId": "4478",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "520",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.2.2",
                        "networkDeviceNotes": None,
                        "releaseId": "90",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8400",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "520",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 4.3.0",
                        "networkDeviceNotes": None,
                        "releaseId": "400",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "ASR-9000V-DC-A",
                    "transceivers": [
                        {
                        "tmgId": "4480",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "521",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.2.2",
                        "networkDeviceNotes": None,
                        "releaseId": "90",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8401",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "521",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 4.3.0",
                        "networkDeviceNotes": None,
                        "releaseId": "400",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "ASR-9000V-DC-E",
                    "transceivers": [
                        {
                        "tmgId": "4482",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "522",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.2.2",
                        "networkDeviceNotes": None,
                        "releaseId": "90",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8402",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "522",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 4.3.0",
                        "networkDeviceNotes": None,
                        "releaseId": "400",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "ASR-9000V-24-A",
                    "transceivers": [
                        {
                        "tmgId": "3915",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "140",
                        "productId": "GLC-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "0 to 70C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "523",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 4.2.3",
                        "networkDeviceNotes": None,
                        "releaseId": "398",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "4483",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "523",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.2.0",
                        "networkDeviceNotes": None,
                        "releaseId": "399",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "4484",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "523",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.2.2",
                        "networkDeviceNotes": None,
                        "releaseId": "90",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8403",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "523",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 4.3.0",
                        "networkDeviceNotes": None,
                        "releaseId": "400",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9KV-V2-AC",
                    "transceivers": [
                        {
                        "tmgId": "4485",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "524",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.2.0",
                        "networkDeviceNotes": None,
                        "releaseId": "399",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "4486",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "524",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.2.2",
                        "networkDeviceNotes": None,
                        "releaseId": "90",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8404",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "524",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 4.3.0",
                        "networkDeviceNotes": None,
                        "releaseId": "400",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9KV-V2-DC-A",
                    "transceivers": [
                        {
                        "tmgId": "4487",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "525",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.2.0",
                        "networkDeviceNotes": None,
                        "releaseId": "399",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "4488",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "525",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.2.2",
                        "networkDeviceNotes": None,
                        "releaseId": "90",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8405",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "525",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 4.3.0",
                        "networkDeviceNotes": None,
                        "releaseId": "400",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9KV-V2-DC-E",
                    "transceivers": [
                        {
                        "tmgId": "4489",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "526",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.2.0",
                        "networkDeviceNotes": None,
                        "releaseId": "399",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "4490",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "526",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.2.2",
                        "networkDeviceNotes": None,
                        "releaseId": "90",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        },
                        {
                        "tmgId": "8406",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "197",
                        "productId": "SFP-GE-T",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": "Y",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "526",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 4.3.0",
                        "networkDeviceNotes": None,
                        "releaseId": "400",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9K-24X10GE-1G-SE",
                    "transceivers": [
                        {
                        "tmgId": "36933",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "1061",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.2.2",
                        "networkDeviceNotes": None,
                        "releaseId": "85",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9K-24X10GE-1G-TR",
                    "transceivers": [
                        {
                        "tmgId": "36974",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "1062",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.2.2",
                        "networkDeviceNotes": None,
                        "releaseId": "85",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9K-48X10GE-1G-SE",
                    "transceivers": [
                        {
                        "tmgId": "37059",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "1063",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.2.2",
                        "networkDeviceNotes": None,
                        "releaseId": "85",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9K-48X10GE-1G-TR",
                    "transceivers": [
                        {
                        "tmgId": "37017",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "1064",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.2.2",
                        "networkDeviceNotes": None,
                        "releaseId": "85",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A9K-RSP440-LT",
                    "transceivers": [
                        {
                        "tmgId": "37617",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "0",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "2161",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 5.2.2",
                        "networkDeviceNotes": None,
                        "releaseId": "90",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A99-48X10GE-1G-SE",
                    "transceivers": [
                        {
                        "tmgId": "43693",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "2801",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.5.2",
                        "networkDeviceNotes": None,
                        "releaseId": "1661",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "A99-48X10GE-1G-TR",
                    "transceivers": [
                        {
                        "tmgId": "43778",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "10BASE-T, 100BASE-T, 1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "2802",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.5.2",
                        "networkDeviceNotes": None,
                        "releaseId": "1661",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    }
                ]
                },
                {
                "productFamily": "NCS540",
                "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/products/collateral/routers/network-convergence-system-500-series-routers/datasheet-c78-740296.html",
                "networkAndTransceiverCompatibility": [
                    {
                    "productId": "N540-24Z8Q2C-SYS",
                    "transceivers": [
                        {
                        "tmgId": "29609",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "1021",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.3.2",
                        "networkDeviceNotes": None,
                        "releaseId": "359",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "N540-ACC-SYS",
                    "transceivers": [
                        {
                        "tmgId": "29673",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "2181",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.3.2",
                        "networkDeviceNotes": None,
                        "releaseId": "359",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "N540X-ACC-SYS",
                    "transceivers": [
                        {
                        "tmgId": "37655",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "2182",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.3.2",
                        "networkDeviceNotes": None,
                        "releaseId": "359",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    },
                    {
                    "productId": "N540-24Z8Q2C-M",
                    "transceivers": [
                        {
                        "tmgId": "42674",
                        "productFamilyId": "11",
                        "productFamily": "SFPGE",
                        "productModelId": "141",
                        "productId": "GLC-TE",
                        "version": " ",
                        "versionId": None,
                        "description": None,
                        "formFactor": "SFP",
                        "reach": "100m",
                        "temperatureRange": "-5 to 85C",
                        "digitalDiagnostic": "N",
                        "cableType": "Cat5e/6A",
                        "media": "Copper",
                        "connectorType": "RJ-45",
                        "transmissionStandard": "1000BASE-T",
                        "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/product_data_sheet0900aecd8033f885.html",
                        "endOfSale": " ",
                        "dataRate": "10/100/1000 Mbps",
                        "transceiverNotes": None,
                        "noteCount": "1",
                        "state": None,
                        "stateMessage": None,
                        "updatedOn": None,
                        "updatedBy": None,
                        "transceiverBusinessUnit": "TMG",
                        "networkModelId": "2641",
                        "breakoutMode": " ",
                        "osType": "IOS XR",
                        "domSupport": " ",
                        "softReleaseMinVer": "IOS XR 6.3.2",
                        "networkDeviceNotes": None,
                        "releaseId": "359",
                        "softReleaseDOM": "—",
                        "type": "Optic"
                        }
                    ]
                    }
                ]
                }
            ]
        }
        responses.add(
            responses.POST,
            "https://tmgmatrix.cisco.com/public/api/networkdevice/search",
            json=resp_json,
            status=200,
        )

        tmg = TMG.TMG()
        res = tmg._search(
            cable_type=["Cat5e/6A"],
            data_rate=["10/100/1000 Mbps"],
            form_factor=["SFP"],
            reach=["100m"],
            os_type=["IOS XR", "UCS"]
        )
        assert res is not None
        assert int(res["totalCount"]) >= 5
        devices = res["networkDevices"]

        # Verify product families
        assert devices[0]["productFamily"] == "UCSB"
        assert devices[1]["productFamily"] == "NCS5000"
        assert devices[2]["productFamily"] == "NCS5500"
        assert devices[3]["productFamily"] == "ASR9000"
        assert devices[4]["productFamily"] == "NCS540"

        # Verify device PIDs
        expected_devices = [
            "UCS-FI-M-6324",
            "UCS-FI-6332-U",
            "UCS-FI-6332-16UP-U",
            "N10-S6100",
            "N10-S6200",
            "N10-E0440",
            "N10-E0600",
            "N20-I6584",
            "UCS-FI-6248UP",
            "UCS-FI-E16UP",
            "UCS-IOM-2208XP",
            "UCS-FI-6454",
            "NCS 5001",
            "NCS 5002",
            "NC55-24H12F-SE",
            "NCS-5501",
            "NCS-5501-SE",
            "NC55-MOD-A-S",
            "NCS-55A2-MOD-S",
            "NC55-MOD-A-SE-S",
            "NCS-55A2-MOD-HD-S",
            "NCS-55A2-MOD-SE-S",
            "NCS-55A2-MOD-HX-S",
            "NCS-55A2-MOD-SE-H-S",
            "A9K-40GE-B",
            "A9K-40GE-E",
            "A9K-2T20GE-B",
            "A9K-2T20GE-E",
            "A9K-2T20GE-L",
            "A9K-40GE-L",
            "A9K-MPA-20X1GE",
            "A9K-40GE-TR",
            "A9K-40GE-SE",
            "A9K-4T16GE-TR",
            "A9K-4T16GE-SE",
            "A9K-RSP440-TR",
            "A9K-RSP440-SE",
            "ASR-9000V-AC",
            "ASR-9000V-DC-A",
            "ASR-9000V-DC-E",
            "ASR-9000V-24-A",
            "A9KV-V2-AC",
            "A9KV-V2-DC-A",
            "A9KV-V2-DC-E",
            "A9K-24X10GE-1G-SE",
            "A9K-24X10GE-1G-TR",
            "A9K-48X10GE-1G-SE",
            "A9K-48X10GE-1G-TR",
            "A9K-RSP440-LT",
            "A99-48X10GE-1G-SE",
            "A99-48X10GE-1G-TR",
            "N540-24Z8Q2C-SYS",
            "N540-ACC-SYS",
            "N540X-ACC-SYS",
            "N540-24Z8Q2C-M"
            ]
        for pf in devices:
            for dev in pf["networkAndTransceiverCompatibility"]:
                assert dev["productId"] in expected_devices
        
        # Verify supported transceivers
        for pf in devices:
            for dev in pf["networkAndTransceiverCompatibility"]:
                for xcvr in dev["transceivers"]:
                    assert xcvr["cableType"] == "Cat5e/6A"
                    assert xcvr["dataRate"] == "10/100/1000 Mbps"
                    assert xcvr["reach"] == "100m"
                    assert xcvr["formFactor"] == "SFP"
                    assert (xcvr["osType"] == "UCS" or xcvr["osType"] == "IOS XR")
                    assert (
                        xcvr["productId"] == "GLC-T" or 
                        xcvr["productId"] == "GLC-TE" or
                        xcvr["productId"] == "SFP-GE-T"
                    )


class TestDeviceSearchingAdvanced:
    @responses.activate
    def test_tmg_search_advanced_ios_xe_fet_10g(self):
        resp_json = {
            "totalCount": "2",
            "itemPerPage": None,
            "page": None,
            "networkDevices": [
                {
                    "productFamily": "C9300",
                    "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/products/switches/catalyst-9300-series-switches/index.html",
                    "networkAndTransceiverCompatibility": [
                        {
                            "productId": "C9300-NM-8X",
                            "transceivers": [
                                {
                                    "tmgId": "18751",
                                    "productFamilyId": "12",
                                    "productFamily": "SFP10G",
                                    "productModelId": "99",
                                    "productId": "FET-10G",
                                    "version": " ",
                                    "versionId": None,
                                    "description": None,
                                    "formFactor": "SFP+",
                                    "reach": "100m",
                                    "temperatureRange": "0 to 70C",
                                    "digitalDiagnostic": "N",
                                    "cableType": "Duplex Fiber",
                                    "media": "MMF",
                                    "connectorType": "LC",
                                    "transmissionStandard": " ",
                                    "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.pdf",
                                    "endOfSale": " ",
                                    "dataRate": "10 Gbps",
                                    "transceiverNotes": None,
                                    "noteCount": "1",
                                    "state": None,
                                    "stateMessage": None,
                                    "updatedOn": None,
                                    "updatedBy": None,
                                    "transceiverBusinessUnit": "TMG",
                                    "networkModelId": "670",
                                    "breakoutMode": " ",
                                    "osType": "IOS XE",
                                    "domSupport": " ",
                                    "softReleaseMinVer": "IOS XE 16.5.1",
                                    "networkDeviceNotes": None,
                                    "releaseId": "657",
                                    "softReleaseDOM": "—",
                                    "type": "Optic",
                                }
                            ],
                        }
                    ],
                },
                {
                    "productFamily": "C9300L",
                    "networkFamilyDataSheet": "https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9500-series-switches/data_sheet-c78-738978.html",
                    "networkAndTransceiverCompatibility": [
                        {
                            "productId": "C9300L-24T-4X",
                            "transceivers": [
                                {
                                    "tmgId": "39519",
                                    "productFamilyId": "12",
                                    "productFamily": "SFP10G",
                                    "productModelId": "99",
                                    "productId": "FET-10G",
                                    "version": " ",
                                    "versionId": None,
                                    "description": None,
                                    "formFactor": "SFP+",
                                    "reach": "100m",
                                    "temperatureRange": "0 to 70C",
                                    "digitalDiagnostic": "N",
                                    "cableType": "Duplex Fiber",
                                    "media": "MMF",
                                    "connectorType": "LC",
                                    "transmissionStandard": " ",
                                    "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.pdf",
                                    "endOfSale": " ",
                                    "dataRate": "10 Gbps",
                                    "transceiverNotes": None,
                                    "noteCount": "0",
                                    "state": None,
                                    "stateMessage": None,
                                    "updatedOn": None,
                                    "updatedBy": None,
                                    "transceiverBusinessUnit": "TMG",
                                    "networkModelId": "1827",
                                    "breakoutMode": " ",
                                    "osType": "IOS XE",
                                    "domSupport": " ",
                                    "softReleaseMinVer": "IOS XE 16.12.1",
                                    "networkDeviceNotes": None,
                                    "releaseId": "1641",
                                    "softReleaseDOM": "—",
                                    "type": "Optic",
                                }
                            ],
                        },
                        {
                            "productId": "C9300L-48T-4X",
                            "transceivers": [
                                {
                                    "tmgId": "39573",
                                    "productFamilyId": "12",
                                    "productFamily": "SFP10G",
                                    "productModelId": "99",
                                    "productId": "FET-10G",
                                    "version": " ",
                                    "versionId": None,
                                    "description": None,
                                    "formFactor": "SFP+",
                                    "reach": "100m",
                                    "temperatureRange": "0 to 70C",
                                    "digitalDiagnostic": "N",
                                    "cableType": "Duplex Fiber",
                                    "media": "MMF",
                                    "connectorType": "LC",
                                    "transmissionStandard": " ",
                                    "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.pdf",
                                    "endOfSale": " ",
                                    "dataRate": "10 Gbps",
                                    "transceiverNotes": None,
                                    "noteCount": "0",
                                    "state": None,
                                    "stateMessage": None,
                                    "updatedOn": None,
                                    "updatedBy": None,
                                    "transceiverBusinessUnit": "TMG",
                                    "networkModelId": "1828",
                                    "breakoutMode": " ",
                                    "osType": "IOS XE",
                                    "domSupport": " ",
                                    "softReleaseMinVer": "IOS XE 16.12.1",
                                    "networkDeviceNotes": None,
                                    "releaseId": "1641",
                                    "softReleaseDOM": "—",
                                    "type": "Optic",
                                }
                            ],
                        },
                        {
                            "productId": "C9300L-24P-4X",
                            "transceivers": [
                                {
                                    "tmgId": "39627",
                                    "productFamilyId": "12",
                                    "productFamily": "SFP10G",
                                    "productModelId": "99",
                                    "productId": "FET-10G",
                                    "version": " ",
                                    "versionId": None,
                                    "description": None,
                                    "formFactor": "SFP+",
                                    "reach": "100m",
                                    "temperatureRange": "0 to 70C",
                                    "digitalDiagnostic": "N",
                                    "cableType": "Duplex Fiber",
                                    "media": "MMF",
                                    "connectorType": "LC",
                                    "transmissionStandard": " ",
                                    "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.pdf",
                                    "endOfSale": " ",
                                    "dataRate": "10 Gbps",
                                    "transceiverNotes": None,
                                    "noteCount": "0",
                                    "state": None,
                                    "stateMessage": None,
                                    "updatedOn": None,
                                    "updatedBy": None,
                                    "transceiverBusinessUnit": "TMG",
                                    "networkModelId": "1829",
                                    "breakoutMode": " ",
                                    "osType": "IOS XE",
                                    "domSupport": " ",
                                    "softReleaseMinVer": "IOS XE 16.12.1",
                                    "networkDeviceNotes": None,
                                    "releaseId": "1641",
                                    "softReleaseDOM": "—",
                                    "type": "Optic",
                                }
                            ],
                        },
                        {
                            "productId": "C9300L-48P-4X",
                            "transceivers": [
                                {
                                    "tmgId": "42136",
                                    "productFamilyId": "12",
                                    "productFamily": "SFP10G",
                                    "productModelId": "99",
                                    "productId": "FET-10G",
                                    "version": " ",
                                    "versionId": None,
                                    "description": None,
                                    "formFactor": "SFP+",
                                    "reach": "100m",
                                    "temperatureRange": "0 to 70C",
                                    "digitalDiagnostic": "N",
                                    "cableType": "Duplex Fiber",
                                    "media": "MMF",
                                    "connectorType": "LC",
                                    "transmissionStandard": " ",
                                    "transceiverModelDataSheet": "https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.pdf",
                                    "endOfSale": " ",
                                    "dataRate": "10 Gbps",
                                    "transceiverNotes": None,
                                    "noteCount": "0",
                                    "state": None,
                                    "stateMessage": None,
                                    "updatedOn": None,
                                    "updatedBy": None,
                                    "transceiverBusinessUnit": "TMG",
                                    "networkModelId": "1830",
                                    "breakoutMode": " ",
                                    "osType": "IOS XE",
                                    "domSupport": " ",
                                    "softReleaseMinVer": "IOS XE 16.12.1",
                                    "networkDeviceNotes": None,
                                    "releaseId": "1641",
                                    "softReleaseDOM": "—",
                                    "type": "Optic",
                                }
                            ],
                        },
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
        params = {
            "cable_type": ["Duplex Fiber"],
            "data_rate": ["10 Gbps"],
            "form_factor": ["SFP+"],
            "reach": ["100m"],
            "os_type": ["IOS XE"],
        }
        res = tmg.search(**params)
        assert res is not None
        assert res.total_count >= 2

        # Verify product families
        assert res.network_devices[0].product_family == "C9300"
        assert res.network_devices[1].product_family == "C9300L"

        # Verify device PIDs
        assert res.network_devices[0].product_id == "C9300-NM-8X"
        assert res.network_devices[1].product_id == "C9300L-24T-4X"
        assert res.network_devices[2].product_id == "C9300L-48T-4X"
        assert res.network_devices[3].product_id == "C9300L-24P-4X"
        assert res.network_devices[4].product_id == "C9300L-48P-4X"

        # Verify each device's transceivers
        assert res.network_devices[0].transceivers[0].product_id == "FET-10G"
        assert res.network_devices[1].transceivers[0].product_id == "FET-10G"
        assert res.network_devices[2].transceivers[0].product_id == "FET-10G"
        assert res.network_devices[3].transceivers[0].product_id == "FET-10G"
        assert res.network_devices[4].transceivers[0].product_id == "FET-10G"


class TestCableTypeValidation:
    def test_cable_type_validation_invalid_data(self):
        invalid_cable_type = ["asdfasdfasdf"]
        tmg = TMG.TMG()
        with pytest.raises(
            ValueError,
            match=r'Invalid Cable Types.*specified'.format(invalid_cable_type),
        ):
            tmg._validate_cable_type(invalid_cable_type)

    def test_cable_type_validation_single_strand(self):
        test_cable_type = ["Single-Strand"]
        expected_return_data = [
            {
                "id": "61",
                "name": "Single-Strand",
                "count": "0",
                "filterChecked": "true",
                "filtername": "cableType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_cable_type(test_cable_type)
        assert results == expected_return_data

    def test_cable_type_validation_na(self):
        test_cable_type = ["N/A (Incl AOC and DAC)"]
        expected_return_data = [
            {
                "id": "1",
                "name": "N/A (Incl AOC and DAC)",
                "count": "0",
                "filterChecked": "true",
                "filtername": "cableType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_cable_type(test_cable_type)
        assert results == expected_return_data

    def test_cable_type_validation_duplex_fiber(self):
        test_cable_type = ["Duplex Fiber"]
        expected_return_data = [
            {
                "id": "2",
                "name": "Duplex Fiber",
                "count": "0",
                "filterChecked": "true",
                "filtername": "cableType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_cable_type(test_cable_type)
        assert results == expected_return_data

    def test_cable_type_validation_ribbon_fiber(self):
        test_cable_type = ["Ribbon Fiber"]
        expected_return_data = [
            {
                "id": "3",
                "name": "Ribbon Fiber",
                "count": "0",
                "filterChecked": "true",
                "filtername": "cableType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_cable_type(test_cable_type)
        assert results == expected_return_data

    def test_cable_type_validation_single_strand_2(self):
        test_cable_type = ["Single-strand"]
        expected_return_data = [
            {
                "id": "5",
                "name": "Single-strand",
                "count": "0",
                "filterChecked": "true",
                "filtername": "cableType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_cable_type(test_cable_type)
        assert results == expected_return_data


class TestDataRateValidation:
    def test_data_rate_validation_invalid_data(self):
        invalid_data_rate = ["asdfasdfasdf"]
        tmg = TMG.TMG()
        with pytest.raises(
            ValueError,
            match=r'Invalid Data Rates.*specified'.format(invalid_data_rate),
        ):
            tmg._validate_data_rate(invalid_data_rate)

    def test_data_rate_validation_100_200_gbps(self):
        test_data_rate = ["100/200 Gbps"]
        expected_return_data = [
            {
                "id": "141",
                "name": "100/200 Gbps",
                "count": "0",
                "filterChecked": "true",
                "filtername": "dataRate",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_10_25_gbps(self):
        test_data_rate = ["10/25 Gbps"]
        expected_return_data = [
            {
                "id": "81",
                "name": "10/25 Gbps",
                "count": "0",
                "filterChecked": "true",
                "filtername": "dataRate",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_100_mbps(self):
        test_data_rate = ["100 Mbps"]
        expected_return_data = [
            {
                "id": "1",
                "name": "100 Mbps",
                "count": "0",
                "filterChecked": "true",
                "filtername": "dataRate",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_155_mbps(self):
        test_data_rate = ["155 Mbps"]
        expected_return_data = [
            {
                "id": "2",
                "name": "155 Mbps",
                "count": "0",
                "filterChecked": "true",
                "filtername": "dataRate",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_622_mbps(self):
        test_data_rate = ["622 Mbps"]
        expected_return_data = [
            {
                "id": "3",
                "name": "622 Mbps",
                "count": "0",
                "filterChecked": "true",
                "filtername": "dataRate",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_2_488_gbps(self):
        test_data_rate = ["2.488 Gbps"]
        expected_return_data = [
            {
                "id": "4",
                "name": "2.488 Gbps",
                "count": "0",
                "filterChecked": "true",
                "filtername": "dataRate",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_40_100_gbps(self):
        test_data_rate = ["40/100 Gbps"]
        expected_return_data = [
            {
                "id": "5",
                "name": "40/100 Gbps",
                "count": "0",
                "filterChecked": "true",
                "filtername": "dataRate",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_40_gbps(self):
        test_data_rate = ["40 Gbps"]
        expected_return_data = [
            {
                "id": "6",
                "name": "40 Gbps",
                "count": "0",
                "filterChecked": "true",
                "filtername": "dataRate",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_100_gbps(self):
        test_data_rate = ["100 Gbps"]
        expected_return_data = [
            {
                "id": "7",
                "name": "100 Gbps",
                "count": "0",
                "filterChecked": "true",
                "filtername": "dataRate",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_25_gbps(self):
        test_data_rate = ["25 Gbps"]
        expected_return_data = [
            {
                "id": "9",
                "name": "25 Gbps",
                "count": "0",
                "filterChecked": "true",
                "filtername": "dataRate",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_10_gbps(self):
        test_data_rate = ["10 Gbps"]
        expected_return_data = [
            {
                "id": "10",
                "name": "10 Gbps",
                "count": "0",
                "filterChecked": "true",
                "filtername": "dataRate",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_8_gbps(self):
        test_data_rate = ["8 Gbps"]
        expected_return_data = [
            {
                "id": "121",
                "name": "8 Gbps",
                "count": "0",
                "filterChecked": "true",
                "filtername": "dataRate",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_16_gbps(self):
        test_data_rate = ["16 Gbps"]
        expected_return_data = [
            {
                "id": "122",
                "name": "16 Gbps",
                "count": "0",
                "filterChecked": "true",
                "filtername": "dataRate",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_32_gbps(self):
        test_data_rate = ["32 Gbps"]
        expected_return_data = [
            {
                "id": "123",
                "name": "32 Gbps",
                "count": "0",
                "filterChecked": "true",
                "filtername": "dataRate",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data


class TestFormFactorValidation:
    def test_form_factor_validation_invalid_data(self):
        invalid_form_factor = ["asdfasdfasdf"]
        tmg = TMG.TMG()
        with pytest.raises(
            ValueError,
            match=r'Invalid Form Factors.*specified'.format(invalid_form_factor),
        ):
            tmg._validate_form_factor(invalid_form_factor)

    def test_form_factor_validation_sfp_plus(self):
        test_form_factor = ["SFP+"]
        expected_return_data = [
            {
                "id": "41",
                "name": "SFP+",
                "count": "0",
                "filterChecked": "true",
                "filtername": "formFactor",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_form_factor(test_form_factor)
        assert results == expected_return_data

    def test_form_factor_validation_sfp28(self):
        test_form_factor = ["SFP28"]
        expected_return_data = [
            {
                "id": "42",
                "name": "SFP28",
                "count": "0",
                "filterChecked": "true",
                "filtername": "formFactor",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_form_factor(test_form_factor)
        assert results == expected_return_data

    def test_form_factor_validation_sfp(self):
        test_form_factor = ["SFP"]
        expected_return_data = [
            {
                "id": "2",
                "name": "SFP",
                "count": "0",
                "filterChecked": "true",
                "filtername": "formFactor",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_form_factor(test_form_factor)
        assert results == expected_return_data

    def test_form_factor_validation_qsfp28(self):
        test_form_factor = ["QSFP28"]
        expected_return_data = [
            {
                "id": "5",
                "name": "QSFP28",
                "count": "0",
                "filterChecked": "true",
                "filtername": "formFactor",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_form_factor(test_form_factor)
        assert results == expected_return_data

    def test_form_factor_validation_gbic(self):
        test_form_factor = ["GBIC"]
        expected_return_data = [
            {
                "id": "7",
                "name": "GBIC",
                "count": "0",
                "filterChecked": "true",
                "filtername": "formFactor",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_form_factor(test_form_factor)
        assert results == expected_return_data

    def test_form_factor_validation_xenpak(self):
        test_form_factor = ["XENPAK"]
        expected_return_data = [
            {
                "id": "8",
                "name": "XENPAK",
                "count": "0",
                "filterChecked": "true",
                "filtername": "formFactor",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_form_factor(test_form_factor)
        assert results == expected_return_data

    def test_form_factor_validation_x2(self):
        test_form_factor = ["X2"]
        expected_return_data = [
            {
                "id": "9",
                "name": "X2",
                "count": "0",
                "filterChecked": "true",
                "filtername": "formFactor",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_form_factor(test_form_factor)
        assert results == expected_return_data

    def test_form_factor_validation_xfp(self):
        test_form_factor = ["XFP"]
        expected_return_data = [
            {
                "id": "10",
                "name": "XFP",
                "count": "0",
                "filterChecked": "true",
                "filtername": "formFactor",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_form_factor(test_form_factor)
        assert results == expected_return_data

    def test_form_factor_validation_qsfp_plus(self):
        test_form_factor = ["QSFP+"]
        expected_return_data = [
            {
                "id": "21",
                "name": "QSFP+",
                "count": "0",
                "filterChecked": "true",
                "filtername": "formFactor",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_form_factor(test_form_factor)
        assert results == expected_return_data


class TestReachValidation:
    def test_reach_validation_invalid_data(self):
        invalid_reach = ["asdfasdfasdf"]
        tmg = TMG.TMG()
        with pytest.raises(
            ValueError, match=r'Invalid Reaches.*specified'.format(invalid_reach),
        ):
            tmg._validate_reach(invalid_reach)

    def test_reach_validation_220m(self):
        test_reach_data = ["220m"]
        expected_return_data = [
            {
                "id": "81",
                "name": "220m",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_400m_om3(self):
        test_reach_data = ["400m (OM3)"]
        expected_return_data = [
            {
                "id": "141",
                "name": "400m (OM3)",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_550m_om3(self):
        test_reach_data = ["550m (OM3)"]
        expected_return_data = [
            {
                "id": "181",
                "name": "550m (OM3)",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_10km_capital(self):
        test_reach_data = ["10Km"]
        expected_return_data = [
            {
                "id": "182",
                "name": "10Km",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_1km_om4(self):
        test_reach_data = ["1km (OM4)"]
        expected_return_data = [
            {
                "id": "183",
                "name": "1km (OM4)",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_4m(self):
        test_reach_data = ["4m"]
        expected_return_data = [
            {
                "id": "41",
                "name": "4m",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_1km(self):
        test_reach_data = ["1km"]
        expected_return_data = [
            {
                "id": "3",
                "name": "1km",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_550m(self):
        test_reach_data = ["550m"]
        expected_return_data = [
            {
                "id": "4",
                "name": "550m",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_70km(self):
        test_reach_data = ["70km"]
        expected_return_data = [
            {
                "id": "5",
                "name": "70km",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_80km(self):
        test_reach_data = ["80km"]
        expected_return_data = [
            {
                "id": "6",
                "name": "80km",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_70m_om3(self):
        test_reach_data = ["70m (OM3)"]
        expected_return_data = [
            {
                "id": "8",
                "name": "70m (OM3)",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_100m_om4(self):
        test_reach_data = ["100m (OM4)"]
        expected_return_data = [
            {
                "id": "9",
                "name": "100m (OM4)",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_500m(self):
        test_reach_data = ["500m"]
        expected_return_data = [
            {
                "id": "10",
                "name": "500m",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_25m(self):
        test_reach_data = ["25m"]
        expected_return_data = [
            {
                "id": "11",
                "name": "25m",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_30m(self):
        test_reach_data = ["30m"]
        expected_return_data = [
            {
                "id": "12",
                "name": "30m",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_25km(self):
        test_reach_data = ["25km"]
        expected_return_data = [
            {
                "id": "13",
                "name": "25km",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_100m_om3(self):
        test_reach_data = ["100m (OM3)"]
        expected_return_data = [
            {
                "id": "14",
                "name": "100m (OM3)",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_300m_om3(self):
        test_reach_data = ["300m (OM3)"]
        expected_return_data = [
            {
                "id": "15",
                "name": "300m (OM3)",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_150m_om4(self):
        test_reach_data = ["150m (OM4)"]
        expected_return_data = [
            {
                "id": "16",
                "name": "150m (OM4)",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_400m_om4(self):
        test_reach_data = ["400m (OM4)"]
        expected_return_data = [
            {
                "id": "17",
                "name": "400m (OM4)",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_10km_lowercase(self):
        test_reach_data = ["10km"]
        expected_return_data = [
            {
                "id": "18",
                "name": "10km",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_40km(self):
        test_reach_data = ["40km"]
        expected_return_data = [
            {
                "id": "19",
                "name": "40km",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_2km(self):
        test_reach_data = ["2km"]
        expected_return_data = [
            {
                "id": "20",
                "name": "2km",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_5m(self):
        test_reach_data = ["5m"]
        expected_return_data = [
            {
                "id": "21",
                "name": "5m",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_3m(self):
        test_reach_data = ["3m"]
        expected_return_data = [
            {
                "id": "22",
                "name": "3m",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_1m(self):
        test_reach_data = ["1m"]
        expected_return_data = [
            {
                "id": "23",
                "name": "1m",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_7m(self):
        test_reach_data = ["7m"]
        expected_return_data = [
            {
                "id": "24",
                "name": "7m",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_10m(self):
        test_reach_data = ["10m"]
        expected_return_data = [
            {
                "id": "25",
                "name": "10m",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_2m(self):
        test_reach_data = ["2m"]
        expected_return_data = [
            {
                "id": "26",
                "name": "2m",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_15m(self):
        test_reach_data = ["15m"]
        expected_return_data = [
            {
                "id": "27",
                "name": "15m",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_20m(self):
        test_reach_data = ["20m"]
        expected_return_data = [
            {
                "id": "28",
                "name": "20m",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_none(self):
        test_reach_data = ["None"]
        expected_return_data = [
            {
                "id": "29",
                "name": "None",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_15km(self):
        test_reach_data = ["15km"]
        expected_return_data = [
            {
                "id": "31",
                "name": "15km",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_20km(self):
        test_reach_data = ["20km"]
        expected_return_data = [
            {
                "id": "32",
                "name": "20km",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_300m(self):
        test_reach_data = ["300m"]
        expected_return_data = [
            {
                "id": "35",
                "name": "300m",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_400m(self):
        test_reach_data = ["400m"]
        expected_return_data = [
            {
                "id": "36",
                "name": "400m",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_2_5m(self):
        test_reach_data = ["2.5m"]
        expected_return_data = [
            {
                "id": "38",
                "name": "2.5m",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_400m_o43(self):
        test_reach_data = ["400m (O43)"]
        expected_return_data = [
            {
                "id": "121",
                "name": "400m (O43)",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_190m_om4(self):
        test_reach_data = ["190m (OM4)"]
        expected_return_data = [
            {
                "id": "161",
                "name": "190m (OM4)",
                "count": "0",
                "filterChecked": "true",
                "filtername": "reach",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data


class TestOSTypeValidation:
    def test_os_type_validation_invalid_data(self):
        invalid_os_type = ["asdfasdfasdf"]
        tmg = TMG.TMG()
        with pytest.raises(
            ValueError, match=r'Invalid OS Types.*specified'.format(invalid_os_type),
        ):
            tmg._validate_os_type(invalid_os_type)

    def test_os_type_validation_nxos(self):
        test_os_type_data = ["NX-OS"]
        expected_return_data = [
            {
                "id": "1",
                "name": "NX-OS",
                "count": "0",
                "filterChecked": "true",
                "filtername": "osType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_ios_xe(self):
        test_os_type_data = ["IOS XE"]
        expected_return_data = [
            {
                "id": "3",
                "name": "IOS XE",
                "count": "0",
                "filterChecked": "true",
                "filtername": "osType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_ios_xr(self):
        test_os_type_data = ["IOS XR"]
        expected_return_data = [
            {
                "id": "11",
                "name": "IOS XR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "osType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_spa(self):
        test_os_type_data = ["SPA"]
        expected_return_data = [
            {
                "id": "15",
                "name": "SPA",
                "count": "0",
                "filterChecked": "true",
                "filtername": "osType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_ie1000(self):
        test_os_type_data = ["IE1000"]
        expected_return_data = [
            {
                "id": "26",
                "name": "IE1000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "osType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_ios(self):
        test_os_type_data = ["IOS"]
        expected_return_data = [
            {
                "id": "48",
                "name": "IOS",
                "count": "0",
                "filterChecked": "true",
                "filtername": "osType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_ucs(self):
        test_os_type_data = ["UCS"]
        expected_return_data = [
            {
                "id": "55",
                "name": "UCS",
                "count": "0",
                "filterChecked": "true",
                "filtername": "osType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_fxos(self):
        test_os_type_data = ["FXOS"]
        expected_return_data = [
            {
                "id": "56",
                "name": "FXOS",
                "count": "0",
                "filterChecked": "true",
                "filtername": "osType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_olt(self):
        test_os_type_data = ["OLT"]
        expected_return_data = [
            {
                "id": "57",
                "name": "OLT",
                "count": "0",
                "filterChecked": "true",
                "filtername": "osType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_nam(self):
        test_os_type_data = ["NAM"]
        expected_return_data = [
            {
                "id": "60",
                "name": "NAM",
                "count": "0",
                "filterChecked": "true",
                "filtername": "osType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_scp(self):
        test_os_type_data = ["SCP"]
        expected_return_data = [
            {
                "id": "61",
                "name": "SCP",
                "count": "0",
                "filterChecked": "true",
                "filtername": "osType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_catos(self):
        test_os_type_data = ["CatOS"]
        expected_return_data = [
            {
                "id": "101",
                "name": "CatOS",
                "count": "0",
                "filterChecked": "true",
                "filtername": "osType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_epa(self):
        test_os_type_data = ["EPA"]
        expected_return_data = [
            {
                "id": "121",
                "name": "EPA",
                "count": "0",
                "filterChecked": "true",
                "filtername": "osType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_wlc(self):
        test_os_type_data = ["WLC"]
        expected_return_data = [
            {
                "id": "141",
                "name": "WLC",
                "count": "0",
                "filterChecked": "true",
                "filtername": "osType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_ios_xr_64(self):
        test_os_type_data = ["IOS XR 64 Bit"]
        expected_return_data = [
            {
                "id": "181",
                "name": "IOS XR 64 Bit",
                "count": "0",
                "filterChecked": "true",
                "filtername": "osType",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data


class TestTransceiverProductFamilyValidation:
    def test_transceiver_product_family_invalid_data(self):
        invalid_xcvr_data = ["asdfasdfasdf"]
        tmg = TMG.TMG()
        with pytest.raises(
            ValueError,
            match=r'Invalid Transceiver Product Families.*specified'.format(
                invalid_xcvr_data
            ),
        ):
            tmg._validate_transceiver_product_family(invalid_xcvr_data)

    def test_transceiver_product_family_ncs5500(self):
        test_xcvr_pf_data = ["NCS5500"]
        expected_return_data = [
            {
                "id": "41",
                "name": "NCS5500",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_sfp25g(self):
        test_xcvr_pf_data = ["SFP25G"]
        expected_return_data = [
            {
                "id": "1",
                "name": "SFP25G",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_sfpocx(self):
        test_xcvr_pf_data = ["SFPOCX"]
        expected_return_data = [
            {
                "id": "2",
                "name": "SFPOCX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_qsfp40g(self):
        test_xcvr_pf_data = ["QSFP40G"]
        expected_return_data = [
            {
                "id": "3",
                "name": "QSFP40G",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_qsfp100(self):
        test_xcvr_pf_data = ["QSFP100"]
        expected_return_data = [
            {
                "id": "5",
                "name": "QSFP100",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_sfpfe(self):
        test_xcvr_pf_data = ["SFPFE"]
        expected_return_data = [
            {
                "id": "8",
                "name": "SFPFE",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_wdm(self):
        test_xcvr_pf_data = ["WDM"]
        expected_return_data = [
            {
                "id": "10",
                "name": "WDM",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_sfpge(self):
        test_xcvr_pf_data = ["SFPGE"]
        expected_return_data = [
            {
                "id": "11",
                "name": "SFPGE",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_sfp10g(self):
        test_xcvr_pf_data = ["SFP10G"]
        expected_return_data = [
            {
                "id": "12",
                "name": "SFP10G",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_xenpak(self):
        test_xcvr_pf_data = ["XENPAK"]
        expected_return_data = [
            {
                "id": "13",
                "name": "XENPAK",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_x2(self):
        test_xcvr_pf_data = ["X2"]
        expected_return_data = [
            {
                "id": "14",
                "name": "X2",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_xfp(self):
        test_xcvr_pf_data = ["XFP"]
        expected_return_data = [
            {
                "id": "15",
                "name": "XFP",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_mds9000(self):
        test_xcvr_pf_data = ["MDS9000"]
        expected_return_data = [
            {
                "id": "21",
                "name": "MDS9000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data


class TestTransceiverProductIdValidation:
    def test_transceiver_product_id_invalid_data(self):
        invalid_xcvr_data = ["asdfasdfasdf"]
        tmg = TMG.TMG()
        with pytest.raises(
            ValueError,
            match=r'Invalid Transceiver Product IDs.*specified'.format(
                invalid_xcvr_data
            ),
        ):
            tmg._validate_transceiver_product_id(invalid_xcvr_data)

    def test_transceiver_product_id_qsfp_100g_sr4_s(self):
        test_xcvr_id_data = ["QSFP-100G-SR4-S"]
        expected_return_data = [
            {
                "id": "1",
                "name": "QSFP-100G-SR4-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_cwdm4_s(self):
        test_xcvr_id_data = ["QSFP-100G-CWDM4-S"]
        expected_return_data = [
            {
                "id": "2",
                "name": "QSFP-100G-CWDM4-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_psm4_s(self):
        test_xcvr_id_data = ["QSFP-100G-PSM4-S"]
        expected_return_data = [
            {
                "id": "3",
                "name": "QSFP-100G-PSM4-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_lr4_s(self):
        test_xcvr_id_data = ["QSFP-100G-LR4-S"]
        expected_return_data = [
            {
                "id": "4",
                "name": "QSFP-100G-LR4-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_sm_sr(self):
        test_xcvr_id_data = ["QSFP-100G-SM-SR"]
        expected_return_data = [
            {
                "id": "5",
                "name": "QSFP-100G-SM-SR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_er4l_s(self):
        test_xcvr_id_data = ["QSFP-100G-ER4L-S"]
        expected_return_data = [
            {
                "id": "6",
                "name": "QSFP-100G-ER4L-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40_100_srbd(self):
        test_xcvr_id_data = ["QSFP-40/100-SRBD"]
        expected_return_data = [
            {
                "id": "7",
                "name": "QSFP-40/100-SRBD",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_cu1m(self):
        test_xcvr_id_data = ["QSFP-100G-CU1M"]
        expected_return_data = [
            {
                "id": "10",
                "name": "QSFP-100G-CU1M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_cu2m(self):
        test_xcvr_id_data = ["QSFP-100G-CU2M"]
        expected_return_data = [
            {
                "id": "11",
                "name": "QSFP-100G-CU2M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_cu3m(self):
        test_xcvr_id_data = ["QSFP-100G-CU3M"]
        expected_return_data = [
            {
                "id": "12",
                "name": "QSFP-100G-CU3M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_cu5m(self):
        test_xcvr_id_data = ["QSFP-100G-CU5M"]
        expected_return_data = [
            {
                "id": "13",
                "name": "QSFP-100G-CU5M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp25g_cu1m(self):
        test_xcvr_id_data = ["QSFP-4SFP25G-CU1M"]
        expected_return_data = [
            {
                "id": "14",
                "name": "QSFP-4SFP25G-CU1M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp25g_cu2m(self):
        test_xcvr_id_data = ["QSFP-4SFP25G-CU2M"]
        expected_return_data = [
            {
                "id": "15",
                "name": "QSFP-4SFP25G-CU2M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp25g_cu3m(self):
        test_xcvr_id_data = ["QSFP-4SFP25G-CU3M"]
        expected_return_data = [
            {
                "id": "16",
                "name": "QSFP-4SFP25G-CU3M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp25g_cu5m(self):
        test_xcvr_id_data = ["QSFP-4SFP25G-CU5M"]
        expected_return_data = [
            {
                "id": "17",
                "name": "QSFP-4SFP25G-CU5M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc1m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC1M"]
        expected_return_data = [
            {
                "id": "18",
                "name": "QSFP-100G-AOC1M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc2m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC2M"]
        expected_return_data = [
            {
                "id": "19",
                "name": "QSFP-100G-AOC2M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc3m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC3M"]
        expected_return_data = [
            {
                "id": "20",
                "name": "QSFP-100G-AOC3M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc5m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC5M"]
        expected_return_data = [
            {
                "id": "21",
                "name": "QSFP-100G-AOC5M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc7m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC7M"]
        expected_return_data = [
            {
                "id": "22",
                "name": "QSFP-100G-AOC7M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc10m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC10M"]
        expected_return_data = [
            {
                "id": "23",
                "name": "QSFP-100G-AOC10M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc15m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC15M"]
        expected_return_data = [
            {
                "id": "24",
                "name": "QSFP-100G-AOC15M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc20m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC20M"]
        expected_return_data = [
            {
                "id": "25",
                "name": "QSFP-100G-AOC20M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc25m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC25M"]
        expected_return_data = [
            {
                "id": "26",
                "name": "QSFP-100G-AOC25M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc30m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC30M"]
        expected_return_data = [
            {
                "id": "27",
                "name": "QSFP-100G-AOC30M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cpak_100g_sr10(self):
        test_xcvr_id_data = ["CPAK-100G-SR10"]
        expected_return_data = [
            {
                "id": "31",
                "name": "CPAK-100G-SR10",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cpak_100g_er4l(self):
        test_xcvr_id_data = ["CPAK-100G-ER4L"]
        expected_return_data = [
            {
                "id": "32",
                "name": "CPAK-100G-ER4L",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cpak_100g_lr4(self):
        test_xcvr_id_data = ["CPAK-100G-LR4"]
        expected_return_data = [
            {
                "id": "33",
                "name": "CPAK-100G-LR4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cpak_10x10g_lr(self):
        test_xcvr_id_data = ["CPAK-10X10G-LR"]
        expected_return_data = [
            {
                "id": "34",
                "name": "CPAK-10X10G-LR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cpak_10x10g_erl(self):
        test_xcvr_id_data = ["CPAK-10X10G-ERL"]
        expected_return_data = [
            {
                "id": "35",
                "name": "CPAK-10X10G-ERL",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cpak_100g_sr4(self):
        test_xcvr_id_data = ["CPAK-100G-SR4"]
        expected_return_data = [
            {
                "id": "36",
                "name": "CPAK-100G-SR4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cpak_100g_cwdm4(self):
        test_xcvr_id_data = ["CPAK-100G-CWDM4"]
        expected_return_data = [
            {
                "id": "37",
                "name": "CPAK-100G-CWDM4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cpak_100g_psm4(self):
        test_xcvr_id_data = ["CPAK-100G-PSM4"]
        expected_return_data = [
            {
                "id": "38",
                "name": "CPAK-100G-PSM4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_fe_100fx(self):
        test_xcvr_id_data = ["GLC-FE-100FX"]
        expected_return_data = [
            {
                "id": "39",
                "name": "GLC-FE-100FX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_ge_100fx(self):
        test_xcvr_id_data = ["GLC-GE-100FX"]
        expected_return_data = [
            {
                "id": "40",
                "name": "GLC-GE-100FX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_fe_100lx(self):
        test_xcvr_id_data = ["GLC-FE-100LX"]
        expected_return_data = [
            {
                "id": "41",
                "name": "GLC-FE-100LX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_fe_100ex(self):
        test_xcvr_id_data = ["GLC-FE-100EX"]
        expected_return_data = [
            {
                "id": "42",
                "name": "GLC-FE-100EX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_fe_100zx(self):
        test_xcvr_id_data = ["GLC-FE-100ZX"]
        expected_return_data = [
            {
                "id": "43",
                "name": "GLC-FE-100ZX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_fe_100bx_d(self):
        test_xcvr_id_data = ["GLC-FE-100BX-D"]
        expected_return_data = [
            {
                "id": "44",
                "name": "GLC-FE-100BX-D",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_fe_100bx_u(self):
        test_xcvr_id_data = ["GLC-FE-100BX-U"]
        expected_return_data = [
            {
                "id": "45",
                "name": "GLC-FE-100BX-U",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_fe_t_i(self):
        test_xcvr_id_data = ["GLC-FE-T-I"]
        expected_return_data = [
            {
                "id": "46",
                "name": "GLC-FE-T-I",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_fe_100fx_rgd(self):
        test_xcvr_id_data = ["GLC-FE-100FX-RGD"]
        expected_return_data = [
            {
                "id": "47",
                "name": "GLC-FE-100FX-RGD",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_fe_100lx_rgd(self):
        test_xcvr_id_data = ["GLC-FE-100LX-RGD"]
        expected_return_data = [
            {
                "id": "48",
                "name": "GLC-FE-100LX-RGD",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc3_mm(self):
        test_xcvr_id_data = ["SFP-OC3-MM"]
        expected_return_data = [
            {
                "id": "49",
                "name": "SFP-OC3-MM",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc3_sr(self):
        test_xcvr_id_data = ["SFP-OC3-SR"]
        expected_return_data = [
            {
                "id": "50",
                "name": "SFP-OC3-SR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc3_ir1(self):
        test_xcvr_id_data = ["SFP-OC3-IR1"]
        expected_return_data = [
            {
                "id": "51",
                "name": "SFP-OC3-IR1",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc3_lr1(self):
        test_xcvr_id_data = ["SFP-OC3-LR1"]
        expected_return_data = [
            {
                "id": "52",
                "name": "SFP-OC3-LR1",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc3_lr2(self):
        test_xcvr_id_data = ["SFP-OC3-LR2"]
        expected_return_data = [
            {
                "id": "53",
                "name": "SFP-OC3-LR2",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc12_mm(self):
        test_xcvr_id_data = ["SFP-OC12-MM"]
        expected_return_data = [
            {
                "id": "54",
                "name": "SFP-OC12-MM",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc12_sr(self):
        test_xcvr_id_data = ["SFP-OC12-SR"]
        expected_return_data = [
            {
                "id": "55",
                "name": "SFP-OC12-SR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc12_ir1(self):
        test_xcvr_id_data = ["SFP-OC12-IR1"]
        expected_return_data = [
            {
                "id": "56",
                "name": "SFP-OC12-IR1",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc12_lr1(self):
        test_xcvr_id_data = ["SFP-OC12-LR1"]
        expected_return_data = [
            {
                "id": "57",
                "name": "SFP-OC12-LR1",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc12_lr2(self):
        test_xcvr_id_data = ["SFP-OC12-LR2"]
        expected_return_data = [
            {
                "id": "58",
                "name": "SFP-OC12-LR2",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc48_sr(self):
        test_xcvr_id_data = ["SFP-OC48-SR"]
        expected_return_data = [
            {
                "id": "59",
                "name": "SFP-OC48-SR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc48_ir1(self):
        test_xcvr_id_data = ["SFP-OC48-IR1"]
        expected_return_data = [
            {
                "id": "60",
                "name": "SFP-OC48-IR1",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc48_lr2(self):
        test_xcvr_id_data = ["SFP-OC48-LR2"]
        expected_return_data = [
            {
                "id": "61",
                "name": "SFP-OC48-LR2",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h25g_cu1m(self):
        test_xcvr_id_data = ["SFP-H25G-CU1M"]
        expected_return_data = [
            {
                "id": "62",
                "name": "SFP-H25G-CU1M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h25g_cu2m(self):
        test_xcvr_id_data = ["SFP-H25G-CU2M"]
        expected_return_data = [
            {
                "id": "63",
                "name": "SFP-H25G-CU2M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h25g_cu3m(self):
        test_xcvr_id_data = ["SFP-H25G-CU3M"]
        expected_return_data = [
            {
                "id": "64",
                "name": "SFP-H25G-CU3M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h25g_cu5m(self):
        test_xcvr_id_data = ["SFP-H25G-CU5M"]
        expected_return_data = [
            {
                "id": "65",
                "name": "SFP-H25G-CU5M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_25g_aoc1m(self):
        test_xcvr_id_data = ["SFP-25G-AOC1M"]
        expected_return_data = [
            {
                "id": "66",
                "name": "SFP-25G-AOC1M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_25g_aoc2m(self):
        test_xcvr_id_data = ["SFP-25G-AOC2M"]
        expected_return_data = [
            {
                "id": "67",
                "name": "SFP-25G-AOC2M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_25g_aoc3m(self):
        test_xcvr_id_data = ["SFP-25G-AOC3M"]
        expected_return_data = [
            {
                "id": "68",
                "name": "SFP-25G-AOC3M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_25g_aoc5m(self):
        test_xcvr_id_data = ["SFP-25G-AOC5M"]
        expected_return_data = [
            {
                "id": "69",
                "name": "SFP-25G-AOC5M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_25g_aoc7m(self):
        test_xcvr_id_data = ["SFP-25G-AOC7M"]
        expected_return_data = [
            {
                "id": "70",
                "name": "SFP-25G-AOC7M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_25g_aoc10m(self):
        test_xcvr_id_data = ["SFP-25G-AOC10M"]
        expected_return_data = [
            {
                "id": "71",
                "name": "SFP-25G-AOC10M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_25g_sr_s(self):
        test_xcvr_id_data = ["SFP-25G-SR-S"]
        expected_return_data = [
            {
                "id": "72",
                "name": "SFP-25G-SR-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_sr(self):
        test_xcvr_id_data = ["SFP-10G-SR"]
        expected_return_data = [
            {
                "id": "73",
                "name": "SFP-10G-SR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_sr_s(self):
        test_xcvr_id_data = ["SFP-10G-SR-S"]
        expected_return_data = [
            {
                "id": "74",
                "name": "SFP-10G-SR-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_sr_x(self):
        test_xcvr_id_data = ["SFP-10G-SR-X"]
        expected_return_data = [
            {
                "id": "75",
                "name": "SFP-10G-SR-X",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_lrm(self):
        test_xcvr_id_data = ["SFP-10G-LRM"]
        expected_return_data = [
            {
                "id": "76",
                "name": "SFP-10G-LRM",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_lr(self):
        test_xcvr_id_data = ["SFP-10G-LR"]
        expected_return_data = [
            {
                "id": "77",
                "name": "SFP-10G-LR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_lr_s(self):
        test_xcvr_id_data = ["SFP-10G-LR-S"]
        expected_return_data = [
            {
                "id": "78",
                "name": "SFP-10G-LR-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_lr_x(self):
        test_xcvr_id_data = ["SFP-10G-LR-X"]
        expected_return_data = [
            {
                "id": "79",
                "name": "SFP-10G-LR-X",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_er(self):
        test_xcvr_id_data = ["SFP-10G-ER"]
        expected_return_data = [
            {
                "id": "80",
                "name": "SFP-10G-ER",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_er_s(self):
        test_xcvr_id_data = ["SFP-10G-ER-S"]
        expected_return_data = [
            {
                "id": "81",
                "name": "SFP-10G-ER-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_zr(self):
        test_xcvr_id_data = ["SFP-10G-ZR"]
        expected_return_data = [
            {
                "id": "82",
                "name": "SFP-10G-ZR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_zr_s(self):
        test_xcvr_id_data = ["SFP-10G-ZR-S"]
        expected_return_data = [
            {
                "id": "83",
                "name": "SFP-10G-ZR-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_bxd_i(self):
        test_xcvr_id_data = ["SFP-10G-BXD-I"]
        expected_return_data = [
            {
                "id": "84",
                "name": "SFP-10G-BXD-I",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_bxu_i(self):
        test_xcvr_id_data = ["SFP-10G-BXU-I"]
        expected_return_data = [
            {
                "id": "85",
                "name": "SFP-10G-BXU-I",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_bx40d_i(self):
        test_xcvr_id_data = ["SFP-10G-BX40D-I"]
        expected_return_data = [
            {
                "id": "86",
                "name": "SFP-10G-BX40D-I",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_bx40u_i(self):
        test_xcvr_id_data = ["SFP-10G-BX40U-I"]
        expected_return_data = [
            {
                "id": "87",
                "name": "SFP-10G-BX40U-I",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h10gb_cu1m(self):
        test_xcvr_id_data = ["SFP-H10GB-CU1M"]
        expected_return_data = [
            {
                "id": "88",
                "name": "SFP-H10GB-CU1M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h10gb_cu3m(self):
        test_xcvr_id_data = ["SFP-H10GB-CU3M"]
        expected_return_data = [
            {
                "id": "89",
                "name": "SFP-H10GB-CU3M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h10gb_cu5m(self):
        test_xcvr_id_data = ["SFP-H10GB-CU5M"]
        expected_return_data = [
            {
                "id": "90",
                "name": "SFP-H10GB-CU5M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h10gb_acu7m(self):
        test_xcvr_id_data = ["SFP-H10GB-ACU7M"]
        expected_return_data = [
            {
                "id": "91",
                "name": "SFP-H10GB-ACU7M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h10gb_acu10m(self):
        test_xcvr_id_data = ["SFP-H10GB-ACU10M"]
        expected_return_data = [
            {
                "id": "92",
                "name": "SFP-H10GB-ACU10M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_aoc1m(self):
        test_xcvr_id_data = ["SFP-10G-AOC1M"]
        expected_return_data = [
            {
                "id": "93",
                "name": "SFP-10G-AOC1M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_aoc2m(self):
        test_xcvr_id_data = ["SFP-10G-AOC2M"]
        expected_return_data = [
            {
                "id": "94",
                "name": "SFP-10G-AOC2M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_aoc3m(self):
        test_xcvr_id_data = ["SFP-10G-AOC3M"]
        expected_return_data = [
            {
                "id": "95",
                "name": "SFP-10G-AOC3M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_aoc5m(self):
        test_xcvr_id_data = ["SFP-10G-AOC5M"]
        expected_return_data = [
            {
                "id": "96",
                "name": "SFP-10G-AOC5M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_aoc7m(self):
        test_xcvr_id_data = ["SFP-10G-AOC7M"]
        expected_return_data = [
            {
                "id": "97",
                "name": "SFP-10G-AOC7M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_aoc10m(self):
        test_xcvr_id_data = ["SFP-10G-AOC10M"]
        expected_return_data = [
            {
                "id": "98",
                "name": "SFP-10G-AOC10M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_fet_10g(self):
        test_xcvr_id_data = ["FET-10G"]
        expected_return_data = [
            {
                "id": "99",
                "name": "FET-10G",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp10g_61_41(self):
        test_xcvr_id_data = ["DWDM-SFP10G-61.41"]
        expected_return_data = [
            {
                "id": "100",
                "name": "DWDM-SFP10G-61.41",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp10g_xx_xx(self):
        test_xcvr_id_data = ["DWDM-SFP10G-XX.XX"]
        expected_return_data = [
            {
                "id": "101",
                "name": "DWDM-SFP10G-XX.XX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cwdm_sfp10g_xxxx(self):
        test_xcvr_id_data = ["CWDM-SFP10G-XXXX"]
        expected_return_data = [
            {
                "id": "102",
                "name": "CWDM-SFP10G-XXXX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_er(self):
        test_xcvr_id_data = ["XENPAK-10GB-ER"]
        expected_return_data = [
            {
                "id": "103",
                "name": "XENPAK-10GB-ER",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_erplus(self):
        test_xcvr_id_data = ["XENPAK-10GB-ER+"]
        expected_return_data = [
            {
                "id": "104",
                "name": "XENPAK-10GB-ER+",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_lr(self):
        test_xcvr_id_data = ["XENPAK-10GB-LR"]
        expected_return_data = [
            {
                "id": "105",
                "name": "XENPAK-10GB-LR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_lrplus(self):
        test_xcvr_id_data = ["XENPAK-10GB-LR+"]
        expected_return_data = [
            {
                "id": "106",
                "name": "XENPAK-10GB-LR+",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_lrm(self):
        test_xcvr_id_data = ["XENPAK-10GB-LRM"]
        expected_return_data = [
            {
                "id": "107",
                "name": "XENPAK-10GB-LRM",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_lw(self):
        test_xcvr_id_data = ["XENPAK-10GB-LW"]
        expected_return_data = [
            {
                "id": "108",
                "name": "XENPAK-10GB-LW",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_lx4(self):
        test_xcvr_id_data = ["XENPAK-10GB-LX4"]
        expected_return_data = [
            {
                "id": "109",
                "name": "XENPAK-10GB-LX4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_sr(self):
        test_xcvr_id_data = ["XENPAK-10GB-SR"]
        expected_return_data = [
            {
                "id": "110",
                "name": "XENPAK-10GB-SR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_cx4(self):
        test_xcvr_id_data = ["XENPAK-10GB-CX4"]
        expected_return_data = [
            {
                "id": "111",
                "name": "XENPAK-10GB-CX4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_zr(self):
        test_xcvr_id_data = ["XENPAK-10GB-ZR"]
        expected_return_data = [
            {
                "id": "112",
                "name": "XENPAK-10GB-ZR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_xenpak_xx_xx(self):
        test_xcvr_id_data = ["DWDM-XENPAK-XX.XX"]
        expected_return_data = [
            {
                "id": "113",
                "name": "DWDM-XENPAK-XX.XX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_x2_10gb_lr(self):
        test_xcvr_id_data = ["X2-10GB-LR"]
        expected_return_data = [
            {
                "id": "114",
                "name": "X2-10GB-LR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_x2_10gb_er(self):
        test_xcvr_id_data = ["X2-10GB-ER"]
        expected_return_data = [
            {
                "id": "115",
                "name": "X2-10GB-ER",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_x2_10gb_zr(self):
        test_xcvr_id_data = ["X2-10GB-ZR"]
        expected_return_data = [
            {
                "id": "116",
                "name": "X2-10GB-ZR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_x2_10gb_sr(self):
        test_xcvr_id_data = ["X2-10GB-SR"]
        expected_return_data = [
            {
                "id": "117",
                "name": "X2-10GB-SR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_x2_10gb_cx4(self):
        test_xcvr_id_data = ["X2-10GB-CX4"]
        expected_return_data = [
            {
                "id": "118",
                "name": "X2-10GB-CX4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_x2_10gb_lx4(self):
        test_xcvr_id_data = ["X2-10GB-LX4"]
        expected_return_data = [
            {
                "id": "119",
                "name": "X2-10GB-LX4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_x2_10gb_lrm(self):
        test_xcvr_id_data = ["X2-10GB-LRM"]
        expected_return_data = [
            {
                "id": "120",
                "name": "X2-10GB-LRM",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_x2_10gb_t(self):
        test_xcvr_id_data = ["X2-10GB-T"]
        expected_return_data = [
            {
                "id": "121",
                "name": "X2-10GB-T",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_x2_xx_xx(self):
        test_xcvr_id_data = ["DWDM-X2-XX.XX"]
        expected_return_data = [
            {
                "id": "122",
                "name": "DWDM-X2-XX.XX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp_10glr_oc192sr(self):
        test_xcvr_id_data = ["XFP-10GLR-OC192SR"]
        expected_return_data = [
            {
                "id": "123",
                "name": "XFP-10GLR-OC192SR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp10glr_192sr_l(self):
        test_xcvr_id_data = ["XFP10GLR-192SR-L"]
        expected_return_data = [
            {
                "id": "124",
                "name": "XFP10GLR-192SR-L",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp_10ger_oc192ir(self):
        test_xcvr_id_data = ["XFP-10GER-OC192IR"]
        expected_return_data = [
            {
                "id": "125",
                "name": "XFP-10GER-OC192IR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp_10ger_192irplus(self):
        test_xcvr_id_data = ["XFP-10GER-192IR+"]
        expected_return_data = [
            {
                "id": "126",
                "name": "XFP-10GER-192IR+",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp10ger_192ir_l(self):
        test_xcvr_id_data = ["XFP10GER-192IR-L"]
        expected_return_data = [
            {
                "id": "127",
                "name": "XFP10GER-192IR-L",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp_10gzr_oc192lr(self):
        test_xcvr_id_data = ["XFP-10GZR-OC192LR"]
        expected_return_data = [
            {
                "id": "128",
                "name": "XFP-10GZR-OC192LR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp_10g_mm_sr(self):
        test_xcvr_id_data = ["XFP-10G-MM-SR"]
        expected_return_data = [
            {
                "id": "129",
                "name": "XFP-10G-MM-SR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp10glr192sr_rgd(self):
        test_xcvr_id_data = ["XFP10GLR192SR-RGD"]
        expected_return_data = [
            {
                "id": "130",
                "name": "XFP10GLR192SR-RGD",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp10ger192ir_rgd(self):
        test_xcvr_id_data = ["XFP10GER192IR-RGD"]
        expected_return_data = [
            {
                "id": "131",
                "name": "XFP10GER192IR-RGD",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp10gzr192lr_rgd(self):
        test_xcvr_id_data = ["XFP10GZR192LR-RGD"]
        expected_return_data = [
            {
                "id": "132",
                "name": "XFP10GZR192LR-RGD",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_xfp_xx_xx(self):
        test_xcvr_id_data = ["DWDM-XFP-XX.XX"]
        expected_return_data = [
            {
                "id": "133",
                "name": "DWDM-XFP-XX.XX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_xfp_c(self):
        test_xcvr_id_data = ["DWDM-XFP-C"]
        expected_return_data = [
            {
                "id": "134",
                "name": "DWDM-XFP-C",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ws_g5483(self):
        test_xcvr_id_data = ["WS-G5483"]
        expected_return_data = [
            {
                "id": "135",
                "name": "WS-G5483",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ws_g5484(self):
        test_xcvr_id_data = ["WS-G5484"]
        expected_return_data = [
            {
                "id": "136",
                "name": "WS-G5484",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ws_g5486(self):
        test_xcvr_id_data = ["WS-G5486"]
        expected_return_data = [
            {
                "id": "137",
                "name": "WS-G5486",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ws_g5487(self):
        test_xcvr_id_data = ["WS-G5487"]
        expected_return_data = [
            {
                "id": "138",
                "name": "WS-G5487",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cwdm_gbic_xxxx(self):
        test_xcvr_id_data = ["CWDM-GBIC-XXXX"]
        expected_return_data = [
            {
                "id": "139",
                "name": "CWDM-GBIC-XXXX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_t(self):
        test_xcvr_id_data = ["GLC-T"]
        expected_return_data = [
            {
                "id": "140",
                "name": "GLC-T",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_te(self):
        test_xcvr_id_data = ["GLC-TE"]
        expected_return_data = [
            {
                "id": "141",
                "name": "GLC-TE",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_sx_mm(self):
        test_xcvr_id_data = ["GLC-SX-MM"]
        expected_return_data = [
            {
                "id": "142",
                "name": "GLC-SX-MM",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_lh_sm(self):
        test_xcvr_id_data = ["GLC-LH-SM"]
        expected_return_data = [
            {
                "id": "143",
                "name": "GLC-LH-SM",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_zx_sm(self):
        test_xcvr_id_data = ["GLC-ZX-SM"]
        expected_return_data = [
            {
                "id": "144",
                "name": "GLC-ZX-SM",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_bx_d(self):
        test_xcvr_id_data = ["GLC-BX-D"]
        expected_return_data = [
            {
                "id": "145",
                "name": "GLC-BX-D",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_bx_u(self):
        test_xcvr_id_data = ["GLC-BX-U"]
        expected_return_data = [
            {
                "id": "146",
                "name": "GLC-BX-U",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40g_sr4(self):
        test_xcvr_id_data = ["QSFP-40G-SR4"]
        expected_return_data = [
            {
                "id": "147",
                "name": "QSFP-40G-SR4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40g_csr4(self):
        test_xcvr_id_data = ["QSFP-40G-CSR4"]
        expected_return_data = [
            {
                "id": "148",
                "name": "QSFP-40G-CSR4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40g_sr4_s(self):
        test_xcvr_id_data = ["QSFP-40G-SR4-S"]
        expected_return_data = [
            {
                "id": "149",
                "name": "QSFP-40G-SR4-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_fet_40g(self):
        test_xcvr_id_data = ["FET-40G"]
        expected_return_data = [
            {
                "id": "150",
                "name": "FET-40G",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40g_sr_bd(self):
        test_xcvr_id_data = ["QSFP-40G-SR-BD"]
        expected_return_data = [
            {
                "id": "151",
                "name": "QSFP-40G-SR-BD",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_lr_s_capital(self):
        test_xcvr_id_data = ["QSFP-4X10G-LR-S"]
        expected_return_data = [
            {
                "id": "152",
                "name": "QSFP-4X10G-LR-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40g_lr4_s(self):
        test_xcvr_id_data = ["QSFP-40G-LR4-S"]
        expected_return_data = [
            {
                "id": "153",
                "name": "QSFP-40G-LR4-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40ge_lr4(self):
        test_xcvr_id_data = ["QSFP-40GE-LR4"]
        expected_return_data = [
            {
                "id": "154",
                "name": "QSFP-40GE-LR4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40g_lr4(self):
        test_xcvr_id_data = ["QSFP-40G-LR4"]
        expected_return_data = [
            {
                "id": "155",
                "name": "QSFP-40G-LR4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40g_er4(self):
        test_xcvr_id_data = ["QSFP-40G-ER4"]
        expected_return_data = [
            {
                "id": "156",
                "name": "QSFP-40G-ER4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_wsp_q40glr4l(self):
        test_xcvr_id_data = ["WSP-Q40GLR4L"]
        expected_return_data = [
            {
                "id": "157",
                "name": "WSP-Q40GLR4L",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp10g_cu5m(self):
        test_xcvr_id_data = ["QSFP-4SFP10G-CU5M"]
        expected_return_data = [
            {
                "id": "158",
                "name": "QSFP-4SFP10G-CU5M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp10g_cu3m(self):
        test_xcvr_id_data = ["QSFP-4SFP10G-CU3M"]
        expected_return_data = [
            {
                "id": "159",
                "name": "QSFP-4SFP10G-CU3M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp10g_cu1m(self):
        test_xcvr_id_data = ["QSFP-4SFP10G-CU1M"]
        expected_return_data = [
            {
                "id": "160",
                "name": "QSFP-4SFP10G-CU1M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_ac7m_capital(self):
        test_xcvr_id_data = ["QSFP-4X10G-AC7M"]
        expected_return_data = [
            {
                "id": "161",
                "name": "QSFP-4X10G-AC7M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_ac10m_capital(self):
        test_xcvr_id_data = ["QSFP-4X10G-AC10M"]
        expected_return_data = [
            {
                "id": "162",
                "name": "QSFP-4X10G-AC10M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_cu5m(self):
        test_xcvr_id_data = ["QSFP-H40G-CU5M"]
        expected_return_data = [
            {
                "id": "163",
                "name": "QSFP-H40G-CU5M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_cu3m(self):
        test_xcvr_id_data = ["QSFP-H40G-CU3M"]
        expected_return_data = [
            {
                "id": "164",
                "name": "QSFP-H40G-CU3M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_cu1m(self):
        test_xcvr_id_data = ["QSFP-H40G-CU1M"]
        expected_return_data = [
            {
                "id": "165",
                "name": "QSFP-H40G-CU1M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_acu7m(self):
        test_xcvr_id_data = ["QSFP-H40G-ACU7M"]
        expected_return_data = [
            {
                "id": "166",
                "name": "QSFP-H40G-ACU7M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_acu10m(self):
        test_xcvr_id_data = ["QSFP-H40G-ACU10M"]
        expected_return_data = [
            {
                "id": "167",
                "name": "QSFP-H40G-ACU10M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_aoc1m(self):
        test_xcvr_id_data = ["QSFP-4X10G-AOC1M"]
        expected_return_data = [
            {
                "id": "168",
                "name": "QSFP-4X10G-AOC1M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_aoc2m(self):
        test_xcvr_id_data = ["QSFP-4X10G-AOC2M"]
        expected_return_data = [
            {
                "id": "169",
                "name": "QSFP-4X10G-AOC2M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_aoc3m(self):
        test_xcvr_id_data = ["QSFP-4X10G-AOC3M"]
        expected_return_data = [
            {
                "id": "170",
                "name": "QSFP-4X10G-AOC3M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_aoc5m(self):
        test_xcvr_id_data = ["QSFP-4X10G-AOC5M"]
        expected_return_data = [
            {
                "id": "171",
                "name": "QSFP-4X10G-AOC5M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_aoc7m(self):
        test_xcvr_id_data = ["QSFP-4X10G-AOC7M"]
        expected_return_data = [
            {
                "id": "172",
                "name": "QSFP-4X10G-AOC7M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_aoc10m(self):
        test_xcvr_id_data = ["QSFP-4X10G-AOC10M"]
        expected_return_data = [
            {
                "id": "173",
                "name": "QSFP-4X10G-AOC10M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc1m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC1M"]
        expected_return_data = [
            {
                "id": "174",
                "name": "QSFP-H40G-AOC1M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc2m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC2M"]
        expected_return_data = [
            {
                "id": "175",
                "name": "QSFP-H40G-AOC2M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc3m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC3M"]
        expected_return_data = [
            {
                "id": "176",
                "name": "QSFP-H40G-AOC3M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc5m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC5M"]
        expected_return_data = [
            {
                "id": "177",
                "name": "QSFP-H40G-AOC5M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc7m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC7M"]
        expected_return_data = [
            {
                "id": "178",
                "name": "QSFP-H40G-AOC7M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc10m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC10M"]
        expected_return_data = [
            {
                "id": "179",
                "name": "QSFP-H40G-AOC10M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc15m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC15M"]
        expected_return_data = [
            {
                "id": "180",
                "name": "QSFP-H40G-AOC15M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc20m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC20M"]
        expected_return_data = [
            {
                "id": "181",
                "name": "QSFP-H40G-AOC20M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cvr_cfp_4sfp10g(self):
        test_xcvr_id_data = ["CVR-CFP-4SFP10G"]
        expected_return_data = [
            {
                "id": "183",
                "name": "CVR-CFP-4SFP10G",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cfp_40g_sr4(self):
        test_xcvr_id_data = ["CFP-40G-SR4"]
        expected_return_data = [
            {
                "id": "184",
                "name": "CFP-40G-SR4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cfp_40g_lr4(self):
        test_xcvr_id_data = ["CFP-40G-LR4"]
        expected_return_data = [
            {
                "id": "185",
                "name": "CFP-40G-LR4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_ac7m_lowercase(self):
        test_xcvr_id_data = ["QSFP-4x10G-AC7M"]
        expected_return_data = [
            {
                "id": "301",
                "name": "QSFP-4x10G-AC7M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_ac10m_lowercase(self):
        test_xcvr_id_data = ["QSFP-4x10G-AC10M"]
        expected_return_data = [
            {
                "id": "302",
                "name": "QSFP-4x10G-AC10M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_cu0_5m(self):
        test_xcvr_id_data = ["QSFP-H40G-CU0-5M"]
        expected_return_data = [
            {
                "id": "361",
                "name": "QSFP-H40G-CU0-5M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_cu2m(self):
        test_xcvr_id_data = ["QSFP-H40G-CU2M"]
        expected_return_data = [
            {
                "id": "362",
                "name": "QSFP-H40G-CU2M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_cu4m(self):
        test_xcvr_id_data = ["QSFP-H40G-CU4M"]
        expected_return_data = [
            {
                "id": "363",
                "name": "QSFP-H40G-CU4M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp10g_c_s(self):
        test_xcvr_id_data = ["DWDM-SFP10G-C-S"]
        expected_return_data = [
            {
                "id": "441",
                "name": "DWDM-SFP10G-C-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_sfp_1gb_lx10(self):
        test_xcvr_id_data = ["MA-SFP-1GB-LX10"]
        expected_return_data = [
            {
                "id": "621",
                "name": "MA-SFP-1GB-LX10",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_sfp_1gb_sx(self):
        test_xcvr_id_data = ["MA-SFP-1GB-SX"]
        expected_return_data = [
            {
                "id": "622",
                "name": "MA-SFP-1GB-SX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_sfp_1gb_tx(self):
        test_xcvr_id_data = ["MA-SFP-1GB-TX"]
        expected_return_data = [
            {
                "id": "623",
                "name": "MA-SFP-1GB-TX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_cbl_40g_1m(self):
        test_xcvr_id_data = ["MA-CBL-40G-1M"]
        expected_return_data = [
            {
                "id": "624",
                "name": "MA-CBL-40G-1M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_cbl_40g_3m(self):
        test_xcvr_id_data = ["MA-CBL-40G-3M"]
        expected_return_data = [
            {
                "id": "625",
                "name": "MA-CBL-40G-3M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_cbl_40g_50cm(self):
        test_xcvr_id_data = ["MA-CBL-40G-50CM"]
        expected_return_data = [
            {
                "id": "626",
                "name": "MA-CBL-40G-50CM",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_cbl_ta_1m(self):
        test_xcvr_id_data = ["MA-CBL-TA-1M"]
        expected_return_data = [
            {
                "id": "627",
                "name": "MA-CBL-TA-1M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_cbl_ta_3m(self):
        test_xcvr_id_data = ["MA-CBL-TA-3M"]
        expected_return_data = [
            {
                "id": "628",
                "name": "MA-CBL-TA-3M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_sfp_10gb_lr(self):
        test_xcvr_id_data = ["MA-SFP-10GB-LR"]
        expected_return_data = [
            {
                "id": "629",
                "name": "MA-SFP-10GB-LR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_sfp_10gb_lrm(self):
        test_xcvr_id_data = ["MA-SFP-10GB-LRM"]
        expected_return_data = [
            {
                "id": "630",
                "name": "MA-SFP-10GB-LRM",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_sfp_10gb_sr(self):
        test_xcvr_id_data = ["MA-SFP-10GB-SR"]
        expected_return_data = [
            {
                "id": "631",
                "name": "MA-SFP-10GB-SR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_cbl_100g_1m(self):
        test_xcvr_id_data = ["MA-CBL-100G-1M"]
        expected_return_data = [
            {
                "id": "632",
                "name": "MA-CBL-100G-1M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_cbl_100g_3m(self):
        test_xcvr_id_data = ["MA-CBL-100G-3M"]
        expected_return_data = [
            {
                "id": "633",
                "name": "MA-CBL-100G-3M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_cbl_100g_50cm(self):
        test_xcvr_id_data = ["MA-CBL-100G-50CM"]
        expected_return_data = [
            {
                "id": "634",
                "name": "MA-CBL-100G-50CM",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_qsfp_40g_csr4(self):
        test_xcvr_id_data = ["MA-QSFP-40G-CSR4"]
        expected_return_data = [
            {
                "id": "635",
                "name": "MA-QSFP-40G-CSR4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_qsfp_40g_lr4(self):
        test_xcvr_id_data = ["MA-QSFP-40G-LR4"]
        expected_return_data = [
            {
                "id": "636",
                "name": "MA-QSFP-40G-LR4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_qsfp_40g_sr4(self):
        test_xcvr_id_data = ["MA-QSFP-40G-SR4"]
        expected_return_data = [
            {
                "id": "637",
                "name": "MA-QSFP-40G-SR4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_qsfp_40g_sr_bd(self):
        test_xcvr_id_data = ["MA-QSFP-40G-SR-BD"]
        expected_return_data = [
            {
                "id": "638",
                "name": "MA-QSFP-40G-SR-BD",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_qsfp_100g_lr4(self):
        test_xcvr_id_data = ["MA-QSFP-100G-LR4"]
        expected_return_data = [
            {
                "id": "639",
                "name": "MA-QSFP-100G-LR4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_qsfp_100g_sr4(self):
        test_xcvr_id_data = ["MA-QSFP-100G-SR4"]
        expected_return_data = [
            {
                "id": "640",
                "name": "MA-QSFP-100G-SR4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_aoc15m(self):
        test_xcvr_id_data = ["QSFP-4X10G-AOC15M"]
        expected_return_data = [
            {
                "id": "281",
                "name": "QSFP-4X10G-AOC15M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_lr_s_lowercase(self):
        test_xcvr_id_data = ["QSFP-4x10G-LR-S"]
        expected_return_data = [
            {
                "id": "401",
                "name": "QSFP-4x10G-LR-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10_25g_lr_s(self):
        test_xcvr_id_data = ["SFP-10/25G-LR-S"]
        expected_return_data = [
            {
                "id": "402",
                "name": "SFP-10/25G-LR-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cvr_4sfp10g_qsfp(self):
        test_xcvr_id_data = ["CVR-4SFP10G-QSFP"]
        expected_return_data = [
            {
                "id": "421",
                "name": "CVR-4SFP10G-QSFP",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40g_csr_s(self):
        test_xcvr_id_data = ["QSFP-40G-CSR-S"]
        expected_return_data = [
            {
                "id": "481",
                "name": "QSFP-40G-CSR-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp_3268(self):
        test_xcvr_id_data = ["DWDM-SFP-3268"]
        expected_return_data = [
            {
                "id": "581",
                "name": "DWDM-SFP-3268",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp_3190(self):
        test_xcvr_id_data = ["DWDM-SFP-3190"]
        expected_return_data = [
            {
                "id": "582",
                "name": "DWDM-SFP-3190",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp_3112(self):
        test_xcvr_id_data = ["DWDM-SFP-3112"]
        expected_return_data = [
            {
                "id": "583",
                "name": "DWDM-SFP-3112",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp_3033(self):
        test_xcvr_id_data = ["DWDM-SFP-3033"]
        expected_return_data = [
            {
                "id": "584",
                "name": "DWDM-SFP-3033",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cwdm_sfp_1470(self):
        test_xcvr_id_data = ["CWDM-SFP-1470"]
        expected_return_data = [
            {
                "id": "601",
                "name": "CWDM-SFP-1470",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cwdm_sfp_1610(self):
        test_xcvr_id_data = ["CWDM-SFP-1610"]
        expected_return_data = [
            {
                "id": "602",
                "name": "CWDM-SFP-1610",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_bx_d_i(self):
        test_xcvr_id_data = ["GLC-BX-D-I"]
        expected_return_data = [
            {
                "id": "641",
                "name": "GLC-BX-D-I",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_bx_u_i(self):
        test_xcvr_id_data = ["GLC-BX-U-I"]
        expected_return_data = [
            {
                "id": "642",
                "name": "GLC-BX-U-I",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_bx40_d_i(self):
        test_xcvr_id_data = ["GLC-BX40-D-I"]
        expected_return_data = [
            {
                "id": "187",
                "name": "GLC-BX40-D-I",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_bx40_u_i(self):
        test_xcvr_id_data = ["GLC-BX40-U-I"]
        expected_return_data = [
            {
                "id": "188",
                "name": "GLC-BX40-U-I",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_bx80_d_i(self):
        test_xcvr_id_data = ["GLC-BX80-D-I"]
        expected_return_data = [
            {
                "id": "189",
                "name": "GLC-BX80-D-I",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_bx80_u_i(self):
        test_xcvr_id_data = ["GLC-BX80-U-I"]
        expected_return_data = [
            {
                "id": "190",
                "name": "GLC-BX80-U-I",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_bx40_da_i(self):
        test_xcvr_id_data = ["GLC-BX40-DA-I"]
        expected_return_data = [
            {
                "id": "191",
                "name": "GLC-BX40-DA-I",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_2bx_d(self):
        test_xcvr_id_data = ["GLC-2BX-D"]
        expected_return_data = [
            {
                "id": "192",
                "name": "GLC-2BX-D",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_ge_s(self):
        test_xcvr_id_data = ["SFP-GE-S"]
        expected_return_data = [
            {
                "id": "193",
                "name": "SFP-GE-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_ge_l(self):
        test_xcvr_id_data = ["SFP-GE-L"]
        expected_return_data = [
            {
                "id": "194",
                "name": "SFP-GE-L",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_ex_smd(self):
        test_xcvr_id_data = ["GLC-EX-SMD"]
        expected_return_data = [
            {
                "id": "195",
                "name": "GLC-EX-SMD",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_ge_z(self):
        test_xcvr_id_data = ["SFP-GE-Z"]
        expected_return_data = [
            {
                "id": "196",
                "name": "SFP-GE-Z",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_ge_t(self):
        test_xcvr_id_data = ["SFP-GE-T"]
        expected_return_data = [
            {
                "id": "197",
                "name": "SFP-GE-T",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_sx_mm_rgd(self):
        test_xcvr_id_data = ["GLC-SX-MM-RGD"]
        expected_return_data = [
            {
                "id": "198",
                "name": "GLC-SX-MM-RGD",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_lx_sm_rgd(self):
        test_xcvr_id_data = ["GLC-LX-SM-RGD"]
        expected_return_data = [
            {
                "id": "199",
                "name": "GLC-LX-SM-RGD",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_zx_sm_rgd(self):
        test_xcvr_id_data = ["GLC-ZX-SM-RGD"]
        expected_return_data = [
            {
                "id": "200",
                "name": "GLC-ZX-SM-RGD",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_sx_mmd(self):
        test_xcvr_id_data = ["GLC-SX-MMD"]
        expected_return_data = [
            {
                "id": "201",
                "name": "GLC-SX-MMD",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_lh_smd(self):
        test_xcvr_id_data = ["GLC-LH-SMD"]
        expected_return_data = [
            {
                "id": "202",
                "name": "GLC-LH-SMD",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_zx_smd(self):
        test_xcvr_id_data = ["GLC-ZX-SMD"]
        expected_return_data = [
            {
                "id": "203",
                "name": "GLC-ZX-SMD",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_gpon_b(self):
        test_xcvr_id_data = ["SFP-GPON-B"]
        expected_return_data = [
            {
                "id": "204",
                "name": "SFP-GPON-B",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_gpon_b_i(self):
        test_xcvr_id_data = ["SFP-GPON-B-I"]
        expected_return_data = [
            {
                "id": "205",
                "name": "SFP-GPON-B-I",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_gpon_c(self):
        test_xcvr_id_data = ["SFP-GPON-C"]
        expected_return_data = [
            {
                "id": "206",
                "name": "SFP-GPON-C",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_gpon_c_i(self):
        test_xcvr_id_data = ["SFP-GPON-C-I"]
        expected_return_data = [
            {
                "id": "207",
                "name": "SFP-GPON-C-I",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cwdm_sfp_xxxx(self):
        test_xcvr_id_data = ["CWDM-SFP-XXXX"]
        expected_return_data = [
            {
                "id": "208",
                "name": "CWDM-SFP-XXXX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp_xxxx(self):
        test_xcvr_id_data = ["DWDM-SFP-XXXX"]
        expected_return_data = [
            {
                "id": "209",
                "name": "DWDM-SFP-XXXX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40g_bd_rx(self):
        test_xcvr_id_data = ["QSFP-40G-BD-RX"]
        expected_return_data = [
            {
                "id": "210",
                "name": "QSFP-40G-BD-RX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc25m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC25M"]
        expected_return_data = [
            {
                "id": "211",
                "name": "QSFP-H40G-AOC25M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc30m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC30M"]
        expected_return_data = [
            {
                "id": "212",
                "name": "QSFP-H40G-AOC30M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cpak_100ge_lr4(self):
        test_xcvr_id_data = ["CPAK-100GE-LR4"]
        expected_return_data = [
            {
                "id": "213",
                "name": "CPAK-100GE-LR4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cxp_100g_sr10(self):
        test_xcvr_id_data = ["CXP-100G-SR10"]
        expected_return_data = [
            {
                "id": "214",
                "name": "CXP-100G-SR10",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cxp_100g_sr12(self):
        test_xcvr_id_data = ["CXP-100G-SR12"]
        expected_return_data = [
            {
                "id": "215",
                "name": "CXP-100G-SR12",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cfp2_100g_er4(self):
        test_xcvr_id_data = ["CFP2-100G-ER4"]
        expected_return_data = [
            {
                "id": "216",
                "name": "CFP2-100G-ER4",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp10g_usr(self):
        test_xcvr_id_data = ["SFP10G-USR"]
        expected_return_data = [
            {
                "id": "217",
                "name": "SFP10G-USR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h10gb_cu1_5m(self):
        test_xcvr_id_data = ["SFP-H10GB-CU1-5M"]
        expected_return_data = [
            {
                "id": "218",
                "name": "SFP-H10GB-CU1-5M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h10gb_cu2m(self):
        test_xcvr_id_data = ["SFP-H10GB-CU2M"]
        expected_return_data = [
            {
                "id": "219",
                "name": "SFP-H10GB-CU2M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h10gb_cu2_5m(self):
        test_xcvr_id_data = ["SFP-H10GB-CU2-5M"]
        expected_return_data = [
            {
                "id": "220",
                "name": "SFP-H10GB-CU2-5M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_ge_dr_lx(self):
        test_xcvr_id_data = ["GLC-GE-DR-LX"]
        expected_return_data = [
            {
                "id": "221",
                "name": "GLC-GE-DR-LX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp10g_30_33(self):
        test_xcvr_id_data = ["DWDM-SFP10G-30.33"]
        expected_return_data = [
            {
                "id": "222",
                "name": "DWDM-SFP10G-30.33",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp10g_c(self):
        test_xcvr_id_data = ["DWDM-SFP10G-C"]
        expected_return_data = [
            {
                "id": "223",
                "name": "DWDM-SFP10G-C",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10_25g_csr_s(self):
        test_xcvr_id_data = ["SFP-10/25G-CSR-S"]
        expected_return_data = [
            {
                "id": "321",
                "name": "SFP-10/25G-CSR-S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cwdm_sfp10g_1530(self):
        test_xcvr_id_data = ["CWDM-SFP10G-1530"]
        expected_return_data = [
            {
                "id": "521",
                "name": "CWDM-SFP10G-1530",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h10gb_cu4m(self):
        test_xcvr_id_data = ["SFP-H10GB-CU4M"]
        expected_return_data = [
            {
                "id": "541",
                "name": "SFP-H10GB-CU4M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ds_sfp_fc8g_sw(self):
        test_xcvr_id_data = ["DS-SFP-FC8G-SW"]
        expected_return_data = [
            {
                "id": "561",
                "name": "DS-SFP-FC8G-SW",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ds_sfp_fc16g_sw(self):
        test_xcvr_id_data = ["DS-SFP-FC16G-SW"]
        expected_return_data = [
            {
                "id": "562",
                "name": "DS-SFP-FC16G-SW",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ds_sfp_fc32g_sw(self):
        test_xcvr_id_data = ["DS-SFP-FC32G-SW"]
        expected_return_data = [
            {
                "id": "563",
                "name": "DS-SFP-FC32G-SW",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cfp2_wdm_det_1hl(self):
        test_xcvr_id_data = ["CFP2-WDM-DET-1HL"]
        expected_return_data = [
            {
                "id": "661",
                "name": "CFP2-WDM-DET-1HL",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cfp2_wdm_d_1hl(self):
        test_xcvr_id_data = ["CFP2-WDM-D-1HL"]
        expected_return_data = [
            {
                "id": "662",
                "name": "CFP2-WDM-D-1HL",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_25g_aoc4m(self):
        test_xcvr_id_data = ["SFP-25G-AOC4M"]
        expected_return_data = [
            {
                "id": "461",
                "name": "SFP-25G-AOC4M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp10g_cu2m(self):
        test_xcvr_id_data = ["QSFP-4SFP10G-CU2M"]
        expected_return_data = [
            {
                "id": "241",
                "name": "QSFP-4SFP10G-CU2M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp10g_cu4m(self):
        test_xcvr_id_data = ["QSFP-4SFP10G-CU4M"]
        expected_return_data = [
            {
                "id": "242",
                "name": "QSFP-4SFP10G-CU4M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp10g_cu0_5m(self):
        test_xcvr_id_data = ["QSFP-4SFP10G-CU0-5M"]
        expected_return_data = [
            {
                "id": "502",
                "name": "QSFP-4SFP10G-CU0-5M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "transceiverProductID",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data


class TestNetworkDeviceProductFamilyValidation:
    def test_network_device_product_family_invalid_data(self):
        invalid_device_data = ["asdfasdfasdf"]
        tmg = TMG.TMG()
        with pytest.raises(
            ValueError,
            match=r'Invalid Network Device Product Families.*specified'.format(
                invalid_device_data
            ),
        ):
            tmg._validate_network_device_product_family(invalid_device_data)

    def test_network_device_product_family_c2960p(self):
        test_device_pf_data = ["C2960P"]
        expected_return_data = [
            {
                "id": "1",
                "name": "C2960P",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2960s(self):
        test_device_pf_data = ["C2960S"]
        expected_return_data = [
            {
                "id": "2",
                "name": "C2960S",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2960sf(self):
        test_device_pf_data = ["C2960SF"]
        expected_return_data = [
            {
                "id": "3",
                "name": "C2960SF",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2960c(self):
        test_device_pf_data = ["C2960C"]
        expected_return_data = [
            {
                "id": "4",
                "name": "C2960C",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2960x(self):
        test_device_pf_data = ["C2960X"]
        expected_return_data = [
            {
                "id": "5",
                "name": "C2960X",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2960xr(self):
        test_device_pf_data = ["C2960XR"]
        expected_return_data = [
            {
                "id": "6",
                "name": "C2960XR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c9400(self):
        test_device_pf_data = ["C9400"]
        expected_return_data = [
            {
                "id": "7",
                "name": "C9400",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c9500(self):
        test_device_pf_data = ["C9500"]
        expected_return_data = [
            {
                "id": "8",
                "name": "C9500",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n3500(self):
        test_device_pf_data = ["N3500"]
        expected_return_data = [
            {
                "id": "9",
                "name": "N3500",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n2000(self):
        test_device_pf_data = ["N2000"]
        expected_return_data = [
            {
                "id": "10",
                "name": "N2000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n5000(self):
        test_device_pf_data = ["N5000"]
        expected_return_data = [
            {
                "id": "11",
                "name": "N5000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n6000(self):
        test_device_pf_data = ["N6000"]
        expected_return_data = [
            {
                "id": "12",
                "name": "N6000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n7000(self):
        test_device_pf_data = ["N7000"]
        expected_return_data = [
            {
                "id": "13",
                "name": "N7000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ucsb(self):
        test_device_pf_data = ["UCSB"]
        expected_return_data = [
            {
                "id": "14",
                "name": "UCSB",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ucsc(self):
        test_device_pf_data = ["UCSC"]
        expected_return_data = [
            {
                "id": "15",
                "name": "UCSC",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_crs(self):
        test_device_pf_data = ["CRS"]
        expected_return_data = [
            {
                "id": "16",
                "name": "CRS",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ncs1000(self):
        test_device_pf_data = ["NCS1000"]
        expected_return_data = [
            {
                "id": "17",
                "name": "NCS1000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ncs5000(self):
        test_device_pf_data = ["NCS5000"]
        expected_return_data = [
            {
                "id": "19",
                "name": "NCS5000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ncs5500(self):
        test_device_pf_data = ["NCS5500"]
        expected_return_data = [
            {
                "id": "20",
                "name": "NCS5500",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ncs6000(self):
        test_device_pf_data = ["NCS6000"]
        expected_return_data = [
            {
                "id": "21",
                "name": "NCS6000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_fprhigh(self):
        test_device_pf_data = ["FPRHIGH"]
        expected_return_data = [
            {
                "id": "22",
                "name": "FPRHIGH",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_fpruhi(self):
        test_device_pf_data = ["FPRUHI"]
        expected_return_data = [
            {
                "id": "23",
                "name": "FPRUHI",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ncs4000(self):
        test_device_pf_data = ["NCS4000"]
        expected_return_data = [
            {
                "id": "24",
                "name": "NCS4000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ce500(self):
        test_device_pf_data = ["CE500"]
        expected_return_data = [
            {
                "id": "25",
                "name": "CE500",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ce520(self):
        test_device_pf_data = ["CE520"]
        expected_return_data = [
            {
                "id": "26",
                "name": "CE520",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_me2400(self):
        test_device_pf_data = ["ME2400"]
        expected_return_data = [
            {
                "id": "27",
                "name": "ME2400",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_me3750(self):
        test_device_pf_data = ["ME3750"]
        expected_return_data = [
            {
                "id": "28",
                "name": "ME3750",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c4ktor(self):
        test_device_pf_data = ["C4KTOR"]
        expected_return_data = [
            {
                "id": "29",
                "name": "C4KTOR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_l3fixed(self):
        test_device_pf_data = ["L3FIXED"]
        expected_return_data = [
            {
                "id": "30",
                "name": "L3FIXED",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2900(self):
        test_device_pf_data = ["C2900"]
        expected_return_data = [
            {
                "id": "31",
                "name": "C2900",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_dsbuoth(self):
        test_device_pf_data = ["DSBUOTH"]
        expected_return_data = [
            {
                "id": "32",
                "name": "DSBUOTH",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2940(self):
        test_device_pf_data = ["C2940"]
        expected_return_data = [
            {
                "id": "33",
                "name": "C2940",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2950(self):
        test_device_pf_data = ["C2950"]
        expected_return_data = [
            {
                "id": "34",
                "name": "C2950",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2960l(self):
        test_device_pf_data = ["C2960L"]
        expected_return_data = [
            {
                "id": "35",
                "name": "C2960L",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2960cx(self):
        test_device_pf_data = ["C2960CX"]
        expected_return_data = [
            {
                "id": "36",
                "name": "C2960CX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2970(self):
        test_device_pf_data = ["C2970"]
        expected_return_data = [
            {
                "id": "37",
                "name": "C2970",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2975(self):
        test_device_pf_data = ["C2975"]
        expected_return_data = [
            {
                "id": "38",
                "name": "C2975",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c3550(self):
        test_device_pf_data = ["C3550"]
        expected_return_data = [
            {
                "id": "39",
                "name": "C3550",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c3560cx(self):
        test_device_pf_data = ["C3560CX"]
        expected_return_data = [
            {
                "id": "40",
                "name": "C3560CX",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c4000(self):
        test_device_pf_data = ["C4000"]
        expected_return_data = [
            {
                "id": "41",
                "name": "C4000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c6500(self):
        test_device_pf_data = ["C6500"]
        expected_return_data = [
            {
                "id": "42",
                "name": "C6500",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c6800(self):
        test_device_pf_data = ["C6800"]
        expected_return_data = [
            {
                "id": "44",
                "name": "C6800",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2350(self):
        test_device_pf_data = ["C2350"]
        expected_return_data = [
            {
                "id": "45",
                "name": "C2350",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2360(self):
        test_device_pf_data = ["C2360"]
        expected_return_data = [
            {
                "id": "46",
                "name": "C2360",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_os(self):
        test_device_pf_data = ["OS"]
        expected_return_data = [
            {
                "id": "47",
                "name": "OS",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n4000(self):
        test_device_pf_data = ["N4000"]
        expected_return_data = [
            {
                "id": "48",
                "name": "N4000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_css(self):
        test_device_pf_data = ["CSS"]
        expected_return_data = [
            {
                "id": "49",
                "name": "CSS",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_erbuold(self):
        test_device_pf_data = ["ERBUOLD"]
        expected_return_data = [
            {
                "id": "55",
                "name": "ERBUOLD",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ubr7200(self):
        test_device_pf_data = ["UBR7200"]
        expected_return_data = [
            {
                "id": "56",
                "name": "UBR7200",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_7300(self):
        test_device_pf_data = ["7300"]
        expected_return_data = [
            {
                "id": "57",
                "name": "7300",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_7304(self):
        test_device_pf_data = ["7304"]
        expected_return_data = [
            {
                "id": "58",
                "name": "7304",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_7500(self):
        test_device_pf_data = ["7500"]
        expected_return_data = [
            {
                "id": "59",
                "name": "7500",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_esr(self):
        test_device_pf_data = ["ESR"]
        expected_return_data = [
            {
                "id": "60",
                "name": "ESR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ubr10k(self):
        test_device_pf_data = ["UBR10K"]
        expected_return_data = [
            {
                "id": "61",
                "name": "UBR10K",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_rfgw10(self):
        test_device_pf_data = ["RFGW10"]
        expected_return_data = [
            {
                "id": "62",
                "name": "RFGW10",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_gsr(self):
        test_device_pf_data = ["GSR"]
        expected_return_data = [
            {
                "id": "63",
                "name": "GSR",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_asr900(self):
        test_device_pf_data = ["ASR900"]
        expected_return_data = [
            {
                "id": "64",
                "name": "ASR900",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_rantran(self):
        test_device_pf_data = ["RANTRAN"]
        expected_return_data = [
            {
                "id": "65",
                "name": "RANTRAN",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_asamid(self):
        test_device_pf_data = ["ASAMID"]
        expected_return_data = [
            {
                "id": "66",
                "name": "ASAMID",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_embunam(self):
        test_device_pf_data = ["EMBUNAM"]
        expected_return_data = [
            {
                "id": "67",
                "name": "EMBUNAM",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_airctu(self):
        test_device_pf_data = ["AIRCTU"]
        expected_return_data = [
            {
                "id": "68",
                "name": "AIRCTU",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_fprmid(self):
        test_device_pf_data = ["FPRMID"]
        expected_return_data = [
            {
                "id": "69",
                "name": "FPRMID",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_scp(self):
        test_device_pf_data = ["SCP"]
        expected_return_data = [
            {
                "id": "70",
                "name": "SCP",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n9000(self):
        test_device_pf_data = ["N9000"]
        expected_return_data = [
            {
                "id": "71",
                "name": "N9000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c4900(self):
        test_device_pf_data = ["C4900"]
        expected_return_data = [
            {
                "id": "72",
                "name": "C4900",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c4900m(self):
        test_device_pf_data = ["C4900M"]
        expected_return_data = [
            {
                "id": "73",
                "name": "C4900M",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ncs540(self):
        test_device_pf_data = ["NCS540"]
        expected_return_data = [
            {
                "id": "121",
                "name": "NCS540",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ncs560(self):
        test_device_pf_data = ["NCS560"]
        expected_return_data = [
            {
                "id": "141",
                "name": "NCS560",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_isr3900(self):
        test_device_pf_data = ["ISR3900"]
        expected_return_data = [
            {
                "id": "181",
                "name": "ISR3900",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_isr4000(self):
        test_device_pf_data = ["ISR4000"]
        expected_return_data = [
            {
                "id": "182",
                "name": "ISR4000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_isr2900(self):
        test_device_pf_data = ["ISR2900"]
        expected_return_data = [
            {
                "id": "183",
                "name": "ISR2900",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_aircti2(self):
        test_device_pf_data = ["AIRCTI2"]
        expected_return_data = [
            {
                "id": "241",
                "name": "AIRCTI2",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_asahigh(self):
        test_device_pf_data = ["ASAHIGH"]
        expected_return_data = [
            {
                "id": "261",
                "name": "ASAHIGH",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c9200(self):
        test_device_pf_data = ["C9200"]
        expected_return_data = [
            {
                "id": "341",
                "name": "C9200",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c9200l(self):
        test_device_pf_data = ["C9200L"]
        expected_return_data = [
            {
                "id": "342",
                "name": "C9200L",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_cbr8(self):
        test_device_pf_data = ["CBR8"]
        expected_return_data = [
            {
                "id": "161",
                "name": "CBR8",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_isr800(self):
        test_device_pf_data = ["ISR800"]
        expected_return_data = [
            {
                "id": "421",
                "name": "ISR800",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c9600(self):
        test_device_pf_data = ["C9600"]
        expected_return_data = [
            {
                "id": "521",
                "name": "C9600",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ms120_series(self):
        test_device_pf_data = ["MS120 Series"]
        expected_return_data = [
            {
                "id": "541",
                "name": "MS120 Series",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ms210_series(self):
        test_device_pf_data = ["MS210 Series"]
        expected_return_data = [
            {
                "id": "542",
                "name": "MS210 Series",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ms225_series(self):
        test_device_pf_data = ["MS225 Series"]
        expected_return_data = [
            {
                "id": "543",
                "name": "MS225 Series",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ms250_series(self):
        test_device_pf_data = ["MS250 Series"]
        expected_return_data = [
            {
                "id": "544",
                "name": "MS250 Series",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ms350_series(self):
        test_device_pf_data = ["MS350 Series"]
        expected_return_data = [
            {
                "id": "545",
                "name": "MS350 Series",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ms355_series(self):
        test_device_pf_data = ["MS355 Series"]
        expected_return_data = [
            {
                "id": "546",
                "name": "MS355 Series",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ms410_series(self):
        test_device_pf_data = ["MS410 Series"]
        expected_return_data = [
            {
                "id": "547",
                "name": "MS410 Series",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ms425_series(self):
        test_device_pf_data = ["MS425 Series"]
        expected_return_data = [
            {
                "id": "548",
                "name": "MS425 Series",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_mx84(self):
        test_device_pf_data = ["MX84"]
        expected_return_data = [
            {
                "id": "550",
                "name": "MX84",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_mx100(self):
        test_device_pf_data = ["MX100"]
        expected_return_data = [
            {
                "id": "551",
                "name": "MX100",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_mx250(self):
        test_device_pf_data = ["MX250"]
        expected_return_data = [
            {
                "id": "552",
                "name": "MX250",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_mx400(self):
        test_device_pf_data = ["MX400"]
        expected_return_data = [
            {
                "id": "553",
                "name": "MX400",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_mx450(self):
        test_device_pf_data = ["MX450"]
        expected_return_data = [
            {
                "id": "554",
                "name": "MX450",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_mx600(self):
        test_device_pf_data = ["MX600"]
        expected_return_data = [
            {
                "id": "555",
                "name": "MX600",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ms450_series(self):
        test_device_pf_data = ["MS450 Series"]
        expected_return_data = [
            {
                "id": "561",
                "name": "MS450 Series",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c9300l(self):
        test_device_pf_data = ["C9300L"]
        expected_return_data = [
            {
                "id": "601",
                "name": "C9300L",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_me1200(self):
        test_device_pf_data = ["ME1200"]
        expected_return_data = [
            {
                "id": "641",
                "name": "ME1200",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c9800(self):
        test_device_pf_data = ["C9800"]
        expected_return_data = [
            {
                "id": "681",
                "name": "C9800",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_rphyshf(self):
        test_device_pf_data = ["RPHYSHF"]
        expected_return_data = [
            {
                "id": "701",
                "name": "RPHYSHF",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ie3200(self):
        test_device_pf_data = ["IE3200"]
        expected_return_data = [
            {
                "id": "721",
                "name": "IE3200",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ie3300(self):
        test_device_pf_data = ["IE3300"]
        expected_return_data = [
            {
                "id": "722",
                "name": "IE3300",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ie3400(self):
        test_device_pf_data = ["IE3400"]
        expected_return_data = [
            {
                "id": "723",
                "name": "IE3400",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n9300(self):
        test_device_pf_data = ["N9300"]
        expected_return_data = [
            {
                "id": "74",
                "name": "N9300",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n3000(self):
        test_device_pf_data = ["N3000"]
        expected_return_data = [
            {
                "id": "75",
                "name": "N3000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c9300(self):
        test_device_pf_data = ["C9300"]
        expected_return_data = [
            {
                "id": "76",
                "name": "C9300",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n9500(self):
        test_device_pf_data = ["N9500"]
        expected_return_data = [
            {
                "id": "77",
                "name": "N9500",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n9200(self):
        test_device_pf_data = ["N9200"]
        expected_return_data = [
            {
                "id": "78",
                "name": "N9200",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ipacces(self):
        test_device_pf_data = ["IPACCES"]
        expected_return_data = [
            {
                "id": "79",
                "name": "IPACCES",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_wanlan(self):
        test_device_pf_data = ["WANLAN"]
        expected_return_data = [
            {
                "id": "82",
                "name": "WANLAN",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_asr9000(self):
        test_device_pf_data = ["ASR9000"]
        expected_return_data = [
            {
                "id": "83",
                "name": "ASR9000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_800bb(self):
        test_device_pf_data = ["800BB"]
        expected_return_data = [
            {
                "id": "84",
                "name": "800BB",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c6000(self):
        test_device_pf_data = ["C6000"]
        expected_return_data = [
            {
                "id": "88",
                "name": "C6000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_7600(self):
        test_device_pf_data = ["7600"]
        expected_return_data = [
            {
                "id": "89",
                "name": "7600",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_asr1000(self):
        test_device_pf_data = ["ASR1000"]
        expected_return_data = [
            {
                "id": "90",
                "name": "ASR1000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_asr903(self):
        test_device_pf_data = ["ASR903"]
        expected_return_data = [
            {
                "id": "91",
                "name": "ASR903",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_asr901(self):
        test_device_pf_data = ["ASR901"]
        expected_return_data = [
            {
                "id": "92",
                "name": "ASR901",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_asr920(self):
        test_device_pf_data = ["ASR920"]
        expected_return_data = [
            {
                "id": "93",
                "name": "ASR920",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ncs4200(self):
        test_device_pf_data = ["NCS4200"]
        expected_return_data = [
            {
                "id": "94",
                "name": "NCS4200",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c3750(self):
        test_device_pf_data = ["C3750"]
        expected_return_data = [
            {
                "id": "97",
                "name": "C3750",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_me3400(self):
        test_device_pf_data = ["ME3400"]
        expected_return_data = [
            {
                "id": "98",
                "name": "ME3400",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_me2600x(self):
        test_device_pf_data = ["ME2600X"]
        expected_return_data = [
            {
                "id": "99",
                "name": "ME2600X",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_me3600x(self):
        test_device_pf_data = ["ME3600X"]
        expected_return_data = [
            {
                "id": "100",
                "name": "ME3600X",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_me3800x(self):
        test_device_pf_data = ["ME3800X"]
        expected_return_data = [
            {
                "id": "101",
                "name": "ME3800X",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_me4600(self):
        test_device_pf_data = ["ME4600"]
        expected_return_data = [
            {
                "id": "102",
                "name": "ME4600",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c4500(self):
        test_device_pf_data = ["C4500"]
        expected_return_data = [
            {
                "id": "103",
                "name": "C4500",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c4500x(self):
        test_device_pf_data = ["C4500X"]
        expected_return_data = [
            {
                "id": "104",
                "name": "C4500X",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ie1000(self):
        test_device_pf_data = ["IE1000"]
        expected_return_data = [
            {
                "id": "105",
                "name": "IE1000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ie2000(self):
        test_device_pf_data = ["IE2000"]
        expected_return_data = [
            {
                "id": "106",
                "name": "IE2000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ie3000(self):
        test_device_pf_data = ["IE3000"]
        expected_return_data = [
            {
                "id": "107",
                "name": "IE3000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ie4000(self):
        test_device_pf_data = ["IE4000"]
        expected_return_data = [
            {
                "id": "108",
                "name": "IE4000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ie5000(self):
        test_device_pf_data = ["IE5000"]
        expected_return_data = [
            {
                "id": "109",
                "name": "IE5000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_cgs2500(self):
        test_device_pf_data = ["CGS2500"]
        expected_return_data = [
            {
                "id": "110",
                "name": "CGS2500",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_cgr2000(self):
        test_device_pf_data = ["CGR2000"]
        expected_return_data = [
            {
                "id": "111",
                "name": "CGR2000",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c3850(self):
        test_device_pf_data = ["C3850"]
        expected_return_data = [
            {
                "id": "112",
                "name": "C3850",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c3750x(self):
        test_device_pf_data = ["C3750X"]
        expected_return_data = [
            {
                "id": "114",
                "name": "C3750X",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c3650(self):
        test_device_pf_data = ["C3650"]
        expected_return_data = [
            {
                "id": "115",
                "name": "C3650",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c3560(self):
        test_device_pf_data = ["C3560"]
        expected_return_data = [
            {
                "id": "116",
                "name": "C3560",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c3560c(self):
        test_device_pf_data = ["C3560C"]
        expected_return_data = [
            {
                "id": "117",
                "name": "C3560C",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c3560x(self):
        test_device_pf_data = ["C3560X"]
        expected_return_data = [
            {
                "id": "118",
                "name": "C3560X",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2960(self):
        test_device_pf_data = ["C2960"]
        expected_return_data = [
            {
                "id": "119",
                "name": "C2960",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n7700(self):
        test_device_pf_data = ["N7700"]
        expected_return_data = [
            {
                "id": "741",
                "name": "N7700",
                "count": "0",
                "filterChecked": "true",
                "filtername": "networkDeviceProductFamily",
            }
        ]
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data
