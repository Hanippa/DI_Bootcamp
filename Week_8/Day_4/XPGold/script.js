// Exercise 1 : print Full Name
// Instructions

//     Create a function called printFullName(studentObj) that accepts an object as a parameter.
//     For example : printFullName({first: 'Elie', last:'Schoppik'}).
//     The function should return a string like the example below

//     printFullName({first: 'Elie', last:'Schoppik'}) 
//     // 'Your full name is Elie Schoppik`

// Destructure this object DIRECTLY from the parameters (ie. Look at the Advanced Object lesson - Part II : Object destructuring used as an assignment to a function)

// The output of the printFullName() function should be the exact same as the displayStudentInfo function. (Exercise XP)
function printFullName(objUser){
  const {first , last } = objUser;
  console.log(`firstname : ${first} lastname : ${last}`)
}

printFullName({first: 'Elie', last:'Schoppik'});



// Exercise 2 : keys and values
// Instructions

//     Create a function that takes an object and returns the keys and values as separate arrays.
//     Return the keys sorted alphabetically, and their corresponding values in the same order.

// Examples
// keysAndValues({ a: 1, b: 2, c: 3 })
// ➞ [["a", "b", "c"], [1, 2, 3]]

// keysAndValues({ a: "Apple", b: "Microsoft", c: "Google" })
// ➞ [["a", "b", "c"], ["Apple", "Microsoft", "Google"]]

// keysAndValues({ key1: true, key2: false, key3: undefined })
// ➞ [["key1", "key2", "key3"], [true, false, undefined]]


const keysAndValues = object => [Object.keys(object) , Object.values(object)]

console.log(keysAndValues({ a: 1, b: 2, c: 3 }))


// Exercise 3 : Counter class
// Instructions

//     Analyze the code below, what will be the output?

class Counter {
  constructor() {
    this.count = 0;
  }

  increment() {
    this.count++;
  }
}

const counterOne = new Counter();
counterOne.increment();
counterOne.increment();

const counterTwo = counterOne;
counterTwo.increment();

console.log(counterOne.count); //3 bacause counterTwo a pointer to counterOne
