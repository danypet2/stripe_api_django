from django.http import HttpRequest
from django.urls import path

from .views import MyModelItem, SuccessView, CancelledView, CreateCheckoutSessionView, MyModelItems

urlpatterns = [
    path('item/<int:pk>/', MyModelItem.as_view(), name='item_detail'),
    path('item/success/', SuccessView.as_view(), name='success'),
    path('item/cancelled/', CancelledView.as_view(), name='cancelled'),
    path('buy/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('item/', MyModelItems.as_view(), name='items')

]