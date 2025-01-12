from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .views import LeaveReviewWizard

urlpatterns = [
    # path('review/<pk:pk>/publish', ReviewPublishView.as_view(), name='review-publish'),
    # path('review/<pk:pk>/delete', ReviewDeleteView.as_view(), name='review-delete'),
    path('', LeaveReviewWizard.as_view(), name='index'),
] 

