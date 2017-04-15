// PART 4 ARRAY EXERCISE

// Create Empty Student Roster Array
// This has been done for you!
var roster = [];

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew(){
  var newName = prompt("Enter new name");
  roster.push(newName);
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//
function remove(){
  var removeName = prompt("Enter name to delete");
  var index = roster.indexOf(removeName);
  roster.splice(index, 1);
}

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display(){
  console.log(roster);
}

// Start by asking if they want to use the web app

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
var start = prompt("Do you want to start the web app?");

var request = "";

if(start === 'Y' || start === 'y'){
  while(request !== 'quit'){
    request = prompt("Enter your request");
    if(request === 'add'){
      addNew();
    }
    else if(request === "remove"){
      remove();
    }
    else if(request === "display"){
      display();
    }
  }
}

alert("Thanks");
