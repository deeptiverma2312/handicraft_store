from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import JsonResponse
from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    product_list = Product.objects.all()
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(
            user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {
        'product_list': product_list,
        'cartItems': cartItems
    }
    return render(request, 'shop/index.html', context)


def search(request):
    product_list = Product.objects.all()
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(
            user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    Product_name = request.GET.get('Product_name')
    if Product_name != '' and Product_name != None:
        product_list = product_list.filter(tag__icontains=Product_name)
    return render(request, 'shop/search.html', {'product_list': product_list,
                                                'cartItems': cartItems})


def category_list(request, cat_slug=None):
    category = None
    categories = Category.objects.all()
    cat_pro = Product.objects.all()
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(
            user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    if cat_slug:
        category = get_object_or_404(Category, cat_slug=cat_slug)
        cat_pro = cat_pro.filter(category=category)
    context = {
        'cartItems': cartItems,
        'categories': categories,
        'category': category,
        'cat_pro': cat_pro

    }

    return render(request, 'shop/category.html', context)


def detail(request, id):
    pro = Product.objects.get(pk=id)
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(
            user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    galary = pro.galary.split(",,,")
    ratings = Rating.objects.all().filter(product_id=id)
    x = 0
    n = 0
    for r in ratings:
        x += r.rating
        n = n+1
    if n == 0:
        n = 1
    rating = format(x/n, '.1f')
    size = pro.size.split(",")
    color = pro.color.split(",")
    material = pro.material.split(",")

    context = {
        'pro': pro,
        'galary': galary,
        'rating': rating,
        'size': size,
        'color': color,
        'material': material,
        'cartItems': cartItems
    }
    return render(request, 'shop/detail.html', context)


@login_required
def cart(request):
    user = request.user
    order, created = Order.objects.get_or_create(
        user=user, complete=False)

    items = order.orderitem_set.all()
    orderItem = OrderItem.objects.all()
    cartItems = order.get_cart_items

    context = {
        'items': items,
        'cartItems': cartItems,
        'user': user,

    }
    return render(request, 'shop/cart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    size = data['size']
    color = data['color']
    material = data['material']

    user = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(user=user, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order,
                                                         product=product, size=size, color=color, material=material)
    if action == "add":
        messages.success(
            request, f'{orderItem.product.title}is added to your cart')

        orderItem.size = size
        orderItem.color = color
        orderItem.material = material

        orderItem.quantity = (orderItem.quantity+1)

        orderItem.save()
    elif action == "inc":
        orderItem.quantity = (orderItem.quantity+1)

        orderItem.save()
    elif action == "remove":

        orderItem.quantity = (orderItem.quantity-1)
        orderItem.save()
    elif action == "delete":
        messages.warning(
            request, f'{orderItem.product.title} is removed from your cart')

        orderItem.delete()

    if orderItem.quantity <= 0:
        messages.warning(
            request, f'{orderItem.product.title} is removed from your cart')
        orderItem.delete()
    return JsonResponse('Item was adder to cart', safe=False)


def updateWishlist(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('action:', action, "productId:", productId)
    user = request.user
    product = Product.objects.get(id=productId)
    wishlist, created = Wishlist.objects.get_or_create(
        user=user)

    wishlistItem, created = WishlistItem.objects.get_or_create(wishlist=wishlist,
                                                               product=product)
    if action == "add":
        messages.success(
            request, f'{wishlistItem.product.title} is added to your wishlist')

        wishlistItem.save()
    elif action == "delete":
        messages.warning(
            request, f'{wishlistItem.product.title} is removed from your wishlist')
        wishlistItem.delete()

    return JsonResponse('Item was adder to wishlist', safe=False)


@login_required
def wishlist(request):
    user = request.user
    wishlist, created = Wishlist.objects.get_or_create(
        user=user)
    wishlistitems = wishlist.wishlistitem_set.all()

    order, created = Order.objects.get_or_create(
        user=user, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    context = {
        'user': user,
        "items": wishlistitems,
        "cartItems": cartItems
    }
    return render(request, 'shop/wishlist.html', context)


def top_pro(request):
    product_list = Product.objects.all()

    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(
            user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {
        'product_list': product_list,
        'cartItems': cartItems
    }
    return render(request, 'shop/top_pro.html', context)
