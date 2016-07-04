import unittest

import near_dublin

class TestRankings(unittest.TestCase):

	def test_SF_km(self):
		""" Test if the distance between San Francisco
			and Dublin rounds to 8178 kms """

		SF_entry = { "latitude": "37.7634475", "user_id": 101, "name": "Anchor Steam", "longitude": "-122.4034693" }	
		expected = 8178

		self.assertEquals(int(round(near_dublin.calc_km_from_dublin(SF_entry))), expected)


	def test_SF_near_dublin(self):
		""" Test that SF is not within 100 km of Dublin """

		SF_entry = { "latitude": "37.7634475", "user_id": 101, "name": "Anchor Steam", "longitude": "-122.4034693" }
		expected = False

		self.assertEquals(near_dublin.is_near_dublin(SF_entry), expected)


	def test_num_customers_near_dublin(self):
		""" Test that 16 customers are within 100 km of Dublin """
		
		expected = 16
		self.assertEquals(len(near_dublin.find_nearby_customers()), expected)


	def test_sorted_by_userid(self):
		""" Test that the nearby customers list
			is sorted by user_id, 
			i.e. the first returned entry has user_id 4 """

		expected = 4

		self.assertEquals(near_dublin.find_nearby_customers()[0]["user_id"], expected)


if __name__ == "__main__":
	unittest.main()