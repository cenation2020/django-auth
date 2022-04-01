from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

# Create your models here.
class MailingList(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True,primary_key=True)
    phone_number = models.CharField(max_length=12)
    flag_choices_insights = (
        ('Y', 'YES'),
        ('N', 'NO')
    )
    insights = models.CharField(max_length=1, choices=flag_choices_insights)

class User(AbstractUser):
    #id = models.UUIDField(editable=False, primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True, primary_key=True)
    password = models.CharField(max_length=255)
    flag_choices_role = (
        ('B', 'Broker'),
        ('P', 'Product Provider'),
        ('W', 'Wealth Business'),

    )
    role = models.CharField(max_length=1, null=True, blank=True, choices=flag_choices_role)
    flag_choices_individual = (
        ('I', 'Individual'),
        ('N', 'Non Individual')
    )
    Individual = models.CharField(max_length=1, null=True, blank=True, choices=flag_choices_individual)
    organization = models.ForeignKey(
        "Organization", on_delete=models.CASCADE, null=True, blank=True
    )
    pan =  models.CharField(max_length=255, null=True, blank=True, unique=True)
    aadhar =  models.CharField(max_length=255, null=True, blank=True, unique=True)
    bank_proof = models.URLField("Bank Proof", null=True, blank=True)
    cancelled_cheque = models.URLField("Cancelled Cheque", null=True, blank=True)
    CRM_report = models.URLField("CMR Report",null=True, blank=True)
    demat = models.URLField("Demant",null=True, blank=True)
    tan = models.CharField("TAN",max_length=255,null=True, blank=True)
    gst = models.CharField("GST",max_length=255, null=True, blank=True)
    flag_choices_transaction_type = (
        ('P', 'Prop Book'),
        ('R', 'Refferal')
    )
    transaction_type = models.CharField(max_length=1, null=True, blank=True, choices=flag_choices_transaction_type)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Organization(models.Model):
    org_id = models.UUIDField(editable=False, primary_key=True, default=uuid4)
    org_name = models.CharField(max_length=255,null=True, blank=True)
    emp_count = models.IntegerField(default=0,null=True, blank=True)
    bio = models.TextField(max_length=1000,null=True, blank=True)
    mission = models.CharField(max_length=255,null=True, blank=True)
    vision = models.CharField(max_length=255,null=True, blank=True)
    contact = models.CharField(max_length=15,null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    address = models.TextField(max_length=255,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    entity_type = models.CharField(max_length=255,null=True, blank=True)
    coi_moa_aoa = models.CharField(max_length=255,null=True, blank=True)
    board_resolution = models.CharField(max_length=255,null=True, blank=True)
    authorized_signatory = models.CharField(max_length=255,null=True, blank=True)

    





