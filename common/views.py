from django.shortcuts import render, redirect
from .models import Profile, User
from .forms import ProfileEditForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def profile_edit(request, user_id):
    profile = Profile.objects.get(user_id=user_id)
    user = User.objects.get(user_id=user_id)
    if request.method == 'POST':
        profile_edit_form = ProfileEditForm(request.POST, instance=profile)
        profile_img = profile.profile_img
        if request.FILES.get('profile_img') != None:
            profile_img = request.FILES['profile_img']
        if profile_edit_form.is_valid:
            user.nickname = request.POST['nickname']
            profile = profile_edit_form.save()
            profile.profile_img = profile_img
            profile.save()
            user.save()
            return redirect('mypage')
    else:
        profile_edit_form = ProfileEditForm(instance=profile)
        context = {'form': profile_edit_form,
                   'user': user,
                   'profile': profile}
    return render(request, 'review/profile_update_form.html', context)


def mypage(request):
    cur_user = request.user
    if cur_user.is_authenticated:
        user = User.objects.get(user_id=cur_user.user_id)
        profile = Profile.objects.get(user_id=cur_user.user_id)
        context = {'user': user, 'profile': profile}
        return render(request, "review/profile.html", context)
    else:
        return redirect('account_login')
