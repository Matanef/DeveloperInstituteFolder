let tableElement = document.getElementById("sampleTable");
// console.log(tableElement);

let trElement = document.getElementsByTagName('tr')
console.log(trElement);
let tdElement = document.getElementsByTagName('td')
console.log(tdElement);

function insertRow (){
	let trElement = document.createElement('tr');
	let rowNum = document.getElementsByTagName("tr").length +1
	// let cellNum = document.getElementsByTagName("tr").length +1

	for (let i =0; i<2; i++){
		let tdElement = document.createElement("td");
		let cellNum = i +1
		let tdText = document.createTextNode(`Row${rowNum} cell${cellNum}`);
		tdElement.appendChild(tdText);
		trElement.appendChild(tdElement);
	}
	// let tableElement = document.querySelector("table");
	let tableElement = document.getElementById("sampleTable");
	tableElement.appendChild(trElement)
	console.log(tableElement);

	// let cellText = document.createTextNode
	// let tableFunc = document.getElementById("sampleTable");
	// let trFunc = document.getElementsByTagName('tr');
	// let tdElement = document.getElementsByTagName('td')
	// let tdText = document.createTextNode(`Row ${tdElement.length} cell1`)
};