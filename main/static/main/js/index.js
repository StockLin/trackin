$(document).ready(function(){
  var mode = 0;

  $(window).on('wheel', function(e) {

    var delta = e.originalEvent.deltaY;

    if (delta > 0){
      // down
      if(mode>=0 && mode < 4){
        mode = mode + 1;
      }else{
        mode = 0;
      }
      if(mode == 0){
        $('.bg_1').css('display','block');
        $('.bg_1').css('animation','moveup 0.5s both');
        $('.text').css('animation','text_moveup 0.5s both');
        $('.bg_2').css('display','none');
        $('.bg_3').css('display','none');
        $('.bg_4').css('display','none');
        $('.bg_end').css('display','none');
      }else if(mode == 1){
        $('.bg_1').css('display','none');
        $('.bg_2').css('display','block');
        $('.bg_2').css('animation','moveup 0.5s both');
        $('.text').css('animation','text_moveup 0.5s both');
        $('.bg_3').css('display','none');
        $('.bg_4').css('display','none');
        $('.bg_end').css('display','none');
      }else if(mode == 2){
        $('.bg_1').css('display','none');
        $('.bg_2').css('display','none');
        $('.bg_3').css('display','block');
        $('.bg_3').css('animation','moveup 0.5s both');
        $('.text').css('animation','text_moveup 0.5s both');
        $('.bg_4').css('display','none');
        $('.bg_end').css('display','none');
      }else if(mode == 3){
        $('.bg_1').css('display','none');
        $('.bg_2').css('display','none');
        $('.bg_3').css('display','none');
        $('.bg_4').css('display','block');
        $('.bg_4').css('animation','moveup 0.5s both');
        $('.text').css('animation','text_moveup 0.5s both');
        $('.bg_end').css('display','none');
      }else{
        $('.bg_1').css('display','none');
        $('.bg_2').css('display','none');
        $('.bg_3').css('display','none');
        $('.bg_4').css('display','none');
        $('.bg_end').css('display','block');
        $('.bg_end').css('animation','moveup 0.5s both');
      }

    }
    else{
      //up
      if(mode>0 && mode <= 4){
        mode = mode - 1;
      }else{
        mode = 4;
      }
      if(mode == 0){
        $('.bg_1').css('display','block');
        $('.bg_1').css('animation','movedown 0.5s both');
        $('.text').css('animation','text_movedown 0.5s both');
        $('.bg_2').css('display','none');
        $('.bg_3').css('display','none');
        $('.bg_4').css('display','none');
        $('.bg_end').css('display','none');
      }else if(mode == 1){
        $('.bg_2').css('display','block');
        $('.bg_2').css('animation','movedown 0.5s both');
        $('.text').css('animation','text_movedown 0.5s both');
        $('.bg_3').css('display','none');
        $('.bg_4').css('display','none');
        $('.bg_1').css('display','none');
        $('.bg_end').css('display','none');
      }else if(mode == 2){
        $('.bg_3').css('display','block');
        $('.bg_3').css('animation','movedown 0.5s both');
        $('.text').css('animation','text_movedown 0.5s both');
        $('.bg_1').css('display','none');
        $('.bg_2').css('display','none');
        $('.bg_4').css('display','none');
        $('.bg_end').css('display','none');
      }else if(mode == 3){
        $('.bg_1').css('display','none');
        $('.bg_2').css('display','none');
        $('.bg_3').css('display','none');
        $('.bg_4').css('display','block');
        $('.bg_4').css('animation','movedown 0.5s both');
        $('.text').css('animation','text_movedown 0.5s both');
        $('.bg_end').css('display','none');
      }else{
        $('.bg_1').css('display','none');
        $('.bg_2').css('display','none');
        $('.bg_3').css('display','none');
        $('.bg_4').css('display','none');
        $('.bg_end').css('display','block');
        $('.bg_end').css('animation','movedown 0.5s both');
      }

    }

    return false; // this line is only added so the whole page won't scroll in the demo
  });


});
