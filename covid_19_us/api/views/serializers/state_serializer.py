from rest_framework import serializers


class StateSerializer(serializers.Serializer):
    date = serializers.DateField()
    state = serializers.CharField(max_length=100)
    fips = serializers.IntegerField()
    cases = serializers.IntegerField()
    deaths = serializers.IntegerField()
