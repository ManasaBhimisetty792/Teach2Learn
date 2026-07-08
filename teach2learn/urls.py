"""
URL configuration for teach2learn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app1 import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home,name='home'),
    path("about/",views.about,name='about'),
    path("howitworks/",views.howitworks,name='howitworks'),
    path("pricing/",views.pricing,name='pricing'),
    path("contact/",views.contact,name='contact'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
    # user paths
    path("dashboard/",views.dashboard,name='dashboard'),
    path("profile/",views.profile,name='profile'),
    path("editProfile/",views.editProfile,name='editProfile'),
    path("certifications/",views.certifications,name='certifications'),
    path("assignments/",views.assignments,name='assignments'),
    path("chat/",views.chat,name='chat'),
    path("interview/",views.interview,name='interview'),
    path("matches/",views.matches,name='matches'),
    path("progress/",views.progress,name='progress'),
    path("sessions/",views.sessions,name='sessions'),
    path("usersubscriptions/",views.usersubscriptions,name='usersubscriptions'),
      # Google login callback
    path("google-login/", views.google_login, name="google_login"),
    


    # admin paths
    path("admin-dashboard/",views.admindashboard,name='admindashboard'),
    path("user-management/",views.usermanagement,name='usermanagement'),
    path("subscriptions/",views.subscriptions,name='subscriptions'),
    path("analytics/",views.analytics,name='analytics'),
    path("support-feedback/",views.support,name='support'),  
    path("my_connections/",views.my_connections,name='my_connections'),
   path("member-profile/<int:id>/", views.member_profile, name="member_profile"),
   path("member-profile1/<int:id>/", views.member_profile1, name="member_profile1"),
   path("send-request/<int:member_id>/",views.send_request,name="send_request"),
   path("notifications/",views.notifications,name="notifications"),

path(
    "accept/<int:request_id>/",
    views.accept_request,
    name="accept_request"
),

path(
    "reject/<int:request_id>/",
    views.reject_request,
    name="reject_request"
),
path('rating/<int:connection_id>/', views.rating,name='rating'),
path(
    "rate-mentor/<int:connection_id>/",
    views.rate_mentor,
    name="rate_mentor",
),


path(
    "support/status/<int:request_id>/<str:status>/",
    views.update_request_status,
    name="update_request_status"
),
path(
    "complete-course/<int:connection_id>/",
    views.complete_course,
    name="complete_course",
),



path('chat/<str:email>/', views.chat, name='chat_with_user'),
path('notifications/mark-read/', views.mark_notification_read, name='mark_notification_read'),
path("chat/", views.chat, name="chat"),
path("premium/", views.premium_page, name="premium_page"),
path("payment-success/", views.payment_success, name="payment_success"),
path("premium-chat/", views.premium_chat, name="premium_chat"),
path("verify-payment/", views.verify_razorpay_payment, name="verify_razorpay_payment"),
path("create-order/", views.create_order, name="create_order"),
path("sessions/", views.sessions, name="sessions"),
path("sessions/<int:connection_id>/", views.sessions, name="sessions_by_connection"),
path("generate-question/",views.generate_question,name="generate_question"),
path(
    "test-ai/",
    views.test_ai,
    name="test_ai"
),

path(
    "evaluate-answer/",
    views.evaluate_answer,
    name="evaluate_answer"
),
path("export-users-csv/", views.export_users_csv, name="export_users_csv"),
path(
    "download-receipt/<int:user_id>/",
    views.download_receipt,
    name="download_receipt"
),
path(
    "support/status/<int:request_id>/<str:status>/",
    views.update_request_status,
    name="update_request_status"
),
path(
    "complete-course/<int:connection_id>/",
    views.complete_course,
    name="complete_course",
),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)