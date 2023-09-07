from django.shortcuts import render


def about_us(request):

    return render(request, 'back_info/about_us.html')


def news(request):

    return render(request, 'back_info/news.html')


def terms_conditions(request):

    return render(request, 'back_info/terms_definitions.html')


def contacts(request):

    return render(request, 'back_info/contacts.html')


def policy(request):

    return render(request, 'back_info/policy.html')


def reviews(request):

    return render(request, 'back_info/reviews.html')


def news_0(request):

    return render(request, 'back_info/news_0.html')


def news_1(request):

    return render(request, 'back_info/news_1.html')


def news_2(request):

    return render(request, 'back_info/news_2.html')


def news_3(request):

    return render(request, 'back_info/news_3.html')


def news_4(request):

    return render(request, 'back_info/news_4.html')


def news_5(request):

    return render(request, 'back_info/news_5.html')
