from employee.models import Employee,Worksite, Item
from rest_framework.decorators import action
from rest_framework import viewsets, permissions
from .serializers import EmployeeSerializer, WorksiteSerializer, ItemSerializer
from employee.models import Worksite
from django.http import JsonResponse


# class IsOwnerOrReadOnly(permissions.BasePermission):

#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj == request.user





class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.filter(owner=self.request.user)

    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



    
    # queryset = Employee.objects.all().order_by('id')
    # serializer_class = EmployeeSerializer
    # permission_classes=(IsOwnerOrReadOnly,)
    

    
    
 


 # filter was filtering by owner_id which was not being saved and thus not returning any of the worksites 
#  so instead request all object with no filter

class WorksiteViewSet(viewsets.ModelViewSet):
    serializer_class = WorksiteSerializer

    def get_queryset(self):
        return Worksite.objects.filter(owner=self.request.user)

        #  the line below this returns all worksites regardless of owner and no filters 
        # return Worksite.objects.all()
    
    def perform_create(self, serializer):
         serializer.save(owner=self.request.user)





    # permission_classes=(IsOwnerOrReadOnly,)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


#  just tried this but gave error trying to find item_set key?

    # class ItemViewSet(viewsets.ModelViewSet):
    #     serializer_class = ItemSerializer
    #     def get_queryset(self):
    #         return Item.objects.filter(owner=self.request.user)



class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    





    # Employee.objects.all().order_by('id')

    # Worksite.objects.all().order_by('name')

    # Item.objects.all()

