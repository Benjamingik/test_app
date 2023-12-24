from django.urls import path

from click.views import result_view, subject_list_view, subject_view, variant_view, result_list_view, VariantCreateView

app_name = 'click'
urlpatterns = [
    path('subjects/', subject_list_view, name='subject_list'),
    path('subjects/<int:pk>/', subject_view, name='subject'),
    path('variant/<int:pk>/', variant_view, name='variant'),
    path('results/', result_list_view, name='result_list'),
    path('results/<int:pk>/', result_view, name='result'),

    # for teachers
    path('variant/create/', VariantCreateView.as_view(), name='variant_create')
    # path('/<int:pk>')
]
