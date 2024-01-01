from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import News

from products.views import get_all_products


def get_all_news(request):
    """Returns all news in Json format.

    Args:
        request (request): HttpRequest object

    Returns:
        JsonResponse (json): Json object including all news.
    """
    all_news = News.objects.all()
    json_data = []
    for news in all_news:
        dic = object_to_dict(news)
        json_data.append(dic)
    return JsonResponse(json_data, safe=False)


def user_login(request):
    """For user login authentication

    Args:
        request (request): HttpRequest object including username and password.

    Returns:
        JsonResponse (json): Json object including True or False.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    elif request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
    else:
        return JsonResponse({"status": False, "message": "登录失败。请检查用户名和密码。"}, status=400)
    user = authenticate(request, username=username, password=password)
    print(username)
    print(password)
    if user is not None:
        login(request, user)
        return JsonResponse({"status": True, "message": "登录成功"}, status=200)
    else:
        return JsonResponse({"status": False, "message": "登录失败。请检查用户名和密码。"}, status=400)


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


def get_by_nid(request):
    """Get Json item by nid.
    Filter the database based on the 'nid' from the request, and return the corresponding JSON data for the given 'nid'.

    Args:
        request (request): HttpRequest object including nid.

    Returns:
        JsonResponse (json): Json object including news by nid.
    """
    nid = request.GET.get('nid')
    print(nid)
    if nid == "8":  # Shopping
        return get_all_products(request)
    if nid == "0":
        all_news = News.objects.all()
    else:
        all_news = News.objects.filter(nid=nid)
    json_data = []
    for news in all_news:
        dic = object_to_dict(news)
        json_data.append(dic)
    return JsonResponse(json_data, safe=False)


def get_nav(request):
    choice = News.choices
    data = []
    for key, value in choice.items():
        print(f"Key: {key}, Value: {value}")
        dic = {
            "id": key,
            "nav": value,
            "type": 1 if key == "8" else 0,
        }
        data.append(dic)
    return JsonResponse(data, safe=False)


def get_by_id(request):
    """ Return Json item by id.

    Args:
        request (HTTPRequest): HttpRequest object including id.

    Returns:
        JsonResponse (json): Json object including news by id.
    """
    id = request.GET.get('id')
    news = News.objects.get(id=id)
    dic = {
        "id": news.id,
        "title": news.product_name,
        "content": news.content,
        "released_date": news.release_date.strftime("%Y-%m-%d %H:%M:%S") if news.release_date is not None else "",
    }
    return JsonResponse(dic, safe=False)
