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

    def _validate_cable_type(self, cable_types):
        if not cable_types:
            return cable_types
        valid_cable_types = CABLE_TYPE_FILTERS
        validated_cable_types = []
        for cable_type in cable_types:
            validated_cable_types += [
                ct for ct in valid_cable_types if ct["name"] == cable_type
            ]
        if validated_cable_types:
            return validated_cable_types
        else:
            raise ValueError(f'Invalid Cable Types "{cable_types}" specified')

    def _validate_data_rate(self, data_rates):
        if not data_rates:
            return data_rates
        valid_data_rates = DATA_RATE_FILTERS
        validated_data_rates = []
        for data_rate in data_rates:
            validated_data_rates += [dr for dr in valid_data_rates if dr["name"] == data_rate]
        if validated_data_rates:
            return validated_data_rates
        else:
            raise ValueError(f'Invalid Data Rates "{data_rates}" specified')

    def _validate_form_factor(self, form_factors):
        if not form_factors:
            return form_factors
        valid_form_factors = FORM_FACTOR_FILTERS
        validated_form_factors = []
        for form_factor in form_factors:
            validated_form_factors += [
                ff for ff in valid_form_factors if ff["name"] == form_factor
            ]
        if validated_form_factors:
            return validated_form_factors
        else:
            raise ValueError(f'Invalid Form Factors "{form_factors}" specified')

    def _validate_reach(self, reaches):
        if not reaches:
            return reaches
        valid_reaches = REACH_FILTERS
        validated_reaches = []
        for reach in reaches:
            validated_reaches += [r for r in valid_reaches if r["name"] == reach]
        if validated_reaches:
            return validated_reaches
        else:
            raise ValueError(f'Invalid Reaches "{reaches}" specified')

    def _validate_os_type(self, os_types):
        if not os_types:
            return os_types
        valid_os_types = OS_TYPE_FILTERS
        validated_os_types = []
        for os_type in os_types:
            validated_os_types += [os for os in valid_os_types if os["name"] == os_type]
        if validated_os_types:
            return validated_os_types
        else:
            raise ValueError(f'Invalid OS Types "{os_types}" specified')

    def _validate_transceiver_product_family(self, transceiver_product_families):
        if not transceiver_product_families:
            return transceiver_product_families
        valid_xcvr_product_families = XCVR_PRODUCT_FAMILY_FILTERS
        validated_pfs = []
        for transceiver_product_family in transceiver_product_families:
            validated_pfs += [
                pf
                for pf in valid_xcvr_product_families
                if pf["name"] == transceiver_product_family
            ]
        if validated_pfs:
            return validated_pfs
        else:
            raise ValueError(
                f'Invalid Transceiver Product Families "{transceiver_product_families}" specified'
            )

    def _validate_transceiver_product_id(self, transceiver_product_ids):
        if not transceiver_product_ids:
            return transceiver_product_ids
        valid_xcvr_product_ids = XCVR_PRODUCT_ID_FILTERS
        validated_pids = []
        for transceiver_product_id in transceiver_product_ids:
            validated_pids += [
                pid
                for pid in valid_xcvr_product_ids
                if pid["name"] == transceiver_product_id
            ]
        if validated_pids:
            return validated_pids
        else:
            raise ValueError(
                f'Invalid Transceiver Product IDs "{transceiver_product_ids}" specified'
            )

    def _validate_network_device_product_family(self, network_device_product_families):
        if not network_device_product_families:
            return network_device_product_families
        valid_device_product_families = NETWORK_DEVICE_PRODUCT_FAMILY_FILTERS
        validated_pfs = []
        for network_device_product_family in network_device_product_families:
            validated_pfs += [
                pf
                for pf in valid_device_product_families
                if pf["name"] == network_device_product_family
            ]
        if validated_pfs:
            return validated_pfs
        else:
            raise ValueError(
                f'Invalid Network Device Product Families "{network_device_product_families}" specified'
            )

    def _validate_network_device_product_id(self, network_device_product_ids):
        # TODO: Not yet supported. Need to reverse-engineer how TMG utilizes this field.
        if not network_device_product_ids:
            return network_device_product_ids
        else:
            raise ValueError(
                f'Invalid Network Device Product ID "{network_device_product_ids}" specified'
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
