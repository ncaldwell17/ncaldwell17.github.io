/* exported fadeInPage */
/* exported togAdmin */
/* global document */
/* global $ */
/* global window */

function fadeInPage() {
    if (!window.AnimationEvent) { return; }
    var fader = document.getElementById('fader');
    fader.classList.add('fade-out');
}

function togAdmin(name) {
    var strname = document.getElementById(name);
    var iconname = document.getElementById(name+'Icon');
    if (strname.style.display === 'none') {
        $(strname).slideToggle(600)
        strname.style.display = 'block';
        $(iconname).removeClass('fa-plus').addClass('fa-minus');
    }
    else {
        strname.style.display = 'none';
        $(iconname).removeClass('fa-minus').addClass('fa-plus');
    }
}