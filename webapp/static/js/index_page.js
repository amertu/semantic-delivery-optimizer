let state = {
    products: [],
    allProducts: false,
    cashEnabled: true,
    cardEnabled: true,
    ordering: "price",
};

function init() {

    $('.dataTables_length').addClass('bs-select');

    let products = getAllProducts(
        function (products) {
            for(product in products) {
                $productItem = $("<button>", {
                    class: "list-group-item list-group-item-action product_item",
                    "data-toggle": "tooltip",
                    "data-placement": "right",
                    "title": products[product].description.value,
                    click: function() { addProductToSelected($(this)) }
                });
                $productItem.text(products[product].product.value);
                $("#list_product").append($productItem);
            }
        }
    );

    $('#checkboxCash').click(
        function() {
            if(!$(this).hasClass("checked")) {
                $(this).addClass('checked');
                state.cashEnabled = true;
            }
            else {
                if($('#checkboxCard').hasClass("checked")) {
                    $(this).removeClass('checked');
                    state.cashEnabled = false;
                }
                else {
                    $(this).prop('checked', true);
                }
            }
            getAllRestaurants(state, printSuggestions);
        }
    );

    $('#checkboxCard').click(
        function() {
            if(!$(this).hasClass("checked")) {
                $(this).addClass('checked');
                state.cardEnabled = true;
            }
            else {
                if($('#checkboxCash').hasClass("checked")) {
                    $(this).removeClass('checked');
                    state.cardEnabled = false;
                }
                else {
                    $(this).prop('checked', true);
                }
            }
            getAllRestaurants(state, printSuggestions);
        }
    );

    $('#radioOrderingPrice').click(() => { state.ordering = "price"; getAllRestaurants(state, printSuggestions); });
    $('#radioOrderingRating').click(() => { state.ordering = "rating"; getAllRestaurants(state, printSuggestions); });
    $('#checkboxAllProducts').click(() => { state.allProducts = !state.allProducts; getAllRestaurants(state, printSuggestions); });
}

function addProductToSelected($productButton) {
    $productButton.addClass("disabled");
    $productIteNew = $("<button>", {
        class: "list-group-item list-group-item-action product_item",
            click: function() {
                $productButton.removeClass("list-group-item-info");
                removeProductFromSelected($(this), $productButton)
            }
        });
    const text = $productButton.text();
    $productIteNew.text(text);
    state.products.push(text);
    $("#list_selected_product").append($productIteNew);

    getAllRestaurants(state, printSuggestions);
}

function removeProductFromSelected($productButton, $disabledButton) {
    $productButton.hide();
    $disabledButton.removeClass("disabled");

    const text = $productButton.text();
    state.products.splice(state.products.indexOf(text), 1);

    getAllRestaurants(state, printSuggestions);
}

function printSuggestions(data) {
    let rows = "";
    for(i in data.results.bindings) {
        let product = data.results.bindings[i];

        let cashPaymentBadge = product.isCashEnabled.value === "ENABLED" ? "<span class=\"badge badge-pill badge-info\">Cash</span>" : "";
        let creditPaymentBadge = product.isCreditEnabled.value === "YES" ? "<span class=\"badge badge-pill badge-success\">Card</span>" : "";

        rows +=
            "<tr>" +
            "<td></td>" +
            "<td>" + product.menuName.value + "</td>" +
            "<td>" + product.restaurantName.value + "</td>" +
            "<td>" + product.menuPrice.value.replace("E0", "&euro;").replace("E1", "&euro;") + "</td>" +
            "<td>" + cashPaymentBadge + creditPaymentBadge + "</td>" +
            "<td>" + product.ratingValue.value.replace("E0", "").replace("E1", "") + "</td>" +
            "</tr>";
    }
    $("#table_suggestions > tbody:last-child").append(rows);
}