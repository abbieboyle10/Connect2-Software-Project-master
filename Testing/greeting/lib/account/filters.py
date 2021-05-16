import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class JobFilter(django_filters.FilterSet):
    Title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Job
        fields = '__all__'
        fields = ('Title', 'status', 'no_applicants')


class JobFilter2(django_filters.FilterSet):
    Title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Job
        fields = '__all__'
        fields = ('Title', 'location', 'contract', 'office_type')
