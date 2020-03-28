from rest_framework.response import Response
from rest_framework import viewsets

from .serializers.county_serializer import CountySerializer
from .utils import get_counties_by_date
from .utils import get_df_from_url
from .utils import get_counties_from_df

url = 'https://raw.githubusercontent.com/\
nytimes/covid-19-data/master/us-counties.csv'
# url = './data/us-states.csv'

df = get_df_from_url(url)
counties = get_counties_from_df(df)


class USCountyViewSet(viewsets.ViewSet):

    def list(self, request):
        date = self.request.query_params.get('date')
        if date:
            countyByDate = get_counties_by_date(date, df)
            serializer = CountySerializer(
                instance=countyByDate.values(), many=True)
            return Response(serializer.data)
        else:
            serializer = CountySerializer(
                instance=counties.values(), many=True)
            return Response(serializer.data)
