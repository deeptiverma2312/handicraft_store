from .models import *


def Pro(request):

    Product_list = Product.objects.all()

    context = {

        'Product_list': Product_list
    }
    return context


def Cat(request):
    Cat_list = Category.objects.all()
    context = {

        'Cat_list': Cat_list
    }
    return context


# def Cart(request):
#     if request.user.is_authenticated:
#         user = request.user
#         order, created = Order.objects.get_or_create(
#             user=user, complete=False)
#         items = order.orderitem_set.all()
#         cartItems = order.get_cart_items
#     else:
#         items = []
#         order = {'get_cart_total': 0, 'get_cart_items': 0}
#         cartItems = order['get_cart_items']

#     context = {
#         'cartItems': cartItems
#     }
#     return context
