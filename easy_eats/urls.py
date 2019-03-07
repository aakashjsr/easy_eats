from django.contrib import admin
from django.urls import path, include


from core import views as core_views


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('analytics/', core_views.AnalyticsOverview.as_view()),
    path('analytics-data/', core_views.AnalyticsData.as_view()),
    path('restaurant-statement/<int:restaurant_id>/', core_views.RestaurantStatement.as_view())
]
