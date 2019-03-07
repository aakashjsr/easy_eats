JET_SIDE_MENU_COMPACT = True

JET_SIDE_MENU_ITEMS = [  # A list of application or custom item dicts
    {
        'label': 'Analytics Dashboards',
        'items': [{'label': 'Overview', 'url': '/analytics/', 'url_blank': False}],
    },
    {
        'label': 'User Management',
        'app_label': 'accounts',
        'items': [
            {'name': 'accounts.user', 'label': 'User'},
            {'name': 'accounts.restaurantowner', 'label': 'Restaurant Owner'},
            {'name': 'accounts.restaurantstaff', 'label': 'Restaurant Staff'},
            {'name': 'accounts.diner', 'label': 'Diner'},
        ],
    },
    {
        'label': 'Restaurant Management',
        'items': [
            {'name': 'restaurants.restaurant', 'label': 'Restaurant'},
            {'name': 'restaurants.fooditem', 'label': 'Food Items'},
            {'name': 'orders.order', 'label': 'Order'},
            {'name': 'core.tag', 'label': 'Tags'},
            {'name': 'core.foodcategory', 'label': 'Food Categories'},
            {'name': 'core.location', 'label': 'Locations'},
        ],
    },
]

JET_INDEX_DASHBOARD = 'easy_eats.dashboards.CustomIndexDashboard'
