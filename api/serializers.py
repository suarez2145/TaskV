from django.contrib.auth.models import User
from employee.models import Employee, Worksite, Item
from rest_framework import serializers, fields


class WorksiteSerializer(serializers.HyperlinkedModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedRelatedField(
        view_name='worksite:detail',
        read_only=True
    )
    
    class Meta:
        model = Worksite
        fields = ['url','id','name','address','item_set','owner', 'contact_info', 'codes_notes']
        



class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = ["id","item_text", "is_complete", "created_date", "worksite"]







class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    manager = serializers.SlugRelatedField(queryset=Employee.objects.all(), slug_field='name', allow_null=True,)
    worksite = WorksiteSerializer(many=True, read_only=True)
    worksite_id = serializers.PrimaryKeyRelatedField(queryset=Worksite.objects.all(), many=True, source="worksite", allow_null=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedRelatedField(
        view_name='employee:detail',
        read_only=True
    )

    class Meta:
        model = Employee
        fields = ["url","id","name", "role", "manager", "worksite","worksite_id",'owner','owner_id']







   













    # def get_manager_from_employee_list(self, employee):
    #     manager = employee.manager
    #     return manager



    


        # manager_info = EmployeeManagerSerializer(source="*")

        #  manager = serializers.SlugRelatedField(queryset=Employee.objects.all(), slug_field='name', allow_null=True)
        # manager = serializers.StringRelatedField(source="manager.name", read_only=False)
        # manager = serializers.SerializerMethodField("get_manager_from_employee_list")