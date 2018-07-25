$(document).ready(function () {
        $('input:radio[name="optradio"]').click(function(){
        if ($(this).is(':checked') && $(this).val() == 'auto') {
            $('#good').addClass('btn-disabled');
            $('#good').attr('disabled', 'disabled');
            $('#good').prop('disabled', true);
            setTimeout(function(){ alert("IP 주소가 DHCP 클라이언트에 의해 자동할당되었습니다."); }, 0);
            $.ajax({
                type: 'GET',
                url: 'http://127.0.0.1:8000/simap/info2/mac_hostname.html',
                dataType: 'json',
                success: function(result){
                     y = result.mac_addresses;
                     x = result.hostname;
                    document.getElementById("wan_ip").value = x;
                    document.getElementById("wan_net").value = y;
                    document.getElementById("wan_gate").value = y;
                }
          });
            document.getElementById("wan_ip").disabled = true;
            document.getElementById("wan_net").disabled = true;
            document.getElementById("wan_gate").disabled = true;
        }else {
            $('#good').prop('disabled', false);
            document.getElementById("wan_ip").disabled = false;
            document.getElementById("wan_net").disabled = false;
            document.getElementById("wan_gate").disabled = false;
        }
});
});