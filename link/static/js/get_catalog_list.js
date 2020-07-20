function jsonReadTwo(staticpath1, staticpath2){
var idLink, idUser, date, linkName, iframeUrl, linkURL, privatey, catalogID;

function getCatalogId() {
    var aKeyValue = window.location.search.substring(1).split('&'),
        idCatalog = aKeyValue[0].split("=")[1];
    return idCatalog;
}

var linkIDArray = [-999];


$(document).ready(function () {
    $.getJSON(staticpath2, function (data) {
        var data;
        var catlogId = getCatalogId();
        $.getJSON(staticpath1, function (data) {
            $.each(data.catalog, function () {
                console.log(data.catalog.option_id);

                if(catlogId == data.catalog.option_id){
                    $("#catalog-header").append("<h1>" + data.catalog.option+ "</h1>");
                }
            });
        });

        $.each(data.listLinks, function (i, obj) {
            if (obj.catalogChice == catlogId) {
                if (!(obj.link_id in linkIDArray)) {
                    linkIDArray[i] = obj.link_id;
                    idLink = obj.link_id;
                    idUser = obj.user_id;
                    date = obj.dateCLastSeen;
                    linkName = obj.name;
                    iframeUrl = obj.urlFrame;
                    linkURL = obj.url;
                    privatey = obj.isPrivate;
                    catalogID = obj.catalogChice;


                    $(".list-container").append("<div class ='grid-item'> <div class ='iframe-sec'><iframe src ='" + iframeUrl +
                        "' width = '300' height = '200' frameborder = '0'></iframe> </div>");
                    $(".list-container .grid-item").append("<div class = 'detail-sec'><a href = '" + linkURL + "' target = '_blank '>" +
                        linkName + "</a>");
                    $(".list-container .grid-item").append("<h6 style='color:red'>" + idLink + "</h5>");
                    $(".list-container .grid-item").append("<h6>" + "Catalog: "  + catalogID + "</h6></div>");
                } else {
                }
            }

        });
    });
})};
