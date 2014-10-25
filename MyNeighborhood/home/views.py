from django.shortcuts import render
import requests
import json


@api_view(['DATA'])
def complaints(request):
	"""
	get the complaints for the filter options selected
	"""
	data = request.DATA
	zipcode = data['zipcode']
	complaint_type = data['complaint_type'] 
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

def complaint_types():
	"""
	returns the unique complaint types for the 1000 issues pulled from SODA API with no filters or queries
	"""
	type_set = set()
	complaints = requests.get('http://data.cityofnewyork.us/resource/erm2-nwe9.json?$select=complaint_type').json()

	for c_type in complaints:
		type_set.add(c_type['complaint_type'])

	return type_set
