from .cart import Cart

#create context processors where can work all pages

def cart(request):
    return{'cart': Cart(request)}