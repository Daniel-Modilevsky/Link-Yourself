from django.contrib import admin
from django.urls import path
from link import views
from django.urls import include
from django.conf.urls.static import static


urlpatterns = [
    # ===========================================
    # Default
    # ===========================================
    path('', views.homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('home/<int:user_id>', views.home, name='home'),
    path('logout/', views.logout1, name='logout1'),
    path('login1/', views.login1, name='login1'),
    path('registerProfile/', views.registerProfile2, name='registerProfile2'),

    # ===========================================
    # CRUD
    # ===========================================
    path('create/', views.create, name="create"),
    path('show/<int:user_id>', views.show, name="show"),
    path('update/<int:id>', views.update, name="update"),
    path('destroy/<int:id>', views.destroy, name="destroy"),
    # ===========================================
    # Extra
    # ===========================================
    path('listAll/', views.listAll, name='listAll'),
    path('catalog/', views.catalog, name='catalog'),
    path('cataloglist/', views.cataloglist, name='cataloglist'),
    path('admin/clearcache/', include('clearcache.urls')),
    path('copyToMe/<int:user_id>', views.copyToMe, name='copyToMe'),
]

