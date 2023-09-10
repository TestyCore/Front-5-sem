from django.shortcuts import render, redirect

from back_info.forms import ReviewForm
from back_info.models import Review


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
    reviews = Review.objects.all()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.client = request.user
            review.save()
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
