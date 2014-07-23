from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tomato.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'tomatoes.views.home', name='home'),
    url(r'^view_favorites/$', 'tomatoes.views.view_favorites', name='view_favorites'),
    url(r'^new_movie_json/$', 'tomatoes.views.new_movie_json', name='new_movie_json'),
    url(r'^new_movie_html/$', 'tomatoes.views.new_movie_html', name='new_movie_html'),
    url(r'^delete_favorite', 'tomatoes.views.delete_favorite', name='delete_favorite'),

    url(r'^admin/', include(admin.site.urls)),
)
