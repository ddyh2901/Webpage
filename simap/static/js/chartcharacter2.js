$('#mac_host').click(function(){
    $.ajax({
                type: 'GET',
                url: 'http://127.0.0.1:8000/simap/info2/mac_hostname.html',
                dataType: 'json',
                success: function(result){
                     y = result.mac_addresses;
                     x = result.hostname;
                    document.getElementById("host").value = x;
                    document.getElementById("mac").value = y;
                }
        });
});