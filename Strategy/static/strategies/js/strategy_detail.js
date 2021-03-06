var radar_func = function(){

  // 偵測、設置radar_chart_sec的高度與寬度一樣
  $('.radar_chart_sec').css('height', $('.radar_chart_sec').width() + 'px');

  // 雷達圖區塊
  (function($){
	$.fn.radar_chart = function(options){
		var settings = $.extend({

      // 雷達圖顯示資料座標顏色
			colors: [
				'#85734a',
			],

      // 座標線條寬度、顏色
			lineWidth: 2,
			lineColor: 'rgba(0,0,0,0.2)',
      // 座標標題顏色
			textColor: '#282F44'
		}, options);

		$(this).each(function(){
			var table = this;

			if(table.tagName.toUpperCase() == 'TABLE'){
				table.radar = {
					attributes: [],
					records: []
				}

				// add all the attributes
				$(table).find('thead th, thead td').each(function(){
					table.radar.attributes.push(this.innerHTML);
				});

				// add all the values
				$(table).find('tbody tr').each(function(){
					var record = {};
					var $tds = $(this).find('td');

					var i = 0;

					$tds.each(function(){
						record[i] = parseFloat(this.innerHTML);
						i++;
					});

					table.radar.records.push(record);
				});

				// set up the canvas
				table.radar.canvas = document.createElement('canvas');

        // 雷達圖canvas的寬高
				table.radar.canvas.width = $('.radar_chart_sec').width();
				table.radar.canvas.height = $('.radar_chart_sec').height();
        $(window).resize(function(){
          table.radar.canvas.width = $('.radar_chart_sec').width();
          table.radar.canvas.height = $('.radar_chart_sec').height();
        });

				table.radar.ctx = table.radar.canvas.getContext('2d');

				radar_redraw(table);

        // 插入canvas畫布
				$(table.radar.canvas).insertAfter(table);
        // 將表格藏起來
				$(table).hide();
			}
		});

		function radar_redraw(table){
			if(table.radar.ctx){
				table.radar.ctx.clearRect(0, 0, table.radar.canvas.width, table.radar.canvas.height);

				var geometry = {
					centre: {
            // 雷達圖於canvas畫布的位置
						x: table.radar.canvas.width / 2,
						y: table.radar.canvas.height / 2
					},

          // 雷達圖座標軸的長、寬度
					radius: Math.min(table.radar.canvas.width / 3.5, table.radar.canvas.height / 3.5),
					text_radius: Math.min(table.radar.canvas.width / 3.2, table.radar.canvas.height / 3.2)
				};

				// grid
				table.radar.ctx.beginPath();

				for(var i = 0; i < 360; i+=(360 / table.radar.attributes.length)){
					var angle = 90 - i;

					table.radar.ctx.moveTo(geometry.centre.x, geometry.centre.y);
					table.radar.ctx.lineWidth = settings.lineWidth;
					table.radar.ctx.strokeStyle = settings.lineColor;
					table.radar.ctx.lineTo(geometry.centre.x + geometry.radius * Math.cos(angle * Math.PI / 180), geometry.centre.y - geometry.radius * Math.sin(angle * Math.PI / 180));
				}

        // 決定雷達圖會有幾圈
				var segments = 3;

				for(var a = 1; a <= segments; a++){
					table.radar.ctx.moveTo(geometry.centre.x + (geometry.radius / segments * a) * Math.cos(90 * Math.PI / 180), geometry.centre.y - (geometry.radius / segments * a) * Math.sin(90 * Math.PI / 180));

					for(var i = 0; i <= 360; i+=(360 / table.radar.attributes.length)){
						var angle = 90 - i;
						table.radar.ctx.lineTo(geometry.centre.x + (geometry.radius / segments * a) * Math.cos(angle * Math.PI / 180), geometry.centre.y - (geometry.radius / segments * a) * Math.sin(angle * Math.PI / 180));
					}
				}

        // 畫出雷達圖座標軸線
				table.radar.ctx.stroke();

				// data
				table.radar.ctx.globalCompositeOperation = 'multiply';

				for(var r in table.radar.records){
					table.radar.ctx.beginPath();

					for(var i in table.radar.records[r]){
						var angle = 90 - (360 / table.radar.attributes.length * i);

						if(i == 0){
							table.radar.ctx.moveTo(geometry.centre.x + (geometry.radius * table.radar.records[r][i] / 100) * Math.cos(angle * Math.PI / 180), geometry.centre.y - (geometry.radius * table.radar.records[r][i] / 100) * Math.sin(angle * Math.PI / 180));
						}else{
							table.radar.ctx.lineTo(geometry.centre.x + (geometry.radius * table.radar.records[r][i] / 100) * Math.cos(angle * Math.PI / 180), geometry.centre.y - (geometry.radius * table.radar.records[r][i] / 100) * Math.sin(angle * Math.PI / 180));
						}
					}

					var t = r;
					while(t >= settings.colors.length){
						t -= settings.colors.length;
					}

					table.radar.ctx.fillStyle = settings.colors[t];
					table.radar.ctx.fill();
				}

				table.radar.ctx.globalCompositeOperation = 'source-over';

				// text

				table.radar.ctx.font = 'normal normal 600 14px 微軟正黑體';
				table.radar.ctx.textAlign = 'center';
				table.radar.ctx.textBaseline = 'middle';
				table.radar.ctx.fillStyle = settings.textColor;

				for(var i in table.radar.attributes){
					var angle = 90 - (360 / table.radar.attributes.length * i);
					if(angle < 0){ angle+=360; }

					var dx = geometry.text_radius * Math.cos(angle * Math.PI / 180);
					var dy = geometry.text_radius * Math.sin(angle * Math.PI / 180);

					if(angle <= 80){
						table.radar.ctx.textAlign = 'left';
					}else if(angle <= 100){
						table.radar.ctx.textAlign = 'center';
					}else if(angle <= 260){
						table.radar.ctx.textAlign = 'right';
					}else if(angle <= 280){
						table.radar.ctx.textAlign = 'center';
					}else {
						table.radar.ctx.textAlign = 'left';
					}

					table.radar.ctx.fillText(table.radar.attributes[i].toUpperCase(), geometry.centre.x + dx, geometry.centre.y - dy);
				}
			}
		}
	};

$(document).ready(function(){
    $('.radar-chart').radar_chart();
  });
})(window.jQuery);
// 雷達圖區塊結束
}
$(document).ready(radar_func);
$(window).resize(function(){
  $('canvas').remove();
});
$(window).resize(radar_func);

$(document).ready(function(){
  $('.like_btn').click(function(){
      $('.like_btn span').toggleClass('glyphicon-heart-empty glyphicon-heart');
  });

  if ($(window).width() < 960){
    $('.strate_detail').css('height', 'calc(' + ($('.strate_detail').width() * 2) + 'px)');
    $('.strate_content').css('height', $('.radar_chart_sec').width());
  }else{
    $('.strate_detail').css('height', 'calc(' + ($('.strate_detail').width() / 2) + 'px)');
    $('.strate_content').css('height', $('.radar_chart_sec').width());
  }

  if ($('.strate_content').width() < 480){
    $('.strate_attr').css('font-size', '15px');
    $('.strate_attr').css('margin-top', '15px');
    $('.data_table_sec').css('padding', '10px 25px');
    $('.table_row').css('margin-bottom', '5px');
    $('.table_head').css('font-size', '15px');
    $('.table_head').css('padding', '3px 25px');
    $('.table_data').css('font-size', '15px');
    $('.table_data').css('padding', '3px 25px');
    $('.strate_explain_title').css('font-size', '18px');
  }else{
    $('.strate_attr').css('font-size', '18px');
    $('.strate_attr').css('margin-top', '25px');
    $('.data_table_sec').css('padding', '15px 25px');
    $('.table_row').css('margin-bottom', '10px');
    $('.table_head').css('font-size', '18px');
    $('.table_head').css('padding', '8px 25px');
    $('.table_data').css('font-size', '18px');
    $('.table_data').css('padding', '8px 25px');
    $('.strate_explain_title').css('font-size', '22px');
  }



  $('.strate_explain_title').click(function(){
    $('.strate_explain_title span').toggleClass('glyphicon-triangle-bottom glyphicon-triangle-top');
    $('.strate_explain').toggleClass('strate_explain_c strate_explain_o');
    if ($('.strate_explain_title').css('color') == 'rgb(230, 175, 46)'){
      $('.strate_explain_title').css('color', 'rgb(40, 47, 68)');
      $('.strate_explain p').css('display', 'block');
    }else{
      $('.strate_explain_title').css('color', 'rgb(230, 175, 46)');
      $('.strate_explain p').css('display', 'none');
    }
  });


  $(window).resize(function(){
    if ($(window).width() < 960){
      $('.strate_detail').css('height', 'calc(' + ($('.strate_detail').width() * 2) + 'px)');
      $('.strate_content').css('height', $('.radar_chart_sec').width());
    }else{
      $('.strate_detail').css('height', 'calc(' + ($('.strate_detail').width() / 2) + 'px)');
      $('.strate_content').css('height', $('.radar_chart_sec').width());
    }

    if ($('.strate_content').width() < 480){
      $('.strate_attr').css('font-size', '15px');
      $('.strate_attr').css('margin-top', '15px');
      $('.data_table_sec').css('padding', '10px 25px');
      $('.table_row').css('margin-bottom', '5px');
      $('.table_head').css('font-size', '15px');
      $('.table_head').css('padding', '3px 25px');
      $('.table_data').css('font-size', '15px');
      $('.table_data').css('padding', '3px 25px');
      $('.strate_explain_title').css('font-size', '18px');
    }else{
      $('.strate_attr').css('font-size', '18px');
      $('.strate_attr').css('margin-top', '25px');
      $('.data_table_sec').css('padding', '15px 25px');
      $('.table_row').css('margin-bottom', '10px');
      $('.table_head').css('font-size', '18px');
      $('.table_head').css('padding', '8px 25px');
      $('.table_data').css('font-size', '18px');
      $('.table_data').css('padding', '8px 25px');
      $('.strate_explain_title').css('font-size', '22px');
    }
  });


});








$(".btn-warning").click(function(){
    alert('你的會員等級不足是否升級!');
    // swal({
    //   title: "Are you sure?",
    //   text: "You will not be able to recover this imaginary file!",
    //   type: "warning",
    //   showCancelButton: true,
    //   confirmButtonColor: "#DD6B55",
    //   confirmButtonText: "Yes, delete it!",
    //   cancelButtonText: "No, cancel plx!",
    //   closeOnConfirm: false,
    //   closeOnCancel: false
    // },
    // function(isConfirm){
    //   if (isConfirm) {
    //     swal("Deleted!", "Your imaginary file has been deleted.", "success");
    //   } else {
    //     swal("Cancelled", "Your imaginary file is safe :)", "error");
    //   }
    // });

});