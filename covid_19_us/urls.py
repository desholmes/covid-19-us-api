from rest_framework import routers
from covid_19_us.api.views.us_states import USStateViewSet
from covid_19_us.api.views.us_counties import USCountyViewSet


router = routers.DefaultRouter()
router.register(r'us/states',
                USStateViewSet,
                basename='us/states')
router.register(r'us/counties',
                USCountyViewSet,
                basename='us/counties')
urlpatterns = router.urls
