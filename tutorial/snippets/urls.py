from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

# Allow to append to URL a suffix to choose the display format we want:
# - .json: force JSON
# - .api: force Browsable API (HTML)
# Or add HTTP accept headers:
# - Accept:application/json  # Request JSON
# - Accept:text/html         # Request HTML
urlpatterns = format_suffix_patterns(urlpatterns)
