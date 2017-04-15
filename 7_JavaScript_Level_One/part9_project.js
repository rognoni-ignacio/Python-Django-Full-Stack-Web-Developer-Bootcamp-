var firstName = prompt("Enter your first name:");

var lastName = prompt("Enter your Last Name:");

var age = prompt("How old are you?");

var height = prompt("How tall are you?");

var petName = prompt("What is the name of your pet?");

var nameCond = false
var ageCond = false
var heightCond = false
var petCond = false


if (firstName[0] === lastName[0]){
  nameCond = true;
}

if (age > 20 && age <30){
  ageCond = true;
}

if (height >= 170){
  heightCond = true;
}

if (petName[petName.length-1] === "y"){
  petCond = true;
}

if (nameCond && ageCond && heightCond && petCond){
  console.log("Welcome Comrade! You've passed the Spy Test")
}else{
  console.log("Sorry, nothing to see here.")
}
