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
