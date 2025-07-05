from django.urls import path
from . import views
urlpatterns = [
    path('addtask',views.addtask,name='addtask'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('showtask',views.showtask,name='showtask'),
    path('edittask/<int:id>',views.edittask,name='edittask'),
    path('deletetask/<int:id>',views.deletetask,name='deletetask'),
    
]
