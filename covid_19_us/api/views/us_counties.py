from rest_framework.response import Response
from rest_framework import viewsets, status

from .serializers.county_serializer import CountySerializer
from .utils import get_counties_by_date
from .utils import get_df_from_url
from .utils import get_counties_from_df

url = 'https://raw.githubusercontent.com/\
nytimes/covid-19-data/master/us-counties.csv'


class USCountyViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            df = get_df_from_url(url)
            counties = get_counties_from_df(df)
            date = self.request.query_params.get('date')

            if date:
                counties = get_counties_by_date(date, df)

        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = CountySerializer(instance=counties.values(), many=True)
        return Response(serializer.data)
