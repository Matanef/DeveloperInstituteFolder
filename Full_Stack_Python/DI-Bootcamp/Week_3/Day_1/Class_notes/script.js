let container = document.getElementById("container");
console.log(container)

let title = container.firstElementChild;
console.log(title)

// retrieve a list of all the h2
let secondTitles = document.getElementsByTagName("h2");
console.log(secondTitles)

let firstSecondTitle = secondTitles[0];
console.log(firstSecondTitle)

// retrieve a list of all the elements with the class wrapping
let wrapping = document.getElementsByClassName("wrapping");
console.log(wrapping)

// retrieving the element that has the id container
let containerQuerySelector = document.querySelector("#container")

// retrieving the elements that has the class container wrapping
let wrappingElements = document.querySelectorAll(".wrapping")

// retrieving the li inside the ul
let allLis = document.querySelectorAll("ul li");


//Add elements on the page

// 1. Retrieve where I want to add the element
let ulParent = document.getElementById("list");

//2. Create the new element - an element node
let liChild = document.createElement("li");

//3. Create a text  - a text node 
let textLi = document.createTextNode("Icon of my website");

//4. Add the text to the li
// parent.appendChild(child)
liChild.appendChild(textLi);

//5. Add the li to the ul
ulParent.appendChild(liChild);


// Retrieve all the h2 an change them with a specific style

let allH2 = document.getElementsByTagName("h2");
// let allH2 = document.querySelectorAll("h2");

// // allH2.classList.add("title") //
// // classList property only works ON an element
// // and here allH2 is not ONE element, it's a list of elements
// // allH2.style.color = "blue"; //impossible

for (let i = 0; i < allH2.length; i++){
	allH2[i].classList.add("title");
}

// Create 3 pictures on the page, each of them with a random
// source image

let pics = [
"https://idsb.tmgrup.com.tr/ly/uploads/images/2021/09/08/thumbs/800x531/142774.jpg",
"https://spca.co.il/wp-content/uploads/2021/11/dog.jpeg",
"https://i1.sndcdn.com/avatars-000570452091-updhur-t500x500.jpg"
];

// display them dynamicaly on the page

// Retrieve where we want to add the images
let section = document.getElementById("game");

function createImg(){

	for (let i = 0; i<pics.length; i++){
		let randomNumber = Math.floor(Math.random() * pics.length);
		// create an img
		let newImg = document.createElement("img");
		newImg.classList.add("animals");
		newImg.setAttribute("src", pics[randomNumber]);
		//append the image on the section
		section.appendChild(newImg);
	}
}

createImg();