import django_filters

from .models import Uav


class UavFilter(django_filters.FilterSet):
## To make filter feature in the uav listing, made this form
## connect with uav models and get the field then write exact value,contains key etc.
    class Meta:
        model = Uav
        fields = {'brand': ['exact'], 'model': ['icontains'], 'weight': ['lt'], 'category': ['exact'], 'price': ['lt'],}
