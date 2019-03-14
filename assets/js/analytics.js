function getSalesHTML(data) {
    html = `<ul class="collection">
                <li class="collection-item teal lighten-1">Earnings from Completed Orders : ${data.completed_orders} </li>
                <li class="collection-item blue lighten-2">Earnings from Pending Orders : ${data.pending_orders}</li>
                <li class="collection-item red lighten-4">Earnings from Cancelled Orders : ${data.cancelled_orders}</li>
                <li class="collection-item teal lighten-5">Gross Earnings : ${data.completed_orders+data.pending_orders+data.cancelled_orders}</li>
           </ul>`
    return html;
}

function getPastOrdersHTML(data) {
console.log(data)
    html = `<ul class="collection">
                <li class="collection-item teal lighten-1">Completed Orders : ${data.completed || 0} </li>
                <li class="collection-item red lighten-4">Cancelled Orders : ${data.cancelled || 0}</li>
                </ul>`
    return html;
}

function getUpcomingOrdersHTML(data) {
console.log(data)
    html = `<ul class="collection">
                <li class="collection-item teal lighten-1">Active Orders : ${data.active || 0} </li>
                <li class="collection-item red lighten-4">Booked Orders : ${data.booked || 0}</li>
                </ul>`
    return html;
}

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

            $("#repeatOrders").text(response.repeat_orders)
            $("#pastOrders").html(getPastOrdersHTML(response.order_by_status))
            $("#upcomingOrders").html(getUpcomingOrdersHTML(response.order_by_status))

            $("#dailyGrossSales").html(getSalesHTML(response.sales.daily))
            $("#weeklyGrossSales").html(getSalesHTML(response.sales.weekly))
            $("#monthlyGrossSales").html(getSalesHTML(response.sales.monthly))
        }
    });

}

loadData();
setInterval(loadData, 10000);