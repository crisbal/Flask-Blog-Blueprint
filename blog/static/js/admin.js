$( ".adminDeleteButton" ).click(function() {
    postId = $(this).attr("post-id");

    $.ajax({
        url: baseAdminDeleteUrl + postId,
        type: 'DELETE',
        success: function(result) {
            if (result.status == "OK"){
                alert ("Succesfully removed post with Id = " + result.postRemoved);
                location.reload();
            }else{
                alert ("Can't remove post with Id " + postId + ".\nError: " + result.error);
            }
            
        },
        error: function(xhr, status, error){
            var err = eval("(" + xhr.responseText + ")");
            alert("ERROR: " + err.Message);
        }
    });
});