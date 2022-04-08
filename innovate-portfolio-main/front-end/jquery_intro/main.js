
$(document).ready(function(){

    $("#change-colour").click(function(){
        $("h1").toggleClass("red-title");
    });
    $("#hide-text").click(function(){
        $("p").toggle();
    });
    $("#activate-dark-mode").click(function(){
        $("body").toggleClass("dark-mode");
    });

});

// vanilla js for comparison

console.log("Hello World!");

function displayDate(id) {
    document.getElementById("date").innerHTML = Date();
}