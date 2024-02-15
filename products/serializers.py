from rest_framework import serializers

from main.models import Category, SubCategory
from warehouse.models import Measure, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon']


class SubCategorySerializer(serializers.ModelSerializer):
    icon = serializers.ImageField(
        max_length=None, allow_empty_file=False,
        allow_null=True, required=False, source='icon'
    )
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category', 'icon']


class MeasureSerIalizer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(read_only=True, source='category.name')
    measure_name = serializers.CharField(read_only=True, source='measure.name')
    stockroom_name = serializers.CharField(read_only=True, source='stockroom.name')


    class Meta:
        model = Product
        fields = [
            'id', 'name', 'as_key', 'p_num', 'category_name', 'image', 'quantity',
            'measure_name', 'stockroom_name', 'count', 'out_count', 'is_active', 'in_use',
            'critical_quantity', 'description'
        ]
