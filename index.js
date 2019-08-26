/* exported fit_to_view */
/* global document */
function fit_to_view(pHeight, idName) {
    var element = document.getElementById(idName);
    element.style.height = pHeight;
    /* Keep for posterity
    for(var i = 0, length = elements.length; i < length; i++) {
        elements[i].style.height = pHeight;
    }
    */
}