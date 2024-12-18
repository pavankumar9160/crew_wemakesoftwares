from django.conf import settings
from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from myapp.models import *


def signup_page(request):
    if request.user.is_authenticated:
        if request.user.is_csa:
            return redirect('/V2_DCEMI/agent_home/')  
        else:
            return redirect('/V2_DCEMI/chat_page_user/')

    return render(request,'newChatUI/signup_user.html')

def login_page(request):
    if request.user.is_authenticated:
        if request.user.is_csa:
            return redirect('/V2_DCEMI/agent_home/')  
        else:
           return redirect( '/V2_DCEMI/chat_page_user/')

    return render(request,'newChatUI/login_user.html') 

@login_required
def chat_page_user(request):
    
    user = request.user
    
    print('user_id' , user.id)

    return render(request,'newChatUI/chat_page_user.html', {'user': user})  

@login_required
def dashboard_user(request):
    
    user = request.user
    profile_picture = user.profile_picture.url 
    print('user',user.name)
    
    return render(request, 'newChatUI/dashboard_user.html', {
        'user': user,
        'profile_picture': profile_picture
    })
    
@login_required
def agent_dashboard(request):
    if request.user.is_csa:
        user = request.user
        profile_picture = user.profile_picture.url 
        return render(request,'newChatUI/agent_dashboard.html',{
            'user': user,
            'profile_picture': profile_picture
    })
    else :
     return render(request,'newChatUI/agent_login.html')
        
@login_required
def agent_home(request):
    if request.user.is_csa:
        
     return render(request,'newChatUI/agent_home.html')
    else:
     return render(request,'newChatUI/agent_login.html')

def agent_login(request):

    return render(request,'newChatUI/agent_login.html')

@login_required
def agreements_user(request):
    
    user = request.user
    profile_picture = user.profile_picture.url 

    return render(request,'newChatUI/Agreements_user.html',{
        'user': user,
        'profile_picture': profile_picture
    })

@login_required
def community_user(request):

    return render(request,'newChatUI/Community_user.html')

@login_required
def details_v2_user(request):
    user = request.user
    profile_picture = user.profile_picture.url 

    return render(request,'newChatUI/details_v2_user.html',{'user': user,'profile_picture': profile_picture})

@login_required
def help_supp_user(request):
    
    user = request.user
    profile_picture = user.profile_picture.url 

    return render(request,'newChatUI/help&supp_user.html', {
        'user': user,
        'profile_picture': profile_picture
    })


@login_required
def init_user(request):

    return render(request,'newChatUI/init_user.html')


@login_required
def onlychat_agent(request):
    
    user = request.user
    profile_picture = user.profile_picture.url 

    return render(request,'newChatUI/onlychat_agent.html', {
        'user': user,
        'profile_picture': profile_picture
    })


@login_required
def personal_details(request):
    
    return render(request,'newChatUI/personal_details.html')   


@login_required
def user_auth_by_agent(request):
    
    user = request.user
    profile_picture = user.profile_picture.url 
    
    return render(request,'newChatUI/user_auth_by_agent.html', {
        'user': user,
        'profile_picture': profile_picture
    })  







from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, login
import json
from django.contrib.auth import get_user_model


User = get_user_model()

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        try:
            name = request.POST.get("name")
            contact1 = request.POST.get("contact1")
            contact2 = request.POST.get("contact2")
            email = request.POST.get("email")
            password = request.POST.get("password")
            password2 = request.POST.get("password2")
            dc_code = request.POST.get("dc_code")  
            date_of_birth = request.POST.get("date_of_birth")  
            occupation = request.POST.get("occupation")  
            ip_address = request.POST.get("ip_address")  
            course_name = request.POST.get("course_name")  
            college_name = request.POST.get("college_name")  
            company_name = request.POST.get("company_name")  
            pan_number = request.POST.get("pan_number")  

            
            profile_picture = request.FILES.get("captured-image-file")
            aadhar_front = request.FILES.get("aadhar_front")
            aadhar_back =  request.FILES.get("aadhar_back")
            pan_card = request.FILES.get("pan_card")
            
             
            
            
            # Check if passwords match
            if password != password2:
                return JsonResponse({"password2": ["Passwords do not match."]}, status=400)

            # Check if user already exists
            if User.objects.filter(email=email).exists():
                return JsonResponse({"email": ["Email already in use."]}, status=400)

            # Create a new user
            user = User(
                    name=name,
                    email=email,
                    contact_number=contact1,
                    alternate_contact_number=contact2,
                    dc_code=dc_code,
                    aadhar_card_front =aadhar_front,
                    aadhar_card_back=aadhar_back,
                    pan_card=pan_card,
                    occupation =occupation,
                    course_name=course_name,
                    college_name=college_name,
                    company_name=company_name,
                    ip_address=ip_address,
                    date_of_birth=date_of_birth,
                    pan_number=pan_number,
                    profile_picture=profile_picture,
                    
                )
            user.set_password(password)
            user.save()


            return JsonResponse({"message": "User registered successfully!"}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid data format."}, status=400)

    return JsonResponse({"error": "Invalid request method."}, status=405)


from django.contrib.auth import authenticate,login
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import redirect

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        print('email', email)
        print('password', password)
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            
            if not user.is_active:
                return JsonResponse({'error': 'Account is inactive. Please contact support.'}, status=403)
            
            user.is_logged_in = True
            user.save()
            
            login(request, user)
            
            user_data = {
                'user': user.name,
                'is_csa': user.is_csa,
                 "profile_photo": user.profile_picture.url if user.profile_picture else None,
            }
            
           
            if user.is_csa:
           
                return JsonResponse({'message': 'Login successful', 'redirect_url': '/V2_DCEMI/agent_home/'})
            else:
            
                return JsonResponse({'message': 'Login successful', 'redirect_url': '/V2_DCEMI/chat_page_user/', 'user': user_data,
                    'to_settings': True})
        
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


@login_required
def chat_page_user(request):
    user = request.user
    profile_picture = user.profile_picture.url 
    
    available_csas = User.objects.filter(is_csa=True, is_idle=True)
    print("available_csa",available_csas)
    if not available_csas:
       
        return JsonResponse({
            'status': 'no_csa_available',
            'message': 'No CSA is available right now. Please try again later.'
            
        })
    user_attachments = Message.objects.filter(sender=user, attachment__isnull=False).exclude(attachment='').order_by('-timestamp') 
    print('attachments',user_attachments)   
    return render(request,'newChatUI/chat_page_user.html',{
        'user': user,
        'profile_picture': profile_picture,
        'available_csas': available_csas,
        'user_attachments': user_attachments
    },)
 
@login_required
def request_chat(request, csaId):
    
    user = request.user
    print("newuser",user)
    # Check if there is an existing chat request for the user that is not accepted yet
    existing_chat_request = ChatRequest.objects.filter(user=user, csa_id=csaId, accepted=False).first()

    if existing_chat_request:
        # If there is an existing unaccepted chat request, use it
        chat_request = existing_chat_request
    else:
        csa = get_object_or_404(User, id=csaId, is_csa=True)       
        chat_request = ChatRequest.objects.create(user=user, csa=csa, accepted=False)
        chat_request.save()
    return JsonResponse({
                'status': 'success',
                 'user': {
                    'user_id': user.id,
                    'email': user.email,
                    'is_csa': user.is_csa,
                    'chat_request_id':chat_request.id
                }
            })
   
    

@login_required 
def get_registered_users_info(request):
    users = User.objects.filter(is_csa=False)
    
    user_data = [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "aadhar_front": user.aadhar_card_front.url if user.aadhar_card_front else None,
            "contact_number": user.contact_number,
            "pan_card": user.pan_card.url  if user.pan_card else None,
            "date_of_birth": user.date_of_birth,
            "aadhar_back": user.aadhar_card_back.url if user.aadhar_card_back else None,
            "profile_photo": user.profile_picture.url if user.profile_picture else None,
            "occupation": user.occupation,
            "company": user.company_name,
            "alternate_contact_number":user.alternate_contact_number,
            "is_active":user.is_active,
            
        }
        for user in users
    ]
    
    return JsonResponse({"users": user_data}, safe=False)
    


from django.shortcuts import redirect
from django.contrib.auth import logout
def logout_view(request):
    
    if request.user.is_authenticated:
        request.user.is_logged_in = False
        request.user.logout_time = now()
        request.user.save()

        if request.user.is_csa:
            logout(request)
            return redirect('/V2_DCEMI/agent_login')  
        else:
            logout(request)
            return redirect('/V2_DCEMI/login_page')   
    else:
        logout(request)
        return redirect('/V2_DCEMI/login_page') 
    
from django.http import JsonResponse
from myapp.models import Message
from django.http import JsonResponse
from myapp.models import Message, ChatRequest
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
import os

@csrf_exempt
@login_required
def view_messages(request, chatRequestId):
    if request.method == "POST":
        # Check if the request contains a file or message
        message = request.POST.get("message", "").strip()
        attachment = request.FILES.get("attachment")

        # Assuming the user is authenticated
        user = request.user

        # Fetch the ChatRequest using the provided chatRequestId
        try:
            chat_request = ChatRequest.objects.get(id=chatRequestId)
        except ChatRequest.DoesNotExist:
            return JsonResponse({'error': 'Chat request not found.'}, status=404)

        if not message and not attachment:
            return JsonResponse({'error': 'Message or attachment must be provided.'}, status=400)

        # Create the new message
        user_message = Message.objects.create(
            chat_request=chat_request,
            sender=user,
            message=message if message else None,
            attachment=attachment if attachment else None
        )

        # Retrieve previous messages linked to the chat request
        previous_messages = Message.objects.filter(chat_request__user=user).order_by('timestamp')

        # Prepare the list of previous messages
        messages = []
        for msg in previous_messages:
            messages.append({
                'sender': msg.sender.name,
                'message': msg.message if msg.message else None,
                'attachment': msg.attachment.url if msg.attachment else None,
                'timestamp':localtime(msg.timestamp).strftime('%Y-%m-%d %H:%M:%S'),
                'profile_picture': msg.sender.profile_picture.url if msg.sender.profile_picture else None,
            })

        # Return the messages in the response
        return JsonResponse({'messages': messages})

    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)



from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import User, Message
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from myapp.models import User, Message, ChatRequest
from django.contrib.auth.decorators import login_required

@login_required
def get_users_info_and_messages(request):
    if request.method == "GET":
        try:
    
            users_with_requests = User.objects.filter(chat_requests__accepted=False).distinct()
            print('userswithreq',users_with_requests)

            user_data = []

            for user in users_with_requests:
                # User info
                user_info = {
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                    'contact_number': user.contact_number,
                    'profile_picture': user.profile_picture.url if user.profile_picture else None,  # Get the URL of the image
                }

               
                chat_requests = ChatRequest.objects.filter(user=user, accepted=False)
                print('chq_rqst',chat_requests)

                chat_request_ids = [chat_request.id for chat_request in chat_requests]

             
                latest_message = Message.objects.filter(chat_request__in=chat_requests,sender=user).order_by('-timestamp').first()

                if latest_message:
                    message_info = {
                        'message': latest_message.message,
                        'timestamp': latest_message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    }
                else:
                    message_info = None

                user_data.append({
                    'user_info': user_info,
                    'chat_request_ids': chat_request_ids,
                    'last_message': message_info
                })

            return JsonResponse({'users': user_data})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)




@csrf_exempt 
@login_required
def toggle_status(request, user_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        is_active = data.get('is_active')
        user = get_object_or_404(User, id=user_id)
        user.is_active = is_active
        user.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False}, status=400)



from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import ChatRequest, Message
from django.contrib.auth.decorators import login_required
from django.utils.timezone import localtime


def agent_chat_page(request):
    user = request.user
    return render (request, 'newChatUI/chat_page_agent.html',{'user':user})



@login_required
def chat_page_agent(request,user_id):
    try:
   
        user = request.user
        print('user', user)
        print('user_id_in_agent_page',user_id)

        if user.is_csa:
            # user.is_idle = False
            user.save()

     
        chat_request = ChatRequest.objects.filter(user=user_id,accepted=False).first()
        if not chat_request:
            return JsonResponse({"error": "Chat request not found or already accepted."}, status=404)

       #chat_request.accepted = True
        chat_request.csa = user
        chat_request.save()

        
        chat_requests = ChatRequest.objects.filter(user=user_id, csa=user)
        print('chat_requests_agent',chat_requests)

        # If no chat requests exist, return an empty list
        if not chat_requests.exists():
            return JsonResponse({"messages": []}, safe=False)

        # Fetch all messages related to these chat requests
        previous_messages = Message.objects.filter(chat_request__in=chat_requests).order_by('timestamp')

        # Prepare messages data for the response
        messages = []
        for message in previous_messages:
            messages.append({
                'is_csa': message.sender.is_csa,
                'sender': message.sender.name,
                'message': message.message,
                'timestamp': localtime(message.timestamp).strftime("%Y-%m-%d %H:%M:%S"),
                'profile_picture': message.sender.profile_picture.url if message.sender.profile_picture else None,
            })

        return JsonResponse({'success': True, 'messages': messages})

    except ChatRequest.DoesNotExist:
        # Handle case where ChatRequest doesn't exist
        return JsonResponse({"error": "Chat request not found or already accepted."}, status=404)



@login_required
def load_new_messages_user(request,csaId):
    
    user = request.user
    try:
         user = request.user
        
        # Fetch all chat requests between the user and the specified CSA
         chat_requests = ChatRequest.objects.filter(user=user,csa_id=csaId)
        
        # If no chat requests exist, return an empty list
         if not chat_requests.exists():
            return JsonResponse({"messages": []}, safe=False)
        
        # Fetch all messages related to these chat requests
         previous_messages = Message.objects.filter(chat_request__in=chat_requests).order_by('timestamp')

        # Prepare messages data for the response
         messages = []
         for message in previous_messages:
            messages.append({
                'sender': message.sender.name,
                'message':  message.message if message.message else None,
                'timestamp': localtime(message.timestamp).strftime("%Y-%m-%d %H:%M:%S"),
                'is_csa': message.sender.is_csa,
                'attachment': message.attachment.url if message.attachment else None,
                'profile_picture': message.sender.profile_picture.url if message.sender.profile_picture else None,  # Get the URL of the image 
            })
            
         user_data = {
            'id': request.user.id,
            'name': request.user.name,
            'email': request.user.email,
            # Add other fields as needed
        }

         return JsonResponse({
            'messages': messages,
            'user': user_data,
        }, safe=False)
        
    except ChatRequest.DoesNotExist:
        # Handle case where ChatRequest doesn't exist
        return JsonResponse({"error": "Chat request not found."}, status=404)
    
    
    
@login_required
def load_new_messages_agent(request,user_id):
    
    user = request.user
    try:
         user = request.user
        
        # Fetch all chat requests between the user and the specified CSA
         chat_requests = ChatRequest.objects.filter(user_id=user_id,csa_id=user.id)
        
        # If no chat requests exist, return an empty list
         if not chat_requests.exists():
            return JsonResponse({"messages": []}, safe=False)
        
        # Fetch all messages related to these chat requests
         previous_messages = Message.objects.filter(chat_request__in=chat_requests).order_by('timestamp')

        # Prepare messages data for the response
         messages = []
         for message in previous_messages:
            messages.append({
                'sender': message.sender.name,
                'message':  message.message if message.message else None,
                'timestamp': localtime(message.timestamp).strftime("%Y-%m-%d %H:%M:%S"),
                'is_csa': message.sender.is_csa,
                'attachment': message.attachment.url if message.attachment else None,
                'profile_picture': message.sender.profile_picture.url if message.sender.profile_picture else None,  # Get the URL of the image 
            })
            
         user_data = {
            'id': request.user.id,
            'name': request.user.name,
            'email': request.user.email,
        
        }

         return JsonResponse({
            'messages': messages,
            'user': user_data,
        }, safe=False)
        
    except ChatRequest.DoesNotExist:
        # Handle case where ChatRequest doesn't exist
        return JsonResponse({"error": "Chat request not found."}, status=404)    


@login_required
def get_user_chat_history(request,chatRequestId):
    
    try:
        # Fetch the current chat request
        chat_request = ChatRequest.objects.get(id=chatRequestId)
    
        chat_user = chat_request.user

        previous_messages = Message.objects.filter(chat_request__user=chat_user).order_by('timestamp')
        # Prepare messages data for the response
        messages = []
        for message in previous_messages:
            messages.append({
                'sender': message.sender.name,
                'message':  message.message if message.message else None,
                'timestamp': localtime(message.timestamp).strftime("%Y-%m-%d %H:%M:%S"),
                'is_csa': message.sender.is_csa,
                'attachment': message.attachment.url if message.attachment else None,
                
                'profile_picture': message.sender.profile_picture.url if message.sender.profile_picture else None,  # Get the URL of the image
                   
            })
            
        user_data = {
            'id': request.user.id,
            'name': request.user.name,
            'email': request.user.email,
            # Add other fields as needed
        }

        return JsonResponse({
            'chat_request_id': chatRequestId,
            'messages': messages,
            'user': user_data,
        }, safe=False)
        
    except ChatRequest.DoesNotExist:
        # Handle case where ChatRequest doesn't exist
        return JsonResponse({"error": "Chat request not found."}, status=404)


from myapp.models import ConsentQuestion

@login_required
def get_consent_form(request):
    questions = ConsentQuestion.objects.all()
    data = []

    for question in questions:
        options = list(question.options.values('id', 'option_text'))
        data.append({
            'question': question.question_text,
            'options': options,
            'question_id': question.id,
        })
        
    return JsonResponse({'questions': data})



from myapp.models import ConsentAnswer, ConsentOption
from django.core.files.storage import FileSystemStorage

@login_required
@csrf_exempt
def save_consent_answers(request):
    if request.method == "POST":
        user = request.user  # Assuming user is logged in
        if ConsentAnswer.objects.filter(user=user).exists():
            return JsonResponse({'status': 'error', 'message': 'You have already submitted the form.'})
        
        questions = request.POST.getlist('questions[]')
        options = request.POST.getlist('options[]')
        language = request.POST.get('language')
        video = request.FILES.get('video')
        
        
        if video:
            fs = FileSystemStorage()
            filename = fs.save(video.name, video)
            video_url = fs.url(filename)
        else:
            video_url = None

        for i in range(len(questions)):
            question_id = questions[i]
            selected_option_id = options[i]
           

            # Get the question and option
            question = ConsentQuestion.objects.get(id=question_id)
            selected_option = ConsentOption.objects.get(id=selected_option_id)

            # Save the user's answer
            ConsentAnswer.objects.create(
                user=user,
                question=question,
                selected_option=selected_option,
                language=language,
                video=video_url
            )

        return JsonResponse({'status': 'success', 'message': 'Answers saved successfully'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

from django.core.exceptions import ObjectDoesNotExist

@login_required
@csrf_exempt
def update_details(request):
    
    if request.method == 'POST':
        user_id = request.POST.get('id')
        try:
          
            user = User.objects.get(id=user_id)
            
            name = request.POST.get('name')
            if name :
               user.name = name
           
            contact_number = request.POST.get('contact_number')
            if contact_number:
                user.contact_number = contact_number
                
            email = request.POST.get('email')
            if email:
                user.email = email
            
            occupation = request.POST.get('occupation')
            if occupation:
                user.occupation = occupation
            
            date_of_birth = request.POST.get('date_of_birth')
            if date_of_birth:
                user.date_of_birth = date_of_birth    
                
            course_name = request.POST.get('course_name')
            if course_name:
                user.course_name = course_name
                
            college_name = request.POST.get('college_name')
            if college_name:
                user.college_name = college_name
                
            company_name = request.POST.get('company_name')
            if company_name:
                user.company_name = company_name
                
            current_residential_address = request.POST.get('current_residential_address')
            if current_residential_address:
                user.current_residential_address = current_residential_address    
                
            permanent_residential_address = request.POST.get('permanent_residential_address')
            if permanent_residential_address:
                user.permanent_residential_address = permanent_residential_address 
            
            
            facebook_id = request.POST.get('facebook_id')
            if facebook_id:
                user.facebook_id = facebook_id           
           
            
            instagram_id = request.POST.get('instagram_id')
            if instagram_id:
                user.instagram_id = instagram_id
                
            company_address = request.POST.get('company_address')
            if company_address:
                user.company_address = company_address
                
            work_contact_number = request.POST.get('work_contact_number')
            if work_contact_number:
                user.work_contact_number = work_contact_number
                
            salary = request.POST.get('salary')
            if salary:
                user.salary = salary
                
                
            years_in_current_role = request.POST.get('years_in_current_role')
            if years_in_current_role:
                user.years_in_current_role = years_in_current_role
                
            year_of_admission = request.POST.get('year_of_admission')
            if year_of_admission:
                user.year_of_admission = year_of_admission 
                
            expected_graduation_year = request.POST.get('expected_graduation_year')
            if expected_graduation_year:
                user.expected_graduation_year = expected_graduation_year       
            
            
            past_employement = request.POST.get('past_employement')
            if past_employement:
                user.past_employement = past_employement                            
                
            achievements = request.POST.get('achievements')
            if achievements:
                user.achievements = achievements   
            

            father_name = request.POST.get('father_name')
            if father_name:
                user.father_name = father_name
                
            father_occupation = request.POST.get('father_occupation')
            if father_occupation:
                user.father_occupation = father_occupation
            
            
            mother_name = request.POST.get('mother_name')
            if mother_name:
                user.mother_name = mother_name
                
            siblings = request.POST.get('siblings')
            if siblings:
                user.siblings = siblings  
                
            
            spouse_name = request.POST.get('spouse_name')
            if spouse_name:
                user.spouse_name = spouse_name 
                
            children_details = request.POST.get('children_details')
            if children_details:
                user.children_details = children_details
                
            
            type_of_residence = request.POST.get('type_of_residence')
            if type_of_residence:
                user.type_of_residence = type_of_residence
                
            
            years_at_current_address = request.POST.get('years_at_current_address')
            if years_at_current_address:
                user.years_at_current_address = years_at_current_address 
                
            
            previous_address = request.POST.get('previous_address')
            if previous_address:
                user.previous_address = previous_address
                
            current_and_past_loans = request.POST.get('current_and_past_loans')
            if current_and_past_loans:
                user.current_and_past_loans = current_and_past_loans      
                
            
            total_monthly_emi_commitments = request.POST.get('total_monthly_emi_commitments')
            if total_monthly_emi_commitments:
                user.total_monthly_emi_commitments = total_monthly_emi_commitments
                
                
            credit_score = request.POST.get('credit_score')
            if credit_score:
                user.credit_score = credit_score
                
                
            association_memberships = request.POST.get('association_memberships')
            if association_memberships:
                user.association_memberships = association_memberships 
                
             
            reference_name = request.POST.get('reference_name')
            if reference_name:
                user.reference_name = reference_name                                                    
                
            reference_relationship = request.POST.get('reference_relationship')
            if reference_relationship:
                user.reference_relationship = reference_relationship     
            
            
            reference_contact_number = request.POST.get('reference_contact_number')
            if reference_contact_number:
                user.reference_contact_number = reference_contact_number
                
            date = request.POST.get('date')
            if date:
                user.date = date    
        

            # Handle file upload
            if 'applicant_signature' in request.FILES:
                user.applicant_signature = request.FILES['applicant_signature']

            # Save the updated user instance
            user.save()

            # Respond with success message
            return JsonResponse({'status': 'success', 'message': 'User details updated successfully!'})

        except ObjectDoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User not found'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    


@login_required
def get_messages(request, csaId):
    try: # Get the logged-in user
        user = request.user
        
        chat_requests = ChatRequest.objects.filter(user=user, csa_id=csaId)

        if not chat_requests.exists():
            return JsonResponse({"messages": []}, safe=False)
       
        messages = Message.objects.filter(chat_request__in=chat_requests).order_by('timestamp')

        messages_data = [
            {
                "id": message.id,
                "sender": message.sender.name if message.sender else None,
                "message": message.message,
                "attachment": message.attachment.url if message.attachment else None,
                "timestamp": message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                'profile_picture': message.sender.profile_picture.url if message.sender.profile_picture else None,
                
            }
            for message in messages
        ]

        return JsonResponse({"messages": messages_data}, safe=False)
    except ObjectDoesNotExist as e:

        return JsonResponse({"error": f"Object not found: {str(e)}"}, status=404)
    except Exception as e:
        return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)



@login_required
def get_message_count(request, csaId):
    
    user= request.user

    chat_requests = ChatRequest.objects.filter(user=user, csa_id=csaId)
        
    if chat_requests:
        new_messages_count = Message.objects.filter(chat_request__in=chat_requests).count()
        return JsonResponse({'message_count': new_messages_count})
    
    return JsonResponse({'message_count': 0})  


def getthe_message_count(request,user_id):
    print("get_message_count called with userId:", user_id)
    user= request.user
    
    chat_requests = ChatRequest.objects.filter(user=user_id, csa_id=user.id)
    if chat_requests:
        new_messages_count = Message.objects.filter(chat_request__in=chat_requests).count()
        print("messagecount",new_messages_count)
        return JsonResponse({'message_count': new_messages_count})
    
    return JsonResponse({'message_count': 0})  

@login_required
@csrf_exempt
def update_user_typing_status(request,chatRequestId):
    if request.method =="POST":
        user = request.user
        chat_request = ChatRequest.objects.get(id =chatRequestId,user=user)     
        user_typing =  request.POST.get('user_typing')
        if user_typing is not None:
            if user_typing.lower() == "true":
                chat_request.user_typing = True
            elif user_typing.lower() == "false":
                chat_request.user_typing = False
            else:
                return JsonResponse(
                    {"status": "error", "message": "Invalid value for `user_typing`. Must be 'true' or 'false'."},
                    status=400,
                )
        
            chat_request.save()
            return JsonResponse({"status": "success", "message": "Typing status updated successfully."})       
        
        return JsonResponse({"status": "error", "message": "`user_typing` field is required."}, status=400)
    
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)   


@login_required
@csrf_exempt
def update_agent_typing_status(request,chatRequestId):
    if request.method =="POST":
        user = request.user
        chat_request = ChatRequest.objects.get(id =chatRequestId,csa=user) 
       
        csa_typing =  request.POST.get('csa_typing')
        print("is_csa_typing",csa_typing)
        if csa_typing is not None:
            if csa_typing.lower() == "true":
                chat_request.csa_typing = True
            elif csa_typing.lower() == "false":
                chat_request.csa_typing = False
            else:
                return JsonResponse(
                    {"status": "error", "message": "Invalid value for `user_typing`. Must be 'true' or 'false'."},
                    status=400,
                )
            
            chat_request.save()
            return JsonResponse({"status": "success", "message": "Typing status updated successfully."})       
        
        return JsonResponse({"status": "error", "message": "`csa_typing` field is required."}, status=400)
    
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)





@login_required
@csrf_exempt
def get_csa_typing_status(request, chatRequestId):
    if request.method == "POST":  

        csa = request.POST.get('csa')
        
        
        if not csa:
            return JsonResponse({"status": "error", "message": "`csa` field is required."}, status=400)

        try:
            
            chat_request = ChatRequest.objects.get(id=chatRequestId, csa=csa)
            
            csa_typing = chat_request.csa_typing
            
            csa_name = chat_request.csa.name
        

            return JsonResponse({"status": "success", "csa_typing": csa_typing, "csa": csa_name})
        
        except ChatRequest.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Chat request not found."}, status=404)

    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)



@login_required
@csrf_exempt
def get_user_typing_status(request, chatRequestId):
    if request.method == "POST":  

        user = request.POST.get('user')
        
        
        if not user:
            return JsonResponse({"status": "error", "message": "`csa` field is required."}, status=400)

        try:
            
            chat_request = ChatRequest.objects.get(id=chatRequestId, user=user)
            
            user_typing = chat_request.user_typing
            user_name = chat_request.user.name
        

            return JsonResponse({"status": "success", "user_typing": user_typing, "user": user_name})
        
        except ChatRequest.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Chat request not found."}, status=404)

    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)




from django.utils.timezone import now

@csrf_exempt
@login_required
def capture_image(request):
    if request.method == 'POST':
        if request.user.is_csa:
            return JsonResponse({"success": True, "message": "Image capture skipped for CSA user"})

       
        image = request.FILES.get('image')
        if image:
            captured_image = HistoryCapturedImage.objects.create(
                user=request.user,
                image_captured=image,
                timestamp=now()
            )
            return JsonResponse({"success": True, "message": "Image captured successfully"})
        
        return JsonResponse({"success": False, "message": "No image data provided"}, status=400)
    
    return JsonResponse({"success": False, "message": "Invalid request method"}, status=405)


@login_required 
@csrf_exempt
def callback_request(request):
    
    if request.method =="POST":
        
        user_name= request.POST.get("user_name")
        
        user_number= request.POST.get("user_number")
        if user_name and user_number:
            callback_request = CallBackRequest.objects.create(
                user=request.user,
                name = user_name,
                contact_number = user_number,
                timestamp=now()
                
            )
            return JsonResponse({"success": True, "message": "Call Back requested successfully"})
        
        return JsonResponse({"success": False, "message": "No request raised"}, status=400)
    
    return JsonResponse({"success": False, "message": "Invalid request method"}, status=405)
        
        


@login_required
@csrf_exempt
def save_user_info(request):
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')
        geolocation = request.POST.get('geolocation')
        device = request.POST.get('device')
        browser = request.POST.get('browser')
        screen_size = request.POST.get('screen_size')
        network_type = request.POST.get('network_type')
        
        if UserInfo.objects.filter(user=request.user).exists():
            return JsonResponse({'message': 'User info already exists. No new data saved.'})
        
        user_info = UserInfo.objects.create(
            user = request.user,
            ip_address=ip_address,
            geolocation=geolocation,
            device=device,
            browser=browser,
            screen_size=screen_size,
            network_type=network_type
        )

        return JsonResponse({'message': 'User info saved successfully!', 'id': user_info.id})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
        


@login_required
def check_consent_status(request):
    has_submitted_consent = ConsentAnswer.objects.filter(user=request.user).exists()
    return JsonResponse({'has_submitted_consent': has_submitted_consent})        




@login_required
def check_profile_completion(request):
    user = request.user

    required_fields = [
        'name', 'contact_number', 'email', 'occupation', 'date_of_birth',
        'course_name', 'college_name', 'company_name', 'current_residential_address',
        'permanent_residential_address', 'facebook_id', 'instagram_id', 'company_address',
        'work_contact_number', 'salary', 'years_in_current_role', 'year_of_admission',
        'expected_graduation_year', 'past_employement', 'achievements', 'father_name', 
        'father_occupation', 'mother_name', 'siblings', 'spouse_name', 'children_details', 
        'type_of_residence', 'years_at_current_address', 'previous_address', 'current_and_past_loans',
        'total_monthly_emi_commitments', 'credit_score', 'association_memberships', 
        'reference_name', 'reference_relationship', 'reference_contact_number', 'date', 
        'applicant_signature'
    ]
    
    incomplete_fields = []
    for field in required_fields:
        if not getattr(user, field, None):
            incomplete_fields.append(field)

    if incomplete_fields:
        return JsonResponse({'status': 'incomplete', 'message': 'Profile update pending. If having any trouble in updating Please contact chat support.'})
    else:
        return JsonResponse({'status': 'complete', 'message': 'Profile is complete.'})
    
    
import uuid
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

def generate_unique_filename():
    """Generate a unique filename using UUID."""
    return str(uuid.uuid4())

@csrf_exempt
def save_video(request):
    """Save the uploaded .webm video directly without conversion."""
    if request.method == 'POST' and request.FILES.get('video'):
        video_file = request.FILES['video']
        chat_request_id = request.POST.get('chatRequestId')

        try:
           
            video = Video.objects.filter(chat_request_id=chat_request_id, status='start') \
                                  .exclude(status='completed') \
                                  .order_by('-timestamp').first()

            if not video:
                return JsonResponse({'status': 'error', 'message': 'Video entry not found or already completed'})

          

            # Update the video record
            video.video = video_file
            video.status = 'completed'
            video.save()
            video_url = video.video.url

            return JsonResponse({
                'status': 'success',
                'message': 'Video saved successfully!',
                'video_url': video_url
            })
        except Video.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Video entry not found'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Failed to save video'})

@csrf_exempt
def start_video_recording(request):
    """Start a new video recording session."""
    if request.method == 'POST':
        data = json.loads(request.body)
        recorded_user_id = data.get('recorded_user_id')
        chat_request_id = data.get('chatRequestId')

        # Check if a recording is already in progress
        existing_video = Video.objects.filter(chat_request_id=chat_request_id, status='start').first()
        if existing_video:
            return JsonResponse({'status': 'error', 'message': 'Recording already in progress for this chatRequestId','video_id': existing_video.id})

        # Create a new video entry
        video = Video.objects.create(
            chat_request_id=chat_request_id,
            recorded_user_id=recorded_user_id,
            status='start',
            user=request.user,
        )

        return JsonResponse({'status': 'success', 'message': 'Recording started', 'chatRequestId': chat_request_id, 'video_id':video.id})

@csrf_exempt
def poll_video_recording(request):
    """Poll the status of the video recording."""
    chat_request_id = request.GET.get('chatRequestId')

    if not chat_request_id:
        return JsonResponse({'status': 'error', 'message': 'Missing chatRequestId'}, status=400)

    video = Video.objects.filter(chat_request_id=chat_request_id).order_by('-timestamp').first()
    
    if video and video.status == 'start':
        return JsonResponse({'status': 'start', 'chatRequestId': video.chat_request_id})
    elif video and video.status == 'completed':
        return JsonResponse({'status': 'completed', 'chatRequestId': video.chat_request_id})
    else:
        return JsonResponse({'status': 'waiting'})
    
    
@csrf_exempt
@login_required    
def check_video_status(request, video_id):
    """Check the status of the video recording."""
    try:
        video = Video.objects.get(id=video_id)
        return JsonResponse({
            'status': 'success',
            'video_status': video.status,
            'message': 'Video status retrieved successfully',
        })
    except Video.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Video not found'})
    

@csrf_exempt
def get_csa_online_status(request):
    
     if request.method == "POST":  

        csa = request.POST.get('csa')
        
        if not csa:
            return JsonResponse({"status": "error", "message": "`csa` field is required."}, status=400)

        try:
            
            user = User.objects.get(id=csa)
            
            user_online_status = user.is_logged_in
            user_logout_time = user.logout_time
                    
            return JsonResponse({"status": "success", "user_online_status": user_online_status,  "user_logout_time": user_logout_time})
        
        except ChatRequest.DoesNotExist:
            return JsonResponse({"status": "error", "message": "user online status not found."}, status=404)

     return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)
 
 
 
 
@csrf_exempt
def get_user_online_status(request):
    
     if request.method == "POST":  

        user = request.POST.get('user_id')
        
        if not user:
            return JsonResponse({"status": "error", "message": "`user` field is required."}, status=400)

        try:
            
            user = User.objects.get(id=user)
            
            user_online_status = user.is_logged_in
            user_logout_time = user.logout_time
                    
            return JsonResponse({"status": "success", "user_online_status": user_online_status,  "user_logout_time": user_logout_time})
        
        except ChatRequest.DoesNotExist:
            return JsonResponse({"status": "error", "message": "user online status not found."}, status=404)

     return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)






def get_csa_current_message_count(request):
    user_id = request.user.id  # Assuming the user is authenticated
    csa_id = request.GET.get('csa_id')

    if csa_id:
        try:
            # Get or create the message count entry
            message, created = MessageCount_csa.objects.get_or_create(
                user_id=user_id,
                csa_id=csa_id,
                defaults={'message_count': 0}
            )
            
            # Return the current message count
            return JsonResponse({'message_count': message.message_count})
        
        except Exception as e:
            # Log the error for debugging and return an error response
            print(f"Error occurred: {e}")
            return JsonResponse({'error': 'An error occurred'}, status=500)

    # If csa_id is not provided, return a bad request response
    return JsonResponse({'message_count': 0}, status=400)





def get_user_current_message_count(request):
    csa_id = request.user.id  
    user_id = request.GET.get('user_id')

    if user_id:
        try:
            # Get or create the message count entry
            message, created = MessageCount_user.objects.get_or_create(
                user_id=user_id,
                csa_id=csa_id,
                defaults={'message_count': 0}
            )
            
            # Log if a new record is created
            if created:
                print(f"Created new record for user_id={user_id}, csa_id={csa_id} with default count=0")
            
            # Return the current message count
            return JsonResponse({'message_count': message.message_count})

        except Exception as e:
            print(f"Error occurred: {e}")
            return JsonResponse({'error': 'An error occurred'}, status=500)

    # If user_id is not provided, return a bad request response
    return JsonResponse({'message_count': 0}, status=400)



@csrf_exempt 
def update_csa_current_message_count(request):
    if request.method == 'POST':
        
        user_id = request.user.id
        csa_id = request.POST.get('csa_id')
        message_count = request.POST.get('message_count')

        try:
            
            message = MessageCount_csa.objects.get(user_id=user_id,csa_id=csa_id)

            message.message_count = message_count
            message.save() 

            return JsonResponse({'status': 'success', 'message_count': message_count})

        except MessageCount_csa.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'CSA not found'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@csrf_exempt 
def update_user_current_message_count(request):
    if request.method == 'POST':
        
        csa_id = request.user.id
        user_id = request.POST.get('user_id')
        message_count = request.POST.get('message_count')

        try:
            
            message = MessageCount_user.objects.get(user_id=user_id,csa_id=csa_id)

            message.message_count = message_count
            message.save() 

            return JsonResponse({'status': 'success', 'message_count': message_count})

        except MessageCount_user.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'CSA not found'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)




def get_videos(request):
    user_id = request.GET.get('user_id')

    if not user_id:
        return JsonResponse({'status': 'error', 'message': 'User ID is required'}, status=400)

    videos = Video.objects.filter(recorded_user_id=user_id).values('id', 'video', 'timestamp', 'status')
    video_list = [
        {
            'id': video['id'],
            'video_url': settings.MEDIA_URL + video['video'],
            'timestamp': video['timestamp'],
            'status': video['status']
        } for video in videos
    ]

    return JsonResponse({'status': 'success', 'videos': video_list})  
  
from django.conf import settings
from django.http import JsonResponse

import os
@csrf_exempt
@login_required
def get_attachments(request):
    user_id = request.POST.get('user')  

    if not user_id:
        return JsonResponse({'error': 'user_id is required'}, status=400)

    try:
        # Fetch all attachments for the given sender_id
        attachments = Message.objects.filter(sender_id=user_id).exclude(attachment="")
        
        # Collect attachments with file size
        attachments_data = []
        for attachment in attachments:
            file_path = os.path.join(settings.MEDIA_ROOT, attachment.attachment.name)
            file_size = os.path.getsize(file_path) if os.path.exists(file_path) else 0  # File size in bytes
            attachments_data.append({
                'url': f"{settings.MEDIA_URL}{attachment.attachment.name}",
                'size': file_size
            })

        return JsonResponse({'attachments': attachments_data}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)




def get_user_details(request):
    user_id = request.GET.get('user_id')  # Get the user_id from the request
    try:
        user = User.objects.get(id=user_id)
        user_data = {
            'name': user.name,
            'email': user.email,
            'contact_number': user.contact_number,
            'occupation': dict(User.OCCUPATION_CHOICES).get(user.occupation, 'Not Specified'),
            'profile_picture': user.profile_picture.url if user.profile_picture else '',
            'course_name': user.course_name,
            'college_name': user.college_name,
            'company_name':user.company_name,
            'dc_code':user.dc_code,
            'ip_address':user.ip_address,
            'current_residential_address':user.current_residential_address,
            'facebook_id':user.facebook_id,
            'instagram_id':user.instagram_id,
            'father_name':user.father_name,
            'father_occupation':user.father_occupation,
            'mother_name':user.mother_name,
            'company_address':user.company_address,
            'work_contact_number':user.work_contact_number,
            'salary':user.salary,
            'year_in_current_role':user.years_in_current_role,
            'year_of_admission': user.year_of_admission,
            'expected_graduation_year':user.expected_graduation_year,
            'past_employement':user.past_employement,
            'siblings':user.siblings,
            'spouse_name':user.spouse_name,
            'children_details':user.children_details,
            
            
            # Add other fields here as needed
        }
        return JsonResponse({'user': user_data})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
