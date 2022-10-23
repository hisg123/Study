let target = document.querySelector("#dynamic");
function blink(){
    target.classList.toggle("active");
}
setInterval(blink, 500);