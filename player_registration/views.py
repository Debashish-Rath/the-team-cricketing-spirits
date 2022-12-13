from django.shortcuts import render
from django.http import HttpResponse
from player_registration.models import Player_Registration_Form

# Create your views here.


def player_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_no = request.POST['phone_no']
        whatsapp_no = request.POST['whatsapp_no']
        role_info = request.POST.get('role_info','')
        reference_person = request.POST['reference_person']
        is_available = request.POST['availability']

        
        Player_Registration_Form.objects.create(name=name, phone_no=phone_no,whatsapp_no=whatsapp_no,role=role_info,reference_person=reference_person,is_available=True)

        # print(player_registeration_form)
        print(name)
        print(phone_no)
        print(whatsapp_no)
        print(reference_person)
        print(is_available)
        return HttpResponse("Successfully Registered")
    else:
        return render(request, 'register.html')