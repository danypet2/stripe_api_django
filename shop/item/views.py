import stripe
from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView, TemplateView
from .models import Item
from shop import settings


stripe.api_key = settings.STRIPE_SECRET_KEY
class MyModelItem(DetailView):
    model = Item
    template_name = 'item/item.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.get(pk=self.kwargs['pk'])
        context.update({"STRIPE_PUBLISHABLE_KEY": settings.STRIPE_PUBLISHABLE_KEY})
        return context





class MyModelItems(TemplateView):
    template_name = 'item/items.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        return context


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        item = Item.objects.get(pk=self.kwargs['pk'])
        DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'rub',
                        'unit_amount': item.price * 100,
                        'product_data': {
                            'name': item.name
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                'item_id': item.id
            },
            mode='payment',
            success_url=DOMAIN + '/item/success/',
            cancel_url=DOMAIN + '/item/cancelled/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


class SuccessView(TemplateView):
    template_name = 'status_payment/success.html'


class CancelledView(TemplateView):
    template_name = 'status_payment/cancelled.html'

# Create your views here.
