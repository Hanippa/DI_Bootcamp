// 🌟 Exercise 1 : List of people
// Instructions

console.log('exercise 1')
// const people = ["Greg", "Mary", "Devon", "James"];
const people = ["Greg", "Mary", "Devon", "James"];

// Part I - Review about arrays

//     Write code to remove “Greg” from the people array.

people.splice(0 , 1)

//     Write code to replace “James” to “Jason”.

people[2] = "Jason"

//     Write code to add your name to the end of the people array.

people[people.length] = "Dekel"

//     Write code that console.logs Mary’s index. take a look at the indexOf method on Google.

console.log(people.indexOf("Mary"))


//     Write code to make a copy of the people array using the slice method.
//         The copy should NOT include “Mary” or your name.
//         Hint: remember that now the people array should look like this const people = ["Mary", "Devon", "Jason", "Yourname"];
//         Hint: Check out the documentation for the slice method

people_copy = people.slice(1)
console.log(people_copy," copy")


//     Write code that gives the index of “Foo”. Why does it return -1 ?

console.log(people.indexOf("Foo"))
// The expresion returns -1 because the string was not found in the array.


//     Create a variable called last which value is the last element of the array.
//     Hint: What is the relationship between the index of the last element in the array and the length of the array?

last = people[people.length-1]

console.log(people , last)



// Part II - Loops

//     Using a loop, iterate through the people array and console.log each person.

//     Using a loop, iterate through the people array and exit the loop after you console.log “Jason” .
//     Hint: take a look at the break statement in the lesson.


for (const i in people) {
   console.log(people[i])
   if (people[i] === 'Jason'){
    break;
   }
}








console.log('exersice 2')
// 🌟 Exercise 2 : Your favorite colors
// Instructions

//     Create an array called colors where the value is a list of your five favorite colors.
colors = ['blue' , 'purple' , 'green' , 'pink' , 'black']

//     Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
for (const i in colors) {
    let suffixes = ["th" , "st" , "nd" , "rd"]
    let suffix = suffixes[0]
    if (Number(i)+1 == 0) suffix = "";
    if (Number(i)+1 % 10 == 1 && Number(i) % 100 != 11) suffix = suffixes[1];
    if (Number(i)+1 % 10 == 2 && Number(i) % 100 != 12) suffix = suffixes[2];
    if (Number(i)+1 % 10 == 3 && Number(i) % 100 != 13) suffix = suffixes[3];
    console.log(`My #${Number(i)+1}${suffix} choice is blue`)
   
}

//     Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
//     Hint : create an array of suffixes to do the Bonus





console.log('exersice 3')
// 🌟 Exercise 3 : Repeat the question
// Instructions

//     Prompt the user for a number.

user_number = "" //prompt("type a number")

//     Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

if(isNaN(user_number)){
    while(user_number < 10){
        console.log('works')
        user_number = prompt("type a number")
    }
}

//     While the number is smaller than 10 continue asking the user for a new number.








console.log('exersice 4')
// 🌟 Exercise 4 : Building Management
// Instructions:

// Review about objects

//     Copy and paste the above object to your Javascript file.

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}



//     Console.log the number of floors in the building.

console.log(building.numberOfFloors)


//     Console.log how many apartments are on the floors 1 and 3.
console.log(building.numberOfAptByFloor.firstFloor , building.numberOfAptByFloor.thirdFloor)


//     Console.log the name of the second tenant and the number of rooms he has in his apartment.

console.log(building.nameOfTenants[1] , building.numberOfRoomsAndRent.dan[0])

//     Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.

if ( building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1] > building.numberOfRoomsAndRent.dan[1]){
    building.numberOfRoomsAndRent.dan[1] = 1200
}

console.log(building)


console.log('exercise 5')
// 🌟 Exercise 5 : Family
// Instructions

//     Create an object called family with a few key value pairs.
family = {'mom' : 'kim' , 'mom' : 'sam' , 'first_child':'yang'}

//     Using a for in loop, console.log the keys of the object.

for ( i in family){
    console.log(i)
}
//     Using a for in loop, console.log the values of the object.

for ( i in family){
    console.log(family[i])
}



console.log('exercise 6')
// Exercise 6 : Rudolf
// Instructions

const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}

//     Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”

final_str = ""
for ( i in details){

    final_str += i + " "
    final_str += details[i] + " "
}
console.log(final_str)


console.log('exercise 7')


// Exercise 7 : Secret Group
// Instructions

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

//     A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
//     Hint: a string is an array of letters
//     Console.log the name of their secret society. The output should be “ABJKPS”

names.sort()
let name = ""
for (i in names){
    name += names[i][0]
}
console.log(name)
