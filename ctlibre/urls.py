from django.conf import settings
from django.conf.urls import patterns, include, url, static
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'ctlibre.views.home', name='home'),
    url(r'^article/(?P<slug>[^/]+)/$', 'news.views.article_detail',
        name='article-detail'),
    url(r'^author/(?P<slug>[^/]+)/$', 'news.views.author_detail',
        name='author-detail'),
    url(r'^archives/$', 'news.views.category_detail', {'slug': None},
        name='archives'),
    url(r'^category/(?P<slug>[^/]+)/$', 'news.views.category_detail',
        name='category-detail'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
)

# Serve static media during development
urlpatterns += static.static(settings.MEDIA_URL,
                             document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
    url(r'^', include('cms.urls')),
)
