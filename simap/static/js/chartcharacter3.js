$(document).ready(function () {
    $.ajax({
                type: 'GET',
                url: 'http://127.0.0.1:8000/system/ip-netmask-gateway',
                dataType: 'json',
                success: function(result){
                     x = result.netmask;
                     z = result.gateway;
                    document.getElementById("wan_net").value = x;
                    document.getElementById("wan_gate").value = z;
                }
          });

        $('#good').click(function(){
          y = document.getElementById("wan_ip").value;
         // $.ajax({
         //       type: 'POST',
         //       url: 'http://127.0.0.1:8000/simap/ip_address.html',
         //     data: {'a': y}
         //  });
          alert("IP 주소가 수동설정 되었습니다.");
        });

        $('input:radio[name="optradio"]').click(function(){
        if ($(this).is(':checked') && $(this).val() == 'auto') {
            $('#good').addClass('btn-disabled');
            $('#good').attr('disabled', 'disabled');
            $('#good').prop('disabled', true);
            setTimeout(function(){ alert("IP 주소가 DHCP 클라이언트에 의해 자동할당되었습니다."); }, 0);
            $.ajax({
                type: 'GET',
                url: 'http://127.0.0.1:8000/system/ip-netmask-gateway',
                dataType: 'json',
                success: function(result){
                     y = result.lan;
                    document.getElementById("wan_ip").value = y;
                }
          });
            document.getElementById("wan_ip").disabled = true;
        }else {
            $('#good').prop('disabled', false);
            document.getElementById("wan_ip").disabled = false;
        }
});
});