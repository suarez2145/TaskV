from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model




class Worksite(models.Model):
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200, null=True)
    contact_info = models.CharField(max_length=200, null=True)
    codes_notes = models.TextField(null=True, blank=True)
    owner = models.ForeignKey('auth.User', default=None, null=True,blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name




class Item(models.Model):
    item_text = models.CharField(max_length=30)
    is_complete = models.BooleanField("complete", default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    worksite = models.ForeignKey( Worksite, on_delete=models.CASCADE)
    



    def __str__(self):
        return self.item_text

    def complete_or_not(self):
        return self.is_complete







class Employee(models.Model):
    STANDARD = 'STD'
    MANAGER = 'MGR'
    SR_MANAGER = 'SRMGR'
    PRESIDENT = 'PRES'

    EMPLOYEE_TYPES = (
        (STANDARD, 'base employee'),
        (MANAGER, 'manager'),
        (SR_MANAGER, 'senior manager'),
        (PRESIDENT, 'president')
    )
    
    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES)
    name = models.CharField(max_length=50)
    manager = models.ForeignKey('self',null=True,blank=True, related_name='employee', on_delete=models.CASCADE)
    worksite = models.ManyToManyField(Worksite, blank=True,)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return self.__str__()


