from django.shortcuts import render
from .models import Kit, VIPSlot

# Create your views here.

def all_products(request):
    kits = Kit.objects.all()
    vipslots = VIPSlot.objects.all()

    context = {
        'kits': kits,
        'vipslots': vipslots,
    }

    return render(request, 'products.html', context=context)