
$('#send-msg').click(function () {
    
    var inputData = $("#message").val();
    $('#main-chat').append('<div><p class="left-chat">'+inputData+'</p></div>');
    console.log("here",inputData)
    $.ajax({
        type: "post",
        url: "/",
        data: {"text":inputData},
        success: function(data){
            let msg = data.msg;
            $('#main-chat').append('<div><p class="right-chat">'+msg+'</p></div>');
            console.log("done",msg)
        }
    });
});
