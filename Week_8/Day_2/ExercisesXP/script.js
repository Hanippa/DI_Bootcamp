// 🌟 Exercise 1 : Scope
// Instructions

//     Analyse the code below, and predict what will be the value of a in all the following functions.
//     Write your prediction as comments in a js file. Explain your predictions.



// // #1
// function funcOne() {
//     let a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }


// ****************ANSWER********************
// The value of a will be 3 because at the start of the function a is bigger then 1 (5)
// ****************ANSWER********************


// // #1.1 - run in the console:
// funcOne()
// // #1.2 What will happen if the variable is declared 
// // with const instead of let ?

// ****************ANSWER********************
// The value of a will not change and it will give the error of, cannot asign value to constant variable.
// ****************ANSWER********************


// //#2
// let a = 0;
// function funcTwo() {
//     a = 5;
// }


// function funcThree() {
//     alert(`inside the funcThree function ${a}`);
// }

// ****************ANSWER********************
// The value of a will be 5
// ****************ANSWER********************


// // #2.1 - run in the console:
// funcThree()
// funcTwo()
// funcThree()
// // #2.2 What will happen if the variable is declared 
// // with const instead of let ?

// ****************ANSWER********************
// first alert to the number 0 then to the number 5 becasuse at first a is 0 then it is changed by the funcTwo function
// if changed to const the alert will be 5 and 5 becuase a is not able to change
// ****************ANSWER********************


// //#3
// function funcFour() {
//     window.a = "hello";
// }


// function funcFive() {
//     alert(`inside the funcFive function ${a}`);
// }

// // #3.1 - run in the console:
// funcFour()
// funcFive()

// ****************ANSWER********************
// a will be 'hello' bacause it is declared as a global variable, and thus is acceible through the function.
// ****************ANSWER********************


// //#4
// let a = 1;
// function funcSix() {
//     let a = "test";
//     alert(`inside the funcSix function ${a}`);
// }


// // #4.1 - run in the console:
// funcSix()
// // #4.2 What will happen if the variable is declared 
// // with const instead of let ?

// ****************ANSWER********************
// a will be 'hello' bacause it is declared as a global variable, and thus is acceible through the function.
// ****************ANSWER********************


// //#5
// let a = 2;
// if (true) {
//     let a = 5;
//     alert(`in the if block ${a}`);
// }
// alert(`outside of the if block ${a}`);

// // #5.1 - run the code in the console
// // #5.2 What will happen if the variable is declared 
// // with const instead of let ?

// ****************ANSWER********************
// alert 5, alert 2 if const is used the result will be the same because one a is declared inside the function, and one outside. they dont inteact.
// ****************ANSWER********************



//------------------------------------------------------------------------------------------


// 🌟 Exercise 2 : Ternary operator

// Transform the winBattle() function to an arrow function.
// Create a variable called experiencePoints.
// Assign to this variable, a ternary operator. If winBattle() is true, the experiencePoints variable should be equal to 10, else the variable should be equal to 1.
// Console.log the experiencePoints variable.

// function winBattle(){
//     return true;
// }

const winBattle = () => true;

const experiencePoints = winBattle ? 10 : 1



//------------------------------------------------------------------------------------------



// 🌟 Exercise 3 : Is it a string ?
// Instructions

//     Write a JavaScript arrow function that checks whether the value of the argument passed, is a string or not. Use ternary operator
//     Check out the example below to see the expected output


let isString = val => typeof(val) === "string" ? true : false



//------------------------------------------------------------------------------------------


// 🌟 Exercise 4 : Colors


// Write a JavaScript program that displays the colors in the following order : “1# choice is Blue.” “2# choice is Green.” “3# choice is Red.” ect…
// Check if at least one element of the array is equal to the value “Violet”. If yes, console.log("Yeah"), else console.log("No...")
// Hint : Use the array methods taught in class. Look at the lesson Array Methods.



const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];

colors.forEach((color , i) => {

    console.log(`#${i+1} ${color}`)
    // color === "Violet" ? console.log('Yeah') : console.log('No...')
});

colors.includes('Violet') ? console.log('Yeah') : console.log('No...')



//------------------------------------------------------------------------------------------



// 🌟 Exercise 5 : Colors #2

// Write a JavaScript program that displays the colors in the following order : “1st choice is Blue .” “2nd choice is Green.” “3rd choice is Red.” ect…
// Hint : Use the array methods taught in class and ternary operator.


const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th","st","nd","rd"];

colors.forEach((color , i) => {

    let suffix = i+1 == 1 ? ordinal[1] : i+1 == 2 ? ordinal[2] : i+1 == 3 ? ordinal[3] : ordinal[0]
    console.log(`${i+1}${suffix} ${color}`)

});



//------------------------------------------------------------------------------------------



// Exercise 6 : Bank Details
// Instructions

// In this exercise, you have to decide which type of variables you have to use (ie. let or const):

//     Create a global variable called bankAmount which value is the amount of money currently in your account.
//     Create a variable that saves the % amount of VAT (In Israel, it’s 17%).
//     Create an array with all your monthly expenses, both positive and negative (money made and money spent).
//     Example : const details = ["+200", "-100", "+146", "+167", "-2900"]
//     Create a program that modifies the expenses (ie. the positive AND the negative expenses) so that they will include taxes (multiply each expense by the VAT).
//     Display your current bankAccount standing at the end of the month.


let bankAmount = 10000;
let vat = 17;
const details = ["+200", "-100", "+146", "+167", "-2900"];
details.forEach((exp , index) => {
    exp_num = Number(exp) + Number(exp) * (vat/100)
    exp_str = exp_num < 0 ? exp_num.toString() :  "+" + exp_num.toString()
    details[index] = exp_str
});


details.forEach(exp => {
    bankAmount = bankAmount + Number(exp)
});