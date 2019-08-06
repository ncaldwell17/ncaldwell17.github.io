function fadeInPage() {
    if (!window.AnimationEvent) { return; }
    var fader = document.getElementById('fader');
    fader.classList.add('fade-out');
}

function launchBlog() {
    var central = document.getElementById("ccc");
    var blog = document.getElementById("bbb");
    
    central.style.display = "none";
    blog.style.display = "block";
}