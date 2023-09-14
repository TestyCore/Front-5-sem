import requests
from django.shortcuts import render, redirect

from back_info.forms import ReviewForm
from back_info.models import Review
from back_info.models import News


import logging
logger = logging.getLogger(__name__)


def about_us(request):

    try:
        response = requests.get('https://api.kanye.rest/')
        if response.status_code == 200:
            data = response.json()
            quote = data["quote"]
        else:
            quote = "Failed to retrieve quote."
    except:
        quote = ""

    context = {
        'quote': quote}

    return render(request, 'back_info/about_us.html', context=context)


def news(request):

    return render(request, 'back_info/news.html')


def terms_conditions(request):

    return render(request, 'back_info/terms_definitions.html')


def contacts(request):

    return render(request, 'back_info/contacts.html')


def policy(request):

    return render(request, 'back_info/policy.html')


def reviews(request):
    reviews = Review.objects.all()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.client = request.user
            review.save()
            logger.info('New rate was created')
            return redirect('back_info:reviews')
    else:
        form = ReviewForm()

    is_customer = request.user.groups.filter(name='Customer').exists()
    user = request.user

    context = {
        'user': user,
        'form': form,
        'reviews': reviews,
        'is_customer': is_customer,

    }
    return render(request, 'back_info/reviews.html', context=context)


def openings(request):

    return render(request, 'back_info/openings.html')


def coupons(request):

    return render(request, 'back_info/coupons.html')


def news_0(request):

    news = News.objects.all().first()

    return render(request, 'back_info/news_0.html', {'news': news})


def news_1(request):

    news = News.objects.all()[1]

    return render(request, 'back_info/news_1.html', {'news': news})


def news_2(request):
    news = News.objects.all()[2]

    return render(request, 'back_info/news_2.html', {'news': news})


def news_3(request):
    news = News.objects.all()[3]

    return render(request, 'back_info/news_3.html', {'news': news})


def news_4(request):
    news = News.objects.all()[4]
    return render(request, 'back_info/news_4.html', {'news': news})


def news_5(request):
    news = News.objects.all()[5]
    return render(request, 'back_info/news_5.html', {'news': news})
