from django.shortcuts import render, redirect


def users_profile(request):
    user = request.user

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        user.save()
        return redirect('users_profile:users_profile')

    return render(request, 'users_profile/profile.html', {'user': user})
