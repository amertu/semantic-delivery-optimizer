function httpGET(url, data, onSuccess, onFailure, contentType, dataType) {
    $.ajax({
        type: "GET",
        contentType: contentType,
        url: url,
        data: data,
        success: onSuccess,
        error: onFailure,
        dataType: dataType
    });
}

function httpPOST(url, data, onSuccess, onFailure, contentType, dataType) {
    $.ajax({
        type: "POST",
        contentType: contentType,
        url: url,
        data: data,
        success: onSuccess,
        error: onFailure,
        dataType: dataType
    });
}

function httpPUT(url, data, onSuccess, onFailure, contentType, dataType) {
    $.ajax({
        type: "PUT",
        contentType: contentType,
        url: url,
        data: data,
        success: onSuccess,
        error: onFailure,
        dataType: dataType
    });
}

function httpDELETE(url, data, onSuccess, onFailure, contentType, dataType) {
    $.ajax({
        type: "DELETE",
        contentType: contentType,
        url: url,
        data: data,
        success: onSuccess,
        error: onFailure,
        dataType: dataType
    });
}