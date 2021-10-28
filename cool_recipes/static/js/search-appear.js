$(window).scroll(function() {
    if ($(this).scrollTop()> 40) {
        $('.search-form').css('display', 'block');
     }
    else {
      $('.search-form').css('display', 'none');
     }
 });