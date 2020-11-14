from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

# ! Not: the following urlpatterns is not wrapped in format_suffix_patterns
# (in contrary to the 5th tutorial page) because it has already been added
# added before (in 2nd tutorial page)
# API endpoints
urlpatterns = [
    path('', views.api_root),
    path('snippets/',
         views.SnippetList.as_view(),
         name='snippet-list'),
    path('snippets/<int:pk>/',
         views.SnippetDetail.as_view(),
         name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
         views.SnippetHighlight.as_view(),
         name='snippet-highlight'),
    path('users/',
         views.UserList.as_view(),
         name='user-list'),
    path('users/<int:pk>/',
         views.UserDetail.as_view(),
         name='user-detail')
]

# Allow to append to URL a suffix to choose the display format we want:
# - .json: force JSON
# - .api: force Browsable API (HTML)
# Or add HTTP accept headers:
# - Accept:application/json  # Request JSON
# - Accept:text/html         # Request HTML
urlpatterns = format_suffix_patterns(urlpatterns)
