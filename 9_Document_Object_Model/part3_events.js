var headerOne = document.getElementById('hoverItem');
var headerTwo = document.getElementById('clickItem');
var headerThree = document.getElementById('doubleClickItem');

headerOne.addEventListener('mouseover', function(){
  headerOne.textContent = 'Mouse currently over!';
  headerOne.style.color = 'red';
});

headerOne.addEventListener('mouseout', function(){
  headerOne.textContent = 'Hover Me';
  headerOne.style.color = 'black';
});

var clicked = false;
headerTwo.addEventListener('click', function(){
  if(!clicked){
    headerTwo.textContent = 'Clicked!';
    headerTwo.style.color = 'red';
  }
  else{
    headerTwo.textContent = 'Click Me';
    headerTwo.style.color = 'black';
  }
  clicked = !clicked;
})

var doubleClicked = false;
headerThree.addEventListener('dblclick', function(){
  if(!doubleClicked){
    headerThree.textContent = 'Double Clicked!';
    headerThree.style.color = 'red';
  }
  else{
    headerThree.textContent = 'Double Click Me';
    headerThree.style.color = 'black';
  }
  doubleClicked = !doubleClicked;
})
