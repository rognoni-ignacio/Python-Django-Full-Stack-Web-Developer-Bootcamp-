// Restart Game Button
var restart = document.querySelector('#b');

// Grab all the squares
var squares = document.querySelectorAll("td");

// Starting Player
var currentPlayer = getStartingPlayer();
changeCurrentPlayerLabel();

//Get Starting player randomly
function getStartingPlayer(){
  var randomPlayer = Math.floor((Math.random() * 2) + 1);
  if(randomPlayer == 1){
    return 'X';
  }
  else{
    return 'O';
  }
}

//Print Current Player
function changeCurrentPlayerLabel() {
  document.getElementById('currentPlayerLabel').textContent = "Current Player: " + currentPlayer;
};

// Clear Squares Function
function clean() {
  for (var i = 0; i < squares.length; i++) {
      squares[i].textContent = '';
  }
  currentPlayer = getStartingPlayer();
  changeCurrentPlayerLabel();
}

//Assign Clean function on click
restart.addEventListener('click', clean);

// Create a function that will check the square marker
function changeMarker(){
    if(this.textContent === ''){
      this.textContent = currentPlayer;
      changeCurrentPlayer();
    }
};

function changeCurrentPlayer(){
  if(currentPlayer === 'X'){
    currentPlayer = 'O';
  }else{
    currentPlayer = 'X';
  }
  changeCurrentPlayerLabel();
}

// Use a for loop to add Event listeners to all the squares
for (var i = 0; i < squares.length; i++) {
    squares[i].addEventListener('click', changeMarker);
}
