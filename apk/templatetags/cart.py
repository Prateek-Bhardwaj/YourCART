from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False


@register.filter(name='cart')
def cart(cart):
    keys = cart
    if cart and len(keys) >=1:
        return True
    return False

@register.filter(name='quant')
def quant(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0

@register.filter(name='product_total_price')
def product_total_price(product, cart):
    return product.price * quant(product, cart)

@register.filter(name='cart_total')
def cart_total(products, cart):
    sum = 0
    for p in products:
        sum += product_total_price(p, cart)
    return sum

@register.filter(name='items')
def items(products, cart):
    sum = 0
    for p in products:
        sum += quant(p, cart)
    return sum


@register.filter(name='status')
def status(stat):
    if stat == 'Completed':
      return True
    return False








'''
<!doctype html>
<html lang="en">
  <head>
    {% load cart %}
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    <link rel="stylesheet" href="/static/css/base.css">
    <title>{% block title %} {% endblock %}</title>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    
    <style>
      body{
        background-color: aliceblue;
      }
      @media screen and (max-lenght:700px) {
        #home{
          display:none;
        }
      }
    </style>
    {% block style %} {% endblock %}
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-info">
        <div class="container-fluid">
          <a class="navbar-brand" href="/">amazon</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" id="home" aria-current="page" href="/">Home</a>
              </li>
            </ul>
            {% if request.session.cart|cart %}
              <a class="btn btn-outline" href="/cart">Cart</a>
              {% endif %}
            {% if user.is_authenticated %}
            <a class="btn btn-outline" href="/profile">{{request.user}} (Orders)</a>
                <a class="btn btn-outline" href="/logout" type="submit">LogOut</a>
              </form>
            {% else %}
            <form action="">
                <a class="btn btn-outline" href="/login">Login</a>
            </form>
            {% endif %}
          </div>
          </div>
        </div>
      </nav>
      {% block body %} {% endblock %}
      
      <footer class="foot">
        all rights reserved.
      </footer>
    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js" integrity="sha384-SR1sx49pcuLnqZUnnPwx6FCym0wLsk5JZuNx2bPPENzswTNFaQU1RDvt3wT4gWFG" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.min.js" integrity="sha384-j0CNLUeiqtyaRmlzUHCPZ+Gy5fQu0dQ6eZ/xAww941Ai1SxSY+0EQqNXNE6DZiVc" crossorigin="anonymous"></script>
    -->
    {% block script %} {% endblock %}
  </body>
</html>
'''