function formValidate(){
    if($("#title").val().trim().length <= 0){
        return false;
    }
    if($("#shortDescription").val().trim().length <= 0){
        return false;
    }
    if($("#body").val().trim().length <= 0){
        return false;
    }
    return true;
}

function postForm(url,operation){
    if(formValidate()){
        $.ajax(
        {
            url: url,
            type: 'POST',
            data: $("#form").serialize(),
            success: function(result) 
            {
                if (result.status == "OK"){
                    window.location =  result.url;
                }else{
                    alert ("Can't " + operation + " this post.\nError: " + result.error);
                }
                
            },
            error: function(xhr, status, error)
            {
                var err = eval("(" + xhr.responseText + ")");
                alert("ERROR: " + err.Message);
            }
        });
    }
}

$( "#editorAddPost" ).click(function() {
        postForm(baseAdminAddUrl, "add")
});
