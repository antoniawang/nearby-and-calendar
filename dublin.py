import json
import math
import os

DUBLIN_LAT_RADIANS = math.radians(53.3381985) 
DUBLIN_LON_RADIANS = math.radians(-6.2592576)

EARTH_RADIUS = 6371 # Earth's radius in km


def calc_km_from_dublin(lat, lon):
	""" Function which uses the Haversine formula for calculating spherical distances
		to determine each customer's km from Dublin based on his/her lat, lon """

	lat_radians = math.radians(float(lat))
	lon_radians = math.radians(float(lon))
	
	km_from_dublin = EARTH_RADIUS * 2 * math.asin( math.sqrt ( math.sin( math.fabs( DUBLIN_LAT_RADIANS - lat_radians ) / 2 ) ** 2 + ( math.cos( DUBLIN_LAT_RADIANS ) * math.cos( lat_radians ) * math.sin( math.fabs( DUBLIN_LON_RADIANS - lon_radians ) / 2 ) ** 2 )) )

	return km_from_dublin

def is_near_dublin(entry):
	""" Function which returns a boolean:
		True if customer is within 100 km of Dublin """

	return calc_km_from_dublin(entry["latitude"], entry["longitude"]) < 100

def find_nearby_customers():
    """ Reads in customers.txt and returns the list customers 
    who are within 100 km of Dublin, sorted by ID. """

    mydir = os.path.dirname(__file__)
    customers_file = os.path.join(mydir, "customers.txt")
    with open(customers_file, 'r') as fp:
        file_data = fp.readlines()

        customer_dict_list = [json.loads(entry) for entry in file_data if len(entry) > 0]
        filtered_list = sorted(filter(is_near_dublin, customer_dict_list, key=lambda k: int(k[0]))
        #my_list = sorted([tuple([entry["user_id"], entry["name"], calc_km_from_dublin(entry["latitude"], entry["longitude"])]) for entry in mydict_list if calc_km_from_dublin(entry["latitude"], entry["longitude"]) < 100], key=lambda k: int(k[0]))
        

    return names_and_ids_list


print find_nearby_customers()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("search", metavar = "search", type = str, nargs = "*", help = "search term for contacts")

    args = parser.parse_args()
    nearby_customers = find_nearby_customers()

    if len(rankings) == 0:
        print "No customers within 100 km found" # Print this message if no contact matches found.
    else:
        print json.dumps(rankings, indent=4, separators=(", ", ": ")) # Python dictionaries have no inherent order, so entries within each contact will have different order from original. 

