import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from blueflamingoapi.models import Technician
from django.utils import timezone
from datetime import datetime

@csrf_exempt
def login_user(request):
    '''Handles the authentication of a technician

    Method arguments:
      request -- The full HTTP request object
    '''

    req_body = json.loads(request.body.decode())

    if request.method == 'POST':

        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            is_staff = authenticated_user.is_staff
            user_id = authenticated_user.id
            data = json.dumps({"valid": True, "token": token.key, "userId": user_id, "isStaff": is_staff})
            return HttpResponse(data, content_type='application/json')

        else:
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type='application/json')

@csrf_exempt
def register_user(request):
    '''Handles the creation of a new technician for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    req_body = json.loads(request.body.decode())

    new_user = User.objects.create_user(
        username=req_body['username'],
        email=req_body['email'],
        password=req_body['password'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name']
    )

    # Now save the extra info in the blueflamingoapi_technician table
    technician = Technician.objects.create(
        user=new_user,
        title=req_body['title'],
        address=req_body['address'],
        phone_number=req_body['phone_number'],    
    )

    # Commit the user to the database by saving it
    technician.save()

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=new_user)
    is_staff = new_user.is_staff
    user_id = new_user.id
    # Return the token to the client
    data = json.dumps({"valid": True, "token": token.key, "userId": user_id, "isStaff": is_staff})
    return HttpResponse(data, content_type='application/json')