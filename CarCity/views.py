from django.shortcuts import render, redirect, get_object_or_404
from .models import Ad
from .forms import AdForm, FilterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def ad_list(request):
    ads = Ad.objects.all()
    return render(request, 'CarCity/ad_list.html', {'ads': ads})

@login_required
def post_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
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
  
            #   SORT ADS

def ad_list(request):
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

    return render(request, 'CarCity/sort_ads.html', context={'ads': ads})

            #  FILTER ADS
                 
def ad_list(request):      
    ads = Ad.objects.all()
    filter_form = FilterForm(request.GET)
    filtered_ads = ads

    distinct_brands = ads.values_list('brand', flat=True).distinct()
    distinct_models = ads.values_list('model', flat=True).distinct()
    distinct_years = ads.values_list('year', flat=True).distinct()

    if filter_form.is_valid():
        if filter_form.cleaned_data['brand']:
            filtered_ads = filtered_ads.filter(brand__icontains=filter_form.cleaned_data['brand'])
        if filter_form.cleaned_data['model']:
            filtered_ads = filtered_ads.filter(model__icontains=filter_form.cleaned_data['model'])
        if filter_form.cleaned_data['year']:
            filtered_ads = filtered_ads.filter(year=filter_form.cleaned_data['year'])
        if filter_form.cleaned_data['price_min']:
            filtered_ads = filtered_ads.filter(price__gte=filter_form.cleaned_data['price_min'])
        if filter_form.cleaned_data['price_max']:
            filtered_ads = filtered_ads.filter(price__lte=filter_form.cleaned_data['price_max'])

    return render(request, 'CarCity/ad_list.html', {
        'filter_form': filter_form,
        'filtered_ads': filtered_ads,
        'distinct_brands': distinct_brands,
        'distinct_models': distinct_models,
        'distinct_years': distinct_years,
    })
