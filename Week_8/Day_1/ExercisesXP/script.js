
// 🌟 Exercise 1 : Change the article


// Using a DOM property, retrieve the h1 and console.log it.

// Using DOM methods, remove the last paragraph in the <article> tag.

// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).

// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

// BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)

// BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)

let h1 = document.getElementsByTagName('h1')[0]

document.querySelector('p:last-child').remove()

let h2 = document.getElementsByTagName('h2')[0]

h2.addEventListener("click" , () => {h2.style.backgroundColor = 'red' })

let h3 = document.getElementsByTagName('h3')[0]

h3.addEventListener("click" , () => {h3.style.display = 'none'})

let htmlbutton = document.getElementsByTagName('button')[0]

let ps = document.getElementsByTagName('p')
ps = Array.from(ps)
htmlbutton.addEventListener("click" , () => {ps.forEach(p => {
    p.style.fontWeight = 'bold' 
});})

h1.addEventListener("mouseover" , () => {h1.style.fontSize = `${Math.random()*100}px`})


secondp = document.getElementsByTagName('p')[1]


secondp.addEventListener("mouseover" , () => {secondp.style.opacity = '0%';
setTimeout(() => {secondp.style.opacity = '100%'} , 5000)
})


// -----------------------------------------------------------------------------------------------


// 🌟 Exercise 2 : Work with forms


// Retrieve the form and console.log it.

// Retrieve the inputs by their id and console.log them.

// Retrieve the inputs by their name attribute and console.log them.

// When the user submits the form (ie. submit event listener)
//     use event.preventDefault(), why ?
//     get the values of the input tags,
//     make sure that they are not empty,
//     create an li per input value,
//     then append them to a the <ul class="usersAnswer"></ul>, below the form.

let form = document.getElementsByTagName('form')[0]
let fname = document.getElementById('fname')
let lname = document.getElementById('lname')
console.log(form , fname , lname)
console.log(`first name : ${form.fname}`, `last name : ${form.lname}`)


form.addEventListener("submit", (event) => {
    event.preventDefault();
    console.log(fname.value)
    console.log(lname.value)
    fname.value = fname.value.replaceAll(' ', '')
    lname.value = lname.value.replaceAll(' ', '')
    if (fname.value.length  && lname.value.length){
        let ua = document.getElementsByClassName('usersAnswer')[0]
        let lif = document.createElement('li')
        let lil = document.createElement('li')
        lif.innerHTML = `first name : ${fname.value}`
        lil.innerHTML = `last name : ${lname.value}`
        ua.append(lif)
        ua.append(lil)
    }
    else{
        alert('not valid')
    }
});


// -----------------------------------------------------------------------------------------------


// 🌟 Exercise 3 : Transform the sentence


// Declare a global variable named allBoldItems.

// Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.

// Create a function called highlight() that changes the color of all the bold text to blue.

// Create a function called return_normal() that changes the color of all the bold text back to black.

// Call the function highlight() on mouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() on mouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example

const allBoldItems = []
const paragraph = document.getElementsByTagName('p')[0]
function getBold_items(){
let strongarr = []
for (i of paragraph.children){
    if (i.nodeName === "STRONG"){
        allBoldItems.push(i)
    }
    
}
return allBoldItems
}


function highlight(){
    for (strong of getBold_items()){
        strong.style.color = 'blue'
    }
}


function return_normal(){
    for (strong of getBold_items()){
        strong.style.color = 'inherit'
    }
}

console.log(getBold_items())

paragraph.addEventListener("mouseover" , (e) => {
    highlight()

})
paragraph.addEventListener("mouseout" , (e) => {
    return_normal()

})



// -----------------------------------------------------------------------------------------------



// 🌟 Exercice 4 : Volume of a sphere
// Instructions

//     Write a JavaScript program to calculate the volume of a sphere. Use the code below as a base:

const form = document.forms.volumeform
const submit = document.getElementById('submit')
const radius = form.radius


submit.addEventListener('click' , (e) => {e.preventDefault();form.volume.value = 4/3 * Math.PI * Math.pow(radius.value, 3)})


