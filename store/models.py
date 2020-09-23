from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Profile
# Create your models here.


class Deal(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=500)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    discount = models.FloatField(default=1)
    active = models.BooleanField(default=False)


class Category(models.Model):
    def __str__(self):
        return self.cat_name
    cat_name = models.CharField(max_length=100)
    cat_slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('category_list', args=[self.cat_slug])


class Product(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)

    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, default=1)
    tag = models.CharField(max_length=500, default="handmade")

    size = models.CharField(max_length=100,  blank=True)

    color = models.CharField(max_length=100,  blank=True)

    material = models.CharField(max_length=100,  blank=True)

    avability = models.BooleanField(default=True)
    item_image = models.CharField(
        max_length=500, default="https://cdn.shopify.com/s/files/1/0169/2660/5412/collections/placeholder-images-collection-1_large_807560ab-9024-46ea-ab0a-bb49df2b3bb8_1200x1200.png?v=1551259616")
    galary = models.CharField(max_length=100000, default="", blank=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={"pk": self.pk})

    def get_discount(self):
        return (self.price * self.deal.discount)

    def save(self, *args, **kwargs):
        for field_name in ['title', 'size', 'color', 'material']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Product, self).save(*args, **kwargs)


class Review(models.Model):
    def __str__(self):
        return "AD00"+str(self.id)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    def __str__(self):
        return "AD00"+str(self.id)
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Order(models.Model):
    def __str__(self):
        return "AD00"+str(self.id)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100)
    @property
    def get_cart_total(self):
        orderItems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderItems])
        return total

    @property
    def get_cart_items(self):
        orderItems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderItems])
        return total


class OrderItem(models.Model):
    def __str__(self):
        return "AD00"+str(self.id)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    pay_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    @property
    def get_total(self):
        total = self.product.price*self.quantity
        return total


class Wishlist(models.Model):
    def __str__(self):
        return "AD00"+str(self.id)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


class WishlistItem(models.Model):
    def __str__(self):
        return "AD00"+str(self.id)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    wishlist = models.ForeignKey(
        Wishlist, on_delete=models.SET_NULL, null=True)


class shippingAdress(models.Model):
    def __str__(self):
        return "AD00"+str(self.id)
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.IntegerField(default=0000)
    date_added = models.DateTimeField(auto_now_add=True)
