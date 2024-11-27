from django.db import models

# Create your models here.
# core/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
import uuid


# core/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.contrib.auth import get_user_model

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

  

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    
    OCCUPATION_CHOICES=[
        (0,'select'),
        (1,'Student'),
        (2,'Salaried'),
        (3,'Self-Employeed'),
        (4,'Others')
    ]
    
    id = models.IntegerField( primary_key=True, editable=False)  # Custom primary key
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    alternate_contact_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField( blank=True, null=True)
    aadhar_card_front = models.ImageField(upload_to='profiles/', blank=True, null=True)
    aadhar_card_back = models.ImageField(upload_to='profiles/', blank=True, null=True)
    pan_card = models.ImageField(upload_to='profiles/', blank=True, null=True)
    pan_number =  models.CharField(max_length=500,blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    occupation = models.IntegerField(choices=OCCUPATION_CHOICES, default =0)
    course_name = models.CharField(max_length=500,blank=True, null=True)
    college_name = models.CharField(max_length=500,blank=True, null=True)
    company_name  = models.CharField(max_length=500,blank=True, null=True)
    dc_code = models.CharField(max_length=20, blank=True, null=True)
    ip_address = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=False)  
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    is_csa = models.BooleanField(default=False,null=True)
    is_logged_in = models.BooleanField(default=False)
    is_idle = models.BooleanField(default=True)
    current_residential_address = models.CharField(max_length=500,blank=True, null=True)
    permanent_residential_adddress = models.CharField(max_length=500,blank=True, null=True)
    facebook_id = models.CharField(max_length=50,blank=True, null=True)
    instagram_id = models.CharField(max_length=50,blank=True, null=True)
    company_address =  models.CharField(max_length=500,blank=True, null=True)
    work_contact_number =  models.CharField(max_length=50,blank=True, null=True)
    salary =  models.CharField(max_length=50,blank=True, null=True)
    years_in_current_role = models.CharField(max_length=50,blank=True, null=True)
    year_of_admission =  models.CharField(max_length=10,blank=True, null=True)
    expected_graduation_year = models.CharField(max_length=50,blank=True, null=True)
    past_employement  =  models.CharField(max_length=500,blank=True, null=True)
    achievements =  models.CharField(max_length=500,blank=True, null=True)
    father_name = models.CharField(max_length=500,blank=True, null=True)
    father_occupation =  models.CharField(max_length=500,blank=True, null=True)
    mother_name = models.CharField(max_length=500,blank=True, null=True)
    siblings =  models.CharField(max_length=500,blank=True, null=True)
    spouse_name =  models.CharField(max_length=500,blank=True, null=True)
    children_details = models.CharField(max_length=500,blank=True, null=True)
    type_of_residence = models.CharField(max_length=500,blank=True, null=True)
    years_at_current_address=  models.CharField(max_length=500,blank=True, null=True)
    previous_address=  models.CharField(max_length=500,blank=True, null=True)
    current_and_past_loans =  models.CharField(max_length=500,blank=True, null=True)
    total_monthly_emi_commitments = models.CharField(max_length=500,blank=True, null=True)
    credit_score = models.CharField(max_length=500,blank=True, null=True)
    association_memberships = models.CharField(max_length=500,blank=True, null=True)
    reference_name= models.CharField(max_length=500,blank=True, null=True)
    reference_relationship =models.CharField(max_length=500,blank=True, null=True)
    reference_contact_number =models.CharField(max_length=500,blank=True, null=True)
    applicant_signature = models.ImageField(upload_to='profiles/', blank=True, null=True)
    date = models.DateField( blank=True, null=True)
    remarks = models.CharField(max_length=500,blank=True, null=True)
    
    
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    objects = UserManager()

    def __str__(self):
        return self.email
    
    


    
    
    
class ChatRequest(models.Model):
    user = models.ForeignKey(User, related_name='chat_requests', on_delete=models.CASCADE)
    csa = models.ForeignKey(User, related_name='assigned_requests', on_delete=models.SET_NULL, null=True, blank=True)
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user_typing = models.BooleanField(default=False)
    csa_typing = models.BooleanField(default=False) 

class Message(models.Model):
    chat_request = models.ForeignKey(ChatRequest, related_name='messages', on_delete=models.CASCADE, null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(blank=True, null=True)
    attachment = models.ImageField(upload_to='chat_images/',blank=True, null=True)
    
    timestamp = models.DateTimeField(auto_now_add=True)       
    
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class ConsentQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    
    def __str__(self):
        return self.question_text


class ConsentOption(models.Model):
    question = models.ForeignKey(ConsentQuestion, related_name='options', on_delete=models.CASCADE)
    option_text = models.CharField(max_length=100)
    
    def __str__(self):
        return self.option_text


class ConsentAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(ConsentQuestion, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(ConsentOption, on_delete=models.CASCADE)
    language = models.CharField(max_length=20)
    video = models.FileField(upload_to='videos/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.name}"


class HistoryCapturedImage(models.Model):
    user = models.ForeignKey(User, related_name='captured_images', on_delete=models.CASCADE,null=True,blank=True)
    image_captured = models.ImageField(upload_to='captured_images/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)