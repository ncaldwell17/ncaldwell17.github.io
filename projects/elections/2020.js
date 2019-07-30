function fadeInPage() {
    if (!window.AnimationEvent) { return; }
    var fader = document.getElementById('fader');
    fader.classList.add('fade-out');
}

function rollBiden() {
    var bigB = document.getElementById("Biden");
    var littleB = document.getElementById("Buttigeig");
    var w = document.getElementById("Warren");
    var k = document.getElementById("Kamala");
    var bb = document.getElementById("Bernie");
    var bigBprof = document.getElementById("Biden-profile")
    
    bigB.style.animation = "roll 2s";
    bigB.style.width = '100%';
    littleB.style.display = "none";
    w.style.display = "none";
    k.style.display = "none";
    bb.style.display = "none";
    bigBprof.style.display = "block";
}

function rollWarren() {
    var bigB = document.getElementById("Biden");
    var littleB = document.getElementById("Buttigeig");
    var w = document.getElementById("Warren");
    var k = document.getElementById("Kamala");
    var bb = document.getElementById("Bernie");
    var wProf = document.getElementById("Warren-profile");
    
    w.style.animation = "rollWarren 2s";
    w.style.width = '100%';
    littleB.style.display = "none";
    bigB.style.display = "none";
    k.style.display = "none";
    bb.style.display = "none";
}

function rollButt() {
    var bigB = document.getElementById("Biden");
    var littleB = document.getElementById("Buttigeig");
    var w = document.getElementById("Warren");
    var k = document.getElementById("Kamala");
    var bb = document.getElementById("Bernie");
    var littleBProf = document.getElementById("Warren-profile");
    
    littleB.style.animation = "rollButt 2s";
    bigB.style.display = "none";
    w.style.display = "none";
    k.style.display = "none";
    bb.style.display = "none";
    
    littleB.style.width = '100%';
    littleB.style.backgroundImage = 'none';
    littleB.style.backgroundColor = 'teal';
    littlB.style.opacity = '0.7';
}
function rollKamala() {
    var bigB = document.getElementById("Biden");
    var littleB = document.getElementById("Buttigeig");
    var w = document.getElementById("Warren");
    var k = document.getElementById("Kamala");
    var bb = document.getElementById("Bernie");
    var kProf = document.getElementById("Kamala-profile");
    
    k.style.animation = "rollKamala 2s";
    littleB.style.display = "none";
    bigB.style.display = "none";
    w.style.display = "none";
    bb.style.display = "none";
    
    k.style.width = '100%';
    k.style.backgroundImage = 'none';
    k.style.backgroundColor = 'dodgerblue';
    k.style.opacity = '0.7';
}
function rollSanders() {
    var bigB = document.getElementById("Biden");
    var littleB = document.getElementById("Buttigeig");
    var w = document.getElementById("Warren");
    var k = document.getElementById("Kamala");
    var bb = document.getElementById("Bernie");
    var bbProf = document.getElementById("Bernie-profile");
    
    bb.style.animation = "rollSanders 2s";
    littleB.style.display = "none";
    bigB.style.display = "none";
    k.style.display = "none";
    w.style.display = "none";
    
    bb.style.width = '100%';
    
    bb.style.fontSize = '50px';
    bb.style.textDecoration = 'underline';
}
































