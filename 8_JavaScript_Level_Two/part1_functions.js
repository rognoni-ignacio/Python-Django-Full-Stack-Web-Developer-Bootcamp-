function hello(){
    console.log("hello world!");
}

hello();


function helloYou(name){
    console.log("hello " + name);
}

helloYou("Ignacio");

function addNum(num1, num2){
    console.log(num1 + num2);
}
addNum(30,20)

//Functions with default value
function helloSomeone(name="Ignacio"){
    console.log("Hello " + name);
}

helloSomeone();


// Returning Values //
// Without Return
function formal(name="Sam",title="Sir"){
    console.log(title + " " + name);
}

//
"Welcome " + formal();
// Welcome undefined


// With a return
function formal(name="Sam", title="Sir"){
    return title + "  " + name;
}

"Welcome " + formal();

var result = formal();


// SCOPE //////////
// Scope is the term we use to describe how objects and variable get defined
// within JavaScript. When discussing scope with functions, as a general rule we
// can say that if a variable is defined only inside a function than its scope is
// limited to that function. For example, consider the following function:

// Multiplies input by 5
function times5(numInput) {
  var result = numInput * 5;
  return result;
}

times5(5);

// Now after running the function try calling:
//numInput // Error
//result // Error

// Not defined outside the scope of the function!

// These errors indicate that these variables are only defined inside the scope of
// the function. So variables defined inside of a function are only defined
// (or redefined) inside of that function. However, variables assigned outside of
// the function are global variables, and the function will have access to them
// due to their scope. For example:

var v = "Global V";
var stuff = "I'm global stuff"

function fun(stuff){
    console.log(v);
    stuff = "Reassign stuff inside func";
    console.log(stuff);
}

// Now see what happens!
fun()

// So what is happening above? The following happens
// console.log(v); will check for the global variable v, the outer scope
// console.log(stuff); will also check for the global variable stuff
// fun(stuff) will accept an argument stuff, print out v, and then reassign stuff
// (in the scope of the function) and print out stuff.
//
// Notice two things:
//
// The reassignment of stuff only effects the scope
// of the stuff variable inside the function
//
// The fun function first checks to see if v is defined
// at the function scope, if not (which was the case) it
// will then search the global scope for a variable names v,
// leading to it printing out "I'm global v".

// Okay! Now you are ready to tackle some actual exercise problems!
