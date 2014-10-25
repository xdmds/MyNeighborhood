from django.shortcuts import render
import requests

# Create your views here.
"""
get the complaints for the filter options selected
"""
def get_complaints(zipcode, complaint_type, address, date_created, latitude, longitude, status){
	complaints = requests.get('http://data.cityofnewyork.us/resource/erm2-nwe9.json?'
						+ 'incident_zip=' + zipcode
						+ 'complaint_type=' + complaint_type
						+ 'incident Address=' + address
						+ 'created_date=' + date_created
						+ 'latitude=' + latitude
						+ 'longitude=' + longitude
						+ 'status=' + status
					)
	return complaints
}