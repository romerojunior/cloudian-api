WIP: Cloudian Rest API
======================

Usage
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

This python package is a working in progress, still not suitable for production.


Fix me
------

* parent calls such as: client.monitor() are broken
* if any API call doesn't return a json the code breaks
* support to HTTP methods POST and DELETE need to be implemented
