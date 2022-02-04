from django.shortcuts import render
from store.models import Product, ReviewRating


def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')

    # get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

#A context is a variable name -> variable value mapping that is passed to a template.
#Context processors let you specify a number of variables that get set in each context automatically
# without you having to specify the variables in each render() call.
    context = {
        'products': products,
        'reviews': reviews,
    }

    return render(request, 'home.html', context)

    #return render(request, 'home.html', {
    #pass to template
    # 'products': products,
    # })


