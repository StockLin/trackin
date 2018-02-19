$(document).ready(function(){
var lis = $('li[id^="content-"]').hide(),
    i = 0;

(function cycle() {

    lis.eq(i).fadeIn(500)
              .delay(3000)
              .fadeOut(500, cycle);

    i = ++i % lis.length;

})();

});
