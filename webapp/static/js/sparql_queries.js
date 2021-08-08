
function getAllProducts(callback) {

    httpGET(
        "/api/products",
        null,
        (data) => { callback(data.results.bindings)},
        (error) => { console.log(error)},
        null,
        "json"
    )
}

function getAllRestaurants(state, callback) {

    $("#table_suggestions > tbody").empty();

    if(state.products.length > 0 || state.allProducts) {

        httpPOST(
            "/api/restaurants",
            JSON.stringify(state),
            (data) => { callback(data) },
            () => { console.log("fail")},
            "application/json; charset=utf-8",
            "json"
        );
    }
}