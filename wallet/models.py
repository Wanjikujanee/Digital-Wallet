import datetime
from django.db import models
from django.utils import timezone


# Create your models here.

class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    gender_choice = (
       ('a', 'Male'),
       ('b', 'Female'),
   )
    gender = models.CharField(max_length=15, choices=gender_choice)
    address=models.CharField(max_length=15)
    age=models.IntegerField()
    nationality=models.CharField(max_length=15)
    # id_number=models.CharField(max_length=15,blank=True, null=True)
    phonenumber=models.CharField(max_length=15)
    email=models.EmailField()
    # profile_picture = models.ImageField(upload_to='profile_pictures/')
    marital_status_choice = (
       ('a', 'Married'),
       ('b', 'Single'),
        ('b', 'Others'),
   )
    marital_status=models.CharField(max_length=15,choices = marital_status_choice)
    signature=models.ImageField(upload_to='signature_pictures/')
    date_created = models.DateTimeField(default=timezone.now)
    employment_status=models.BooleanField()
    
class Wallet(models.Model):
    balance=models.IntegerField()
    customer=models.OneToOneField('Customer', on_delete=models.CASCADE,related_name='Wallet_customer')
    pin=models.IntegerField()
    # currency =models.ForeignKey('Currency', on_delete=models.CASCADE, related_name ='Wallet_currency')
    active=models.BooleanField()
    date_created=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=20)
    
class Account(models.Model):
    account_type=models.CharField(max_length=20)
    account_name=models.CharField(max_length=20)
    savings=models.IntegerField()
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Account_wallet')
    destination=models.CharField(max_length=15)
    
class Transaction(models.Model):
    transaction_type=models.CharField(max_length=10)
    # original_account=models.ForeignKey('Original_Account', on_delete=models.CASCADE,related_name='Transaction_original_account')
    # destination_account=models.ForeignKey('Destination_Account', on_delete=models.CASCADE,related_name='Transaction_destination_account')
    thirdParty=models.ForeignKey('ThirdParty',on_delete=models.CASCADE,related_name='Transaction_third_party')
    transaction_date=models.DateTimeField(default=timezone.now)
    receipt=models.ForeignKey('Receipts',on_delete=models.CASCADE,related_name='Transaction_receipts')
    status=models.CharField(max_length=15)  
    
 
class Card(models.Model):
    date_Issued=models.DateTimeField(default=timezone.now)
    card_status= models.CharField(max_length=15)
    security_code=models.IntegerField()
    signature=models.ImageField(upload_to='signature_pictures/')
    issuer=models.CharField(max_length=15)
    account=models.ForeignKey('Account', on_delete=models.CASCADE,related_name='Card_account') 
   
class ThirdParty(models.Model):
    name=models.CharField(max_length=15)
    email=models.EmailField()
    phone_Number=models.IntegerField()
    transaction_cost=models.IntegerField()
    account=models.ForeignKey('Account', on_delete=models.CASCADE,related_name='ThirdPary_account')
    active=models.BooleanField()
    
    

class Notifications(models.Model):
    date_created=models.DateTimeField(default=timezone.now)
    message=models.CharField(max_length=15)
    # recipient=models.ForeignKey('Recipient', on_delete=models.CASCADE,related_name='notification_recipient')   
    isactive=models.BooleanField()
    image=models.ImageField(upload_to='profile_pictures/')
 
class Receipts(models.Model):
    receipt_date=models.DateTimeField(default=timezone.now)
    transaction=models.ForeignKey('Transaction', on_delete=models.CASCADE,related_name='Reciepts_transaction')
    recipt_File=models.FileField(upload_to='wallet/')
 
class Loan(models.Model):        
    loan_type=models.CharField(max_length=25)
    amount=models.IntegerField()
    wallet=models.ForeignKey('Wallet', on_delete=models.CASCADE,related_name='Loan_wallet')
    date=models.DateTimeField(default=timezone.now)
    loan_term=models.IntegerField()
    due_date=models.DateField(default=timezone.now)
    # guaranter=models.ForeignKey('guaranter', on_delete=models.CASCADE,related_name='Loan_guaranter')
    loan_balance=models.IntegerField()
    duration=models.CharField(max_length=15)
    interest_rate=models.IntegerField()
    status=models.CharField(max_length=15)
 
class Reward(models.Model):
    wallet=models.ForeignKey('wallet',on_delete=models.CASCADE,related_name='Reward_wallet')
    points=models.CharField(max_length=25)
    date=models.DateTimeField(default=timezone.now)
    TRANSACTION_CHOICES=(
    ('a','receipts'),
    ('b','purchases'),
    ('c','sales'),
    ('d','payments')
)
    transaction=models.ForeignKey('Transaction', on_delete=models.CASCADE,choices=TRANSACTION_CHOICES,related_name='Reward_transaction')
    GENDER_CHOICES = (
       ('a', 'Male'),
       ('b', 'Female'),
   )
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)

    


 

    




    

