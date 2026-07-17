//Terminates the pywebview miniplayer
const destroy = document.getElementById("destroy");
destroy.addEventListener("click", function() {
    destroy.style.color = "white";
    pywebview.api.destroy();
});

//Handles Close Button Logic - only shows the button when hovered over the miniplayer
document.addEventListener('mouseenter', function() {
    destroy.style.visibility = "visible";
})
document.addEventListener('mouseleave', function() {
    destroy.style.visibility = "hidden";
})


//Fire & HP Logic
const fire = document.getElementById("fire");
function state(health) {
    document.getElementById("dead").innerHTML = health + " HP";

    if (health >= 80 && health <= 100) {
        fire.style.transition = "filter 2s";
        fire.style.filter = "saturate(2.3)";
    }
    if (health < 80 && health >= 60) {
        fire.style.transition = "filter 2s";
        fire.style.filter = "saturate(1.5) blur(3px)";
    }
    if (health < 60 && health >= 30) {
        fire.style.transition = "filter 2s";
        fire.style.filter = "blur(5px) brightness(0.7)";
    }
    if (health < 30 && health >= 1) {
        fire.style.transition = "filter width height 2s";
        fire.style.filter = "blur(6px) brightness(0.4)";
        fire.style.maxWidth = "70%";
        fire.style.maxHeight = "70%";
    }
    if (health < 1) {
        document.body.style.backgroundColor = "rgb(92, 92, 92)"
        fire.src = "fire-dead.gif"
        fire.style.marginTop = "130px"
        fire.style.filter = "saturate(0.5)"
        document.getElementById("dead").innerHTML = "DEAD";
    }
}

function survived() {
    document.getElementById("dead").innerHTML = "SURVIVED";
}