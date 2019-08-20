function fadeInPage() {
    if (!window.AnimationEvent) { return; }
    var fader = document.getElementById('fader');
    fader.classList.add('fade-out');
}

const element = document.querySelector('#myHeader')
element.classList.add('animated', 'bounceOutLeft')

element.addEventListener('animationend', function () {
    // do something
})

function animateCSS(element, fadeIn, callback) {
    const node = document.querySelector(element)
    node.classList.add('.animated', 'fadeIn')
    
    function handleAnimationEnd() {
        node.classList.remove('animated', fadeIn)
        node.removeEventListener('animationend', handleAnimationEnd)
        
        if (typeof callback === 'function') callback()
    }
    
    node.addEventListener('animationend', handleAnimationEnd)
}