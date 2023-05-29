// 🌟 Exercise 1 : Comparison
// Instructions

//     Create a function called compareToTen(num) that takes a number as an argument.
//     The function should return a Promise:
//         the promise resolves if the argument is less than 10
//         the promise rejects if argument is greater than 10.

const compareToTen = (num) => {
  let promise = new Promise((resolve, reject) => { 
  if(num < 10) { 
    resolve('lower then 10'); 
  } else { 
    reject('higher then 10'); 
  } 
});
promise.then((fromRes) => console.log(fromRes)).catch((fromRej) => console.log(fromRej));
};


compareToTen(10)


//------------------------------------------------------------------------------------------------------


// 🌟 Exercise 2 : Promises
// Instructions

//     Create a promise that resolves itself in 4 seconds and returns a “success” string.
//     How can you make your promise from part 1 shorter using Promise.resolve() and console.log “success”?
//     Add code to catch errors and console.log ‘Ooops something went wrong’.

const fourseconds = () => {
    let promise = new Promise((resolve, reject) => { 
    setTimeout(() => {resolve('success')} , 4*1000)
  });
  promise.then((fromRes) => console.log(fromRes)).catch((fromRej) => console.log('Ooops something went wrong'));
  };
  
  fourseconds()


//------------------------------------------------------------------------------------------------------



// 🌟 Exercise 3 : Resolve & Reject
// Instructions

//     Use Promise.resolve(value) to create a promise that will resolve itself with a value of 3.
//     Use Promise.reject(error) to create a promise that will reject itself with the string “Boo!”

let promise = new Promise((resolve, reject) => { 
    resolve(3)
    reject('Boo')
  }).then((value) => console.log(value)).catch((error) => console.log(error))
