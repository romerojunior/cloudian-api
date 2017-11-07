WiP: Cloudian™ REST Admin API Client
====================================

Example
-----

```
client = CloudianAPIClient(
    url=None
    user=None,
    key=None,
    port=None
)

print client.monitor.host(nodeId="storage-node01")
print client.monitor.nodelist()
print client.monitor.events(nodeId="storage-node01", region="eu-west-1")
print client.monitor.notificationrules(region="eu-west-1")
print client.system.license()
print client.group.list()
print client.user.list(groupId="CustomerABC", userType="all", userStatus="active")
```


Work in Progress
----------------

This python package is a working in progress, although suitable for testing environments and production, it still has limited features (check **Fix Me & To do**). Feel free to contribute by either making a PR or creating a new issue.

How to install
--------------

Simply run:

```
pip install cloudianapi
```

How it works
------------

All Cloudian™ Hyperstore Admin API endpoints are dynamically mapped through `cloudianapi.components` package in a object-oriented approach, however, currently only the HTTP GET method is supported (DELETE and POST methods are expected to be implemented soon). Each call, such as `client.monitor.nodelist()`, returns a JSON compatible dictionary that could easily be parsed to any data structure. All API calls parameters (such as nodeId, region, userType and so on) are case sensitive, check your Cloudian™ Admin API documentation for more details.

Fix me & To do
--------------

* Test across multiple platforms;
