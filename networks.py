import meraki
import csv

api_key = '***'
org_id = '***'

dashboard = meraki.DashboardAPI(api_key, suppress_logging = True)
with open('networks.csv', 'w', newline = '') as csvfile:
    export = csv.DictWriter(csvfile, [
        # comment out what you don't want in the csv'id',
                                      'organizationId',
                                      'name',
                                      'timeZone',
                                      'tags',
                                      'productTypes',
                                      'enrollmentString',
                                      'notes',
                                      'isBoundToConfigTemplate',
                                      ], 
                            extrasaction = 'ignore'
                            )
    export.writeheader()
    networks = dashboard.organizations.getOrganizationNetworks(org_id, total_pages = -1)
    for network in networks:
        export.writerow(network)
