from django.shortcuts import render
from .models import Info, Resume, Contact


def info_view(request):
    my_info = Info.objects.all().last()
    my_resume = Resume.objects.all()

    if my_info.status == True:
        my_info.status = 'در دسترس'
    else:
        my_info.status = 'غیر فعال'

    # contact_us page view
    full_name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    if request.method == 'POST':
        Contact.objects.create(name=full_name, email=email, message=message)

    return render(request, 'index.html', {'info': my_info, 'resume': my_resume})

