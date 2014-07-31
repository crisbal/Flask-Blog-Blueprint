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

function postForm(url){
    if(formValidate()){
        console.log($("#form").serialize());
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
                    alert ("Can't complete operation.\nError: " + result.error);
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

$( "#editorApply" ).click(function() {
        postForm(saveEditsUrl)
});
