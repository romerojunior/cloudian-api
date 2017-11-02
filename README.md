WiP: Cloudian™ Rest API Client
========================

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

This python package is a working in progress, still not suitable for production. Feel free to contribute by either making a PR or creating a new issue.

How it works
------------

All Cloudian™ Hyperstore Admin API endpoints are dynamically mapped through `cloudianapi.components` package, however, currently only the HTTP GET method is supported (DELETE and POST methods are expected to be implemented soon). Each call, such as `client.monitor.nodelist()`, returns a JSON encoded string that could easily be parsed to any data structure.

Fix me & To do
--------------

* Parent calls such as client.monitor() are broken, needs attention;
* If any API call returns a plain-text string instead of JSON encoded string the code breaks, this needs proper handling;
* HTTP support to methods POST and DELETE needs to be implemented;
* Better error handling on module `cloudianapi.core.requestors` is needed;
* Metadata about package needs to be added (versioning, author, etc).
