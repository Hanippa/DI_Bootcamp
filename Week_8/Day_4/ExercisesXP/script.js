// 🌟 Exercise 1 : Location
// Instructions

//     Analyze the code below. What will be the output?

// const person = {
//     name: 'John Doe',
//     age: 25,
//     location: {
//         country: 'Canada',
//         city: 'Vancouver',
//         coordinates: [49.2827, -123.1207]
//     }
// }

// const {name, location: {country, city, coordinates: [lat, lng]}} = person;

// console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);


// The output of this would be : "I am John Doe from Vancouver, Canada. Latitude49.2827, Longitude-123.1207" // the reason is that this code destructrues the object in multipule levels.




//-------------------------------------------------------------------------------------





// 🌟 Exercise 2: Display Student Info
// Instructions

function displayStudentInfo(objUser){
    const {first , last } = objUser;
    console.log(`firstname : ${first} lastname : ${last}`)
}

displayStudentInfo({first: 'Elie', last:'Schoppik'});


//     Using the code above, destructure the parameter inside the function and return a string as the example seen below:
//     //output : 'Your full name is Elie Schoppik'




//-------------------------------------------------------------------------------------





// 🌟 Exercise 3: User & id
// Instructions

// Using this object 
const users = { user1: 18273, user2: 92833, user3: 90315 }

//     Using methods taught in class, turn the users object into an array:
//     Excepted output: [ [ 'user1', 18273 ], [ 'user2', 92833 ], [ 'user3', 90315 ] ]
//     FYI : The number is their ID number.

//     Modify the outcome of part 1, by multipling the user’s ID by 2.
//     Excepted output: [ [ 'user1', 36546 ], [ 'user2', 185666 ], [ 'user3', 180630 ] ]


const usersarray = []
Object.keys(users).forEach(key => usersarray.push([key , users[key]]))
console.log(usersarray)
usersarray.length=0
Object.keys(users).forEach(key => usersarray.push([key , users[key]*2]))
console.log(usersarray)




//-------------------------------------------------------------------------------------




// Exercise 4 : Person class
// Instructions

//     Analyze the code below. What will be the output?

class Person {
  constructor(name) {
    this.name = name;
  }
}

const member = new Person('John');
console.log(typeof member);

// the output will be type "Object", because member is a Person object. to get person you would need to use instanceof.




//-------------------------------------------------------------------------------------






// 🌟 Exercise 5 : Dog class
// Instructions

// Using the Dog class below:

class Dog {
  constructor(name) {
    this.name = name;
  }
};

//     Analyze the options below. Which constructor will successfully extend the Dog class?

//   // 1
// class Labrador extends Dog {
//   constructor(name, size) {
//     this.size = size;
//   }
// };


  // 2
class Labrador extends Dog {
  constructor(name, size) {
    super(name);
    this.size = size;
  }
};


//   // 3
// class Labrador extends Dog {
//   constructor(size) {
//     super(name);
//     this.size = size;
//   }
// };


//   // 4
// class Labrador extends Dog {
//   constructor(name, size) {
//     this.name = name;
//     this.size = size;
//   }
// };


// The second one becuase the constructor has to call the super function and get both name and the new value, size.





//-------------------------------------------------------------------------------------






// 🌟 Exercise 6 : Challenges

//     Evaluate these (ie True or False)

//     [2] === [2]  // False / Because they are indentical but not the same object.
//     {} === {} // False / Because they are indentical but not the same object.


//     What is, for each object below, the value of the property number and why?

//     const object1 = { number: 5 };  // 5 / set
//     const object2 = object1; // 5 / reference copy 
//     const object3 = object2; // 5 / reference copy 
//     const object4 = { number: 5}; // 5 / set

//     object1.number = 4;
//     console.log(object2.number) // 4 reference to object 1 
//     console.log(object3.number) // 4 reference to object 2 => reference to object 1
//     console.log(object4.number) // 5  set


//     Create a class Animal with the attributes name, type and color. The type is the animal type, for example: dog, cat, dolphin ect …
class Animal {
    constructor(name , type , color) {
      this.name = name;
      this.type = type;
      this.color = color
    }
  };
  class Mammal extends Animal{
    constructor(name , type , color) {
      super(name , type , color)
    }
    sound(sound) {
        
        return `${sound} I'm a ${this.type} named ${this.name} and I'm ${this.color}`
    }

  };
  const farmerCow = new Mammal('Lily' , 'cow' , 'brown and white')

  console.log(farmerCow.sound('Moooo'))


//     Create a class Mamal that extends from the Animal class. Inside the class, add a method called sound(). This method takes a parameter: the sound the animal makes, and returns the details of the animal (name, type and color) as well as the sound it makes.

//     Create a farmerCow object that is an instance of the class Mamal. The object accepts a name, a type and a color and calls the sound method that “moos” her information.
//     For example: Moooo I'm a cow, named Lily and I'm brown and white


