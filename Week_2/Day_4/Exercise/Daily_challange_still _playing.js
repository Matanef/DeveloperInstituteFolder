let wordListArr = []
for (let i = 0; i <= 3; i++)
wordListArr.push(prompt("Please enter a word"))
console.log(wordListArr)
console.log(wordListArr.join(", "))
		 let brk = wordListArr.split('~')
         let res = brk.join(" <br> ")
         console.log("<br><br>"+res);