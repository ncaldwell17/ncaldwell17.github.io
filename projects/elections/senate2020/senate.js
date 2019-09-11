/* exported fadeInPage */
/* exported fitHeight */
/* exported vanish */
/* exported animatePolls */
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

/* make this flexible */ 
function animatePolls() {
    var jWidth = String(document.getElementById("jeanneBar").offsetWidth)+"px"; 
    var cWidth = String(document.getElementById("coreyBar").offsetWidth)+"px";
    $("#jeanneBar").animate({width: "0px"}, 0, 'linear');
    $("#coreyBar").animate({width: "0px"}, 0, 'linear');
    $("#jeanneBar").animate({width: jWidth}, 2500, 'linear');
    $("#coreyBar").animate({width: cWidth}, 2500, 'linear');
}