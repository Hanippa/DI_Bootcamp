// Part I

//     In your Javascript file, using setTimeout, call a function after 2 seconds.
//     The function will alert “Hello World”.


// Part II

//     In your Javascript file, using setTimeout, call a function after 2 seconds.
//     The function will add a new paragraph <p>Hello World</p> to the <div id="container">.


// Part III

//     In your Javascript file, using setInterval, call a function every 2 seconds.
//     The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
//     The interval will be cleared (ie. clearInterval), when the user will click on the button.
//     Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">.

const div = document.getElementById('container')

function newpara(){
let p = document.createElement('p')
p.innerHTML = 'Hello World'
div.append(p)
}



setTimeout(() => {
    newpara()
    alert('Hello World')
}, 2000);

const inter = setInterval(() => { 
    newpara()
    if (div.children.length >= 5){
        clearInterval(inter)
    }
    
},2000)


function clearf(){
    clearInterval(inter)
}



// Copy the code above, to a structured HTML file.
// In your Javascript file, use setInterval to move the <div id="animate"> to the right side of the <div id="container">, when the button is clicked on.

// The <div id="animate"> should move 1px to the right every milisecond, until it reaches the end of the <div id="container">.
// Hint : use clearInterval as soon as the box reaches the right end side of the container
// Hint : check out the demonstration in the Course Noted named JS Functions
let i = 0
function myMove(){
    boxint = setInterval(() => {document.getElementById('animate').style.left = `${i}px`
    i++
    if (i >= 350){
        clearInterval(boxint)
    }
}, 1)
}