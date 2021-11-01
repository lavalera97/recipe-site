$(document).ready(function () {

    ChangeSearch();

    $(window).resize(function () {
        ChangeSearch();
    });

    function ChangeSearch() {
        var bodyWidth = $('body').width();
        $(window).scroll(function() {
            if (bodyWidth <= 700) {
                $('.search-form').css('display', 'none');
             }
            else if ($(this).scrollTop()> 10) {
                $('.search-form').css('display', 'block');
             }
            else {
              $('.search-form').css('display', 'none');
             }
         });
        }
});