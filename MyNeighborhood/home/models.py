from django.db import models

class Location(models.Model):
	"""
	Location is the higest level of division, and is the 
	first sorting the user completes
	"""
	zip_code=models.SmallIntegerField()

class Complaint_type(models.Model):
	"""
	Complaint_type represents the grouping of complaints by type,
	specific to the location
	"""
	category=models.CharField(max_length=20)
	num_comps=models.SmallIntegerField()
	location=models.ForeignKey(Location)

class Complaint(models.Model):
	"""
	Complaint is the leaf of the graph, and holds the
	incident-specific data
	"""
	address=models.CharField(max_length=50)
	date_time=models.DateTimeField()
	complaint_type=models.ForeignKey(Complaint_type)
	status=models.CharField(max_length=20)
	x_coor=models.IntegerField()
	y_coor=models.IntegerField()


