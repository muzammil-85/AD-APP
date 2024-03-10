from .models import Ad, Stand
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Ad
from .forms import AdForm


def login_adlist(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ad_list')  # Redirect to the ad list page
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def ad_view(request, pk):
    stand = Stand.objects.get(id=pk)  # Assuming the stand is associated with the user
    print(stand)
    ads = stand.ads.all().order_by('created_at')  # Get all ads for the stand, ordered by creation time
    print(ads)
    length = len(ads)
    ad_duration = ads[length-1].ad_shown_duration
    context = {'ads': ads,'ad_duration':ad_duration}
    return render(request, 'app/ad.html',context)

def ad_add_view(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ad_list')
    else:
        form = AdForm()
    return render(request, 'app/ad_form.html', {'form': form})

def ad_edit_view(request, ad_id):
    ad = Ad.objects.get(id=ad_id)
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ad_list')
    else:
        form = AdForm(instance=ad)
    return render(request, 'app/ad_form.html', {'form': form})

@login_required
def ad_list_view(request):
    ads = Ad.objects.all()
    stand_filter = request.GET.get('stand')
    if stand_filter:
        ads = ads.filter(stand=stand_filter)
    stands = Stand.objects.all()
    return render(request, 'app/ad_list.html', {'ads': ads,'stands':stands})

def ad_delete_view(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if request.method == 'POST':
        ad.delete()
        return redirect('ad_list')  # Redirect to the ad list page
    return redirect('ad_list')  # Redirect to the ad list page

def login_view(request):
    if request.method == 'POST':
        stand_id = request.POST.get('stand')
        print(stand_id)
        return redirect('ad',pk=stand_id)
    stands = Stand.objects.all()
    context = {'stands': stands}
    return render(request, 'app/login.html', context)

def stand_detail_view(request, stand_id):
    stand = Stand.objects.get(id=stand_id)
    ads = stand.ads.all()
    context = {'stand': stand, 'ads': ads}
    return render(request, 'app/stand_detail.html', context)

def logoutuser(request):
    logout(request)
    return redirect('login_adlist')



# def ad_upload(request):
#     if request.method == 'POST':
#         form = AdForm(request.POST, request.FILES)
#         if form.is_valid():
#             ad = form.save(commit=False)
#             ad.save()
#             form.save_m2m()  # Save many-to-many relationships
#             return redirect('ad_list')  # Assuming 'ad_list' is the URL name for listing ads
#     else:
#         form = AdForm()
#     return render(request, 'app/ad_upload.html', {'form': form})

# def get_ads_by_stand(request):
#     stand = request.GET.get('stand')
#     ads = Ad.objects.filter(user__stand=stand)
#     data = {'ads': list(ads.values())}
#     return JsonResponse(data)

# def ad_update(request, pk):
#     ad = Ad.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = AdForm(request.POST, request.FILES, instance=ad)
#         if form.is_valid():
#             form.save()
#             return redirect('ad_list')  # Assuming 'ad_list' is the URL name for listing ads
#     else:
#         stand = request.user.stand  # Assuming the current user has a stand attribute
#         form = AdForm(instance=ad, stand=stand)
#     return render(request, 'app/ad_upload.html', {'form': form})


# def ad_list(request):
#     ads = Ad.objects.all()
#     return render(request, 'app/ad_list.html', {'ads': ads})
