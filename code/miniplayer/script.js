const destroy = document.getElementById("destroy");
destroy.addEventListener("click", function() {
    destroy.style.color = "white";
    pywebview.api.destroy();
});