from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

admin.site.site_header = "UCLA Stats 141SL"
admin.site.site_title = "Group Sugano 2"
admin.site.index_title = "UCLA Toxic Course Combination Portal"
urlpatterns = [
    url('admin/', admin.site.urls), 
]

if 'survey' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'', include('survey.urls'))
    ]