from api.views import AssetTypeViewSet, AssetsViewSet, TicketsViewSet, DistributorViewSet, PaymentTypeViewSet, PaymentsViewSet, PrioritiesViewSet, RolemappingViewSet, RolesViewSet, SupplierViewSet, TicketStatusViewSet, UsersViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(prefix='tickets', viewset=TicketsViewSet)
router.register(prefix='assets-type', viewset=AssetTypeViewSet)
router.register(prefix='assets', viewset=AssetsViewSet)
router.register(prefix='distributor', viewset=DistributorViewSet)
router.register(prefix='paymenttype', viewset=PaymentTypeViewSet)
router.register(prefix='payments', viewset=PaymentsViewSet)
router.register(prefix='priorities', viewset=PrioritiesViewSet)
router.register(prefix='rolemapping', viewset=RolemappingViewSet)
router.register(prefix='roles', viewset=RolesViewSet)
router.register(prefix='supplier', viewset=SupplierViewSet)
router.register(prefix='ticketstatus', viewset=TicketStatusViewSet)
router.register('users', UsersViewSet, 'users')

#router.register(prefix='login', viewset=LoginViewSet)

#router.register(prefix='userslogin' , viewset=UsersLoginViewset)
#router.register(prefix='login', viewset=LoginViewSet)


from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('req/', UsersViewSet.as_view({"get": "home"})),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)