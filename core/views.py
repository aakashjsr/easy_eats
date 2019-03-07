import pytz
from datetime import datetime, timedelta
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.views import APIView

from core.permissions import SuperUserPermission
from restaurants.models import Restaurant
from orders.models import Order
from accounts.models import Diner


class AnalyticsOverview(TemplateView):
    template_name = 'analytics.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseRedirect("/admin")
        return super().get(request, *args, **kwargs)


class AnalyticsData(APIView):
    permission_classes = (SuperUserPermission, )
    def get(request, *args, **kwargs):
        restaurants = Restaurant.objects.all()
        today = timezone.now().date()
        last_monday = today - timedelta(days=today.weekday())
        month_first_day = today.replace(day=1)

        data = {
            "sign_ups": {
                "daily": Diner.objects.filter(created__date=today).count(),
                "weekly": Diner.objects.filter(Q(created__date__gte=last_monday) & Q(created__date__lte=today)).count(),
                "monthly": Diner.objects.filter(Q(created__date__gte=month_first_day) & Q(created__date__lte=today)).count()
            },
            "orders": {
                "daily": Order.objects.filter(created__date=today).count(),
                "weekly": Order.objects.filter(Q(created__date__gte=last_monday) & Q(created__date__lte=today)).count(),
                "monthly": Order.objects.filter(Q(created__date__gte=month_first_day) & Q(created__date__lte=today)).count()
            },
            "restaurants": {
                "online": restaurants.filter(Q(dineout_online=True) | Q(takeaway_online=True)).count(),
                "offline": restaurants.filter(Q(dineout_online=False) & Q(takeaway_online=False)).count()
            }
        }
        return Response(data)
