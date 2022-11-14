from wfs import get_wfs
from uldk import uldk_to_csv, uldk_to_postgis
from postgis import connection, wkt_to_postgis

url = 'https://geoportal.powiat.kielce.pl/map/geoportal/wfs.php' 
service = 'WFS'
request = 'GetFeature'
version = '2.0.0'
typenames = 'ewns:dzialki'
bbox = '324922,607897,326156,611727'
srsname = 'EPSG:2180'

# get_wfs(url, service, request, version, typenames, bbox, srsname)


csv = 'radko.csv'
metoda = 'GetParcelById'
#metoda = 'GetAggregateArea'
format = 'geom_wkt'
# format = 'geom_extend'
output = 'radko.wkt'

# uldk_to_csv(csv, metoda, format, output)


bazaTest = connection('użytkownik', 'hasło', 'ip', 'port', 'nazwa_bazy')
uldk_to_postgis(csv, metoda,format,bazaTest,'plots')
