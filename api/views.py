from django.shortcuts import render
from rest_framework import viewsets
from .models import AssetType, Assets, Tickets, Distributor, PaymentType, Payments, Priorities, Rolemapping, Roles, Supplier, TicketStatus, Users  
from .serializers import AssetTypeSerializer, AssetsSerializer, TicketsSerializer, DistributorSerializer, PaymentTypeSerializer, PaymentsSerializer, PrioritiesSerializer, UsersSerializer, TicketStatusSerializer, RolemappingSerializer, RolesSerializer, SupplierSerializer
from django_filters.rest_framework import DjangoFilterBackend


from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
# Create your views here.

class AssetTypeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = AssetType.objects.all()
    serializer_class = AssetTypeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('asset_type_id','asset_type_name')

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'status':True,'assets_type': serializer.data})


class AssetsViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer
    filter_backends = (DjangoFilterBackend,)
    #filterset_fields = ('barcode','asset_id')
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            data = {'status':True, 'msg':'Submitted Successfuly','assets':[{'asset_id':serializer.data['asset_id']}]}
            return Response(data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'status':False,'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


    def list(self, request, *args, **kwargs):
       self.object_list = self.filter_queryset(self.get_queryset())
       serializer = self.get_serializer(self.object_list, many=True)
       query_params = request.query_params
       if query_params:
           barcode= request.query_params.get('barcode')
           asset_id = request.query_params.get('asset_id')
           print("barcode",request.query_params)

           q_barcode = Assets.objects.filter(barcode=barcode)
           q_asset_id = Assets.objects.filter(asset_id=asset_id)

           if q_asset_id:
              q_obj_list = list(Assets.objects.filter(asset_id=asset_id))
              print('list',q_obj_list)
              serializer = self.get_serializer(q_obj_list, many=True)
              return Response({'assets':serializer.data})
           elif q_barcode:
              q_obj_list = list(Assets.objects.filter(barcode=barcode))
              print('list-bar',q_obj_list)
              serializer = self.get_serializer(q_obj_list, many=True)
              return Response({'status':True,'assets':serializer.data})
           else:
                return Response({'status':False,'msg':'Invalid Credentials'})

       return Response({'status':True,'assets':serializer.data})

class TicketsViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer
    filter_backends = (DjangoFilterBackend,)
    #filterset_fields = ('user_id','ticket_id','asset_id')

    # @action(methods=['post'], detail=False)
    # def register(self,request):
    #     serializer = self.serializer_class(data=request.GET)
    #     print("request",self.request.query_params)
    #     print("request method",serializer)
       
       
    #     if serializer.is_valid():
    #         serializer.save()
    #         print("inside")
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response({"Successfuly":serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            data = {'status':True, 'msg':'Submitted Successfuly','tickets':[{'ticket_id':serializer.data['ticket_id']}]}
            return Response(data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'status':False,'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


    def list(self, request, *args, **kwargs):
       self.object_list = self.filter_queryset(self.get_queryset())
       serializer = self.get_serializer(self.object_list, many=True)
       query_params = request.query_params
       if query_params:
           user_id = request.query_params.get('user_id')
           asset_id = request.query_params.get('asset_id')
           location = request.query_params.get('location')
           priority = request.query_params.get('priority')
           ticket_id = request.query_params.get('ticket_id')

           print("params",request.query_params)


           q_user_id = Tickets.objects.filter(user_id=user_id)
           q_asset_id = Tickets.objects.filter(asset_id=asset_id)
           q_location = Tickets.objects.filter(location=location)
           q_priority = Tickets.objects.filter(priority=priority)
           q_ticket_id = Tickets.objects.filter(ticket_id=ticket_id)

           if q_ticket_id:
              q_obj_list = list(Tickets.objects.filter(ticket_id=ticket_id))
              serializer = self.get_serializer(q_obj_list, many=True)
              return Response({'tickets':serializer.data})
           elif q_asset_id:
              q_obj_list = list(Tickets.objects.filter(asset_id=asset_id))
              serializer = self.get_serializer(q_obj_list, many=True)
              return Response({'tickets':serializer.data})
           elif q_location:
              q_obj_list = list(Tickets.objects.filter(location=location))
              serializer = self.get_serializer(q_obj_list, many=True)
              return Response({'tickets':serializer.data})
           elif q_priority:
              q_obj_list = list(Tickets.objects.filter(priority=priority))
              serializer = self.get_serializer(q_obj_list, many=True)
              return Response({'tickets':serializer.data})
           elif q_user_id:
              q_obj_list = list(Tickets.objects.filter(user_id=user_id))
              serializer = self.get_serializer(q_obj_list, many=True)
              return Response({'status':True,'tickets':serializer.data})            
           else:
                return Response({'status':False,'msg':'Invalid Credentials'})

       return Response({'status':True,'tickets':serializer.data})

class DistributorViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('distributor_id','name')

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'status':True,'distributors': serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            data = {'status':True, 'msg':'Registered Successfuly'}
            return Response(data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'status':False,'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)            

class PaymentTypeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('payment_type_id',)

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'status':True,'payment_types': serializer.data})    

class PaymentsViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('asset_id','payment_id','ticket_id')  

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'status':True,'payments': serializer.data})  

class PrioritiesViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Priorities.objects.all()
    serializer_class = PrioritiesSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('priority_id',)    

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'status':True,'priorities': serializer.data})

class RolemappingViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Rolemapping.objects.all()
    serializer_class = RolemappingSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('rolemapping_id','user_id','role_id')  

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'status':True,'role_mappings': serializer.data})          


class RolesViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('role_id','role_name')   

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'status':True,'roles': serializer.data}) 

class SupplierViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('supplier_id','distributor_id')   

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'status':True,'suppliers': serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            data = {'status':True, 'msg':'Registered Successfuly'}
            return Response(data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'status':False,'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST) 

class TicketStatusViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = TicketStatus.objects.all()
    serializer_class = TicketStatusSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('ticket_status_id',)    

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'status':True,'tickets_status': serializer.data})

class UsersViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = (DjangoFilterBackend,)
    #filterset_fields = ('user_id','name','email','password')

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data,)
    # @action(methods=['get'], detail=True)
    # def home(self,request, pk=None):
    #     print("request", pk)
    #     return Response("Successfuly")

    # def get_queryset(self):
    #     name= self.request.query_params.get('name')
    #     password= self.request.query_params.get('password')
    #     print("name {}, password {}".format(name,password))
    #     queryset = Users.objects.all()
    #     if self.action=='list':
    #         q_obj = Users.objects.filter(name=name,password=password)
    #         if q_obj:
    #             q_obj_list = list(Users.objects.filter(name=name,password=password))
    #             print(q_obj_list[0].status)
    #             queryset = q_obj
    #         else:
    #             print("set",q_obj)
    #             queryset = q_obj
    #     return queryset
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            print("Result",serializer.data)
            data = {'status':True, 'msg':'Registered Successfuly'}
            return Response(data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            print("else case")
            return Response({'status':False,'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


    def list(self, request, *args, **kwargs):
       self.object_list = self.filter_queryset(self.get_queryset())
       serializer = self.get_serializer(self.object_list, many=True)
       query_params = request.query_params
       if query_params:
           email= request.query_params.get('email')
           password= request.query_params.get('password')

           q_obj = Users.objects.filter(email=email,password=password)
           if q_obj:
              q_obj_list = list(Users.objects.filter(email=email,password=password))
              serializer = self.get_serializer(q_obj_list, many=True)
              return Response({'status':True,'users':serializer.data})
           else:
                return Response({'status':False,'msg':'Invalid Credentials'})

       return Response({'status':True,'users':serializer.data})

