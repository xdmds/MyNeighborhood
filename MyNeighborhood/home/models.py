from django.db import models

class Complaint(model.Model):
	address=models.CharField(max_length=50)
	date_time=models.DatetimeField()
	#zip_code=models.SmallIntegerField()
	complaint_type=models.ForeignKey(Grouping)


class Grouping(model.Model):
	complaint_type=models.CharField(max_length=20)
	num_comps=models.SmallIntegerField()
	location=models.ForeignKey(Location)

class Location(model.Model):
	zip_code=models.SmallIntgerField()

