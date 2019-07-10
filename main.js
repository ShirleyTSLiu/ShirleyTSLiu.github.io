document.querySelector('html').onclick = function() {
    alert('Ouch! Stop poking me!');
}

var myImage = document.querySelector('img');

myImage.onclick = function() {
    var mySrc = myImage.getAttribute('src');
    if(mySrc === 'images/images.jpg') {
      myImage.setAttribute ('src','images/im2.jpg');
    } else {
      myImage.setAttribute ('src','images/images.jpg');
    }
}
var myButton = document.querySelector('button');
var myHeading = document.querySelector('h1');

function setUserName() {
    var myName = prompt('Please enter your name.');
    localStorage.setItem('name', myName);
    myHeading.innerHTML = 'The website is cool, ' + myName;
  }

if(!localStorage.getItem('name')) {
    setUserName();
  } else {
    var storedName = localStorage.getItem('name');
    myHeading.innerHTML = 'The website is cool, ' + storedName;
  }
myButton.onclick = function() {
    setUserName();
  }