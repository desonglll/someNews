from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Product
from django.utils import timezone


def object_to_dict(obj):
    """Converts an object to a dictionary

    Args:
        obj (News): the object to convert

    Returns:
        result (dict): the converted dictionary
    """
    result = {}
    for field in obj._meta.fields:
        print(field.name)
        if field.name == 'release_date' and getattr(obj, field.name) != None:
            result[field.name] = str(getattr(obj, field.name).strftime("%Y-%m-%d %H:%M:%S"))
        else:
            result[field.name] = str(getattr(obj, field.name))
    return result


def get_all_products(request):
    products = Product.objects.all()
    json_data = []
    for product in products:
        dic = object_to_dict(product)
        json_data.append(dic)
    return JsonResponse(json_data, safe=False)


def purchase_product(request):
    # 处理购买逻辑
    method = "GET" if request.method == 'GET' else "POST"

    # 假设您有一个表单字段叫做 'quantity'，表示购买数量
    product_id = int(request.GET.get('product_id', 0)) if method == 'GET' else int(request.POST.get('product_id', 0))
    product_price = int(request.GET.get('price', 0)) if method == 'GET' else int(request.POST.get('price', 0))
    product = Product.objects.get(pk=product_id)
    quantity_to_purchase = int(request.GET.get('quantity', 0)) if method == 'GET' else int(
        request.POST.get('quantity', 0))
    username = str(request.GET.get('name', '')) if method == 'GET' else str(request.POST.get('name', ''))
    address = str(request.GET.get('address', '')) if method == 'GET' else str(request.POST.get('address', ''))
    phone = str(request.GET.get('phone', '')) if method == 'GET' else str(request.POST.get('phone', ''))

    # 创建购买记录，记录购买时间
    purchase_time = timezone.now()
    Product.objects.create(product_name=product.product_name,
                           price=product_price,
                           quantity=quantity_to_purchase,
                           buy_date=purchase_time,
                           operation="1",
                           name=username,
                           address=address,
                           phone=phone)

    print(quantity_to_purchase)
    return render(request, 'buy_page.html',
                  {'message': f'购买成功，购买了{quantity_to_purchase}件商品'})

    return render(request, 'buy_page.html', {'product': "rrr"})
