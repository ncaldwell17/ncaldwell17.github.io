/* exported fadeInPage */
/* exported fitHeight */
/* exported vanish */
/* global document */
/* global window */
/* global $ */

function fadeInPage() {
    if (!window.AnimationEvent) { return; }
    var fader = document.getElementById('fader');
    fader.classList.add('fade-out');
}

function fitHeight() {
    var h = String(window.innerHeight)+'px';
    document.getElementById('main').style.height = h;
}

function vanish() {
    $("#main").addClass("hidden");
}