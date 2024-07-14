from django.urls import path
from.import views


urlpatterns = [
    path('home/', views.homepage, name='homep'),
    path('hmp2/', views.hompg, name='hompg'),
    path('blood_request/', views.make_blood_request, name='make_blood_request'),
    path('req_succ/',views.request_succ, name='request_succ'),
    path('blooddonation/', views.make_blood_donation, name='make_blood_donation'),
    path('don_succ/', views.donation_succ, name='donation_succ'),
    path('signu/', views.signup, name='signup'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('blood_req/,', views.my_blood_request, name='my_blood_request'),
    path('blood_don/', views.my_blood_donation, name='my_blood_donation'),
    path('medad/', views.medadd, name='medadd'),
    path('medlist/', views.medi_prods, name='medi_prods'),
    path('booking/<int:pk>/', views.product_book, name='product_book'),
    path('book_succ/', views.booking_succ, name='booking_succ'),
    path('search/', views.search_p, name='search_p'),
    path('profile/', views.profile, name='profile'),
    path('ord/', views.order_view, name='order_view'),
    path('filter/', views.filtered_products, name='filtered_products'),
    path('cancel_order/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    
]