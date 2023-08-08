from django.shortcuts import render, redirect, get_object_or_404
from .models import Ad
from .forms import AdForm, FilterForm
from django.contrib.auth.decorators import login_required

def ad_list(request):
    ads = Ad.objects.all()
    return render(request, 'CarCity/ad_list.html', {'ads': ads})

@login_required
def post_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect('CarCity:ad_list')
    else:
        form = AdForm()
    return render(request, 'CarCity/post_ad.html', {'form': form})

def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    return render(request, 'CarCity/ad_detail.html', {'ad': ad})

def filter_ads(request):
    form = FilterForm(request.GET)
    ads = Ad.objects.all()

    if form.is_valid():
        brand = form.cleaned_data.get('brand')
        model = form.cleaned_data.get('model')
        year = form.cleaned_data.get('year')
        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')

        if brand:
            ads = ads.filter(brand__icontains=brand)
        if model:
            ads = ads.filter(model__icontains=model)
        if year:
            ads = ads.filter(year=year)
        if price_min:
            ads = ads.filter(price__gte=price_min)
        if price_max:
            ads = ads.filter(price__lte=price_max)

    return render(request, 'CarCity/filter_ads.html', {'ads': ads, 'filter_form': form})

def sort_ads(request):
    sort_by = request.GET.get('sort_by', None)
    ads = Ad.objects.all()

    if sort_by == 'year_asc':
        ads = ads.order_by('year')
    elif sort_by == 'year_desc':
        ads = ads.order_by('-year')
    elif sort_by == 'price_asc':
        ads = ads.order_by('price')
    elif sort_by == 'price_desc':
        ads = ads.order_by('-price')
    elif sort_by == 'date_asc':
        ads = ads.order_by('date_published')
    elif sort_by == 'date_desc':
        ads = ads.order_by('-date_published')

    return render(request, 'CarCity/sort_ads.html', {'ads': ads})



