function reset_active(id1, id2, id3, id4) {
    var first = document.getElementById(id1);
    var second = document.getElementById(id2);
    var third = document.getElementById(id3);
    var fourth = document.getElementById(id4);
    first.classList.remove('active2');
    second.classList.remove('active2');
    third.classList.remove('active2');
    fourth.classList.remove('active2');
}

function reset_display(d1, d2, d3) {
    var first = document.getElementById(d1);
    var second = document.getElementById(d2);
    var third = document.getElementById(d3)
    first.style.display = 'none';
    second.style.display = 'none';
    third.style.display = 'none';
}

function flip(target, activate) {
    var toTog = document.getElementById(target);
    var toAct = document.getElementById(activate);
    toTog.style.display = 'block';
    toAct.classList.add('active2');
}

function toggle(id_name) {
    var tar = document.getElementById(id_name);
    tar.style.display = 'block';
}