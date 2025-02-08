//<script>
    var password = document.getElementbyId("password");
    var letter = document.getElementbyId("letter");
    var capital = document.getElementbyId("capital");
    var num = document.getElementbyId("number");
    var length = document.getElementbyId("length");

    userInput.onfocus = function() {
        document.getElementbyId("password").style.display = "block"
        } 

    userInput.onfocus = function(){
        document.getElementbyId("password").style.display = "none"
    }

var numbers = /[0-9]/g;
if(userInput.value.match(upperCase)){
    num.classList.remove("invalid");
    num.classList.add("valid");
} else{
    num.classList.add("invalid");
    num.classList.remove("valid");
}

var upperCase = /[A-Z]/g;
if(userInput.value.match(upperCase)){
    letter.classList.remove("invalid");
    letter.classList.add("valid");
} else{
    letter.classList.add("invalid");
    letter.classList.remove("valid");
}

if(userInput.value.length >= 8){

    if(userInput.value.match(upperCase)){
        length.classList.remove("invalid");
        length.classList.add("valid");
    } else{
        length.classList.add("invalid");
        length.classList.remove("valid");
    }

}






//</script>