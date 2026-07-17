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

