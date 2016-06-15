from django.db import models

# Create your models here.
class MobileDetail(models.Model):
	device_name = models.CharField('Device Name', max_length=50, default="", null=False)
	device_url = models.CharField('Device Url', max_length=500, default="", null=False)
	source_website = models.CharField('Website', max_length=50, default="", null=False,)
	price = models.FloatField('Current Price')
	manufacturer = models.CharField(default='Samsung', max_length=50)
	
class UserDetail(models.Model):    
	user_name = models.CharField('User Name', max_length=50, default="", null=False)
	user_email = models.CharField('user email', max_length=50, null=False)
	
class UserDevice(models.Model):    
	device_name = models.ForeignKey(MobileDetail, on_delete=models.CASCADE)
	minimum_price = models.FloatField('Price range')
	user_name = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
	
	#class Meta:
	#	unique_together = (user_id, device_id