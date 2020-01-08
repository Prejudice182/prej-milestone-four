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


def get_kit_detail(slug):
    kit = Kit.objects.filter(slug__exact=slug).first()
    context = {
        'product': kit
    }
    return context

def get_vip_detail(slug):
    vip = VIPSlot.objects.filter(slug__exact=slug).first()

    context = {
        'product': vip
    }

    return context

def get_product_detail(request, product_type, slug):
    if product_type == 'kit':
        context = get_kit_detail(slug)
    elif product_type == 'vip':
        context = get_vip_detail(slug)
    
    return render(request, 'product_detail.html', context=context)