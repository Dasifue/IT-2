from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0, blank=True)
    image = models.ImageField(upload_to="products", default="default/product.png", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return f"{self.name}"
    
    @property
    def price_with_discount(self):
        return self.price - (self.price * self.discount / 100)
    

    @property
    def rating(self):
        comments = self.comments.values_list('rating', flat=True)
        try:
            return round(sum(comments) / len(comments), 2)
        except ZeroDivisionError:
            return 0


class Comment(models.Model):
    email = models.EmailField()
    text = models.TextField()
    rating = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comments"
    )

class CommentProductImage(models.Model):
    image = models.ImageField(upload_to="comments")
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="images"
    )
