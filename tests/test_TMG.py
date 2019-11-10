import pytest
import responses
import json
from pytmg import TMG
from pytmg import TMGResult
from .models import test_TMG_models


def test_tmg_init():
    tmg = TMG.TMG()
    assert tmg is not None


class TestPrivateSearchMethodSimple:
    @responses.activate
    def test_tmg_private_search_for_n9k_93180yc_ex(self):
        resp_json = test_TMG_models.N9K_C93180YC_EX_MODEL
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
        resp_json = test_TMG_models.N9K_C9372PX_MODEL
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
        resp_json = test_TMG_models.WS_C3750_24PS_MODEL
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
        resp_json = test_TMG_models.ALL_3750S_MODEL
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
        resp_json = test_TMG_models.N9K_C93180YC_EX_MODEL
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
        resp_json = test_TMG_models.N9K_C9372PX_MODEL
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
        resp_json = test_TMG_models.WS_C3750_24PS_MODEL
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
        resp_json = test_TMG_models.ALL_3750S_MODEL
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
                resp_json = test_TMG_models.N9K_C93180YC_FX_MODEL
                return (
                    200,
                    {"content-type": "application/json"},
                    json.dumps(resp_json),
                )
            elif payload["searchInput"][0] == "C9300-48S":
                resp_json = test_TMG_models.C9300_48S_MODEL
                return (
                    200,
                    {"content-type": "application/json"},
                    json.dumps(resp_json),
                )
            elif payload["searchInput"][0] == "2951":
                resp_json = test_TMG_models.ISR2951_MODEL
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
        resp_json = test_TMG_models.ADV_SEARCH_IOS_XE_FET_10G_MODEL
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
        resp_json = test_TMG_models.ADV_SEARCH_UCS_XR_1GBPS_MODEL
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
            os_type=["IOS XR", "UCS"],
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
            "N540-24Z8Q2C-M",
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
                    assert xcvr["osType"] == "UCS" or xcvr["osType"] == "IOS XR"
                    assert (
                        xcvr["productId"] == "GLC-T"
                        or xcvr["productId"] == "GLC-TE"
                        or xcvr["productId"] == "SFP-GE-T"
                    )


class TestDeviceSearchingAdvanced:
    @responses.activate
    def test_tmg_search_advanced_ios_xe_fet_10g(self):
        resp_json = test_TMG_models.ADV_SEARCH_IOS_XE_FET_10G_MODEL
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
            match=r"Invalid Cable Types.*specified".format(invalid_cable_type),
        ):
            tmg._validate_cable_type(invalid_cable_type)

    def test_cable_type_validation_single_strand(self):
        test_cable_type = ["Single-Strand"]
        expected_return_data = test_TMG_models.CABLE_TYPE_SINGLE_STRAND
        tmg = TMG.TMG()
        results = tmg._validate_cable_type(test_cable_type)
        assert results == expected_return_data

    def test_cable_type_validation_na(self):
        test_cable_type = ["N/A (Incl AOC and DAC)"]
        expected_return_data = test_TMG_models.CABLE_TYPE_NA
        tmg = TMG.TMG()
        results = tmg._validate_cable_type(test_cable_type)
        assert results == expected_return_data

    def test_cable_type_validation_duplex_fiber(self):
        test_cable_type = ["Duplex Fiber"]
        expected_return_data = test_TMG_models.CABLE_TYPE_DUPLEX_FIBER
        tmg = TMG.TMG()
        results = tmg._validate_cable_type(test_cable_type)
        assert results == expected_return_data

    def test_cable_type_validation_ribbon_fiber(self):
        test_cable_type = ["Ribbon Fiber"]
        expected_return_data = test_TMG_models.CABLE_TYPE_RIBBON_FIBER
        tmg = TMG.TMG()
        results = tmg._validate_cable_type(test_cable_type)
        assert results == expected_return_data

    def test_cable_type_validation_single_strand_2(self):
        test_cable_type = ["Single-strand"]
        expected_return_data = test_TMG_models.CABLE_TYPE_SINGLE_STRAND_2
        tmg = TMG.TMG()
        results = tmg._validate_cable_type(test_cable_type)
        assert results == expected_return_data


class TestDataRateValidation:
    def test_data_rate_validation_invalid_data(self):
        invalid_data_rate = ["asdfasdfasdf"]
        tmg = TMG.TMG()
        with pytest.raises(
            ValueError,
            match=r"Invalid Data Rates.*specified".format(invalid_data_rate),
        ):
            tmg._validate_data_rate(invalid_data_rate)

    def test_data_rate_validation_100_200_gbps(self):
        test_data_rate = ["100/200 Gbps"]
        expected_return_data = test_TMG_models.DATA_RATE_100_200_GBPS
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_10_25_gbps(self):
        test_data_rate = ["10/25 Gbps"]
        expected_return_data = test_TMG_models.DATA_RATE_10_25_GBPS
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_100_mbps(self):
        test_data_rate = ["100 Mbps"]
        expected_return_data = test_TMG_models.DATA_RATE_100_MBPS
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_155_mbps(self):
        test_data_rate = ["155 Mbps"]
        expected_return_data = test_TMG_models.DATA_RATE_155_MBPS
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_622_mbps(self):
        test_data_rate = ["622 Mbps"]
        expected_return_data = test_TMG_models.DATA_RATE_622_MBPS
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_2_488_gbps(self):
        test_data_rate = ["2.488 Gbps"]
        expected_return_data = test_TMG_models.DATA_RATE_2_488_GBPS
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_40_100_gbps(self):
        test_data_rate = ["40/100 Gbps"]
        expected_return_data = test_TMG_models.DATA_RATE_40_100_GBPS
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_40_gbps(self):
        test_data_rate = ["40 Gbps"]
        expected_return_data = test_TMG_models.DATA_RATE_40_GBPS
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_100_gbps(self):
        test_data_rate = ["100 Gbps"]
        expected_return_data = test_TMG_models.DATA_RATE_100_GBPS
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_25_gbps(self):
        test_data_rate = ["25 Gbps"]
        expected_return_data = test_TMG_models.DATA_RATE_25_GBPS
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_10_gbps(self):
        test_data_rate = ["10 Gbps"]
        expected_return_data = test_TMG_models.DATA_RATE_10_GBPS
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_8_gbps(self):
        test_data_rate = ["8 Gbps"]
        expected_return_data = test_TMG_models.DATA_RATE_8_GBPS
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_16_gbps(self):
        test_data_rate = ["16 Gbps"]
        expected_return_data = test_TMG_models.DATA_RATE_16_GBPS
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data

    def test_data_rate_validation_32_gbps(self):
        test_data_rate = ["32 Gbps"]
        expected_return_data = test_TMG_models.DATA_RATE_32_GBPS
        tmg = TMG.TMG()
        results = tmg._validate_data_rate(test_data_rate)
        assert results == expected_return_data


class TestFormFactorValidation:
    def test_form_factor_validation_invalid_data(self):
        invalid_form_factor = ["asdfasdfasdf"]
        tmg = TMG.TMG()
        with pytest.raises(
            ValueError,
            match=r"Invalid Form Factors.*specified".format(invalid_form_factor),
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
            ValueError, match=r"Invalid Reaches.*specified".format(invalid_reach),
        ):
            tmg._validate_reach(invalid_reach)

    def test_reach_validation_220m(self):
        test_reach_data = ["220m"]
        expected_return_data = test_TMG_models.REACH_220M
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_400m_om3(self):
        test_reach_data = ["400m (OM3)"]
        expected_return_data = test_TMG_models.REACH_400M_OM3
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_550m_om3(self):
        test_reach_data = ["550m (OM3)"]
        expected_return_data = test_TMG_models.REACH_550M_OM3
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_10km_capital(self):
        test_reach_data = ["10Km"]
        expected_return_data = test_TMG_models.REACH_10KM_CAPITAL
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_1km_om4(self):
        test_reach_data = ["1km (OM4)"]
        expected_return_data = test_TMG_models.REACH_1KM_OM4
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_4m(self):
        test_reach_data = ["4m"]
        expected_return_data = test_TMG_models.REACH_4M
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_1km(self):
        test_reach_data = ["1km"]
        expected_return_data = test_TMG_models.REACH_1KM
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_550m(self):
        test_reach_data = ["550m"]
        expected_return_data = test_TMG_models.REACH_550M
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_70km(self):
        test_reach_data = ["70km"]
        expected_return_data = test_TMG_models.REACH_70KM
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_80km(self):
        test_reach_data = ["80km"]
        expected_return_data = test_TMG_models.REACH_80KM
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_70m_om3(self):
        test_reach_data = ["70m (OM3)"]
        expected_return_data = test_TMG_models.REACH_70M_OM3
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_100m_om4(self):
        test_reach_data = ["100m (OM4)"]
        expected_return_data = test_TMG_models.REACH_100M_OM4
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_500m(self):
        test_reach_data = ["500m"]
        expected_return_data = test_TMG_models.REACH_500M
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_25m(self):
        test_reach_data = ["25m"]
        expected_return_data = test_TMG_models.REACH_25M
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_30m(self):
        test_reach_data = ["30m"]
        expected_return_data = test_TMG_models.REACH_30M
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_25km(self):
        test_reach_data = ["25km"]
        expected_return_data = test_TMG_models.REACH_25KM
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_100m_om3(self):
        test_reach_data = ["100m (OM3)"]
        expected_return_data = test_TMG_models.REACH_100M_OM3
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_300m_om3(self):
        test_reach_data = ["300m (OM3)"]
        expected_return_data = test_TMG_models.REACH_300M_OM3
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_150m_om4(self):
        test_reach_data = ["150m (OM4)"]
        expected_return_data = test_TMG_models.REACH_150M_OM4
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_400m_om4(self):
        test_reach_data = ["400m (OM4)"]
        expected_return_data = test_TMG_models.REACH_400M_OM4
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_10km_lowercase(self):
        test_reach_data = ["10km"]
        expected_return_data = test_TMG_models.REACH_10KM_LOWERCASE
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_40km(self):
        test_reach_data = ["40km"]
        expected_return_data = test_TMG_models.REACH_40KM
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_2km(self):
        test_reach_data = ["2km"]
        expected_return_data = test_TMG_models.REACH_2KM
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_5m(self):
        test_reach_data = ["5m"]
        expected_return_data = test_TMG_models.REACH_5M
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_3m(self):
        test_reach_data = ["3m"]
        expected_return_data = test_TMG_models.REACH_3M
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_1m(self):
        test_reach_data = ["1m"]
        expected_return_data = test_TMG_models.REACH_1M
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_7m(self):
        test_reach_data = ["7m"]
        expected_return_data = test_TMG_models.REACH_7M
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_10m(self):
        test_reach_data = ["10m"]
        expected_return_data = test_TMG_models.REACH_10M
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_2m(self):
        test_reach_data = ["2m"]
        expected_return_data = test_TMG_models.REACH_2M
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_15m(self):
        test_reach_data = ["15m"]
        expected_return_data = test_TMG_models.REACH_15M
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_20m(self):
        test_reach_data = ["20m"]
        expected_return_data = test_TMG_models.REACH_20M
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_none(self):
        test_reach_data = ["None"]
        expected_return_data = test_TMG_models.REACH_NONE
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_15km(self):
        test_reach_data = ["15km"]
        expected_return_data = test_TMG_models.REACH_15KM
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_20km(self):
        test_reach_data = ["20km"]
        expected_return_data = test_TMG_models.REACH_20KM
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_300m(self):
        test_reach_data = ["300m"]
        expected_return_data = test_TMG_models.REACH_300M
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_400m(self):
        test_reach_data = ["400m"]
        expected_return_data = test_TMG_models.REACH_400M
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_2_5m(self):
        test_reach_data = ["2.5m"]
        expected_return_data = test_TMG_models.REACH_2_5M
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_400m_o43(self):
        test_reach_data = ["400m (O43)"]
        expected_return_data = test_TMG_models.REACH_400M_O43
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data

    def test_reach_validation_190m_om4(self):
        test_reach_data = ["190m (OM4)"]
        expected_return_data = test_TMG_models.REACH_190M_OM4
        tmg = TMG.TMG()
        results = tmg._validate_reach(test_reach_data)
        assert results == expected_return_data


class TestOSTypeValidation:
    def test_os_type_validation_invalid_data(self):
        invalid_os_type = ["asdfasdfasdf"]
        tmg = TMG.TMG()
        with pytest.raises(
            ValueError, match=r"Invalid OS Types.*specified".format(invalid_os_type),
        ):
            tmg._validate_os_type(invalid_os_type)

    def test_os_type_validation_nxos(self):
        test_os_type_data = ["NX-OS"]
        expected_return_data = test_TMG_models.OS_TYPE_NXOS
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_ios_xe(self):
        test_os_type_data = ["IOS XE"]
        expected_return_data = test_TMG_models.OS_TYPE_IOS_XE
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_ios_xr(self):
        test_os_type_data = ["IOS XR"]
        expected_return_data = test_TMG_models.OS_TYPE_IOS_XR
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_spa(self):
        test_os_type_data = ["SPA"]
        expected_return_data = test_TMG_models.OS_TYPE_SPA
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_ie1000(self):
        test_os_type_data = ["IE1000"]
        expected_return_data = test_TMG_models.OS_TYPE_IE1000
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_ios(self):
        test_os_type_data = ["IOS"]
        expected_return_data = test_TMG_models.OS_TYPE_IOS
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_ucs(self):
        test_os_type_data = ["UCS"]
        expected_return_data = test_TMG_models.OS_TYPE_UCS
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_fxos(self):
        test_os_type_data = ["FXOS"]
        expected_return_data = test_TMG_models.OS_TYPE_FXOS
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_olt(self):
        test_os_type_data = ["OLT"]
        expected_return_data = test_TMG_models.OS_TYPE_OLT
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_nam(self):
        test_os_type_data = ["NAM"]
        expected_return_data = test_TMG_models.OS_TYPE_NAM
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_scp(self):
        test_os_type_data = ["SCP"]
        expected_return_data = test_TMG_models.OS_TYPE_SCP
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_catos(self):
        test_os_type_data = ["CatOS"]
        expected_return_data = test_TMG_models.OS_TYPE_CATOS
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_epa(self):
        test_os_type_data = ["EPA"]
        expected_return_data = test_TMG_models.OS_TYPE_EPA
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_wlc(self):
        test_os_type_data = ["WLC"]
        expected_return_data = test_TMG_models.OS_TYPE_WLC
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data

    def test_os_type_validation_ios_xr_64(self):
        test_os_type_data = ["IOS XR 64 Bit"]
        expected_return_data = test_TMG_models.OS_TYPE_IOS_XR_64_BIT
        tmg = TMG.TMG()
        results = tmg._validate_os_type(test_os_type_data)
        assert results == expected_return_data


class TestTransceiverProductFamilyValidation:
    def test_transceiver_product_family_invalid_data(self):
        invalid_xcvr_data = ["asdfasdfasdf"]
        tmg = TMG.TMG()
        with pytest.raises(
            ValueError,
            match=r"Invalid Transceiver Product Families.*specified".format(
                invalid_xcvr_data
            ),
        ):
            tmg._validate_transceiver_product_family(invalid_xcvr_data)

    def test_transceiver_product_family_ncs5500(self):
        test_xcvr_pf_data = ["NCS5500"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_FAMILY_NCS5500
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_sfp25g(self):
        test_xcvr_pf_data = ["SFP25G"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_FAMILY_SFP25G
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_sfpocx(self):
        test_xcvr_pf_data = ["SFPOCX"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_FAMILY_SFPOCX
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_qsfp40g(self):
        test_xcvr_pf_data = ["QSFP40G"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_FAMILY_QSFP40G
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_qsfp100(self):
        test_xcvr_pf_data = ["QSFP100"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_FAMILY_QSFP100
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_sfpfe(self):
        test_xcvr_pf_data = ["SFPFE"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_FAMILY_SFPFE
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_wdm(self):
        test_xcvr_pf_data = ["WDM"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_FAMILY_WDM
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_sfpge(self):
        test_xcvr_pf_data = ["SFPGE"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_FAMILY_SFPGE
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_sfp10g(self):
        test_xcvr_pf_data = ["SFP10G"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_FAMILY_SFP10G
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_xenpak(self):
        test_xcvr_pf_data = ["XENPAK"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_FAMILY_XENPAK
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_x2(self):
        test_xcvr_pf_data = ["X2"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_FAMILY_X2
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_xfp(self):
        test_xcvr_pf_data = ["XFP"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_FAMILY_XFP
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data

    def test_transceiver_product_family_mds9000(self):
        test_xcvr_pf_data = ["MDS9000"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_FAMILY_MDS9000
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_family(test_xcvr_pf_data)
        assert results == expected_return_data


class TestTransceiverProductIdValidation:
    def test_transceiver_product_id_invalid_data(self):
        invalid_xcvr_data = ["asdfasdfasdf"]
        tmg = TMG.TMG()
        with pytest.raises(
            ValueError,
            match=r"Invalid Transceiver Product IDs.*specified".format(
                invalid_xcvr_data
            ),
        ):
            tmg._validate_transceiver_product_id(invalid_xcvr_data)

    def test_transceiver_product_id_qsfp_100g_sr4_s(self):
        test_xcvr_id_data = ["QSFP-100G-SR4-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_SR4_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_cwdm4_s(self):
        test_xcvr_id_data = ["QSFP-100G-CWDM4-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_CWDM4_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_psm4_s(self):
        test_xcvr_id_data = ["QSFP-100G-PSM4-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_PSM4_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_lr4_s(self):
        test_xcvr_id_data = ["QSFP-100G-LR4-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_LR4_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_sm_sr(self):
        test_xcvr_id_data = ["QSFP-100G-SM-SR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_SM_SR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_er4l_s(self):
        test_xcvr_id_data = ["QSFP-100G-ER4L-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_ER4L_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40_100_srbd(self):
        test_xcvr_id_data = ["QSFP-40/100-SRBD"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_40_100_SRBD
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_cu1m(self):
        test_xcvr_id_data = ["QSFP-100G-CU1M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_CU1M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_cu2m(self):
        test_xcvr_id_data = ["QSFP-100G-CU2M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_CU2M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_cu3m(self):
        test_xcvr_id_data = ["QSFP-100G-CU3M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_CU3M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_cu5m(self):
        test_xcvr_id_data = ["QSFP-100G-CU5M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_CU5M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp25g_cu1m(self):
        test_xcvr_id_data = ["QSFP-4SFP25G-CU1M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4SFP25G_CU1M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp25g_cu2m(self):
        test_xcvr_id_data = ["QSFP-4SFP25G-CU2M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4SFP25G_CU2M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp25g_cu3m(self):
        test_xcvr_id_data = ["QSFP-4SFP25G-CU3M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4SFP25G_CU3M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp25g_cu5m(self):
        test_xcvr_id_data = ["QSFP-4SFP25G-CU5M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4SFP25G_CU5M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc1m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC1M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_AOC1M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc2m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC2M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_AOC2M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc3m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC3M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_AOC3M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc5m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC5M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_AOC5M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc7m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC7M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_AOC7M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc10m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC10M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_AOC10M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc15m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC15M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_AOC15M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc20m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC20M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_AOC20M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc25m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC25M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_AOC25M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_100g_aoc30m(self):
        test_xcvr_id_data = ["QSFP-100G-AOC30M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_100G_AOC30M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cpak_100g_sr10(self):
        test_xcvr_id_data = ["CPAK-100G-SR10"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CPAK_100G_SR10
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cpak_100g_er4l(self):
        test_xcvr_id_data = ["CPAK-100G-ER4L"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CPAK_100G_ER4L
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cpak_100g_lr4(self):
        test_xcvr_id_data = ["CPAK-100G-LR4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CPAK_100G_LR4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cpak_10x10g_lr(self):
        test_xcvr_id_data = ["CPAK-10X10G-LR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CPAK_10X10G_LR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cpak_10x10g_erl(self):
        test_xcvr_id_data = ["CPAK-10X10G-ERL"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CPAK_10X10G_ERL
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cpak_100g_sr4(self):
        test_xcvr_id_data = ["CPAK-100G-SR4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CPAK_100G_SR4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cpak_100g_cwdm4(self):
        test_xcvr_id_data = ["CPAK-100G-CWDM4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CPAK_100G_CWDM4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cpak_100g_psm4(self):
        test_xcvr_id_data = ["CPAK-100G-PSM4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CPAK_100G_PSM4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_fe_100fx(self):
        test_xcvr_id_data = ["GLC-FE-100FX"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_FE_100FX
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_ge_100fx(self):
        test_xcvr_id_data = ["GLC-GE-100FX"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_GE_100FX
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_fe_100lx(self):
        test_xcvr_id_data = ["GLC-FE-100LX"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_FE_100LX
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_fe_100ex(self):
        test_xcvr_id_data = ["GLC-FE-100EX"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_FE_100EX
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_fe_100zx(self):
        test_xcvr_id_data = ["GLC-FE-100ZX"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_FE_100ZX
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_fe_100bx_d(self):
        test_xcvr_id_data = ["GLC-FE-100BX-D"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_FE_100BX_D
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_fe_100bx_u(self):
        test_xcvr_id_data = ["GLC-FE-100BX-U"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_FE_100BX_U
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_fe_t_i(self):
        test_xcvr_id_data = ["GLC-FE-T-I"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_FE_T_I
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_fe_100fx_rgd(self):
        test_xcvr_id_data = ["GLC-FE-100FX-RGD"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_FE_100FX_RGD
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_fe_100lx_rgd(self):
        test_xcvr_id_data = ["GLC-FE-100LX-RGD"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_FE_100LX_RGD
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc3_mm(self):
        test_xcvr_id_data = ["SFP-OC3-MM"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_OC3_MM
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc3_sr(self):
        test_xcvr_id_data = ["SFP-OC3-SR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_OC3_SR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc3_ir1(self):
        test_xcvr_id_data = ["SFP-OC3-IR1"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_OC3_IR1
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc3_lr1(self):
        test_xcvr_id_data = ["SFP-OC3-LR1"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_OC3_LR1
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc3_lr2(self):
        test_xcvr_id_data = ["SFP-OC3-LR2"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_OC3_LR2
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc12_mm(self):
        test_xcvr_id_data = ["SFP-OC12-MM"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_OC12_MM
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc12_sr(self):
        test_xcvr_id_data = ["SFP-OC12-SR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_OC12_SR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc12_ir1(self):
        test_xcvr_id_data = ["SFP-OC12-IR1"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_OC12_IR1
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc12_lr1(self):
        test_xcvr_id_data = ["SFP-OC12-LR1"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_OC12_LR1
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc12_lr2(self):
        test_xcvr_id_data = ["SFP-OC12-LR2"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_OC12_LR2
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc48_sr(self):
        test_xcvr_id_data = ["SFP-OC48-SR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_OC48_SR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc48_ir1(self):
        test_xcvr_id_data = ["SFP-OC48-IR1"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_OC48_IR1
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_oc48_lr2(self):
        test_xcvr_id_data = ["SFP-OC48-LR2"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_OC48_LR2
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h25g_cu1m(self):
        test_xcvr_id_data = ["SFP-H25G-CU1M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_H25G_CU1M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h25g_cu2m(self):
        test_xcvr_id_data = ["SFP-H25G-CU2M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_H25G_CU2M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h25g_cu3m(self):
        test_xcvr_id_data = ["SFP-H25G-CU3M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_H25G_CU3M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h25g_cu5m(self):
        test_xcvr_id_data = ["SFP-H25G-CU5M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_H25G_CU5M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_25g_aoc1m(self):
        test_xcvr_id_data = ["SFP-25G-AOC1M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_25G_AOC1M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_25g_aoc2m(self):
        test_xcvr_id_data = ["SFP-25G-AOC2M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_25G_AOC2M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_25g_aoc3m(self):
        test_xcvr_id_data = ["SFP-25G-AOC3M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_25G_AOC3M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_25g_aoc5m(self):
        test_xcvr_id_data = ["SFP-25G-AOC5M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_25G_AOC5M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_25g_aoc7m(self):
        test_xcvr_id_data = ["SFP-25G-AOC7M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_25G_AOC7M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_25g_aoc10m(self):
        test_xcvr_id_data = ["SFP-25G-AOC10M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_25G_AOC10M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_25g_sr_s(self):
        test_xcvr_id_data = ["SFP-25G-SR-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_25G_SR_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_sr(self):
        test_xcvr_id_data = ["SFP-10G-SR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_SR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_sr_s(self):
        test_xcvr_id_data = ["SFP-10G-SR-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_SR_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_sr_x(self):
        test_xcvr_id_data = ["SFP-10G-SR-X"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_SR_X
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_lrm(self):
        test_xcvr_id_data = ["SFP-10G-LRM"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_LRM
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_lr(self):
        test_xcvr_id_data = ["SFP-10G-LR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_LR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_lr_s(self):
        test_xcvr_id_data = ["SFP-10G-LR-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_LR_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_lr_x(self):
        test_xcvr_id_data = ["SFP-10G-LR-X"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_LR_X
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_er(self):
        test_xcvr_id_data = ["SFP-10G-ER"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_ER
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_er_s(self):
        test_xcvr_id_data = ["SFP-10G-ER-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_ER_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_zr(self):
        test_xcvr_id_data = ["SFP-10G-ZR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_ZR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_zr_s(self):
        test_xcvr_id_data = ["SFP-10G-ZR-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_ZR_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_bxd_i(self):
        test_xcvr_id_data = ["SFP-10G-BXD-I"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_BXD_I
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_bxu_i(self):
        test_xcvr_id_data = ["SFP-10G-BXU-I"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_BXU_I
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_bx40d_i(self):
        test_xcvr_id_data = ["SFP-10G-BX40D-I"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_BX40D_I
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_bx40u_i(self):
        test_xcvr_id_data = ["SFP-10G-BX40U-I"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_BX40U_I
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h10gb_cu1m(self):
        test_xcvr_id_data = ["SFP-H10GB-CU1M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_H10GB_CU1M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h10gb_cu3m(self):
        test_xcvr_id_data = ["SFP-H10GB-CU3M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_H10GB_CU3M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h10gb_cu5m(self):
        test_xcvr_id_data = ["SFP-H10GB-CU5M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_H10GB_CU5M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h10gb_acu7m(self):
        test_xcvr_id_data = ["SFP-H10GB-ACU7M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_H10GB_ACU7M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h10gb_acu10m(self):
        test_xcvr_id_data = ["SFP-H10GB-ACU10M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_H10GB_ACU10M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_aoc1m(self):
        test_xcvr_id_data = ["SFP-10G-AOC1M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_AOC1M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_aoc2m(self):
        test_xcvr_id_data = ["SFP-10G-AOC2M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_AOC2M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_aoc3m(self):
        test_xcvr_id_data = ["SFP-10G-AOC3M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_AOC3M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_aoc5m(self):
        test_xcvr_id_data = ["SFP-10G-AOC5M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_AOC5M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_aoc7m(self):
        test_xcvr_id_data = ["SFP-10G-AOC7M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_AOC7M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10g_aoc10m(self):
        test_xcvr_id_data = ["SFP-10G-AOC10M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10G_AOC10M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_fet_10g(self):
        test_xcvr_id_data = ["FET-10G"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_FET_10G
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp10g_61_41(self):
        test_xcvr_id_data = ["DWDM-SFP10G-61.41"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_DWDM_SFP10G_61_41
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp10g_xx_xx(self):
        test_xcvr_id_data = ["DWDM-SFP10G-XX.XX"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_DWDM_SFP10G_XX_XX
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cwdm_sfp10g_xxxx(self):
        test_xcvr_id_data = ["CWDM-SFP10G-XXXX"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CWDM_SFP10G_XXXX
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_er(self):
        test_xcvr_id_data = ["XENPAK-10GB-ER"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XENPAK_10GB_ER
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_erplus(self):
        test_xcvr_id_data = ["XENPAK-10GB-ER+"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XENPAK_10GB_ER_PLUS
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_lr(self):
        test_xcvr_id_data = ["XENPAK-10GB-LR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XENPAK_10GB_LR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_lrplus(self):
        test_xcvr_id_data = ["XENPAK-10GB-LR+"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XENPAK_10GB_LR_PLUS
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_lrm(self):
        test_xcvr_id_data = ["XENPAK-10GB-LRM"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XENPAK_10GB_LRM
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_lw(self):
        test_xcvr_id_data = ["XENPAK-10GB-LW"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XENPAK_10GB_LW
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_lx4(self):
        test_xcvr_id_data = ["XENPAK-10GB-LX4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XENPAK_10GB_LX4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_sr(self):
        test_xcvr_id_data = ["XENPAK-10GB-SR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XENPAK_10GB_SR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_cx4(self):
        test_xcvr_id_data = ["XENPAK-10GB-CX4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XENPAK_10GB_CX4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xenpak_10gb_zr(self):
        test_xcvr_id_data = ["XENPAK-10GB-ZR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XENPAK_10GB_ZR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_xenpak_xx_xx(self):
        test_xcvr_id_data = ["DWDM-XENPAK-XX.XX"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_DWDM_XENPAK_XX_XX
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_x2_10gb_lr(self):
        test_xcvr_id_data = ["X2-10GB-LR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_X2_10GB_LR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_x2_10gb_er(self):
        test_xcvr_id_data = ["X2-10GB-ER"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_X2_10GB_ER
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_x2_10gb_zr(self):
        test_xcvr_id_data = ["X2-10GB-ZR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_X2_10GB_ZR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_x2_10gb_sr(self):
        test_xcvr_id_data = ["X2-10GB-SR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_X2_10GB_SR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_x2_10gb_cx4(self):
        test_xcvr_id_data = ["X2-10GB-CX4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_X2_10GB_CX4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_x2_10gb_lx4(self):
        test_xcvr_id_data = ["X2-10GB-LX4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_X2_10GB_LX4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_x2_10gb_lrm(self):
        test_xcvr_id_data = ["X2-10GB-LRM"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_X2_10GB_LRM
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_x2_10gb_t(self):
        test_xcvr_id_data = ["X2-10GB-T"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_X2_10GB_T
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_x2_xx_xx(self):
        test_xcvr_id_data = ["DWDM-X2-XX.XX"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_DWDM_X2_XX_XX
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp_10glr_oc192sr(self):
        test_xcvr_id_data = ["XFP-10GLR-OC192SR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XFP_10GLR_OC192SR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp10glr_192sr_l(self):
        test_xcvr_id_data = ["XFP10GLR-192SR-L"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XFP10GLR_192SR_L
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp_10ger_oc192ir(self):
        test_xcvr_id_data = ["XFP-10GER-OC192IR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XFP_10GER_OC192IR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp_10ger_192irplus(self):
        test_xcvr_id_data = ["XFP-10GER-192IR+"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XFP_10GER_192IR_PLUS
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp10ger_192ir_l(self):
        test_xcvr_id_data = ["XFP10GER-192IR-L"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XFP10GER_192IR_L
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp_10gzr_oc192lr(self):
        test_xcvr_id_data = ["XFP-10GZR-OC192LR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XFP_10GZR_OC192LR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp_10g_mm_sr(self):
        test_xcvr_id_data = ["XFP-10G-MM-SR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XFP_10G_MM_SR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp10glr192sr_rgd(self):
        test_xcvr_id_data = ["XFP10GLR192SR-RGD"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XFP10GLR192SR_RGD
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp10ger192ir_rgd(self):
        test_xcvr_id_data = ["XFP10GER192IR-RGD"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XFP10GER192IR_RGD
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_xfp10gzr192lr_rgd(self):
        test_xcvr_id_data = ["XFP10GZR192LR-RGD"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_XFP10GZR192LR_RGD
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_xfp_xx_xx(self):
        test_xcvr_id_data = ["DWDM-XFP-XX.XX"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_DWDM_XFP_XX_XX
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_xfp_c(self):
        test_xcvr_id_data = ["DWDM-XFP-C"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_DWDM_XFP_C
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ws_g5483(self):
        test_xcvr_id_data = ["WS-G5483"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_WS_G5483
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ws_g5484(self):
        test_xcvr_id_data = ["WS-G5484"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_WS_G5484
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ws_g5486(self):
        test_xcvr_id_data = ["WS-G5486"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_WS_G5486
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ws_g5487(self):
        test_xcvr_id_data = ["WS-G5487"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_WS_G5487
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cwdm_gbic_xxxx(self):
        test_xcvr_id_data = ["CWDM-GBIC-XXXX"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CWDM_GBIC_XXXX
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_t(self):
        test_xcvr_id_data = ["GLC-T"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_T
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_te(self):
        test_xcvr_id_data = ["GLC-TE"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_TE
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_sx_mm(self):
        test_xcvr_id_data = ["GLC-SX-MM"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_SX_MM
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_lh_sm(self):
        test_xcvr_id_data = ["GLC-LH-SM"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_LH_SM
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_zx_sm(self):
        test_xcvr_id_data = ["GLC-ZX-SM"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_ZX_SM
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_bx_d(self):
        test_xcvr_id_data = ["GLC-BX-D"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_BX_D
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_bx_u(self):
        test_xcvr_id_data = ["GLC-BX-U"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_BX_U
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40g_sr4(self):
        test_xcvr_id_data = ["QSFP-40G-SR4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_40G_SR4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40g_csr4(self):
        test_xcvr_id_data = ["QSFP-40G-CSR4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_40G_CSR4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40g_sr4_s(self):
        test_xcvr_id_data = ["QSFP-40G-SR4-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_40G_SR4_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_fet_40g(self):
        test_xcvr_id_data = ["FET-40G"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_FET_40G
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40g_sr_bd(self):
        test_xcvr_id_data = ["QSFP-40G-SR-BD"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_40G_SR_BD
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_lr_s_capital(self):
        test_xcvr_id_data = ["QSFP-4X10G-LR-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4X10G_LR_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40g_lr4_s(self):
        test_xcvr_id_data = ["QSFP-40G-LR4-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_40G_LR4_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40ge_lr4(self):
        test_xcvr_id_data = ["QSFP-40GE-LR4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_40GE_LR4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40g_lr4(self):
        test_xcvr_id_data = ["QSFP-40G-LR4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_40G_LR4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40g_er4(self):
        test_xcvr_id_data = ["QSFP-40G-ER4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_40G_ER4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_wsp_q40glr4l(self):
        test_xcvr_id_data = ["WSP-Q40GLR4L"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_WSP_Q40GLR4L
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp10g_cu5m(self):
        test_xcvr_id_data = ["QSFP-4SFP10G-CU5M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4SFP10G_CU5M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp10g_cu3m(self):
        test_xcvr_id_data = ["QSFP-4SFP10G-CU3M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4SFP10G_CU3M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp10g_cu1m(self):
        test_xcvr_id_data = ["QSFP-4SFP10G-CU1M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4SFP10G_CU1M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_ac7m_capital(self):
        test_xcvr_id_data = ["QSFP-4X10G-AC7M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4X10G_AC7M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_ac10m_capital(self):
        test_xcvr_id_data = ["QSFP-4X10G-AC10M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4X10G_AC10M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_cu5m(self):
        test_xcvr_id_data = ["QSFP-H40G-CU5M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_H40G_CU5M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_cu3m(self):
        test_xcvr_id_data = ["QSFP-H40G-CU3M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_H40G_CU3M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_cu1m(self):
        test_xcvr_id_data = ["QSFP-H40G-CU1M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_H40G_CU1M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_acu7m(self):
        test_xcvr_id_data = ["QSFP-H40G-ACU7M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_H40G_ACU7M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_acu10m(self):
        test_xcvr_id_data = ["QSFP-H40G-ACU10M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_H40G_ACU10M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_aoc1m(self):
        test_xcvr_id_data = ["QSFP-4X10G-AOC1M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4X10G_AOC1M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_aoc2m(self):
        test_xcvr_id_data = ["QSFP-4X10G-AOC2M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4X10G_AOC2M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_aoc3m(self):
        test_xcvr_id_data = ["QSFP-4X10G-AOC3M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4X10G_AOC3M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_aoc5m(self):
        test_xcvr_id_data = ["QSFP-4X10G-AOC5M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4X10G_AOC5M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_aoc7m(self):
        test_xcvr_id_data = ["QSFP-4X10G-AOC7M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4X10G_AOC7M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_aoc10m(self):
        test_xcvr_id_data = ["QSFP-4X10G-AOC10M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4X10G_AOC10M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc1m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC1M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_H40G_AOC1M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc2m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC2M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_H40G_AOC2M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc3m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC3M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_H40G_AOC3M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc5m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC5M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_H40G_AOC5M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc7m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC7M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_H40G_AOC7M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc10m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC10M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_H40G_AOC10M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc15m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC15M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_H40G_AOC15M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc20m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC20M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_H40G_AOC20M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cvr_cfp_4sfp10g(self):
        test_xcvr_id_data = ["CVR-CFP-4SFP10G"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CVR_CFP_4SFP10G
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cfp_40g_sr4(self):
        test_xcvr_id_data = ["CFP-40G-SR4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CFP_40G_SR4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cfp_40g_lr4(self):
        test_xcvr_id_data = ["CFP-40G-LR4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CFP_40G_LR4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_ac7m_lowercase(self):
        test_xcvr_id_data = ["QSFP-4x10G-AC7M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4x10G_AC7M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_ac10m_lowercase(self):
        test_xcvr_id_data = ["QSFP-4x10G-AC10M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4x10G_AC10M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_cu0_5m(self):
        test_xcvr_id_data = ["QSFP-H40G-CU0-5M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_H40G_CU0_5M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_cu2m(self):
        test_xcvr_id_data = ["QSFP-H40G-CU2M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_H40G_CU2M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_cu4m(self):
        test_xcvr_id_data = ["QSFP-H40G-CU4M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_H40G_CU4M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp10g_c_s(self):
        test_xcvr_id_data = ["DWDM-SFP10G-C-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_DWDM_SFP10G_C_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_sfp_1gb_lx10(self):
        test_xcvr_id_data = ["MA-SFP-1GB-LX10"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_SFP_1GB_LX10
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_sfp_1gb_sx(self):
        test_xcvr_id_data = ["MA-SFP-1GB-SX"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_SFP_1GB_SX
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_sfp_1gb_tx(self):
        test_xcvr_id_data = ["MA-SFP-1GB-TX"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_SFP_1GB_TX
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_cbl_40g_1m(self):
        test_xcvr_id_data = ["MA-CBL-40G-1M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_CBL_40G_1M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_cbl_40g_3m(self):
        test_xcvr_id_data = ["MA-CBL-40G-3M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_CBL_40G_3M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_cbl_40g_50cm(self):
        test_xcvr_id_data = ["MA-CBL-40G-50CM"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_CBL_40G_50CM
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_cbl_ta_1m(self):
        test_xcvr_id_data = ["MA-CBL-TA-1M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_CBL_TA_1M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_cbl_ta_3m(self):
        test_xcvr_id_data = ["MA-CBL-TA-3M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_CBL_TA_3M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_sfp_10gb_lr(self):
        test_xcvr_id_data = ["MA-SFP-10GB-LR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_SFP_10GB_LR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_sfp_10gb_lrm(self):
        test_xcvr_id_data = ["MA-SFP-10GB-LRM"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_SFP_10GB_LRM
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_sfp_10gb_sr(self):
        test_xcvr_id_data = ["MA-SFP-10GB-SR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_SFP_10GB_SR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_cbl_100g_1m(self):
        test_xcvr_id_data = ["MA-CBL-100G-1M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_CBL_100G_1M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_cbl_100g_3m(self):
        test_xcvr_id_data = ["MA-CBL-100G-3M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_CBL_100G_3M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_cbl_100g_50cm(self):
        test_xcvr_id_data = ["MA-CBL-100G-50CM"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_CBL_100G_50CM
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_qsfp_40g_csr4(self):
        test_xcvr_id_data = ["MA-QSFP-40G-CSR4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_QSFP_40G_CSR4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_qsfp_40g_lr4(self):
        test_xcvr_id_data = ["MA-QSFP-40G-LR4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_QSFP_40G_LR4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_qsfp_40g_sr4(self):
        test_xcvr_id_data = ["MA-QSFP-40G-SR4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_QSFP_40G_SR4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_qsfp_40g_sr_bd(self):
        test_xcvr_id_data = ["MA-QSFP-40G-SR-BD"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_QSFP_40G_SR_BD
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_qsfp_100g_lr4(self):
        test_xcvr_id_data = ["MA-QSFP-100G-LR4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_QSFP_100G_LR4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ma_qsfp_100g_sr4(self):
        test_xcvr_id_data = ["MA-QSFP-100G-SR4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_MA_QSFP_100G_SR4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_aoc15m(self):
        test_xcvr_id_data = ["QSFP-4X10G-AOC15M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4X10G_AOC15M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4x10g_lr_s_lowercase(self):
        test_xcvr_id_data = ["QSFP-4x10G-LR-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4x10G_LR_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10_25g_lr_s(self):
        test_xcvr_id_data = ["SFP-10/25G-LR-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10_25G_LR_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cvr_4sfp10g_qsfp(self):
        test_xcvr_id_data = ["CVR-4SFP10G-QSFP"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CVR_4SFP10G_QSFP
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40g_csr_s(self):
        test_xcvr_id_data = ["QSFP-40G-CSR-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_40G_CSR_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp_3268(self):
        test_xcvr_id_data = ["DWDM-SFP-3268"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_DWDM_SFP_3268
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp_3190(self):
        test_xcvr_id_data = ["DWDM-SFP-3190"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_DWDM_SFP_3190
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp_3112(self):
        test_xcvr_id_data = ["DWDM-SFP-3112"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_DWDM_SFP_3112
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp_3033(self):
        test_xcvr_id_data = ["DWDM-SFP-3033"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_DWDM_SFP_3033
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cwdm_sfp_1470(self):
        test_xcvr_id_data = ["CWDM-SFP-1470"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CWDM_SFP_1470
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cwdm_sfp_1610(self):
        test_xcvr_id_data = ["CWDM-SFP-1610"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CWDM_SFP_1610
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_bx_d_i(self):
        test_xcvr_id_data = ["GLC-BX-D-I"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_BX_D_I
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_bx_u_i(self):
        test_xcvr_id_data = ["GLC-BX-U-I"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_BX_U_I
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_bx40_d_i(self):
        test_xcvr_id_data = ["GLC-BX40-D-I"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_BX40_D_I
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_bx40_u_i(self):
        test_xcvr_id_data = ["GLC-BX40-U-I"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_BX40_U_I
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_bx80_d_i(self):
        test_xcvr_id_data = ["GLC-BX80-D-I"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_BX80_D_I
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_bx80_u_i(self):
        test_xcvr_id_data = ["GLC-BX80-U-I"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_BX80_U_I
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_bx40_da_i(self):
        test_xcvr_id_data = ["GLC-BX40-DA-I"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_BX40_DA_I
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_2bx_d(self):
        test_xcvr_id_data = ["GLC-2BX-D"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_2BX_D
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_ge_s(self):
        test_xcvr_id_data = ["SFP-GE-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_GE_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_ge_l(self):
        test_xcvr_id_data = ["SFP-GE-L"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_GE_L
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_ex_smd(self):
        test_xcvr_id_data = ["GLC-EX-SMD"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_EX_SMD
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_ge_z(self):
        test_xcvr_id_data = ["SFP-GE-Z"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_GE_Z
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_ge_t(self):
        test_xcvr_id_data = ["SFP-GE-T"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_GE_T
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_sx_mm_rgd(self):
        test_xcvr_id_data = ["GLC-SX-MM-RGD"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_SX_MM_RGD
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_lx_sm_rgd(self):
        test_xcvr_id_data = ["GLC-LX-SM-RGD"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_LX_SM_RGD
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_zx_sm_rgd(self):
        test_xcvr_id_data = ["GLC-ZX-SM-RGD"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_ZX_SM_RGD
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_sx_mmd(self):
        test_xcvr_id_data = ["GLC-SX-MMD"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_SX_MMD
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_lh_smd(self):
        test_xcvr_id_data = ["GLC-LH-SMD"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_LH_SMD
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_zx_smd(self):
        test_xcvr_id_data = ["GLC-ZX-SMD"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_ZX_SMD
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_gpon_b(self):
        test_xcvr_id_data = ["SFP-GPON-B"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_GPON_B
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_gpon_b_i(self):
        test_xcvr_id_data = ["SFP-GPON-B-I"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_GPON_B_I
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_gpon_c(self):
        test_xcvr_id_data = ["SFP-GPON-C"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_GPON_C
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_gpon_c_i(self):
        test_xcvr_id_data = ["SFP-GPON-C-I"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_GPON_C_I
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cwdm_sfp_xxxx(self):
        test_xcvr_id_data = ["CWDM-SFP-XXXX"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CWDM_SFP_XXXX
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp_xxxx(self):
        test_xcvr_id_data = ["DWDM-SFP-XXXX"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_DWDM_SFP_XXXX
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_40g_bd_rx(self):
        test_xcvr_id_data = ["QSFP-40G-BD-RX"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_40G_BD_RX
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc25m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC25M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_H40G_AOC25M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_h40g_aoc30m(self):
        test_xcvr_id_data = ["QSFP-H40G-AOC30M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_H40G_AOC30M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cpak_100ge_lr4(self):
        test_xcvr_id_data = ["CPAK-100GE-LR4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CPAK_100GE_LR4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cxp_100g_sr10(self):
        test_xcvr_id_data = ["CXP-100G-SR10"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CXP_100G_SR10
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cxp_100g_sr12(self):
        test_xcvr_id_data = ["CXP-100G-SR12"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CXP_100G_SR12
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cfp2_100g_er4(self):
        test_xcvr_id_data = ["CFP2-100G-ER4"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CFP2_100G_ER4
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp10g_usr(self):
        test_xcvr_id_data = ["SFP10G-USR"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP10G_USR
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h10gb_cu1_5m(self):
        test_xcvr_id_data = ["SFP-H10GB-CU1-5M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_H10GB_CU1_5M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h10gb_cu2m(self):
        test_xcvr_id_data = ["SFP-H10GB-CU2M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_H10GB_CU2M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h10gb_cu2_5m(self):
        test_xcvr_id_data = ["SFP-H10GB-CU2-5M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_H10GB_CU2_5M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_glc_ge_dr_lx(self):
        test_xcvr_id_data = ["GLC-GE-DR-LX"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_GLC_GE_DR_LX
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp10g_30_33(self):
        test_xcvr_id_data = ["DWDM-SFP10G-30.33"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_DWDM_SFP10G_30_33
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_dwdm_sfp10g_c(self):
        test_xcvr_id_data = ["DWDM-SFP10G-C"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_DWDM_SFP10G_C
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_10_25g_csr_s(self):
        test_xcvr_id_data = ["SFP-10/25G-CSR-S"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_10_25G_CSR_S
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cwdm_sfp10g_1530(self):
        test_xcvr_id_data = ["CWDM-SFP10G-1530"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CWDM_SFP10G_1530
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_h10gb_cu4m(self):
        test_xcvr_id_data = ["SFP-H10GB-CU4M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_H10GB_CU4M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ds_sfp_fc8g_sw(self):
        test_xcvr_id_data = ["DS-SFP-FC8G-SW"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_DS_SFP_FC8G_SW
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ds_sfp_fc16g_sw(self):
        test_xcvr_id_data = ["DS-SFP-FC16G-SW"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_DS_SFP_FC16G_SW
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_ds_sfp_fc32g_sw(self):
        test_xcvr_id_data = ["DS-SFP-FC32G-SW"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_DS_SFP_FC32G_SW
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cfp2_wdm_det_1hl(self):
        test_xcvr_id_data = ["CFP2-WDM-DET-1HL"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CFP2_WDM_DET_1HL
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_cfp2_wdm_d_1hl(self):
        test_xcvr_id_data = ["CFP2-WDM-D-1HL"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_CFP2_WDM_D_1HL
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_sfp_25g_aoc4m(self):
        test_xcvr_id_data = ["SFP-25G-AOC4M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_SFP_25G_AOC4M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp10g_cu2m(self):
        test_xcvr_id_data = ["QSFP-4SFP10G-CU2M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4SFP10G_CU2M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp10g_cu4m(self):
        test_xcvr_id_data = ["QSFP-4SFP10G-CU4M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4SFP10G_CU4M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data

    def test_transceiver_product_id_qsfp_4sfp10g_cu0_5m(self):
        test_xcvr_id_data = ["QSFP-4SFP10G-CU0-5M"]
        expected_return_data = test_TMG_models.XCVR_PRODUCT_ID_QSFP_4SFP10G_CU0_5M
        tmg = TMG.TMG()
        results = tmg._validate_transceiver_product_id(test_xcvr_id_data)
        assert results == expected_return_data


class TestNetworkDeviceProductFamilyValidation:
    def test_network_device_product_family_invalid_data(self):
        invalid_device_data = ["asdfasdfasdf"]
        tmg = TMG.TMG()
        with pytest.raises(
            ValueError, match=r"Invalid Network Device Product Families.*specified"
        ):
            tmg._validate_network_device_product_family(invalid_device_data)

    def test_network_device_product_family_c2960p(self):
        test_device_pf_data = ["C2960P"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C2960P
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2960s(self):
        test_device_pf_data = ["C2960S"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C2960S
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2960sf(self):
        test_device_pf_data = ["C2960SF"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C2960SF
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2960c(self):
        test_device_pf_data = ["C2960C"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C2960C
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2960x(self):
        test_device_pf_data = ["C2960X"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C2960X
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2960xr(self):
        test_device_pf_data = ["C2960XR"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C2960XR
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c9400(self):
        test_device_pf_data = ["C9400"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C9400
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c9500(self):
        test_device_pf_data = ["C9500"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C9500
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n3500(self):
        test_device_pf_data = ["N3500"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_N3500
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n2000(self):
        test_device_pf_data = ["N2000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_N2000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n5000(self):
        test_device_pf_data = ["N5000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_N5000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n6000(self):
        test_device_pf_data = ["N6000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_N6000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n7000(self):
        test_device_pf_data = ["N7000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_N7000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ucsb(self):
        test_device_pf_data = ["UCSB"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_UCSB
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ucsc(self):
        test_device_pf_data = ["UCSC"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_UCSC
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_crs(self):
        test_device_pf_data = ["CRS"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_CRS
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ncs1000(self):
        test_device_pf_data = ["NCS1000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_NCS1000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ncs5000(self):
        test_device_pf_data = ["NCS5000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_NCS5000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ncs5500(self):
        test_device_pf_data = ["NCS5500"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_NCS5500
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ncs6000(self):
        test_device_pf_data = ["NCS6000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_NCS6000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_fprhigh(self):
        test_device_pf_data = ["FPRHIGH"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_FPRHIGH
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_fpruhi(self):
        test_device_pf_data = ["FPRUHI"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_FPRUHI
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ncs4000(self):
        test_device_pf_data = ["NCS4000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_NCS4000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ce500(self):
        test_device_pf_data = ["CE500"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_CE500
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ce520(self):
        test_device_pf_data = ["CE520"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_CE520
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_me2400(self):
        test_device_pf_data = ["ME2400"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ME2400
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_me3750(self):
        test_device_pf_data = ["ME3750"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ME3750
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c4ktor(self):
        test_device_pf_data = ["C4KTOR"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C4KTOR
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_l3fixed(self):
        test_device_pf_data = ["L3FIXED"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_L3FIXED
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2900(self):
        test_device_pf_data = ["C2900"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C2900
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_dsbuoth(self):
        test_device_pf_data = ["DSBUOTH"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_DSBUOTH
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2940(self):
        test_device_pf_data = ["C2940"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C2940
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2950(self):
        test_device_pf_data = ["C2950"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C2950
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2960l(self):
        test_device_pf_data = ["C2960L"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C2960L
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2960cx(self):
        test_device_pf_data = ["C2960CX"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C2960CX
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2970(self):
        test_device_pf_data = ["C2970"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C2970
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2975(self):
        test_device_pf_data = ["C2975"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C2975
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c3550(self):
        test_device_pf_data = ["C3550"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C3550
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c3560cx(self):
        test_device_pf_data = ["C3560CX"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C3560CX
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c4000(self):
        test_device_pf_data = ["C4000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C4000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c6500(self):
        test_device_pf_data = ["C6500"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C6500
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c6800(self):
        test_device_pf_data = ["C6800"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C6800
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2350(self):
        test_device_pf_data = ["C2350"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C2350
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2360(self):
        test_device_pf_data = ["C2360"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C2360
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_os(self):
        test_device_pf_data = ["OS"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_OS
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n4000(self):
        test_device_pf_data = ["N4000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_N4000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_css(self):
        test_device_pf_data = ["CSS"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_CSS
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_erbuold(self):
        test_device_pf_data = ["ERBUOLD"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ERBUOLD
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ubr7200(self):
        test_device_pf_data = ["UBR7200"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_UBR7200
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_7300(self):
        test_device_pf_data = ["7300"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_7300
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_7304(self):
        test_device_pf_data = ["7304"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_7304
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_7500(self):
        test_device_pf_data = ["7500"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_7500
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_esr(self):
        test_device_pf_data = ["ESR"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ESR
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ubr10k(self):
        test_device_pf_data = ["UBR10K"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_UBR10K
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_rfgw10(self):
        test_device_pf_data = ["RFGW10"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_RFGW10
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_gsr(self):
        test_device_pf_data = ["GSR"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_GSR
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_asr900(self):
        test_device_pf_data = ["ASR900"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ASR900
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_rantran(self):
        test_device_pf_data = ["RANTRAN"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_RANTRAN
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_asamid(self):
        test_device_pf_data = ["ASAMID"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ASAMID
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_embunam(self):
        test_device_pf_data = ["EMBUNAM"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_EMBUNAM
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_airctu(self):
        test_device_pf_data = ["AIRCTU"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_AIRCTU
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_fprmid(self):
        test_device_pf_data = ["FPRMID"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_FPRMID
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_scp(self):
        test_device_pf_data = ["SCP"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_SCP
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n9000(self):
        test_device_pf_data = ["N9000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_N9000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c4900(self):
        test_device_pf_data = ["C4900"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C4900
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c4900m(self):
        test_device_pf_data = ["C4900M"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C4900M
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ncs540(self):
        test_device_pf_data = ["NCS540"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_NCS540
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ncs560(self):
        test_device_pf_data = ["NCS560"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_NCS560
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_isr3900(self):
        test_device_pf_data = ["ISR3900"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ISR3900
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_isr4000(self):
        test_device_pf_data = ["ISR4000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ISR4000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_isr2900(self):
        test_device_pf_data = ["ISR2900"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ISR2900
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_aircti2(self):
        test_device_pf_data = ["AIRCTI2"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_AIRCTI2
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_asahigh(self):
        test_device_pf_data = ["ASAHIGH"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ASAHIGH
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c9200(self):
        test_device_pf_data = ["C9200"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C9200
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c9200l(self):
        test_device_pf_data = ["C9200L"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C9200L
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_cbr8(self):
        test_device_pf_data = ["CBR8"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_CBR8
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_isr800(self):
        test_device_pf_data = ["ISR800"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ISR800
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c9600(self):
        test_device_pf_data = ["C9600"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C9600
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ms120_series(self):
        test_device_pf_data = ["MS120 Series"]
        expected_return_data = (
            test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_MS120_SERIES
        )
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ms210_series(self):
        test_device_pf_data = ["MS210 Series"]
        expected_return_data = (
            test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_MS210_SERIES
        )
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ms225_series(self):
        test_device_pf_data = ["MS225 Series"]
        expected_return_data = (
            test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_MS225_SERIES
        )
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ms250_series(self):
        test_device_pf_data = ["MS250 Series"]
        expected_return_data = (
            test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_MS250_SERIES
        )
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ms350_series(self):
        test_device_pf_data = ["MS350 Series"]
        expected_return_data = (
            test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_MS350_SERIES
        )
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ms355_series(self):
        test_device_pf_data = ["MS355 Series"]
        expected_return_data = (
            test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_MS355_SERIES
        )
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ms410_series(self):
        test_device_pf_data = ["MS410 Series"]
        expected_return_data = (
            test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_MS410_SERIES
        )
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ms425_series(self):
        test_device_pf_data = ["MS425 Series"]
        expected_return_data = (
            test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_MS425_SERIES
        )
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_mx84(self):
        test_device_pf_data = ["MX84"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_MX84
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_mx100(self):
        test_device_pf_data = ["MX100"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_MX100
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_mx250(self):
        test_device_pf_data = ["MX250"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_MX250
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_mx400(self):
        test_device_pf_data = ["MX400"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_MX400
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_mx450(self):
        test_device_pf_data = ["MX450"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_MX450
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_mx600(self):
        test_device_pf_data = ["MX600"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_MX600
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
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C9300L
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_me1200(self):
        test_device_pf_data = ["ME1200"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ME1200
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c9800(self):
        test_device_pf_data = ["C9800"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C9800
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_rphyshf(self):
        test_device_pf_data = ["RPHYSHF"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_RPHYSHF
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ie3200(self):
        test_device_pf_data = ["IE3200"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_IE3200
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ie3300(self):
        test_device_pf_data = ["IE3300"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_IE3300
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ie3400(self):
        test_device_pf_data = ["IE3400"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_IE3400
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n9300(self):
        test_device_pf_data = ["N9300"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_N9300
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n3000(self):
        test_device_pf_data = ["N3000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_N3000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c9300(self):
        test_device_pf_data = ["C9300"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C9300
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n9500(self):
        test_device_pf_data = ["N9500"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_N9500
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n9200(self):
        test_device_pf_data = ["N9200"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_N9200
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ipacces(self):
        test_device_pf_data = ["IPACCES"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_IPACCES
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_wanlan(self):
        test_device_pf_data = ["WANLAN"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_WANLAN
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_asr9000(self):
        test_device_pf_data = ["ASR9000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ASR9000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_800bb(self):
        test_device_pf_data = ["800BB"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_800BB
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c6000(self):
        test_device_pf_data = ["C6000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C6000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_7600(self):
        test_device_pf_data = ["7600"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_7600
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_asr1000(self):
        test_device_pf_data = ["ASR1000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ASR1000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_asr903(self):
        test_device_pf_data = ["ASR903"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ASR903
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_asr901(self):
        test_device_pf_data = ["ASR901"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ASR901
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_asr920(self):
        test_device_pf_data = ["ASR920"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ASR920
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ncs4200(self):
        test_device_pf_data = ["NCS4200"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_NCS4200
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c3750(self):
        test_device_pf_data = ["C3750"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C3750
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_me3400(self):
        test_device_pf_data = ["ME3400"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ME3400
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_me2600x(self):
        test_device_pf_data = ["ME2600X"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ME2600X
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_me3600x(self):
        test_device_pf_data = ["ME3600X"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ME3600X
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_me3800x(self):
        test_device_pf_data = ["ME3800X"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ME3800X
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_me4600(self):
        test_device_pf_data = ["ME4600"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_ME4600
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c4500(self):
        test_device_pf_data = ["C4500"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C4500
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c4500x(self):
        test_device_pf_data = ["C4500X"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C4500X
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ie1000(self):
        test_device_pf_data = ["IE1000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_IE1000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ie2000(self):
        test_device_pf_data = ["IE2000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_IE2000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ie3000(self):
        test_device_pf_data = ["IE3000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_IE3000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ie4000(self):
        test_device_pf_data = ["IE4000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_IE4000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_ie5000(self):
        test_device_pf_data = ["IE5000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_IE5000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_cgs2500(self):
        test_device_pf_data = ["CGS2500"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_CGS2500
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_cgr2000(self):
        test_device_pf_data = ["CGR2000"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_CGR2000
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c3850(self):
        test_device_pf_data = ["C3850"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C3850
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c3750x(self):
        test_device_pf_data = ["C3750X"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C3750X
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c3650(self):
        test_device_pf_data = ["C3650"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C3650
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c3560(self):
        test_device_pf_data = ["C3560"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C3560
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c3560c(self):
        test_device_pf_data = ["C3560C"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C3560C
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c3560x(self):
        test_device_pf_data = ["C3560X"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C3560X
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_c2960(self):
        test_device_pf_data = ["C2960"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_C2960
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data

    def test_network_device_product_family_n7700(self):
        test_device_pf_data = ["N7700"]
        expected_return_data = test_TMG_models.NETWORK_DEVICE_PRODUCT_FAMILY_N7700
        tmg = TMG.TMG()
        results = tmg._validate_network_device_product_family(test_device_pf_data)
        assert results == expected_return_data
