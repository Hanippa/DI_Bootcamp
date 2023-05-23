// Exercise 1 : Dog competition
// Instructions

// Using the following data

const data = [
  {
    name: 'Butters',
    age: 3,
    type: 'dog'
  },
   {
    name: 'Cuty',
    age: 5,
    type: 'rabbit'
  },
  {
    name: 'Lizzy',
    age: 6,
    type: 'dog'
  },
  {
    name: 'Red',
    age: 1,
    type: 'cat'
  },
  {
    name: 'Joey',
    age: 3,
    type: 'dog'
  },
  {
    name: 'Rex',
    age: 10,
    type: 'dog'
  },
];

// Hint: Dog Years -> the dog’s age is the age multiplied by 7.

//     Use a loop to find the sum of all the dog’s ages in dog years.
//     Using the reduce() method, find the sum of all the dog’s ages in dog years.
let sum = 0
data.forEach(animal => sum+=animal.age*7)
console.log(sum)


//-----------------------------------------------------------------------------------



// Exercise 2 : Email
// Instructions

//     Clean up this email to have no whitespaces. Do it in a single line (return a new string).
//     const userEmail3 = ' cannotfillemailformcorrectly@gmail.com '

const userEmail3 = ' cannotfillemailformcorrectly@gmail.com '

const cleanemail = userEmail3.replaceAll(' ' , '')



//-----------------------------------------------------------------------------------



// Exercise 3 : Employees #3
// Instructions

// Using this array

const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
             { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
             { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
             { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
             { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
             { firstName: 'Wes', lastName: 'Reid', role: 'Instructor'},
             { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor'}];

//     Change the structure of the users array. The user’s full name should be the key and the user’s role should be the value.
//     Example: { 'Bradley Bouley': 'Full Stack Resident' }
//     Hint: Step one, create an empty object.

let newusers = []
users.forEach(user => newusers.push({[user.firstName] : user.role}))



//-----------------------------------------------------------------------------------



// Exercise 4 : Array to Object
// Instructions

// Using this array const letters = ['x', 'y', 'z', 'z'];

//     Use a for loop to get this output { x: 1, y: 1, z: 2 };
//     Use the reduce() method to get this output { x: 1, y: 1, z: 2 };


const letters = ['x', 'y', 'z', 'z'];

lettersobject = {}
letters.forEach(letter => lettersobject[letter] = isNaN(lettersobject[letter]) ? 1 : lettersobject[letter]+1)


const letterCount = letters.reduce((acc, letter) => {
  acc[letter] = (acc[letter] || 0) + 1;
  return acc;
}, {});

console.log(letterCount);