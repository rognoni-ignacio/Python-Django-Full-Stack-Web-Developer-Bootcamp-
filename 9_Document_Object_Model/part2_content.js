var x = document.querySelector("p");

// Show Text
x.textContent;
console.log("Text Content: " + x.textContent);

// Reassign Text
x.textContent = "new";
console.log("Reassing Text: " + x.textContent);

// Refresh the page
// Show actual HTML
x.innerHTML
console.log("Inner HTML: " + x.innerHTML);

// Edit HTML
x.innerHTML = "This is <strong>BOLD</strong>"
console.log(x.innerHTML);

// Can't do that with just textContent


// Attributes //

var special = document.querySelector("#special");
var specialA = special.querySelector("a");

specialA.getAttribute("href");
console.log(specialA.getAttribute("href"));

specialA.setAttribute("href","https://www.amazon.com");
