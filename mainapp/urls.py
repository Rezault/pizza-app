from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index),
    path("profile/", views.profile, name="profile"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html", redirect_authenticated_user=True), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("signup/", views.signup, name="signup"),
    path("create/", views.create_pizza, name="create_pizza"),
    path("cart/", views.view_cart, name="view_cart"),
    path("remove-item/<int:item_id>", views.remove_cart_item, name="remove_cart_item"),
    path("checkout", views.checkout, name="checkout"),
    path("order_confirmation/<int:id>", views.order_confirmation, name="order_confirmation")
]
