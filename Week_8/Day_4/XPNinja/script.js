// Exercise 1 : Bird class
// Instructions

//     Analyze the code below, what will be the output?

class Bird {
  constructor() {
    console.log("I'm a bird. 🦢");
  }
}

class Flamingo extends Bird {
  constructor() {
    console.log("I'm pink. 🌸");
    super();
  }
}

const pet = new Flamingo();

// The output will be 
// ""I'm pink. 🌸""
// "I'm a bird 🦢"
// the reason for that is that when you create a new instance of flamingo it starts by executing the constructor and console.logging the 
// ""I'm pink. 🌸"" then it creates the bird with the super and executes the "I'm a bird. 🦢"