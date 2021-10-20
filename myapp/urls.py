
from django.urls.conf import path

from myapp.views import Index_page, addTodo, delete, update


urlpatterns = [
    path('',Index_page),
    path('add/',addTodo),
    path('update/<int:id>/',update),
    path('delete/<int:id>/',delete)
]