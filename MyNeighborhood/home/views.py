from django.shortcuts import render
import requests
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST', 'DATA'])
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

	return Response(complaint_list)

@api_view(['GET'])
def complaint_types(request):
	"""
	returns the unique complaint types for the 1000 issues pulled from SODA API with no filters or queries
	"""
	type_set = set()
	complaints = requests.get('http://data.cityofnewyork.us/resource/erm2-nwe9.json?$select=complaint_type').json()

	for c_type in complaints:
		type_set.add(c_type['complaint_type'])

	return Response(type_set)


def gen_bar_data(request):
	conplaints=conplaint_types()
	complaint_set=set(complaints)
	num_complaints={}
	for c in complaint_set:
		temp_dict={}
		temp_dict['label']=c
		temp_dict['value']=(complaints.count(c)/len(complaints))*100
		num_complaints.append(temp_dict)
	return num_complaints

