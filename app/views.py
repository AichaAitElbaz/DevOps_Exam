from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Guest
from .models import UserAccount
from django.contrib.auth.decorators import login_required


User = get_user_model()



def my_view(request):
    user_ip = request.META.get('REMOTE_ADDR')

    # Vérifiez si l'adresse IP existe déjà dans la base de données
    guest, created = Guest.objects.get_or_create(ip_address=user_ip)

    # Incrémentez le compteur de visites
    guest.visit_counter += 1
    guest.save()

    return render(request, 'template.html', {'user_ip': user_ip})







def count_users(request):
    if request.method == 'GET':
        user_count = User.objects.count()
        return JsonResponse({'user_count': user_count})

    return JsonResponse({'error': 'Invalid request method'})






def display_all_users(request):
    users = User.objects.all()
    user_data = []

    for user in users:
        user_data.append({
            'id': user.id,
            'email': user.email,
            'firstname': user.firstname,
            'lastname': user.lastname,
            'date_joined': user.date_joined,
            # Ajoutez d'autres champs si nécessaire
        })

    return JsonResponse({'users': user_data})


