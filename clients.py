import meraki
import csv

api_key = '***'
org_id = '***'

dashboard = meraki.DashboardAPI(api_key, suppress_logging = True)

with open('clients.csv', 'w', newline = '') as csvfile:
    export = csv.DictWriter(csvfile, [
      # comment out what you don't want in the csv
                                      'network_id', 'network_name',
                                      'usage',
                                      'description',
                                      'mac',
                                      'ip',
                                      'user',
                                      'vlan',
                                      'namedVlan',
                                      'switchpor',
                                      'adaptivePolicyGroup',
                                      'ip6',
                                      'firstSeen',
                                      'lastSeen',
                                      'manufacturer',
                                      'os',
                                      'deviceTypePrediction',
                                      'recentDeviceSerial',
                                      'recentDeviceName',
                                      'recentDeviceMac',
                                      'recentDeviceConnection',
                                      'ssid',
                                      'status',
                                      'notes',
                                      'ip6Local',
                                      'smInstalled',
                                      'groupPolicy8021x'
                                      ], 
                            extrasaction = 'ignore'
                            )
    export.writeheader()
    networks = dashboard.organizations.getOrganizationNetworks(org_id, total_pages = -1)
    for network in networks:
        clients = dashboard.networks.getNetworkClients(networkId=network['id'], total_pages = -1)
        [export.writerow({'network_id': network['id'], 'network_name': network['name'], **client}) for client in clients]
