from django.db import models

# Create your models here.
class Emplyoee(models.Model):
	emplyoee_name=models.CharField(max_length=50)
	emplyoee_id=models.IntegerField(default=0)
	emplyoee_address=models.CharField(max_length=50)
	salary=models.IntegerField(default=0)

class Production(models.Model):
	current_time=models.DateField(null=True)
	shift=models.CharField(max_length=50)
	total_production=models.IntegerField(default=0)
	machine_in_use=models.IntegerField(default=0)

class Machine(models.Model):
	machine_id=models.IntegerField(default=0)
	status=models.CharField(max_length=60)
	current_output=models.IntegerField(default=0)
	last_maintainance=models.DateField(null=True)

class Shift(models.Model):
	shift=models.CharField(max_length=60)
	date=models.DateField(null=True)
	production_output=models.IntegerField(default=0)
	issues=models.TextField()

	
class Maintainance(models.Model):
	machine=models.IntegerField(default=0)
	upcoming_maintainance=models.DateField(null=True)
	recent_maintainance=models.DateField(null=True)

class Order(models.Model):
	date_placed=models.DateField(null=True)
	customer_name=models.CharField(max_length=60)
	contact_number=models.IntegerField(default=0)
	address=models.CharField(max_length=60)
	product_name=models.CharField(max_length=50)
	quantity=models.IntegerField(null=True)
	total_price=models.IntegerField(default=0)
	payment_method=models.CharField(max_length=60)
	total_paid=models.IntegerField(default=0)
	delivery_status=models.CharField(max_length=60)
	expected_del=models.DateField(null=True)	