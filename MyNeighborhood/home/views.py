from django.shortcuts import render
import requests
import json

# Create your views here.
"""
get the complaints for the filter options selected
"""
def complaints(zipcode, complaint_type):
	print (zipcode)
	print (complaint_type)
	string = 'http://data.cityofnewyork.us/resource/erm2-nwe9.json?'+ '$select=latitude,longitude&incident_zip=' + zipcode + '&complaint_type=' + complaint_type
	complaints = requests.get(string).json()
	print (complaints)

	complaint_list = []
	for c in complaints:
		if 'latitude' in c and 'longitude' in c:
			complaint_list.append( (c['latitude'], c['longitude']) )

	return complaint_list

"""
returns the unique complaint types for the 1000 issues pulled from SODA API with no filters or queries
"""
def complaint_types():
	type_set = set()
	complaints = requests.get('http://data.cityofnewyork.us/resource/erm2-nwe9.json?$select=complaint_type').json()

	for c_type in complaints:
		type_set.add(c_type['complaint_type'])

	return type_set
