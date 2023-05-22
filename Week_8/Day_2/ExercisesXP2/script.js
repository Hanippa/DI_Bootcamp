// 🌟 Exercise 1 : Find the sum
// Instructions

//     Create a one line function (ie. an arrow function) that receives two numbers as parameters and returns the sum.

// const sum = (a , b) => a+b


//-----------------------------------------------------------------------------


// 🌟 Exercise 2 : Kg and grams
// Instructions

// Create a function that receives a weight in kilograms and returns it in grams. (Hint: 1 kg is 1000gr)

//     First, use function declaration and invoke it.
//     Then, use function expression and invoke it.
//     Write in a one line comment, the difference between function declaration and function expression.
//     Finally, use a one line arrow function and invoke it.





// function k_to_g(val){
//     return val*1000
// }

// const k_to_g = val => val*1000

// the biggest differences are that you have to declare the function before you call with function expression. also you can make expression function without a name. you canmt self invoke function expression.


//-----------------------------------------------------------------------------


// 🌟 Exercise 3 : Fortune teller
// Instructions

//     Create a self invoking function that takes 4 arguments: number of children, partner’s name, geographic location, job title.
//     The function should display in the DOM a sentence like "You will be a <job title> in <geographic location>, and married to <partner's name> with <number of children> kids."



// (function sentence(children, partner, location, job){
//     let sentence = `You will be a ${job} in ${location}, and married to ${partner} with ${children} kids.`
//     let body = document.getElementsByTagName('body')[0];
//     let p = document.createElement('p');
//     p.innerText = sentence;
//     body.appendChild(p);
// })();



//-----------------------------------------------------------------------------



// 🌟 Exercise 4 : Welcome
// Instructions

// John has just signed in to your website and you want to welcome him.

//     Create a Bootstrap Navbar in your HTML file.
//     In your js file, create a self invoking funtion that takes 1 argument: the name of the user that just signed in.
//     The function should add a div in the nabvar, displaying the name of the user and his profile picture.





(function login(name){
    navbar = document.getElementById('navbarSupportedContent')
    namediv = document.createElement('div')
    namediv.innerHTML = name
    namediv.style.margin = '10px'
    img = document.createElement('img')
    img.classList.add("rounded")
    img.classList.add("float-right")
    img.src = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png"
    img.style.width = "20px"
    img.style.height = "20px"
    navbar.append(namediv)
    navbar.append(img)
})("Dekel")



//-----------------------------------------------------------------------------



// 🌟 Exercise 5 : Juice Bar
// Instructions

// You will use nested functions, to open a new juice bar.
// Part I:

//     The outer function named makeJuice receives 1 argument: the size of the beverage the client wants - small, medium or large.

//     The inner function named addIngredients receives 3 ingredients, and displays on the DOM a sentence like The client wants a <size drink> juice, containing <first ingredient>, <second ingredient>, <third ingredient>".

//     Invoke the inner function ONCE inside the outer function. Then invoke the outer function in the global scope.



// const p = document.createElement('p')
// p.innerText = `The client wants a ${size} juice, containing ${ingredient1},${ingredient2}, ${ingredient3}".`
// body = document.getElementsByTagName('body')[0]
// body.append(p)



// const makeJuice = (size) =>  (ingredient1,ingredient2,ingredient3) => {
    
//     const p = document.createElement('p')
//     p.innerText = `The client wants a ${size} juice, containing ${ingredient1},${ingredient2}, ${ingredient3}".`
//     body = document.getElementsByTagName('body')[0]
//     body.append(p) 
// }


function makeJuice (size) {
    let ingredients = []
    function addIngredients(ingredient1, ingredient2, ingredient3) {
        ingredients.push(ingredient1, ingredient2, ingredient3);
    }

    function displayJuice() {
        const p = document.createElement('p')
        p.innerText = `The client wants a ${size} juice, containing`
        ingredients.forEach(ingredient => {
            p.innerText += ` ${ingredient}, `
        })
        body = document.getElementsByTagName('body')[0]
        body.append(p) 
    }

    addIngredients('strawberry', 'banana', 'dragon fruit');
    addIngredients('kiwi', 'passion fruit', 'orange');
    displayJuice();
}

makeJuice('large');