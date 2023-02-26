import django_filters

from .models import Uav


class UavFilter(django_filters.FilterSet):

    class Meta:
        model = Uav
        fields = {'brand': ['exact'], 'model': ['icontains'], 'weight': ['lt'], 'category': ['exact'], 'price': ['lt'],}
