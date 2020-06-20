#!/usr/bin/env python3
from pyzabbix import ZabbixAPI
import sys

zapi = ZabbixAPI("http://!!ID_ZABBIX_SERVER_CONTAINER")
zapi.login("!!API_ZABBIX_USER", "!!API_ZABBIX_PASSWORD")
print("Connected to Zabbix API Version %s" % zapi.api_version())

host_name = sys.argv[1]
varname = zapi.host.get(filter={"host": host_name}, selectInventory=["alias"])
if varname:
    host_alias = varname[0]["inventory"]["alias"]
    print("Host alias: {0}".format(host_alias))

hosts = zapi.host.get(filter={"host": host_name}, selectInterfaces=["interfaceid"])
if hosts:
    host_id = hosts[0]["hostid"]
    print("Found host id {0}".format(host_id))

    try:
        item = zapi.host.update(
            hostid=host_id,
            name=host_alias
        )
    except ZabbixAPIException as e:
        print(e)
        sys.exit()
    print("Old:" ,host_name, "New:" ,host_alias)
else:
    print("No hosts found")
