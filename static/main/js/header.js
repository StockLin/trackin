$(document).ready(function(){
  $(window).bind('scroll', function() {

// navbar區塊
    if ($(window).scrollTop() > 1) {
      $('.navbar_center').css('background-color', 'rgba(40, 47, 68, 1)');
      $('.rest_day_alert p').css('background-color', 'rgba(40, 47, 68, 1)');
      $('.hambg_sidebar').css('background-color', 'rgba(40, 47, 68, 1)');
    }else{
      $('.navbar_center').css('background-color', 'rgba(40, 47, 68, 0)');
      $('.rest_day_alert p').css('background-color', 'rgba(40, 47, 68, 0)');
      $('.hambg_sidebar').css('background-color', 'rgba(40, 47, 68, 0)');
    }
});
// 剩餘天數區塊
$('.rest_day_alert').css('right', 'calc((100% - ' + $('.container').innerWidth() + 'px) / 2)');
$(window).resize(function(){
$('.rest_day_alert').css('right', 'calc((100% - ' + $('.container').innerWidth() + 'px) / 2)');
});

//hambg sidebar區塊
var func_nav = function(){
  var hambg_icon_show = true;

if ($(window).width() < 960){
  $('.navbar_sec').css('display', 'none');
  $('.hambg_sidebar').css('display', 'block');
  $('.hambg_icon').click(function(){
    if (hambg_icon_show == true){
      $('.nav_bg').css('background-color', '#282F44');
      $('.hambg_icon').css('padding', '30px 20px');
      $('.hambg_icon').css('padding', '30px 20px');
      $('.line1').css('transform', 'rotate(45deg)');
      $('.line1').css('position', 'absolute');
      $('.line2').css('display', 'none');
      $('.line3').css('transform', 'rotate(-45deg)');
      $('.line3').css('position', 'absolute');
      $('.hambg_items').css('display', 'block');
      $('.hambg_items').css('animation', '1s cover_fullpg both');
      hambg_icon_show = false;
    }else{
      $('.nav_bg').css('background-color', '');
      $('.hambg_icon').css('padding', '20px');
      $('.line1').css('transform', 'rotate(0deg)');
      $('.line1').css('position', 'relative');
      $('.line2').css('display', 'block');
      $('.line3').css('transform', 'rotate(0deg)');
      $('.line3').css('position', 'relative');
      $('.hambg_items').css('animation', '1s close_fullpg');
      $('.hambg_items').css('display', 'none');
      hambg_icon_show = true;
    }
  });
}else{
  $('.hambg_sidebar').css('display', 'none');
  $('.navbar_sec').css('display', 'block');
}
}
$(window).ready(func_nav);
$(window).resize(func_nav);
$('.hambg_dropdown').click(function(e){
  e.preventDefault();
  // $(this).parent().find('.hambg_sub_items');
  $('.hambg_sub_items').toggle(1000);
});

});
