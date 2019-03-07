function loadData() {
    $.ajax({
        type: "GET",
        url: "/analytics-data/",
        dataType: "json",
        error: function(response) {
            alert("unable to load data")
        },
        success: function(response) {
            $("#dailySignup").text(response.sign_ups.daily)
            $("#weeklySignup").text(response.sign_ups.weekly)
            $("#monthlySignup").text(response.sign_ups.monthly)

            $("#dailyOrder").text(response.orders.daily)
            $("#weeklyOrder").text(response.orders.weekly)
            $("#monthlyOrder").text(response.orders.monthly)

            $("#onlineRestaurants").text(response.restaurants.online)
            $("#offlineRestaurants").text(response.restaurants.offline)
        }
    });

}

loadData();
setInterval(loadData, 3000);