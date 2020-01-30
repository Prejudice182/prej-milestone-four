($ => {
    // Add active class to current page link
    $('nav a').parents('li,ul').removeClass('active');
    $('a[href="' + this.location.pathname + '"]').parents('li,ul').addClass('active');

    // Add sr-only to current page
    $('.sr-only').remove()
    $('a[href="' + this.location.pathname + '"]').append('<span class="sr-only">(current)</span>')
})(jQuery);