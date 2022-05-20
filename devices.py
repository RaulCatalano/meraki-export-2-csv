import meraki
import csv

api_key = '***'
org_id = '***'

dashboard = meraki.DashboardAPI(api_key, suppress_logging=True)

with open('devices.csv', 'w', newline = '') as csvfile:
    export = csv.DictWriter(csvfile, [
      # comment out what you don't want in the csv
                                      'network_id', 'network_name',
                                      'name',
                                      'lat',
                                      'lng',
                                      'serial',
                                      'mac',
                                      'model',
                                      'address',
                                      'notes',
                                      'lanIp',
                                      'tags',
                                      'networkId',
                                      'beaconIdParams',
                                      'firmware',
                                      'floorPlanId',
                                      ], 
                            extrasaction = 'ignore'
                            )
    export.writeheader()
    networks = dashboard.organizations.getOrganizationNetworks(org_id, total_pages = -1)
    for network in networks:
      devices = dashboard.networks.getNetworkDevices(networkId=network['id'])
      for device in devices:
        [export.writerow({'network_id': network['id'], 'network_name': network['name'], **device}) for device in devices]