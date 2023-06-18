from .models import Product

def liked_product_count(request):
    if request.user.is_authenticated:
        return {'liked_product_count': request.user.liked_products.count()}
    else:
        return {}