from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
import datetime
from django.db import models

# Create your models here.
class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    password=models.TextField(null=True)
    Usertype=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_login'
class user_register(models.Model):
    user_id=models.AutoField(primary_key=True)
    login_id=models.IntegerField()
    Name=models.CharField(max_length=50, null=True)
    phone_number=models.BigIntegerField(null=True)
    Email=models.CharField(max_length=50)
    Address=models.TextField()
    class Meta:
        db_table='tbl_customer_register'
class membership_amount(models.Model):
    membership_amount_id=models.AutoField(primary_key=True)
    amount=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    class Meta:
        db_table='tbl_membership_amount'
class category(models.Model):
    category_id=models.AutoField(primary_key=True)
    category=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_category'
class author_name(models.Model):
    author_id=models.AutoField(primary_key=True)
    author=models.CharField(max_length=50)
    about_author=models.TextField()
    class Meta:
        db_table='tbl_author_name'
class language(models.Model):
    language_id=models.AutoField(primary_key=True)
    language=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_language'
class book(models.Model):
    book_id=models.AutoField(primary_key=True)
    category_id=models.IntegerField()
    author_id=models.IntegerField()
    language_id=models.IntegerField()
    type=models.CharField(max_length=50)
    book_name=models.CharField(max_length=50)
    quantity=models.IntegerField(blank=True, null=True)
    price=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    doc=models.CharField(max_length=50,blank=True, null=True)
    image=models.CharField(max_length=50)
    description=models.TextField()
    user_type=models.CharField(max_length=50,default="Admin")
    status=models.CharField(max_length=50,default="Approved")
    class Meta:
        db_table='tbl_book'

class order(models.Model):
    order_id=models.AutoField(primary_key=True)
    book_id=models.IntegerField()
    amount=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    quantity=models.IntegerField(blank=True, null=True)
    status=models.CharField(max_length=50)
    entry_date=models.DateTimeField(default=datetime.datetime.now)
    user_login_id=models.IntegerField()
    check_no_order=models.IntegerField(blank=True, null=True)
    class Meta:
        db_table='tbl_order'
class complaint(models.Model):
    complaint_id=models.AutoField(primary_key=True)
    complaint_subject=models.CharField(max_length=50)
    complaint=models.CharField(max_length=150)
    user_login_id=models.IntegerField()
    reply=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_complaint'

class feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    feedback_subject=models.CharField(max_length=50)
    feedback=models.TextField()
    user_login_id=models.IntegerField()
    reply=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_feedback'
class author(models.Model):
    author_id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    address=models.TextField()
    email_id=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    phone_number=models.BigIntegerField(null=True)
    photo=models.CharField(max_length=50)
    login_id=models.IntegerField()
    membership=models.CharField(max_length=50,default="Not Member")
    expiry_date=models.DateField(blank=True, null=True)
    class Meta:
        db_table='tbl_author'
class fee(models.Model):
    fee_id=models.AutoField(primary_key=True)
    fee=models.IntegerField()
    class Meta:
        db_table='tbl_fee'