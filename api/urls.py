from django.urls import path
from .views import ChatList, ChatDetail, ChatCreate, ChatDelete, ChatUpdate

urlpatterns = [
    path('', ChatList),
    path('create/', ChatCreate),
    path('delete/<int:pk>', ChatDelete),
    path('update/<int:pk>', ChatUpdate),
    path('<int:pk>', ChatDetail),
]