# coding: utf-8

from pycti import OpenCTIApiClient

# Variables
api_url = "https://greenmountains.octi.filigran.io:4000"
api_token = "88a71cb8-0e85-4b4d-bc83-34f7c8615b67"

# OpenCTI initialization
opencti_api_client = OpenCTIApiClient(api_url, api_token)

# Exact IP match
opencti_api_client.stix_cyber_observable.create(
    simple_observable_key="IPv4-Addr.value", simple_observable_value="110.172.180.180"
)
print("IP ADDRESS")
observable = opencti_api_client.stix_cyber_observable.read(
    filters={
        "mode": "and",
        "filters": [{"key": "value", "values": ["110.172.180.180"]}],
        "filterGroups": [],
    }
)
print(observable)

