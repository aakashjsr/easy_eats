from accounts.models import *
from restaurants.models import *
from core.models import *
from orders.models import *


class PopulateData:
    def populate_tags(self):
        names = ["hot", "spicy", "cheap", "sweet", "sour"]
        for name in names:
            Tag.objects.create(name=name)

    def populate_user(self):
        User.objects.create_superuser(
            email="admin@admin.com",
            password="Testing123",
            first_name="Admin",
            last_name="User",
        )
        self.user_1 = User.objects._create_user(
            email="test_1@gmail.com",
            password="Testing123",
            first_name="Test",
            last_name="User 1",
        )
        self.user_2 = User.objects._create_user(
            email="test_2@gmail.com",
            password="Testing123",
            first_name="Test",
            last_name="User 2",
        )
        self.user_3 = User.objects._create_user(
            email="test_3@gmail.com",
            password="Testing123",
            first_name="Test",
            last_name="User 3",
        )
        self.user_4 = User.objects._create_user(
            email="test_4@gmail.com",
            password="Testing123",
            first_name="Test",
            last_name="User 4",
        )
        self.user_5 = User.objects._create_user(
            email="test_5@gmail.com",
            password="Testing123",
            first_name="Test",
            last_name="User 5",
        )
        self.user_6 = User.objects._create_user(
            email="test_6@gmail.com",
            password="Testing123",
            first_name="Test",
            last_name="User 6",
        )

        self.resturant_owner_1 = RestaurantOwner.objects.create(user=self.user_1)
        self.resturant_staff_1 = RestaurantStaff.objects.create(user=self.user_2)
        self.member_1 = Diner.objects.create(user=self.user_3)

        self.resturant_owner_2 = RestaurantOwner.objects.create(user=self.user_4)
        self.resturant_staff_2 = RestaurantStaff.objects.create(user=self.user_5)
        self.member_2 = Diner.objects.create(user=self.user_6)

    def populate_resturants(self):
        self.resturant_1 = Restaurant.objects.create(
            name="Resturaunt 1",
            address="Temp 2",
            phone="1313123",
            staff=self.resturant_staff_1,
            owner=self.resturant_owner_1,
            bank_name="qsdas",
            bank_acc_name="314124",
            bank_acc_number="13412213",
            transaction_fee_rate=10.23,
            sales_service_tax=11.2,
            service_charge_rate=42.3,
            has_dine_in_service_charge=True,
            has_takeaway_service_charge=True,
            dineout_online=True,
            takeaway_online=True,
            search_position=1,
            seats=100,
            cost_index=3,
        )

        self.resturant_2 = Restaurant.objects.create(
            name="Resturaunt 2",
            address="Temp 343",
            phone="1313123",
            staff=self.resturant_staff_2,
            owner=self.resturant_owner_2,
            bank_name="qsdas",
            bank_acc_name="314124",
            bank_acc_number="13412213",
            transaction_fee_rate=10.23,
            sales_service_tax=11.2,
            service_charge_rate=42.3,
            has_dine_in_service_charge=True,
            has_takeaway_service_charge=True,
            dineout_online=True,
            takeaway_online=True,
            search_position=1,
            seats=100,
            cost_index=3,
        )

        self.resturant_3 = Restaurant.objects.create(
            name="Resturaunt 3",
            address="Temp 343",
            phone="1313123",
            staff=self.resturant_staff_2,
            owner=self.resturant_owner_2,
            bank_name="qsdas",
            bank_acc_name="314124",
            bank_acc_number="13412213",
            transaction_fee_rate=10.23,
            sales_service_tax=11.2,
            service_charge_rate=42.3,
            has_dine_in_service_charge=True,
            has_takeaway_service_charge=True,
            dineout_online=True,
            takeaway_online=True,
            search_position=1,
            seats=100,
            cost_index=3,
        )
