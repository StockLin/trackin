  $(document).ready(function(){
  $(window).bind('scroll', function() {

    if ($(window).scrollTop() > 1) {
      $('.navbar_center').css('background-color', 'rgba(40, 47, 68, 1)');
      $('.rest_day_alert p').css('background-color', 'rgba(40, 47, 68, 1)');
    }else{
      $('.navbar_center').css('background-color', 'rgba(40, 47, 68, 0)');
      $('.rest_day_alert p').css('background-color', 'rgba(40, 47, 68, 0)');
    }
});


  $('.rest_day_alert').css('right', 'calc((100% - ' + $('.container').innerWidth() + 'px) / 2)');
$(window).resize(function(){
  $('.rest_day_alert').css('right', 'calc((100% - ' + $('.container').innerWidth() + 'px) / 2)');
});

});
