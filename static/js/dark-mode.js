($ => {

const darkMode = (isDark) => {
    if (isDark.matches) {
        $('.navbar').removeClass('navbar-light bg-light').addClass('navbar-dark bg-dark');
        console.log('darkmode on');
    } else {
        $('.navbar').addClass('navbar-light bg-light').removeClass('navbar-dark bg-dark');
        console.log('darkmode off')
    }
};

let isDark = window.matchMedia('(prefers-color-scheme: dark)');

darkMode(isDark);

isDark.addListener(darkMode);

})(jQuery);