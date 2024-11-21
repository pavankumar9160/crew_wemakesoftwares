from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from myapp.models import *


def signup_page(request):
    if request.user.is_authenticated:
        if request.user.is_csa:
            return redirect('/agent_home/')  
        else:
            return redirect('/dashboard_user/')

    return render(request,'signup_user.html')

def login_page(request):
    if request.user.is_authenticated:
        if request.user.is_csa:
            return redirect('/agent_home/')  
        else:
            return redirect('/dashboard_user/')

    return render(request,'login_user.html') 

@login_required
def chat_page_user(request):
    
    user = request.user
    
    print('user_id' , user.id)

    return render(request,'chat_page_user.html', {'user': user})  

@login_required
def dashboard_user(request):
    
    user = request.user
    profile_picture = user.profile_picture.url 
    print('user',user.name)
    
    return render(request, 'dashboard_user.html', {
        'user': user,
        'profile_picture': profile_picture
    })
    
@login_required
def agent_dashboard(request):
    if request.user.is_csa:
        user = request.user
        profile_picture = user.profile_picture.url 
        return render(request,'agent_dashboard.html',{
            'user': user,
            'profile_picture': profile_picture
    })
    else :
     return render(request,'agent_login.html')
        
@login_required
def agent_home(request):
    if request.user.is_csa:
        
     return render(request,'agent_home.html')
    else:
     return render(request,'agent_login.html')

def agent_login(request):

    return render(request,'agent_login.html')

@login_required
def agreements_user(request):
    
    user = request.user
    profile_picture = user.profile_picture.url 

    return render(request,'Agreements_user.html',{
        'user': user,
        'profile_picture': profile_picture
    })

@login_required
def community_user(request):

    return render(request,'Community_user.html')

@login_required
def details_v2_user(request):
    user = request.user
    profile_picture = user.profile_picture.url 

    return render(request,'details_v2_user.html',{'user': user,'profile_picture': profile_picture})

@login_required
def help_supp_user(request):
    
    user = request.user
    profile_picture = user.profile_picture.url 

    return render(request,'help&supp_user.html', {
        'user': user,
        'profile_picture': profile_picture
    })


@login_required
def init_user(request):

    return render(request,'init_user.html')


@login_required
def onlychat_agent(request):
    
    user = request.user
    profile_picture = user.profile_picture.url 

    return render(request,'onlychat_agent.html', {
        'user': user,
        'profile_picture': profile_picture
    })


@login_required
def personal_details(request):
    
    return render(request,'personal_details.html')   


@login_required
def user_auth_by_agent(request):
    
    user = request.user
    profile_picture = user.profile_picture.url 
    
    return render(request,'user_auth_by_agent.html', {
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
            
           
            if user.is_csa:
           
                return JsonResponse({'message': 'Login successful', 'redirect_url': '/agent_home/'})
            else:
            
                return JsonResponse({'message': 'Login successful', 'redirect_url': '/dashboard_user/'})
        
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)



@login_required
def request_chat(request):
    user = request.user
    profile_picture = user.profile_picture.url 
    
    available_csas = User.objects.filter(is_csa=True, is_idle=True, is_logged_in=True)
    print("available_csa",available_csas)
    if not available_csas:
       
        return JsonResponse({
            'status': 'no_csa_available',
            'message': 'No CSA is available right now. Please try again later.'
        })
        
    # Check if there is an existing chat request for the user that is not accepted yet
    existing_chat_request = ChatRequest.objects.filter(user=user, accepted=False).first()

    if existing_chat_request:
        # If there is an existing unaccepted chat request, use it
        chat_request = existing_chat_request
    else:
        # If no unaccepted chat request, create a new one
        chat_request = ChatRequest.objects.create(user=user, accepted=False)
        chat_request.save()

    # Get the previous chat history, if any
    previous_messages = Message.objects.filter(
        chat_request__user=user).order_by('timestamp')

    # Prepare the list of previous messages to send
    messages = []
    for message in previous_messages:
        messages.append({
            'sender': message.sender.name,
            'message':  message.message if message.message else None,
            'timestamp': message.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'attachment': message.attachment.url if message.attachment else None,
            'profile_picture': message.sender.profile_picture.url if message.sender.profile_picture else None,  # Get the URL of the image
        })
        
    # If the request is AJAX (for the messages), return a JSON response
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':

            return JsonResponse({
                'status': 'success',
                'messages': messages,
                 'user': {
                    'user': user.name,
                    'email': user.email,
                    'is_csa': user.is_csa,
                }
            })
    print('user',user)    


    return render(request,'chat_page_user.html',{
        'chat_request_id': chat_request.id,
        'messages': messages, 
        'user': user,
        'profile_picture': profile_picture
    },)

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
    
    if request.user.is_authenticated and request.user.is_csa: 
        logout(request) 
        return redirect('agent_login')  
    else:
        logout(request)
        return redirect('login_page') 
    
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
                'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
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
            # Filter users who have chat requests with accepted=False
            users_with_requests = User.objects.filter(chat_requests__accepted=False).distinct()
            print('userswithreq',users_with_requests)

            user_data = []

            for user in users_with_requests:
                # User info
                user_info = {
                    'id': user.id,
                    'name': user.name,
                    'contact_number': user.contact_number,
                }

                # Retrieve all chat requests for the user where accepted=False
                chat_requests = ChatRequest.objects.filter(user=user, accepted=False)
                print('chq_rqst',chat_requests)

                # Gather chat_request_ids
                chat_request_ids = [chat_request.id for chat_request in chat_requests]

                # Retrieve the latest message for the user's chat requests
                latest_message = Message.objects.filter(chat_request__in=chat_requests,sender=user).order_by('-timestamp').first()

                # Message info
                if latest_message:
                    message_info = {
                        'message': latest_message.message,
                        'timestamp': latest_message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    }
                else:
                    message_info = None

                # Append user info, chat request ids, and latest message
                user_data.append({
                    'user_info': user_info,
                    'chat_request_ids': chat_request_ids,
                    'last_message': message_info
                })

            # Return the user data as a JsonResponse
            return JsonResponse({'users': user_data})

        except Exception as e:
            # Return an error response if something goes wrong
            return JsonResponse({'error': str(e)}, status=500)




@csrf_exempt 
@login_required# Only use @csrf_exempt if you are testing without CSRF protection
def toggle_status(request, user_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        is_active = data.get('is_active')

        # Fetch the user and update the is_active status
        user = get_object_or_404(User, id=user_id)
        user.is_active = is_active
        user.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False}, status=400)



from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import ChatRequest, Message
from django.contrib.auth.decorators import login_required

@login_required
def chat_page_agent(request, chatRequestId):
    try:
        # Fetch the current chat request
        chat_request = ChatRequest.objects.get(id=chatRequestId)
        
        # Mark the chat request as accepted by the CSA
        user = request.user
        print('user',user)
        if user.is_csa:
            # user.is_idle = False
            user.save()

        chat_request.accepted = True
        chat_request.csa = user
        chat_request.save()
        
        # Get the user associated with the chat request
        chat_user = chat_request.user

        previous_messages = Message.objects.filter(chat_request__user=chat_user).order_by('timestamp')
        # Prepare messages data for the response
        messages = []
        for message in previous_messages:
            messages.append({
                'is_csa':message.sender.is_csa,
                'sender': message.sender.name,
                'message': message.message,
                'timestamp': message.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                'profile_picture': message.sender.profile_picture.url if message.sender.profile_picture else None,  # Get the URL of the image
               
            })
            
            

        # If the request is AJAX (for the messages), return a JSON response
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':

            return JsonResponse({
                'status': 'success',
                'messages': messages,
                 'user': {
                    'user': user.name,
                    'email': user.email,
                    'is_csa': user.is_csa,
                }
            })
        print('user',user)
        # For non-AJAX requests, render the chat page template with the messages data
        return render(request, 'chat_page_agent.html', {
            
            'chat_request_id': chatRequestId,
            'messages': messages,
            'user':user
            
        })
        
        
    
    except ChatRequest.DoesNotExist:
        # Handle case where ChatRequest doesn't exist
        return JsonResponse({"error": "Chat request not found or already accepted."}, status=404)


@login_required
def load_new_messages(request,chatRequestId):
    
    
    try:
        # Fetch the current chat request
        chat_request = ChatRequest.objects.get(id=chatRequestId)
        
        # Mark the chat request as accepted by the CSA
        user = request.user
        
        # Get the user associated with the chat request
        chat_user = chat_request.user

        previous_messages = Message.objects.filter(chat_request__user=chat_user).order_by('timestamp')
        # Prepare messages data for the response
        messages = []
        for message in previous_messages:
            messages.append({
                'sender': message.sender.name,
                'message':  message.message if message.message else None,
                'timestamp': message.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
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
                'timestamp': message.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
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
        questions = request.POST.getlist('questions[]')
        options = request.POST.getlist('options[]')
        language = request.POST.get('language')
        video = request.FILES.get('video')
        
        # Save video if provided
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
    
    