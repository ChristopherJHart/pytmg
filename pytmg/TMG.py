"""
Base class for the pyTMG library.
"""
import json
import requests
from pytmg.TMGResult import TMGResult
from pytmg.models.tmg_filters import (
    CABLE_TYPE_FILTERS,
    DATA_RATE_FILTERS,
    FORM_FACTOR_FILTERS,
    REACH_FILTERS,
    OS_TYPE_FILTERS,
    XCVR_PRODUCT_FAMILY_FILTERS,
    XCVR_PRODUCT_ID_FILTERS,
    NETWORK_DEVICE_PRODUCT_FAMILY_FILTERS,
)


class TMG:
    """
    The TMG object is the primary point of entry for pyTMG.

    A TMG object instantiates basic access information for Cisco's TMG
    (Transceiver Module Group) Compatibility Matrix, as well as provides
    methods for common tasks performed through the TMG web application.
    """

    def __init__(self):
        """
        Instantiates an object of class TMG.
        """
        self.search_url = "https://tmgmatrix.cisco.com/public/api/networkdevice/search"

    def _search(
        self,
        cable_type=[],
        data_rate=[],
        form_factor=[],
        reach=[],
        search_input=[],
        os_type=[],
        transceiver_product_family=[],
        transceiver_product_id=[],
        network_device_product_family=[],
        network_device_product_id=[],
    ):
        # TODO: Add support for advanced search functionality - right now,
        #       only "search_input" is really supported.
        body = {
            "cableType": self._validate_cable_type(cable_type),
            "dataRate": self._validate_data_rate(data_rate),
            "formFactor": self._validate_form_factor(form_factor),
            "reach": self._validate_reach(reach),
            "searchInput": search_input,
            "osType": self._validate_os_type(os_type),
            "transceiverProductFamily": self._validate_transceiver_product_family(
                transceiver_product_family
            ),
            "transceiverProductID": self._validate_transceiver_product_id(
                transceiver_product_id
            ),
            "networkDeviceProductFamily": self._validate_network_device_product_family(
                network_device_product_family
            ),
            "networkDeviceProductID": self._validate_network_device_product_id(
                network_device_product_id
            ),
        }
        headers = {"content-type": "application/json"}

        res = requests.post(self.search_url, json=body, headers=headers)
        res.raise_for_status()
        return res.json()

    def _validate_cable_type(self, cable_type):
        if not cable_type:
            return cable_type
        valid_cable_types = CABLE_TYPE_FILTERS
        validated_cable_type = [
            ct for ct in valid_cable_types if ct["name"] == cable_type
        ]
        if validated_cable_type:
            return validated_cable_type
        else:
            raise ValueError(f'Invalid Cable Type "{cable_type}" specified')

    def _validate_data_rate(self, data_rate):
        if not data_rate:
            return data_rate
        valid_data_rates = DATA_RATE_FILTERS
        validated_data_rate = [dr for dr in valid_data_rates if dr["name"] == data_rate]
        if validated_data_rate:
            return validated_data_rate
        else:
            raise ValueError(f'Invalid Data Rate "{data_rate}" specified')

    def _validate_form_factor(self, form_factor):
        if not form_factor:
            return form_factor
        valid_form_factors = FORM_FACTOR_FILTERS
        validated_form_factor = [
            ff for ff in valid_form_factors if ff["name"] == form_factor
        ]
        if validated_form_factor:
            return validated_form_factor
        else:
            raise ValueError(f'Invalid Form Factor "{form_factor}" specified')

    def _validate_reach(self, reach):
        if not reach:
            return reach
        valid_reaches = REACH_FILTERS
        validated_reach = [r for r in valid_reaches if r["name"] == reach]
        if validated_reach:
            return validated_reach
        else:
            raise ValueError(f'Invalid Reach "{reach}" specified')

    def _validate_os_type(self, os_type):
        if not os_type:
            return os_type
        valid_os_types = OS_TYPE_FILTERS
        validated_os_type = [os for os in valid_os_types if os["name"] == os_type]
        if validated_os_type:
            return validated_os_type
        else:
            raise ValueError(f'Invalid OS Type "{os_type}" specified')

    def _validate_transceiver_product_family(self, transceiver_product_family):
        if not transceiver_product_family:
            return transceiver_product_family
        valid_xcvr_product_families = XCVR_PRODUCT_FAMILY_FILTERS
        validated_pf = [
            pf
            for pf in valid_xcvr_product_families
            if pf["name"] == transceiver_product_family
        ]
        if validated_pf:
            return validated_pf
        else:
            raise ValueError(
                f'Invalid Transceiver Product Family "{transceiver_product_family}" specified'
            )

    def _validate_transceiver_product_id(self, transceiver_product_id):
        if not transceiver_product_id:
            return transceiver_product_id
        valid_xcvr_product_ids = XCVR_PRODUCT_ID_FILTERS
        validated_pid = [
            pid
            for pid in valid_xcvr_product_ids
            if pid["name"] == transceiver_product_id
        ]
        if validated_pid:
            return validated_pid
        else:
            raise ValueError(
                f'Invalid Transceiver Product ID "{transceiver_product_id}" specified'
            )

    def _validate_network_device_product_family(self, network_device_product_family):
        if not network_device_product_family:
            return network_device_product_family
        valid_device_product_families = NETWORK_DEVICE_PRODUCT_FAMILY_FILTERS
        validated_pf = [
            pf
            for pf in valid_device_product_families
            if pf["name"] == network_device_product_family
        ]
        if validated_pf:
            return validated_pf
        else:
            raise ValueError(
                f'Invalid Network Device Product Family "{network_device_product_family}" specified'
            )

    def _validate_network_device_product_id(self, network_device_product_id):
        # TODO: Not yet supported. Need to reverse-engineer how TMG utilizes this field.
        if not network_device_product_id:
            return network_device_product_id
        else:
            raise ValueError(
                f'Invalid Network Device Product ID "{network_device_product_id}" specified'
            )
        # valid_device_product_ids = []
        # validated_pid = [
        #     pid
        #     for pid in valid_device_product_ids
        #     if pid["name"] == network_device_product_id
        # ]
        # if validated_pid:
        #     return validated_pid
        # else:
        #     raise ValueError(
        #         f'Invalid Network Device Product ID "{network_device_product_id}" specified'
        #     )

    def search(self, **kwargs):
        """
        Performs a search query against Cisco's TMG (Transceiver Module Group)
        Compatibility Matrix.

        :param dict kwargs: A dictionary containing specific parameters of the
            search query.
        
        :Examples:

        >>> from pytmg import TMG
        >>> tmg = TMG.TMG()
        >>> params = {
        ...     "search_input": ["N9K-C93180YC-EX"],
        ... }
        >>> tmg_res = tmg.search(**params)
        """
        results = self._search(
            cable_type=kwargs.get("cable_type", []),
            data_rate=kwargs.get("data_rate", []),
            form_factor=kwargs.get("form_factor", []),
            reach=kwargs.get("reach", []),
            search_input=kwargs.get("search_input", []),
            os_type=kwargs.get("os_type", []),
            transceiver_product_family=kwargs.get("transceiver_product_family", []),
            transceiver_product_id=kwargs.get("transceiver_product_id", []),
            network_device_product_family=kwargs.get(
                "network_device_product_family", []
            ),
            network_device_product_id=kwargs.get("network_device_product_id", []),
        )
        return TMGResult(results)

    def search_device(self, search_device):
        """
        Performs a search for a network device.

        This method performs a simple search for all transceivers supported by
        a specific network device. This is akin to using the "search bar"
        functionality on Cisco's official web application.

        :param str search_device: The PID/model number of the Cisco network
            device that you would like to search for.

        :Examples:

        >>> from pytmg import TMG
        >>> tmg = TMG.TMG()
        >>> tmg_res = tmg.search_device("N9K-C93180YC-EX")

        >>> from pytmg import TMG
        >>> tmg = TMG.TMG()
        >>> tmg_res = tmg.search_device("WS-C2960")
        """
        search_terms = {"search_input": [search_device]}
        res = self.search(**search_terms)
        return res

    def search_devices(self, search_devices):
        """
        Performs a search for multiple network devices.

        This method performs a simple search for all transceivers supported by
        a list of specific network devices. This is akin to adding multiple
        network devices to the "search bar" on Cisco's official web
        application.

        :param list search_devices: A list of PIDs/model numbers of Cisco
            network devices that you would like to search for.
        
        :Examples:

        >>> from pytmg import TMG
        >>> tmg = TMG.TMG()
        >>> device_list = [
        ...     "N9K-C93180YC-EX",
        ...     "WS-C2960",
        ...     "WS-C3750",
        ... ]
        >>> tmg_res_list = tmg.search_devices(device_list)
        >>> len(tmg_res_list)
        3
        """
        tmg_results = []
        for device in search_devices:
            res = self.search_device(device)
            tmg_results.append(res)
        return tmg_results
