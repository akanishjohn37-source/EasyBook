import os
import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from bookapp.models import *
from django.contrib.auth import authenticate
from django.db import connection
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.auth import logout
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')
def sign_in(request):
    return render(request,'login.html')
def customer_registration(request):
    return render(request,'customer_registration.html')
def author_registration(request):
    return render(request,'author_registration.html')
def customer_action(request):
    username=request.POST.get("username")
    data = {
       'username_exists':      login.objects.filter(username=username).exists(),
        'error':"Username Already Exist"
        }
    if(data["username_exists"]==False):
            tbl1=login()
            username=request.POST.get("username")
            tbl1.username=request.POST.get("username")
            password=request.POST.get("password")
            tbl1.password=password
            tbl1.Usertype="User"
            tbl1.status="Approved"
            tbl1.save()
            obj=login.objects.get(username=username,password=password)

            u=user_register()
            u.login_id = obj.login_id
            u.Name=request.POST.get("Name")
            u.phone_number =request.POST.get("phone")
            u.Email=request.POST.get("Email")
            u.Address=request.POST.get("Address")
            u.save()
            messages.add_message(request, messages.INFO, 'Registered successfully.')
            return redirect('/customer_registration/')
    else:
            messages.add_message(request, messages.INFO, 'Failed .. Username already exist.')
            return redirect('/customer_registration/')
 
def sign_in_process(request):
    u=request.POST.get("username")
    p=request.POST.get("password")
    obj=authenticate(username=u,password=p)
    if obj is not None:
        if obj.is_superuser == 1:
            request.session['aname'] = u
            request.session['slogid'] = obj.id
            return redirect('/admin_home/')
        else:
          messages.add_message(request, messages.INFO, 'Invalid User.')
          return redirect('/login/')
    else:
        newp=p
        try:
            obj1=login.objects.get(username=u,password=newp)


            if  obj1.Usertype=="User":
                request.session['uname'] = u
                request.session['slogid'] = obj1.login_id
                return redirect('/Customer/')
            elif  obj1.Usertype=="Author":
                request.session['auname'] = u
                request.session['slogid'] = obj1.login_id
                return redirect('/author_home/')
            else:
                 messages.add_message(request, messages.INFO, 'Invalid User.')
                 return redirect('/login/')
        except login.DoesNotExist:
         messages.add_message(request, messages.INFO, 'Invalid User.')
         return redirect('/login/')
def admin_home(request):
    if 'aname' in request.session:
     return render(request,'Master/index.html')
    else:
      return redirect('/login/')
def author_home(request):
    if 'auname' in request.session:
     return render(request,'Author/index.html')
    else:
      return redirect('/login/')
def admin_logout(request):
    logout(request)
    return redirect('/login/')
def user_logout(request):
    logout(request)
    request.session.delete()
    return redirect('/login/')
def customer_list(request):
    if 'aname' in request.session:
        data=user_register.objects.all()
        return render(request,'Master/customer_list.html',{'data':data})
    else:
         return redirect('/login/')
    
# -------------------Category -----------------------------
def save_category(request):
    if 'aname' in request.session:
        id=request.session['slogid']
        tbl=category()
        tbl.category=request.POST.get("category")
        tbl.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/add_category/')
    else:
        return redirect('/login')
def add_category(request):
 if 'aname' in request.session:
    data=category.objects.all()
    return render(request,'Master/category.html',{'data':data})
 else:
      return redirect('/login/')
def edit_category(request,id):
 if 'aname' in request.session:
    data=category.objects.get(category_id=id)
    return render(request,'Master/edit_category.html',{'data':data})
 else:
      return redirect('/login/')


def update_category(request,id):
 if 'aname' in request.session:
    tbl=category.objects.get(category_id=id)
    tbl.category=request.POST.get("category")
    tbl.save()
    messages.add_message(request, messages.INFO, 'Updated successfully.')
    return redirect('/add_category/')
 else:
      return redirect('/login/')
def delete_category(request,id):
 if 'aname' in request.session:
    tbl=category.objects.get(category_id=id)
    tbl.delete()
    messages.add_message(request, messages.INFO, 'Deleted successfully.')
    return redirect('/add_category/')
 else:
      return redirect('/login/')
def author_action(request):
        username=request.POST.get("username")
        data = {
       'username_exists':      login.objects.filter(username=username).exists(),
        'error':"Username Already Exist"
        }
        if(data["username_exists"]==False):
           
            tbl1=login()
            username=request.POST.get("username")
            tbl1.username=request.POST.get("username")
            password=request.POST.get("password1")
            tbl1.password=password
            tbl1.Usertype="Author"
            tbl1.status="Approved"
            tbl1.save()
            obj=login.objects.get(username=username,password=password)

            tbl=author()
            tbl.login_id = obj.login_id
            tbl.firstname=request.POST.get("firstname")
            tbl.lastname=request.POST.get("lastname")
            tbl.address=request.POST.get("address")
            tbl.email_id=request.POST.get("email")
           
            tbl.gender=request.POST.get("gender")
            tbl.phone_number=request.POST.get("phone_number")
    
            photo=request.FILES['photo']

            split_tup = os.path.splitext(photo.name)
            file_extension = split_tup[1]
            # folder path
            dir_path = settings.MEDIA_ROOT
            count = 0
            # Iterate directory
            for path in os.listdir(dir_path):
            # check if current path is a file
                if os.path.isfile(os.path.join(dir_path, path)):
                    count += 1
            filecount=count+1
            filename=str(filecount)+"."+file_extension
            obj=FileSystemStorage()
            file=obj.save(filename,photo)
            url1=obj.url(file)
            tbl.photo=url1
            tbl.save()
            messages.add_message(request, messages.INFO, 'Added successfully.')
            return redirect('/author_registration/')
        else:
            messages.add_message(request, messages.INFO, 'Failed .. Username already exist.')
            return redirect('/author_registration/')
 

def save_language(request):
    if 'aname' in request.session:
        id=request.session['slogid']
        tbl=language()
        tbl.language=request.POST.get("language")
        tbl.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/add_language/')
    else:
        return redirect('/login')
def add_language(request):
 if 'aname' in request.session:
    data=language.objects.all()
    return render(request,'Master/language.html',{'data':data})
 else:
      return redirect('/login/')
def edit_language(request,id):
 if 'aname' in request.session:
    data=language.objects.get(language_id=id)
    return render(request,'Master/edit_language.html',{'data':data})
 else:
      return redirect('/login/')


def update_language(request,id):
 if 'aname' in request.session:
    tbl=language.objects.get(language_id=id)
    tbl.language=request.POST.get("language")
    tbl.save()
    messages.add_message(request, messages.INFO, 'Updated successfully.')
    return redirect('/add_language/')
 else:
      return redirect('/login/')
def delete_language(request,id):
 if 'aname' in request.session:
    tbl=language.objects.get(language_id=id)
    tbl.delete()
    messages.add_message(request, messages.INFO, 'Deleted successfully.')
    return redirect('/add_language/')
 else:
      return redirect('/login/')
 
def save_author(request):
    if 'aname' in request.session:
        
        tbl=author_name()
        tbl.author=request.POST.get("author")
        tbl.about_author=request.POST.get("about_author")
        tbl.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/add_author/')
    else:
        return redirect('/login')
def add_author(request):
 if 'aname' in request.session:
    data=author_name.objects.all()
    return render(request,'Master/author.html',{'data':data})
 else:
      return redirect('/login/')
def edit_author(request,id):
 if 'aname' in request.session:
    data=author_name.objects.get(author_id=id)
    return render(request,'Master/edit_author.html',{'data':data})
 else:
      return redirect('/login/')


def update_author(request,id):
 if 'aname' in request.session:
    tbl=author_name.objects.get(author_id=id)
    tbl.author=request.POST.get("author")
    tbl.about_author=request.POST.get("about_author")
    tbl.save()
    messages.add_message(request, messages.INFO, 'Updated successfully.')
    return redirect('/add_author/')
 else:
      return redirect('/login/')
def delete_author(request,id):
 if 'aname' in request.session:
    tbl=author_name.objects.get(author_id=id)
    tbl.delete()
    messages.add_message(request, messages.INFO, 'Deleted successfully.')
    return redirect('/add_author/')
 else:
      return redirect('/login/')
 
def save_product(request):
    if 'aname' in request.session:
        tbl=book()
        tbl.category_id=request.POST.get("category")
        tbl.author_id=request.POST.get("author_id")
        tbl.language_id=request.POST.get("language_id")
        tbl.type=request.POST.get("type")
        tbl.book_name=request.POST.get("book_name")
        tbl.quantity=request.POST.get("quantity")
        tbl.price=request.POST.get("price")
        tbl.description=request.POST.get("description")
        image=request.FILES['image']
        split_tup = os.path.splitext(image.name)
        file_extension = split_tup[1]
        # folder path
        dir_path = settings.MEDIA_ROOT
        count = 0
        # Iterate directory
        for path in os.listdir(dir_path):
        # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        filecount=count+1
        filename=str(filecount)+"."+file_extension
        obj=FileSystemStorage()
        file=obj.save(filename,image)
        url1=obj.url(file)
        tbl.image=url1

        doc=request.FILES['doc']
        split_tup = os.path.splitext(doc.name)
        file_extension = split_tup[1]
        # folder path
        dir_path = settings.MEDIA_ROOT
        count = 0
        # Iterate directory
        for path in os.listdir(dir_path):
        # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        filecount=count+1
        filename=str(filecount)+"."+file_extension
        obj=FileSystemStorage()
        file=obj.save(filename,doc)
        url1=obj.url(file)
        tbl.doc=url1

        tbl.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/add_product/')
    else:
        return redirect('/login/')
def product_list(request):
    if 'aname' in request.session:
        data1=category.objects.all()
        data2=author_name.objects.all()
        data3=language.objects.all()
        id=request.session['slogid']

        cursor=connection.cursor()
        cursor.execute("select p.*,c.category,a.author,l.language from  tbl_book as p inner join   tbl_category as c on p.category_id =c.category_id inner join tbl_author_name as a on p.author_id=a.author_id inner join tbl_language as l on p.language_id=l.language_id where p.user_type='Admin'")
        data=cursor.fetchall()

        return render(request,'Master/product_list.html',{'data':data,'data1':data1,'data2':data2,'data3':data3})
    else:
       return redirect('/login/')
def add_product(request):
 if 'aname' in request.session:
    data1=category.objects.all()
    data2=author_name.objects.all()
    data3=language.objects.all()
    return render(request,'Master/product.html',{'data1':data1,'data2':data2,'data3':data3})
 else:
      return redirect('/login/')
def edit_product(request,id):
 if 'aname' in request.session:
    data=book.objects.get(book_id=id)
    data1=category.objects.all()
    data2=author_name.objects.all()
    data3=language.objects.all()
    return render(request,'Master/edit_product.html',{'data':data,'data1':data1,'data2':data2,'data3':data3})
 else:
      return redirect('/login/')
def update_product(request,id):
 if 'aname' in request.session:
        tbl=book.objects.get(book_id=id)
        if "image" in request.FILES:

            image=request.FILES['image']
            split_tup = os.path.splitext(image.name)
            file_extension = split_tup[1]
            # folder path
            dir_path = settings.MEDIA_ROOT
            count = 0
            # Iterate directory
            for path in os.listdir(dir_path):
            # check if current path is a file
                if os.path.isfile(os.path.join(dir_path, path)):
                    count += 1
            filecount=count+1
            filename=str(filecount)+"."+file_extension
            obj=FileSystemStorage()
            file=obj.save(filename,image)
            url1=obj.url(file)
            tbl.image=url1
        if "doc" in request.FILES:

            doc=request.FILES['doc']
            split_tup = os.path.splitext(image.name)
            file_extension = split_tup[1]
            # folder path
            dir_path = settings.MEDIA_ROOT
            count = 0
            # Iterate directory
            for path in os.listdir(dir_path):
            # check if current path is a file
                if os.path.isfile(os.path.join(dir_path, path)):
                    count += 1
            filecount=count+1
            filename=str(filecount)+"."+file_extension
            obj=FileSystemStorage()
            file=obj.save(filename,doc)
            url1=obj.url(file)
            tbl.doc=url1
        tbl.category_id=request.POST.get("category")
        tbl.author_id=request.POST.get("author_id")
        tbl.language_id=request.POST.get("language_id")
        tbl.type=request.POST.get("type")
        tbl.book_name=request.POST.get("book_name")
        tbl.quantity=request.POST.get("quantity")
        tbl.price=request.POST.get("price")
        tbl.description=request.POST.get("description")
   
        tbl.save()
        messages.add_message(request, messages.INFO, 'Updated successfully.')
        return redirect('/product_list')
 else:
      return redirect('/login/')
def delete_product(request,id):
 if 'aname' in request.session:
    tbl=book.objects.get(book_id=id)
    tbl.delete()
    messages.add_message(request, messages.INFO, 'Deleted successfully.')
    return redirect('/product_list')
 else:
      return redirect('/login/')
 
def display_product(request):
        category = request.GET.get("category")
        author = request.GET.get("author")
        language = request.GET.get("language")
        type = request.GET.get("type")
        str1="<table class='table table-striped table-bordered'><thead><th>Id</th><th>Type</th><th>Name</th><th>Quanitity</th><th>Price</th><th>Image</th><th>Details</th><th>Document</th><th>#</th></thead>"
        cursor=connection.cursor()
        cursor.execute("select p.*,c.category,a.author,l.language from  tbl_book as p inner join   tbl_category as c on p.category_id =c.category_id inner join tbl_author_name as a on p.author_id=a.author_id inner join tbl_language as l on p.language_id=l.language_id  where p.category_id="+str(category))
        data=cursor.fetchall()
        count=1
        for i in data:
          str1+="<tr><td>"+str(count)+"</td><td>"+str(i[4])+"</td><td>"+str(i[5])+"</td><td>"+str(i[6])+"</td><td>"+str(i[7])+"</td><td><img src="+str(i[9])+" width='100' height='80'></td><td>"+str(i[10])+"</td> <td><a href="+str(i[8])+" class=''>Download</a></td><td><a href='/edit_product/"+str(i[0])+"' class='btn btn-info'>Edit</a></td>  <td><a href='/delete_product/"+str(i[0])+"' onclick='return ConfirmDialog();' class='btn btn-danger'>Delete</a></td></tr>"
          count=count+1
        return HttpResponse(str1)

     # ----------------Admin feedback -------------

def Customer(request):
    if 'uname' in request.session:
        data=book.objects.filter(status='Approved')
        data1=category.objects.all()
        data2=author_name.objects.all()
        data3=language.objects.all()
        return render(request,'User/index.html',{'data':data,'data1':data1,'data2':data2,'data3':data3})
    else:
         return redirect('/login/')
    
def user_logout(request):
    logout(request)
    request.session.delete()
    return redirect('/login/')

def checkout(request):
     if 'uname' in request.session:
        logid=request.session['slogid']

        check_no1=random.randint(100,999999)
        for i in range(1,20):
            if(request.POST.get("item_id_"+str(i))):

                item_id=request.POST.get("item_id_"+str(i))
                tbl=book.objects.get(book_id=item_id)
                item_image=tbl.image
                item_name=tbl.book_name
                amount=request.POST.get("amount_"+str(i))
                quantity=request.POST.get("quantity_"+str(i))

                obj=order()
                obj.book_id=item_id
                obj.amount=int(amount)*int(quantity)
                obj.quantity=quantity
                obj.status='Not Paid'
                obj.user_login_id=logid
                obj.check_no_order=check_no1
                obj.save()

            #    // list=[item_name,quantity,amount,item_image,i,item_id]

        return redirect('/cart_check_out/'+str(check_no1))
      
     else:
      return redirect('/login/')
def cart_check_out(request,id):
    if 'uname' in request.session:
        cursor=connection.cursor()
        cursor.execute("select p.*,c.* from  tbl_order as p inner join   tbl_book as c on p.book_id =c.book_id  where p.check_no_order="+str(id))
        data=cursor.fetchall()
    
        return render(request,'User/checkout.html',{'data':data,'check_no1':id})
    else:
        return redirect('/login/')
    

def remove_order(request):
    if 'suname' in request.session:
        oid=request.GET.get("oid")
        tbl=order.objects.get(order_id=oid)
        tbl.delete()
def add_qty(request):
    oid=request.GET.get("oid")
    newqty=request.GET.get("newqty")
    order.objects.filter(order_id=oid).update(quantity=newqty)
    data=[]
    try:

        cursor=connection.cursor()
        cursor.execute("select p.price from  tbl_order as o inner join   tbl_book as p on p.book_id =o.book_id  where o.order_id="+str(oid))
        data2=cursor.fetchall()

        for i in data2:
            nprice=int(i[0])*int(newqty)
            order.objects.filter(order_id=oid).update(amount=nprice)
            data1 = {
            'price':nprice
                    }
    except Exception:
        data['error_message'] = 'error'
        return JsonResponse(data)
    return JsonResponse(data1)
def sub_qty(request):
    oid=request.GET.get("oid")
    newqty=request.GET.get("newqty")
    order.objects.filter(order_id=oid).update(quantity=newqty)
    data=[]
    try:

        cursor=connection.cursor()
        cursor.execute("select p.price from  tbl_order as o inner join   tbl_book as p on p.book_id =o.book_id  where o.order_id="+str(oid))
        data2=cursor.fetchall()

        for i in data2:
            nprice=int(i[0])*int(newqty)
            order.objects.filter(order_id=oid).update(amount=nprice)
            data1 = {
            'price':nprice
                    }
    except Exception:
        data['error_message'] = 'error'
        return JsonResponse(data)
    return JsonResponse(data1)


def payment(request,id):
    if 'uname' in request.session:
        data=order.objects.filter(check_no_order=id)
        sum=0
        for i in data:
            sum+=i.amount


        return render(request,'User/payment.html',{'sum':sum,'check_no1':id})
    else:
       return redirect('/login/')
def pay_action(request):
    if 'uname' in request.session:
        id=request.POST.get("cno")
        order.objects.filter(check_no_order=id).update(status="Paid")

        cursor=connection.cursor()
        cursor.execute("select o.quantity as oqty,p.quantity as pqty,p.book_id from  tbl_order as o inner join   tbl_book as p on p.book_id =o.book_id  where o.check_no_order="+str(id))
        data=cursor.fetchall()
        newqty=0
        for i in data:
            newqty=int(i[1])-int(i[0])
            pid=i[2]
            book.objects.filter(book_id=pid).update(quantity=newqty)

        return redirect('/clear_cart/')
    else:
       return redirect('/login/')

def myorder(request):
    if 'uname' in request.session:
        logid= request.session['slogid']

        cursor=connection.cursor()
        cursor.execute("select o.*,p.book_name,p.quantity,p.image,p.price,u.Name,u.phone_number,u.Email,u.address,p.type,p.doc from  tbl_order as o inner join   tbl_book as p on p.book_id =o.book_id inner join tbl_category as c on p.category_id=c.category_id inner join tbl_customer_register as u  on o.user_login_id=u.login_id  where o.status!='Not Paid'  and o.user_login_id="+str(logid)+" order by  o.entry_date desc")

        data=cursor.fetchall()
        return render(request,'User/myorder.html',{'data':data})

    else:
       return redirect('/login/')
def clear_cart(request):
    if 'uname' in request.session:

        return render(request,'User/clear_cart.html')
    else:
       return redirect('/login/')
    


def order_list(request):
    if 'aname' in request.session:
        logid=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select o.*,p.book_name,p.quantity,p.image,p.price,u.Name,u.phone_number,u.Email,u.Address,p.type  from  tbl_order as o inner join   tbl_book as p on p.book_id =o.book_id inner join tbl_category as c on p.category_id=c.category_id inner join tbl_customer_register as u  on o.user_login_id=u.login_id where   o.status='Paid' and p.user_type='Admin' order by  o.entry_date")
        data=cursor.fetchall()
        return render(request,'Master/order.html',{'data':data})
    else:
      return redirect('/login/')
def deliver(request,id):
    if 'aname' in request.session:
        tbl=order.objects.get(order_id=id)
        tbl.status="Delivered"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Delivered successfully.')
        return redirect('/order_list/')
    else:
       return redirect('/login/')
def deliverd_list(request):
    if 'aname' in request.session:
        logid=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select o.*,p.book_name,p.quantity,p.image,p.price,u.Name,u.phone_number,u.Email,u.Address  from  tbl_order as o inner join   tbl_book as p on p.book_id =o.book_id inner join tbl_category as c on p.category_id=c.category_id inner join tbl_customer_register as u  on o.user_login_id=u.login_id where o.status='Delivered' and  p.user_type='Admin'  order by  o.entry_date")
        data=cursor.fetchall()
        return render(request,'Master/deliverd_list.html',{'data':data})
    else:
      return redirect('/login/')
def single_book(request,id):
    if 'uname' in request.session:
        data=book.objects.get(book_id=id)
        usertype=data.user_type
        if usertype=="Admin": 
            cursor=connection.cursor()
            cursor.execute("select p.*,c.category,a.author,l.language from  tbl_book as p inner join   tbl_category as c on p.category_id =c.category_id inner join tbl_author_name as a on p.author_id=a.author_id inner join tbl_language as l on p.language_id=l.language_id  where p.book_id="+str(id)+" and  p.status='Approved'")
            data=cursor.fetchall()
        else:
            cursor=connection.cursor()
            cursor.execute("select p.*,c.category,CONCAT(a.firstname,a.lastname) as f,l.language from  tbl_book as p inner join   tbl_category as c on p.category_id =c.category_id inner join tbl_author as a on p.author_id=a.login_id inner join tbl_language as l on p.language_id=l.language_id  where p.book_id="+str(id)+" and p.status='Approved'")
            data=cursor.fetchall()
        return render(request,'User/single.html',{'data':data,'usertype':usertype})
    else:
      return redirect('/login/')

def single_category(request,id):
    if 'uname' in request.session:
        data=book.objects.filter(category_id=id,status='Approved')
        data1=category.objects.all()
        data2=author_name.objects.all()
        data3=language.objects.all()
        return render(request,'User/index.html',{'data':data,'data1':data1,'data2':data2,'data3':data3})
    else:
         return redirect('/login/')
def search_book(request):
    if 'uname' in request.session:
        search=request.POST.get("search")
        data=book.objects.filter(book_name__contains=search,status='Approved')
        data1=category.objects.all()
        data2=author_name.objects.all()
        data3=language.objects.all()
        return render(request,'User/index.html',{'data':data,'data1':data1,'data2':data2,'data3':data3})
    else:
         return redirect('/login/')
def single_language(request,id):
    if 'uname' in request.session:
        data=book.objects.filter(language_id=id,status='Approved')
        data1=category.objects.all()
        data2=author_name.objects.all()
        data3=language.objects.all()
        return render(request,'User/index.html',{'data':data,'data1':data1,'data2':data2,'data3':data3})
    else:
         return redirect('/login/')
def single_author(request,id):
    if 'uname' in request.session:
        data=book.objects.filter(author_id=id,status='Approved')
        data1=category.objects.all()
        data2=author_name.objects.all()
        data3=language.objects.all()
        return render(request,'User/index.html',{'data':data,'data1':data1,'data2':data2,'data3':data3})
    else:
         return redirect('/login/')
def single_type(request,id):
    if 'uname' in request.session:
        data=book.objects.filter(type=id,status='Approved')
        data1=category.objects.all()
        data2=author_name.objects.all()
        data3=language.objects.all()
        return render(request,'User/index.html',{'data':data,'data1':data1,'data2':data2,'data3':data3})
    else:
         return redirect('/login/')
    
def payment_no_book(request,id):
    if 'uname' in request.session:
        logid=request.session['slogid']
        tbl=book.objects.get(book_id=id)
        amount=tbl.price
        obj=order()
        obj.book_id=id
        obj.amount=amount
        obj.status='Not Paid'
        obj.user_login_id=logid
        obj.save()
        c = order.objects.last().order_id
        return render(request,'User/payment_no_book.html',{'sum':amount,'oid':c})
    else:
       return redirect('/login/')
      
def pay_no_book_action(request):
    if 'uname' in request.session:
        id=request.POST.get("oid")
        order.objects.filter(order_id=id).update(status="Paid")
        messages.add_message(request, messages.INFO, 'Paid successfully.')
        return redirect('/Customer/')
    else:
       return redirect('/login/')
    
def view_feedback(request):
    if 'aname' in request.session:
        cursor=connection.cursor()
        cursor.execute("select c.*,u.* from  tbl_feedback as c inner join  tbl_customer_register as u  on c.user_login_id =u.login_id where c.reply='Nil'  order by c.feedback_id desc")
        data=cursor.fetchall()
        return render(request,'Master/view_feedback.html',{'data':data})
    else:
       return redirect('/login')
def replied_feedback_list(request):
    if 'aname' in request.session:
        cursor=connection.cursor()
        cursor.execute("select c.*,u.* from  tbl_feedback as c inner join  tbl_customer_register as u  on c.user_login_id =u.login_id where c.reply!='Nil' order by c.feedback_id desc")
        data=cursor.fetchall()
        return render(request,'Master/replied_feedback.html',{'data':data})
    else:
       return redirect('/login')
def adm_reply_feedback(request,id):
    if 'aname' in request.session:

        return render(request,'Master/reply_feedback.html',{'id':id})
    else:
       return redirect('/login')
    

def add_reply_feedback(request,id):
    tbl=feedback.objects.get(feedback_id=id)
    tbl.reply=request.POST.get("reply")
    tbl.save()
    return redirect('/replied_feedback_list')

def feedback_frm(request):
    if 'uname' in request.session:

        return render(request,'User/feedback.html')
    else:
       return redirect('/login/')
def save_feedback(request):
    if 'uname' in request.session:
        tbl=feedback()
        tbl.user_login_id=request.session['slogid']
        tbl.feedback_subject=request.POST.get("subject")
        tbl.feedback=request.POST.get("feedback")
        tbl.reply="Nil"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/feedback')
    else:
       return redirect('/login/')
def feedback_list(request):
     if 'uname' in request.session:
        id=request.session['slogid']
        data1 = feedback.objects.filter(user_login_id=id)
        return render(request,'User/feedback_list.html',{'data1':data1})
     else:
       return redirect('/login/')
def delete_feedback(request,id):
    if 'uname' in request.session:
        tbl=feedback.objects.get(feedback_id=id)
        tbl.delete()
        messages.add_message(request, messages.INFO, 'Deleted successfully.')
        return redirect('/feedback_list')
    else:
       return redirect('/login/')
    

# .....................
def view_complaint(request):
    if 'aname' in request.session:
        cursor=connection.cursor()
        cursor.execute("select c.*,u.* from  tbl_complaint as c inner join  tbl_customer_register as u  on c.user_login_id =u.login_id where c.reply='Nil'  order by c.complaint_id desc")
        data=cursor.fetchall()
        return render(request,'Master/view_complaint.html',{'data':data})
    else:
       return redirect('/login')
def replied_list(request):
    if 'aname' in request.session:
        cursor=connection.cursor()
        cursor.execute("select c.*,u.* from  tbl_complaint as c inner join  tbl_customer_register as u  on c.user_login_id =u.login_id where c.reply!='Nil' order by c.complaint_id desc")
        data=cursor.fetchall()
        return render(request,'Master/replied_complaint.html',{'data':data})
    else:
       return redirect('/login')
def adm_reply_complaint(request,id):
    if 'aname' in request.session:

        return render(request,'Master/reply_complaint.html',{'id':id})
    else:
       return redirect('/login')
    

def add_reply(request,id):
    tbl=complaint.objects.get(complaint_id=id)
    tbl.reply=request.POST.get("reply")
    tbl.save()
    return redirect('/replied_list')

def complaint_frm(request):
    if 'uname' in request.session:

        return render(request,'User/complaint.html')
    else:
       return redirect('/login/')
def save_complaint(request):
    if 'uname' in request.session:
        tbl=complaint()
        tbl.user_login_id=request.session['slogid']
        tbl.complaint_subject=request.POST.get("subject")
        tbl.complaint=request.POST.get("complaint")
        tbl.reply="Nil"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/complaint/')
    else:
       return redirect('/login/')
def complaint_list(request):
     if 'uname' in request.session:
        id=request.session['slogid']
        data1 = complaint.objects.filter(user_login_id=id)
        return render(request,'User/complaint_list.html',{'data1':data1})
     else:
       return redirect('/login/')
def delete_complaint(request,id):
    if 'uname' in request.session:
        tbl=complaint.objects.get(complaint_id=id)
        tbl.delete()
        messages.add_message(request, messages.INFO, 'Deleted successfully.')
        return redirect('/complaint_list')
    else:
       return redirect('/login/')
    

def au_add_product(request):
 if 'auname' in request.session:
    today = datetime.datetime.today()
    data1=category.objects.all()
    data2=author_name.objects.all()
    data3=language.objects.all()
    logid=request.session['slogid']
    data4=author.objects.filter(login_id=logid,membership='Member').filter(Q(expiry_date__gte=today))
    data5=book.objects.filter(author_id=logid).count()
    return render(request,'Author/product.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5})
 else:
      return redirect('/login/')
 
def au_save_product(request):
    if 'auname' in request.session:
        tbl=book()
        id=request.session['slogid']
        tbl.category_id=request.POST.get("category")
        tbl.author_id=id
        tbl.language_id=request.POST.get("language_id")
        tbl.type=request.POST.get("type")
        tbl.book_name=request.POST.get("book_name")
        tbl.quantity=request.POST.get("quantity")
        tbl.price=request.POST.get("price")
        tbl.description=request.POST.get("description")
        tbl.user_type="Author"
        tbl.status="Not Approved"
        image=request.FILES['image']
      
        split_tup = os.path.splitext(image.name)
        file_extension = split_tup[1]
        # folder path
        dir_path = settings.MEDIA_ROOT
        count = 0
        # Iterate directory
        for path in os.listdir(dir_path):
        # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        filecount=count+1
        filename=str(filecount)+"."+file_extension
        obj=FileSystemStorage()
        file=obj.save(filename,image)
        url1=obj.url(file)
        tbl.image=url1
        if "doc" in request.FILES:
            doc=request.FILES['doc']
            split_tup = os.path.splitext(doc.name)
            file_extension = split_tup[1]
            # folder path
            dir_path = settings.MEDIA_ROOT
            count = 0
            # Iterate directory
            for path in os.listdir(dir_path):
            # check if current path is a file
                if os.path.isfile(os.path.join(dir_path, path)):
                    count += 1
            filecount=count+1
            filename=str(filecount)+"."+file_extension
            obj=FileSystemStorage()
            file=obj.save(filename,doc)
            url1=obj.url(file)
            tbl.doc=url1

        tbl.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/au_add_product/')
    else:
        return redirect('/login/')
    
def au_product_list(request):
    if 'auname' in request.session:
        data1=category.objects.all()
        data2=author_name.objects.all()
        data3=language.objects.all()
        id=request.session['slogid']
        
        cursor=connection.cursor()
        cursor.execute("select p.*,c.category,l.language from  tbl_book as p inner join   tbl_category as c on p.category_id =c.category_id inner join tbl_language as l on p.language_id=l.language_id where user_type='Author' and p.author_id="+str(id))
        data=cursor.fetchall()

        return render(request,'Author/product_list.html',{'data':data,'data1':data1,'data2':data2,'data3':data3})
    else:
       return redirect('/login/')
    
def au_edit_product(request,id):
 if 'auname' in request.session:
    data=book.objects.get(book_id=id)
    data1=category.objects.all()
    data2=author_name.objects.all()
    data3=language.objects.all()
    return render(request,'Author/edit_product.html',{'data':data,'data1':data1,'data2':data2,'data3':data3})
 else:
      return redirect('/login/')
def au_update_product(request,id):
 if 'auname' in request.session:
        tbl=book.objects.get(book_id=id)
        if "image" in request.FILES:

            image=request.FILES['image']
            split_tup = os.path.splitext(image.name)
            file_extension = split_tup[1]
            # folder path
            dir_path = settings.MEDIA_ROOT
            count = 0
            # Iterate directory
            for path in os.listdir(dir_path):
            # check if current path is a file
                if os.path.isfile(os.path.join(dir_path, path)):
                    count += 1
            filecount=count+1
            filename=str(filecount)+"."+file_extension
            obj=FileSystemStorage()
            file=obj.save(filename,image)
            url1=obj.url(file)
            tbl.image=url1
        if "doc" in request.FILES:

            doc=request.FILES['doc']
            split_tup = os.path.splitext(image.name)
            file_extension = split_tup[1]
            # folder path
            dir_path = settings.MEDIA_ROOT
            count = 0
            # Iterate directory
            for path in os.listdir(dir_path):
            # check if current path is a file
                if os.path.isfile(os.path.join(dir_path, path)):
                    count += 1
            filecount=count+1
            filename=str(filecount)+"."+file_extension
            obj=FileSystemStorage()
            file=obj.save(filename,doc)
            url1=obj.url(file)
            tbl.doc=url1
        tbl.category_id=request.POST.get("category")
        tbl.language_id=request.POST.get("language_id")
        tbl.type=request.POST.get("type")
        tbl.book_name=request.POST.get("book_name")
        tbl.quantity=request.POST.get("quantity")
        tbl.price=request.POST.get("price")
        tbl.description=request.POST.get("description")
   
        tbl.save()
        messages.add_message(request, messages.INFO, 'Updated successfully.')
        return redirect('/au_product_list')
 else:
      return redirect('/login/')
def au_delete_product(request,id):
 if 'auname' in request.session:
    tbl=book.objects.get(book_id=id)
    tbl.delete()
    messages.add_message(request, messages.INFO, 'Deleted successfully.')
    return redirect('/au_product_list')
 else:
      return redirect('/login/')
def registered_author_list(request):
    if 'aname' in request.session:

        id=request.session['slogid']
        data=author.objects.all()

        return render(request,'Master/registered_author_list.html',{'data':data})
    else:
       return redirect('/login/')
def approval_author_book(request):
    if 'aname' in request.session:
      
        cursor=connection.cursor()
        cursor.execute("select p.*,c.category,l.language,a.* from  tbl_book as p inner join   tbl_category as c on p.category_id =c.category_id inner join tbl_author as a on p.author_id=a.login_id inner join tbl_language as l on p.language_id=l.language_id where p.status='Not Approved' and p.user_type='Author'")
        data=cursor.fetchall()

        return render(request,'Master/approval_author_book.html',{'data':data})
    else:
       return redirect('/login/')
    
def approve_author_book(request,id):
    if 'aname' in request.session:
        tbl=book.objects.get(book_id=id)
        tbl.status="Approved"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Updated successfully.')
        return redirect('/approval_author_book/')
    else:
       return redirect('/index/')
def reject_author_book(request,id):
    if 'aname' in request.session:
        tbl=book.objects.get(book_id=id)
        tbl.status="Rejected"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Rejected successfully.')
        return redirect('/approval_author_book/')
    else:
        return redirect('/login')
def approved_author_book(request):
    if 'aname' in request.session:
      
        cursor=connection.cursor()
        cursor.execute("select p.*,c.category,l.language,a.* from  tbl_book as p inner join   tbl_category as c on p.category_id =c.category_id inner join tbl_author as a on p.author_id=a.login_id inner join tbl_language as l on p.language_id=l.language_id where p.status='Approved' and p.user_type='Author'")
        data=cursor.fetchall()

        return render(request,'Master/approved_author_book.html',{'data':data})
    else:
       return redirect('/login/')
def reject_author_book2(request,id):
    if 'aname' in request.session:
        tbl=book.objects.get(book_id=id)
        tbl.status="Rejected"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Rejected successfully.')
        return redirect('/approved_author_book/')
    else:
        return redirect('/login')
def au_approved_list(request):
    if 'auname' in request.session:
        data1=category.objects.all()
        data2=author_name.objects.all()
        data3=language.objects.all()
        id=request.session['slogid']
        
        cursor=connection.cursor()
        cursor.execute("select p.*,c.category,l.language from  tbl_book as p inner join   tbl_category as c on p.category_id =c.category_id inner join tbl_language as l on p.language_id=l.language_id where user_type='Author' and status='Approved' and p.author_id="+str(id))
        data=cursor.fetchall()

        return render(request,'Author/au_approved_list.html',{'data':data,'data1':data1,'data2':data2,'data3':data3})
    else:
       return redirect('/login/')
def au_rejected_list(request):
    if 'auname' in request.session:
        data1=category.objects.all()
        data2=author_name.objects.all()
        data3=language.objects.all()
        id=request.session['slogid']
        
        cursor=connection.cursor()
        cursor.execute("select p.*,c.category,l.language from  tbl_book as p inner join   tbl_category as c on p.category_id =c.category_id inner join tbl_language as l on p.language_id=l.language_id where user_type='Author' and status='Rejected' and p.author_id="+str(id))
        data=cursor.fetchall()

        return render(request,'Author/au_rejected_list.html',{'data':data,'data1':data1,'data2':data2,'data3':data3})
    else:
       return redirect('/login/')
def auth_single_type(request,id):
    if 'uname' in request.session:
        data=book.objects.filter(type=id,user_type='Author',status='Approved')
        data1=category.objects.all()
        data2=author_name.objects.all()
        data3=language.objects.all()
        return render(request,'User/index.html',{'data':data,'data1':data1,'data2':data2,'data3':data3})
    else:
         return redirect('/login/')


def au_order_list(request):
    if 'auname' in request.session:
        logid=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select o.*,p.book_name,p.quantity,p.image,p.price,u.Name,u.phone_number,u.Email,u.Address,p.type  from  tbl_order as o inner join   tbl_book as p on p.book_id =o.book_id inner join tbl_category as c on p.category_id=c.category_id inner join tbl_customer_register as u  on o.user_login_id=u.login_id where   o.status='Paid' and p.user_type='Author' and p.author_id="+str(logid)+" order by  o.entry_date")
        data=cursor.fetchall()
        return render(request,'Author/order.html',{'data':data})
    else:
      return redirect('/login/')
def au_deliver(request,id):
    if 'auname' in request.session:
        tbl=order.objects.get(order_id=id)
        tbl.status="Delivered"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Delivered successfully.')
        return redirect('/au_order_list/')
    else:
       return redirect('/login/')
def au_deliverd_list(request):
    if 'auname' in request.session:
        logid=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select o.*,p.book_name,p.quantity,p.image,p.price,u.Name,u.phone_number,u.Email,u.Address  from  tbl_order as o inner join   tbl_book as p on p.book_id =o.book_id inner join tbl_category as c on p.category_id=c.category_id inner join tbl_customer_register as u  on o.user_login_id=u.login_id where  o.status='Delivered' and p.user_type='Author' and p.author_id="+str(logid)+" order by  o.entry_date")
        data=cursor.fetchall()
        return render(request,'Author/deliverd_list.html',{'data':data})
    else:
      return redirect('/login/')

def add_fee(request):
 if 'aname' in request.session:
     data1 = fee.objects.all()
     return render(request,'Master/fee.html',{'data':data1})
 else:
      return redirect('/index/')
    
def save_fee(request):
    if 'aname' in request.session:
        d = fee.objects.all()
        if d:
            messages.add_message(request, messages.INFO, ' Already Exist. Please Edit')
            return redirect('/add_fee/')
        else:
            tbl=fee()
            tbl.fee=request.POST.get("fee")
            tbl.save()
            messages.add_message(request, messages.INFO, 'Added successfully.')
            return redirect('/add_fee/')
    else:
      return redirect('/index/')
def edit_fee(request,id):
 if 'aname' in request.session:
     data1 = fee.objects.get(fee_id=id)
     return render(request,'Master/edit_fee.html',{'data':data1})
 else:
      return redirect('/index/')
def update_fee(request,id):
 if 'aname' in request.session:
    tbl = fee.objects.get(fee_id=id)
    tbl.fee=request.POST.get("fee")
    tbl.save()
    messages.add_message(request, messages.INFO, 'Updated successfully.')
    return redirect('/add_fee/')
 else:
      return redirect('/index/')
 
def author_members(request):
    if 'aname' in request.session:

        data=author.objects.filter(membership='Member')

        return render(request,'Master/author_members.html',{'data':data})
    else:
       return redirect('/login/')
def add_membership(request):
    if 'auname' in request.session:
        data1=fee.objects.all()
        for i in data1:
          f=i.fee
        today = datetime.datetime.today()
        logid=request.session['slogid']
        data=author.objects.filter(login_id=logid,membership='Member').filter(Q(expiry_date__gte=today))
        return render(request,'Author/add_membership.html',{'data':data,'f':f})
    else:
       return redirect('/login/')
    
def membership_payment(request):
    if 'auname' in request.session:
        data1=fee.objects.all()
        for i in data1:
          f=i.fee
        return render(request,'Author/membership_payment.html',{'f':f})
    else:
       return redirect('/login/')
    
def pay_membership_action(request):
    if 'auname' in request.session:
        logid=request.session['slogid']
        date_now = datetime.date.today()
        years_to_add = date_now.year + 1

        date_1 = date_now.strftime('%Y-%m-%d')
        date_2 = date_now.replace(year=years_to_add).strftime('%Y-%m-%d')
                
        author.objects.filter(login_id=logid).update(membership="Member",expiry_date=date_2)
        messages.add_message(request, messages.INFO, 'You are a member.')
        return redirect('/add_membership/')
    else:
       return redirect('/login/')