function registerFunctions() {

    $('#alert_input').hide();

    $( "#btn_add" ).click(() =>  {

        let firstName = $( "#input_first_name" ).val();
        let lastName = $( "#input_last_name" ).val();
        let adress = $( "#input_adress" ).val();
        let product = $( "#input_product" ).val();

        console.log(firstName, lastName, adress, product);

        if(!firstName || !lastName || !adress || !product) {
            $("#alert_input").fadeTo(2000, 500).slideUp(500, function(){
                $("#alert_input").slideUp(500);
            });
        }
        else {
            addProductListItem(product);
        }

        /* httpPOST(
            "/api/add",
            JSON.stringify({product: product}),
            (data) => { addRestaurantListItem(data) },
            () => { alert("Failed") },
            "application/json",
            "json"
        ); */
    });
}

function addProductListItem(product) {

    $productItem = $("<li>", {
        class: "list-group-item text-center d-inline-block"
    });
    $productItem.html(product)

    $( "#list_product" ).append($productItem);
    $( "#input_product" ).val("");
}
