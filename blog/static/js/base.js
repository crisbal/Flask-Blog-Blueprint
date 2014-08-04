function search(){
    searchInput = $("#searchInput").val()
    if(searchInput.length > 0)
        window.location = baseTagUrl + searchInput;

    return false;

}

$( "#searchSubmit" ).click(function() {

    search();
});

