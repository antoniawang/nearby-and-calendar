import json
import math
import os


# Declare constants
DUBLIN_LAT_RADIANS = math.radians(53.3381985) 
DUBLIN_LON_RADIANS = math.radians(-6.2592576)

EARTH_RADIUS = 6371 # earth's radius in km
NEARBY_DIST = 100 # nearby defined as within 100 km



def calc_km_from_dublin(entry):
	""" Function which uses the Haversine formula for calculating spherical distances
		to determine each customer's km from Dublin based on his/her lat, lon """

	# convert lat, lon degrees to radians
	lat_radians = math.radians(float(entry["latitude"]))
	lon_radians = math.radians(float(entry["longitude"]))
	
	km_from_dublin = EARTH_RADIUS * 2 * math.asin( math.sqrt ( math.sin( math.fabs( DUBLIN_LAT_RADIANS - lat_radians ) / 2 ) ** 2 
		+ ( math.cos( DUBLIN_LAT_RADIANS ) * math.cos( lat_radians ) * math.sin( math.fabs( DUBLIN_LON_RADIANS - lon_radians ) / 2 ) ** 2 )) )

	return km_from_dublin

def is_near_dublin(entry):
	""" Function which returns a boolean:
		True if customer is within 100 km of Dublin """

	return calc_km_from_dublin(entry) <= NEARBY_DIST

def is_float(value):
	""" Function which checks if lat, lon strings
		can be converted to valid floats """
	try:
  		float(value)
  		return True
  	except ValueError:
  		return False

def is_entry_valid(entry):
	""" Function which checks if entry is well-formed """

	# check that all entries have relevant data
	if "user_id" not in entry or "name" not in entry or "latitude" not in entry or "longitude" not in entry:
		return False

	# check that lat, lon strings can be converted into valid floats
	if not is_float(entry["latitude"]) or not is_float(entry["longitude"]):
		return False

	return True


def find_nearby_customers():
    """ Reads in customers.txt and returns the list customers 
    who are within nearby distance (100 km) of Dublin, sorted by ID. """

    mydir = os.path.dirname(__file__)
    customers_file = os.path.join(mydir, "customers.txt")
    with open(customers_file, 'r') as fp:
        file_data = fp.readlines()

        customer_dict_list = filter(is_entry_valid, [json.loads(entry) for entry in file_data if len(entry) > 0]) # check for valid entry and ignore blank lines in txt file
        filtered_list = sorted(filter(is_near_dublin, customer_dict_list), key=lambda k: k['user_id']) # filter for nearby customers and sort results by user_id

    return filtered_list


if __name__ == '__main__':
    nearby_customers = find_nearby_customers()

    if len(nearby_customers) == 0:
        print "No customers within 100 km found" # Print this message if no nearby customers found.
    else:
    	print "The following customers are nearby: \n", "\n".join([", ".join([entry["name"], str(entry["user_id"])]) for entry in nearby_customers])


