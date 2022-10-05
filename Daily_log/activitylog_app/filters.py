import django_filters
from django_filters import DateFilter, CharFilter,DateTimeFilter

from .models import *

class CommentFilter(django_filters.FilterSet):
	details = CharFilter(field_name='details', lookup_expr='icontains')
	start_date = DateTimeFilter(field_name="date_time", lookup_expr='gte')
	end_date = DateTimeFilter(field_name="date_time", lookup_expr='lte')


	class Meta:
		model = Comment
		fields = ['satellite', 'subsystem_type','details','start_date','end_date',]
		# fields = '__all__'
		# exclude = ['photo','upload' ]