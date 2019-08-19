from rest_framework import serializers
from catalog_api.models import CarPart

class CarPartSerializer(serializers.ModelSerializer):
	make = serializers.ReadOnlyField(source='CarMake.make_name')
	model = serializers.ReadOnlyField(source='CarModel.model_name')

	class Meta:
		model = CarPart
		fields = ['id', 'make', 'model', 'color']