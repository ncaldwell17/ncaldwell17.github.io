/* exported fit_to_view */
/* exported toggleResume */
/* exported toggleResume2 */
/* exported toggleResume3 */
/* global document */

function toggleResume() {
    var ig1 = document.getElementById("ig1Content");
    var ig2 = document.getElementById("ig2Content");
    var ig3 = document.getElementById("ig3Content");
    var about = document.getElementById("textContent");
    if (about.style.display === "block") {
        about.style.display = "none";
        ig1.style.display = "block";
    }
    else if (ig2.style.display === "block") {
        ig2.style.display = "none";
        ig1.style.display = "block";
    }
    else if (ig3.style.display === "block") {
        ig3.style.display = "none";
        ig1.style.display = "block";
    }
    else {
        ig1.style.display = "none";
        about.style.display = "block";
    }
}
function toggleResume2() {
    var ig1 = document.getElementById("ig1Content");
    var ig2 = document.getElementById("ig2Content");
    var ig3 = document.getElementById("ig3Content");
    var about = document.getElementById("textContent");
    if (about.style.display === "block") {
        about.style.display = "none";
        ig2.style.display = "block";
    }
    else if (ig1.style.display === "block") {
        ig1.style.display = "none";
        ig2.style.display = "block";
    }
    else if (ig3.style.display === "block") {
        ig3.style.display = "none";
        ig2.style.display = "block";
    }
    else {
        ig2.style.display = "none";
        about.style.display = "block";
    }
}
function toggleResume3() {
    var ig1 = document.getElementById("ig1Content");
    var ig2 = document.getElementById("ig2Content");
    var ig3 = document.getElementById("ig3Content");
    var about = document.getElementById("textContent");
    if (about.style.display === "block") {
        about.style.display = "none";
        ig3.style.display = "block";
    }
    else if (ig2.style.display === "block") {
        ig2.style.display = "none";
        ig3.style.display = "block";
    }
    else if (ig1.style.display === "block") {
        ig1.style.display = "none";
        ig3.style.display = "block";
    }
    else {
        ig3.style.display = "none";
        about.style.display = "block";
    }
}

function fit_to_view(pHeight, idName) {
    var element = document.getElementById(idName);
    element.style.height = pHeight;
    /* Keep for posterity
    for(var i = 0, length = elements.length; i < length; i++) {
        elements[i].style.height = pHeight;
    }
    */
}