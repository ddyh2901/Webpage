    var data = [];
    var data2 = [];
    var dataset, dataset2;
    var totalPoints = 50;
    var updateInterval = 1000;
    var now = new Date().getTime();
    var count = 0;
    var count2 = 1;

    function GetData1() {
        $.ajax({
                type: 'GET',
                url: 'http://127.0.0.1:8000/simap/info/cpu-ram',
                dataType: 'json',
                success: function(result){
                  if(data.length > totalPoints){
                    data.shift();
                    data2.shift();
                  }
                    var w = result.time;
                    var y = result.cpu;
                    var x = result.ram;
                    var temp = [now += updateInterval, y];
                    var temp2 = [now += updateInterval, x];
                    data.push(temp);
                    data2.push(temp2);

                    if(y > 75){
                        if(count<5)
                        {
                            count++;
                         }
                        else
                        {
                            count++;
                            var id = '#div_'+ count2;
                            var id2 = '#a_' + count2;
                            $(id).remove();
                            $(id2).remove();
                            count2++;
                        }
                        var html = '<div class="dropdown-divider" id="div_' + count + '"></div>';
                            html += '<a class="dropdown-item" id="a_' + count + '" href="log.html">';
                            html += '<span class="text-danger">';
                            html += '<strong>';
                            html += '<i class="fa fa-long-arrow-up fa-fw"></i>CPU 75% 이상 사용!</strong>';
                            html += '</span>';
                            html += '<span class="small float-right text-muted">' + w + '</span>';
                            html += '<div class="dropdown-message small">This is an automated server response message. All systems are online.</div></a>';

                        $("#starting").prepend(html);
                    }

                    if(x > 75){
                        if(count<5)
                         {
                            count++;
                         }
                        else
                        {
                            count++;
                            var id = '#div_'+ count2;
                            var id2 = '#a_' + count2;
                            $(id).remove();
                            $(id2).remove();
                            count2++;
                        }
                        var html = '<div class="dropdown-divider" id="div_' + count + '"></div>';
                            html += '<a class="dropdown-item" id="a_' + count + '" href="#">';
                            html += '<span class="text-success">';
                            html += '<strong>';
                            html += '<i class="fa fa-long-arrow-up fa-fw"></i>메모리 75% 이상 사용!</strong>';
                            html += '</span>';
                            html += '<span class="small float-right text-muted">' + w + '</span>';
                            html += '<div class="dropdown-message small">This is an automated server response message. All systems are online.</div></a>';
                            $("#starting").prepend(html);
                    }
                }
         });
    }

$(document).ready(function() {

        var nowTime = new Date().getTime();

        function update() {
            GetData1();

            setTimeout(update, updateInterval);
        }

        update();
});