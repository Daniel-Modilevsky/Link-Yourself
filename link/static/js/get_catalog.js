function jsonReadOne(staticpath){
$(document).ready(function () {
    console.log("Daniel Modilevsky");
    $.getJSON(staticpath, function (data) {
        $("h1").html(data.listName);
        $.each(data.catalog, function () {
            $(".btn-group").append("<button type ='button' class ='btn btn-secondary btn-info'><a href='/cataloglist/?option_id=" + this.option_id + "' target='_blank'>" + this.option +
                "</a></button>");
        });
    });
})};
