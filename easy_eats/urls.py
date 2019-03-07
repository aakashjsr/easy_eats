from django.contrib import admin
from django.urls import path, include


from core.views import AnalyticsData, AnalyticsOverview


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('analytics/', AnalyticsOverview.as_view()),
    path('analytics-data/', AnalyticsData.as_view())
]
