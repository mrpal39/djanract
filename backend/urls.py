
# from os import name
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
# from rest_framework.documentation import include_docs_urls  # new
# from rest_framework.schemas import get_schema_view  # new


# API_TITLE = 'Blog API'  # new
# API_DESCRIPTION = 'A Web API for creating and editing blog posts.'  # new
# schema_view = get_schema_view(title=API_TITLE)  # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    # path('api/', include('core.urls'), name='api'),
    # path('blogs/', include('blog.urls')),
    # path('blog/', TemplateView.as_view(template_name='blog/blog.html')),

    # path('api/v1/', include('blog.urls')),  # new
    # path('api-auth/', include('rest_framework.urls')),  # new
    # path('api/v1/rest-auth/', include('rest_auth.urls')),
    # path('api/v1/rest-auth/registration/',  # new
    #      include('rest_auth.registration.urls')),  # new
    # path('docs/', include_docs_urls(title=API_TITLE,
    #                                 description=API_DESCRIPTION)),  # new
    # path('swagger-docs/', schema_view),  # new
]
