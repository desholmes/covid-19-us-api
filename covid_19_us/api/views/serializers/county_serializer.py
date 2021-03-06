from rest_framework import serializers


class CountySerializer(serializers.Serializer):
    date = serializers.DateField()
    county = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)
    fips = serializers.IntegerField()
    cases = serializers.IntegerField()
    deaths = serializers.IntegerField()
