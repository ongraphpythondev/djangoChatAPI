function data_to_dict(serializedData){
    data = {}
    for (var i = 0; i < serializedData.length; i++) {
        data[serializedData[i]['name']] = serializedData[i]['value']
    }
    return data
}   
$("#registerForm").submit(function(e) {
    e.preventDefault()
    var serializeddata = $(this).serialize();
    // serializeddata = data_to_dict(serializeddata)
    // serializeddata = JSON.stringify(serializeddata)
    // var formData = new FormData(this);
    console.log(serializeddata)
    $.ajax({
        type: 'POST',
        url: '/signup/',
        data: serializeddata,
        processData: false,
        success: function(data){
            console.log(data)
            $("#register-success").append('<h3>Register successfully Please login<\h3>')
            location.replace("/login/")

        },
        error: function (response) {
            console.log(response)
            alert(response.responseJSON.msg)
        }
    });
})