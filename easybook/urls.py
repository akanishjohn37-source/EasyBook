"""
URL configuration for easybook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index),
    path('index/',views.index),
    path('login/',views.sign_in),
    path('customer_registration/',views.customer_registration),
    path('author_registration/',views.author_registration),
    path('customer_action/',views.customer_action),
    path('author_action/',views.author_action),
    
    path('login_action/', views.sign_in_process),
    path('admin_home/', views.admin_home),
    path('admin_logout/', views.admin_logout),
     path('customer_list/', views.customer_list),
    path('add_category/', views.add_category),
    path('save_category/', views.save_category),
    path('edit_category/<int:id>', views.edit_category),
    path('update_category/<int:id>', views.update_category),
    path('delete_category/<int:id>', views.delete_category),

    path('add_language/', views.add_language),
    path('save_language/', views.save_language),
    path('edit_language/<int:id>', views.edit_language),
    path('update_language/<int:id>', views.update_language),
    path('delete_language/<int:id>', views.delete_language),

    path('add_author/', views.add_author),
    path('save_author/', views.save_author),
    path('edit_author/<int:id>', views.edit_author),
    path('update_author/<int:id>', views.update_author),
    path('delete_author/<int:id>', views.delete_author),


    
    path('add_product/', views.add_product),
    path('save_product/', views.save_product),
    path('edit_product/<int:id>', views.edit_product),
    path('update_product/<int:id>', views.update_product),
    path('delete_product/<int:id>', views.delete_product),
    path('product_list/', views.product_list),
    path('display_product/', views.display_product, name='display_product'),

    path('Customer/', views.Customer),

    path('checkout/', views.checkout),
    path('cart_check_out/<int:id>', views.cart_check_out),
    path('user_logout/', views.user_logout),
    path('add_qty/', views.add_qty, name='add_qty'),
    path('sub_qty/', views.add_qty, name='sub_qty'),


    path('payment/<int:id>', views.payment),
    path('pay_action/', views.pay_action),
    path('myorder/', views.myorder),
    path('order_list/', views.order_list),
    path('deliver/<int:id>', views.deliver),
    path('deliverd_list/', views.deliverd_list),
    path('clear_cart/', views.clear_cart),

    path('single_book/<int:id>', views.single_book),
    


    path('single_category/<int:id>', views.single_category),
    path('search_book/', views.search_book),
    path('single_language/<int:id>', views.single_language),
    path('single_author/<int:id>', views.single_author),

    path('single_type/<str:id>', views.single_type),

     path('payment_no_book/<int:id>', views.payment_no_book),
   path('pay_no_book_action/', views.pay_no_book_action),
    path('pay_no_book_action/', views.pay_no_book_action),


        #feedback
    path('view_feedback/', views.view_feedback),
    path('replied_feedback_list/', views.replied_feedback_list),
    path('adm_reply_feedback/<int:id>', views.adm_reply_feedback),
    path('add_reply_feedback/<int:id>', views.add_reply_feedback),

    #  Customer
    path('feedback/', views.feedback_frm),
    path('save_feedback/', views.save_feedback),
    path('feedback_list/', views.feedback_list),
    path('delete_feedback/<int:id>', views.delete_feedback),
        #complaint
    path('view_complaint/', views.view_complaint),
    path('replied_list/', views.replied_list),
    path('adm_reply_complaint/<int:id>', views.adm_reply_complaint),
    path('add_reply/<int:id>', views.add_reply),

    #  Customer
    path('complaint/', views.complaint_frm),
    path('save_complaint/', views.save_complaint),
    path('complaint_list/', views.complaint_list),
    path('delete_complaint/<int:id>', views.delete_complaint),

    # Author

   path('author_home/', views.author_home),

   path('au_add_product/', views.au_add_product),
   path('au_save_product/', views.au_save_product),
   
   path('au_product_list/', views.au_product_list),
   path('au_edit_product/<int:id>', views.au_edit_product),
    path('au_update_product/<int:id>', views.au_update_product),
    path('au_delete_product/<int:id>', views.au_delete_product),

       path('registered_author_list/', views.registered_author_list),
       path('approval_author_book/', views.approval_author_book),
     path('reject_author_book/<int:id>', views.reject_author_book),
       path('approve_author_book/<int:id>', views.approve_author_book),
path('approved_author_book/', views.approved_author_book),
 path('reject_author_book2/<int:id>', views.reject_author_book2),
path('au_approved_list/', views.au_approved_list),
path('au_rejected_list/', views.au_rejected_list),  
path('auth_single_type/<str:id>', views.auth_single_type),    
path('au_order_list/', views.au_order_list),
path('au_deliver/<int:id>', views.au_deliver),
path('au_deliverd_list/', views.au_deliverd_list),

path('add_fee/', views.add_fee),
path('save_fee/', views.save_fee),
path('edit_fee/<int:id>', views.edit_fee),
path('update_fee/<int:id>', views.update_fee),


path('author_members/', views.author_members),
path('add_membership/', views.add_membership),
path('membership_payment/', views.membership_payment),
path('pay_membership_action/', views.pay_membership_action),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)