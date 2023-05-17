
// 🌟 Exercise 1 : Find the numbers divisible by 23
// Instructions

//     Create a function call isDivisible() that takes no parameter.

//     In the function, loop through numbers 0 to 500.

//     Console.log all the numbers divisible by 23.

//     At the end, console.log the sum of all numbers that are divisible by 23.


function isDivisible(num) {
    let sum = 0
    for(i=0;i<500;i++){
        if(i % num == 0){
            console.log(i)
            sum += i
        }
        
    }
    console.log('sum : ' , sum)
  }
  isDivisible(23)








//   🌟 Exercise 2 : Shopping List

//   Add the stock and prices objects to your js file.

//   Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.

//   Create a function called myBill() that takes no parameters.

//   The function should return the total price of your shoppingList. In order to do this you must follow these rules:
//       The item must be in stock. (Hint : check out if .. in)
//       If the item is in stock find out the price in the prices object.

//   Call the myBill() function.

//   Bonus: If the item is in stock, decrease the item’s stock by 1


  const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

const shoppingList = ["banana" , "orange" , "apple"]

function myBill(){
    let sum = 0
    for (item of shoppingList){
        if (stock[item] > 0){
            sum += prices[item]
            stock[item]--
        }
    }
    return sum
}

console.log(myBill() , stock);







// Exercise 3 : What’s in my wallet ?
// Instructions

// Note: Read the illustration (point 4), while reading the instructions

//     Create a function named changeEnough(itemPrice, amountOfChange) that receives two arguments :
//         an item price
//         and an array representing the amount of change in your pocket.

//     In the function, determine whether or not you can afford the item.
//         If the sum of the change is bigger or equal than the item’s price (ie. it means that you can afford the item), the function should return true
//         If the sum of the change is smaller than the item’s price (ie. it means that you cannot afford the item) the function should return false

//     Change will always be represented in the following order: quarters, dimes, nickels, pennies.


function changeEnough(itemPrice, amountOfChange){
    sum = 0
    for (let i = 0;i<amountOfChange.length;i++){
        switch(i){
            case 0:
                sum += (amountOfChange[i] * 0.25)
                break;
            case 1:
                sum += (amountOfChange[i] * 0.10)
                break;
            case 2:
                sum += (amountOfChange[i] * 0.05)
                break;
            case 3:
                sum += (amountOfChange[i] * 0.01)
                break;
        }
        
    }
    if (sum > itemPrice){
        return true
    }
    return false
}

console.log(changeEnough(0.75, [0,0,20,5]) , 'change')











// 🌟 Exercise 4 : Vacations Costs
// Instructions

// Let’s create functions that calculate your vacation’s costs:

//     Define a function called hotelCost().
//         It should ask the user for the number of nights they would like to stay in the hotel.
//         If the user doesn’t answer or if the answer is not a number, ask again.
//         The hotel costs $140 per night. The function should return the total price of the hotel.

//     Define a function called planeRideCost().
//         It should ask the user for their destination.
//         If the user doesn’t answer or if the answer is not a string, ask again.
//         The function should return a different price depending on the location.
//             “London”: 183$
//             “Paris” : 220$
//             All other destination : 300$

//     Define a function called rentalCarCost().
//         It should ask the user for the number of days they would like to rent the car.
//         If the user doesn’t answer or if the answer is not a number, ask again.
//         Calculate the cost to rent the car. The car costs $40 everyday.
//             If the user rents a car for more than 10 days, they get a 5% discount.
//         The function should return the total price of the car rental.

//     Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
//     Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
//     Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().

//     Call the function totalVacationCost()



function hotelCost(){
    let user_nights = prompt('how many nights would you like to stay?')
    while (!Number(user_nights)){
        user_nights = prompt('how many nights would you like to stay?')
    }
    return user_nights*140

}

function planeRideCost(){
    user_dest = prompt('what is your destanation?')
    while (!isNaN(user_dest)){
        user_dest = prompt('what is your destanation?')

    } 
    switch(user_dest){
        case "London":
            return 180;
        case "Paris":
            return 220;
        default:
            return 300;
    }
}



function rentalCarCost(){
    let user_car_days = prompt('for how many days would you like to rent the car?')
    while (!Number(user_car_days)){
        user_car_days = prompt('for how many days would you like to rent the car?')
    }
    if (user_car_days > 10){
        return (user_car_days*40)-user_car_days*0.05
    }
    return user_car_days*40

}

function totalVacationCost(){
    return `The car cost $${rentalCarCost()}, the hotel cost $${hotelCost()}, the plane tickets cost $${planeRideCost()}`
}










// 🌟 Exercise 5 : Users

// Using Javascript:
//     Retrieve the div and console.log it
//     Change the name “Pete” to “Richard”.
//     Delete the <li> that contains the text node “Sarah”. (It’s the second <li> of the second <ul>)
//     Change each first name of the two <ul>'s to your name. (Hint : use a loop)

// Using Javascript:
//     Add a class called student_list to both of the <ul>'s.
//     Add the classes university and attendance to the first <ul>.

// Using Javascript:
//     Add a “light blue” background color and some padding to the <div>.
//     Do not display the <li> that contains the text node “John”. (the first <li> of the <ul>)
//     Add a border to the <li> that contains the text node “Richard”. (the second <li> of the <ul>)
//     Change the font size of the whole body.

// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).


div = document.getElementsByTagName('div')
console.log(div)
const lists = document.getElementsByClassName('list')
lists[0].children[1].innerHTML = 'Richard'

lists[1].children[1].remove()

for (i of document.getElementsByTagName('li')){
    i.innerHTML = 'Dekel'
}

document.getElementsByTagName('ul')[0].classList.add('class')
document.getElementsByTagName('ul')[1].classList.add('class')

document.getElementsByTagName('ul')[0].classList.add('university')
document.getElementsByTagName('ul')[0].classList.add('attentence')
div[0].style.backgroundColor='lightblue' 
div[0].style.padding='50px'
document.getElementsByTagName('body')[0].style.fontSize = '50px'



if (div[0].style.backgroundColor == 'lightblue'){
    alert(`Hello ${lists[0].children[0].innerHTML} and  ${lists[0].children[1].innerHTML}`)
}


// Exercises 6 and 7 are on different files in the same directory.