from rest_framework.response import Response
from rest_framework import viewsets, status

from .serializers.state_serializer import StateSerializer
from .utils import get_states_by_date
from .utils import get_df_from_url
from .utils import get_states_from_df

url = 'https://raw.githubusercontent.com/nytimes/\
covid-19-data/master/us-states.csv'


class USStateViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            df = get_df_from_url(url)
            states = get_states_from_df(df)
            date = self.request.query_params.get('date')

            if date:
                states = get_states_by_date(date, df)

        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = StateSerializer(instance=states.values(), many=True)
        return Response(serializer.data)
