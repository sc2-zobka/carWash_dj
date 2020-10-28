
let menu = document.getElementById("menu")
//let header = document.getElementById("header")
let header = document.getElementsByTagName("header")[0]
//let nav = document.getElementById("nav")
let nav = document.getElementsByTagName("nav")[0]

menu.addEventListener("click", function() {
    
    if(header.style.height == "60px" || header.offsetHeight == 60) {
        header.style.height = 60 + nav.offsetHeight + "px"
    } else {
        header.style.height = "60px"
    }
})

window.addEventListener("resize", function() {
    let ancho = document.documentElement.clientWidth

    if(ancho > 480) {
        header.style = "none"
    }

})