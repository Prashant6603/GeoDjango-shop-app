from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.gis.geos import Point
from .models import Shop
from .forms import ShopForm, CustomSignupForm, CustomLoginForm


def shop_map(request):
    """Display shops on dashboard + map."""

    query = request.GET.get("q")
    category = request.GET.get("category")
    show_all = request.GET.get("all") == "1"

    shops = Shop.objects.all()

    # Show only own shops unless user clicks "View All"
    if request.user.is_authenticated and not show_all:
        shops = shops.filter(owner=request.user)

    if query:
        shops = shops.filter(
            Q(name__icontains=query) |
            Q(address__icontains=query)
        )

    if category:
        shops = shops.filter(category__icontains=category)

    return render(request, "dashboard.html", {"shops": shops})


@login_required
def create_shop(request):
    """Create a new shop with GeoDjango PointField."""

    if request.method == "POST":
        form = ShopForm(request.POST)

        if form.is_valid():
            shop = form.save(commit=False)
            shop.owner = request.user   # assign owner
            shop.save()                 # location is already set inside form.save()
            return redirect("shop_map")

    else:
        form = ShopForm()

    return render(request, "shop_form.html", {"form": form})


@login_required
def update_shop(request, pk):
    """Update an existing shop (name, address, category, location)."""

    shop = get_object_or_404(Shop, pk=pk, owner=request.user)

    if request.method == "POST":
        form = ShopForm(request.POST)

        if form.is_valid():
            # Update basic fields
            shop.name = form.cleaned_data["name"]
            shop.address = form.cleaned_data["address"]
            shop.category = form.cleaned_data["category"]

            # Update coordinates → Point
            lat = form.cleaned_data.get("latitude")
            lng = form.cleaned_data.get("longitude")
            shop.location = Point(float(lng), float(lat), srid=4326)

            shop.save()
            return redirect("shop_map")

    else:
        # Pre-fill hidden coordinate fields so map loads correctly
        initial_data = {
            "name": shop.name,
            "address": shop.address,
            "category": shop.category,
            "latitude": shop.location.y,
            "longitude": shop.location.x,
        }
        form = ShopForm(initial=initial_data)

    return render(request, "shop_form.html", {"form": form})


@login_required
def delete_shop(request, pk):
    shop = get_object_or_404(Shop, pk=pk, owner=request.user)
    shop.delete()
    return redirect("shop_map")


@login_required
def view_shops(request):
    """Table of user-owned shops."""
    shops = Shop.objects.filter(owner=request.user)
    return render(request, "view_shop.html", {"all_shops": shops})


def custom_login(request):
    """Login user using custom login form."""
    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)

        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )
            if user:
                login(request, user)
                return redirect("shop_map")
    else:
        form = CustomLoginForm()

    return render(request, "login.html", {"form": form})


def signup_view(request):
    """Register new user and auto-login."""
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("shop_map")
    else:
        form = CustomSignupForm()

    return render(request, "sign_up.html", {"form": form})

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('login')
