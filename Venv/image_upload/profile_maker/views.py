from django.shortcuts import render
from .forms import Profile_Form
from .models import User_Profile
import datetime
import os
import shutil

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
def create_profile(request):
    l=[]
    form = Profile_Form()
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.Upload_Picture = request.FILES['Upload_Picture']
            file_type = user_pr.Upload_Picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'profile_maker/error.html')
            user_pr.save()
            for r, d, f in os.walk("/root/Desktop/Python/school_django/image_upload/media/"):
                for i in f:
                    l+=[i]
            print(l)
            return render(request, 'profile_maker/test.html')
        
    context = {"form": form,}
    return render(request, 'profile_maker/create.html', context)
