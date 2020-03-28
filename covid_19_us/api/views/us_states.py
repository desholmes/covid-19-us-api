from rest_framework.response import Response
from rest_framework import viewsets

from .serializers.state_serializer import StateSerializer
from .utils import get_states_by_date
from .utils import get_df_from_url
from .utils import get_states_from_df

url = 'https://raw.githubusercontent.com/nytimes/\
covid-19-data/master/us-states.csv'
# url = './data/us-states.csv'

df = get_df_from_url(url)
states = get_states_from_df(df)


class USStateViewSet(viewsets.ViewSet):

    def list(self, request):
        date = self.request.query_params.get('date')
        if date:
            stateByDate = get_states_by_date(date, df)
            serializer = StateSerializer(
                instance=stateByDate.values(), many=True)
            return Response(serializer.data)
        else:
            serializer = StateSerializer(
                instance=states.values(), many=True)
            return Response(serializer.data)
