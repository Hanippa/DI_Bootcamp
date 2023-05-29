// 1rst daily challenge

//     Create two functions. Each function should return a promise.
//     The first function called makeAllCaps(), takes an array of words as an argument
//         If all the words in the array are strings, resolve the promise. The value of the resolved promise is the array of words uppercased.
//         else, reject the promise with a reason.
//     The second function called sortWords(), takes an array of words uppercased as an argument
//         If the array length is bigger than 4, resolve the promise. The value of the resolved promise is the array of words sorted in alphabetical order.
//         else, reject the promise with a reason.



const makeAllCaps = (array) =>{
    return new Promise ((resolve , reject) => {
        if (array.every(a => typeof a === "string" )){
            resolve(array.map(a=> a.toUpperCase()))
        }
        else{
            reject('array contains something other then strings!')
        }
    })
}



const sortWords = (array) => {
    return new Promise ((resolve , reject) => {
        if (array.length <= 4){
            resolve(array.sort())
        }
        else{
            reject('array contains more then 4 strings!')
        }
    })
}


sortWords(['falksjdf' , 'asdfasdf' , 'zsdfasdf']).then((result) => {return result}).then((result) => {return makeAllCaps(result)}).then((result => {console.log(result)}))



// -------------------------------------------------------------------------------


// 2nd daily challenge

const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`

// Create three functions. The two first functions should return a promise..

// The first function is named toJs():
//     this function converts the morse json string provided above to a morse javascript object.
//     if the morse javascript object is empty, throw an error (use reject)
//     else return the morse javascript object (use resolve)

// The second function called toMorse(morseJS), takes one argument: the new morse javascript object.
//     This function asks the user for a word or a sentence.
//     if the user entered a character that doesn’t exist in the new morse javascript object, throw an error. (use reject)
//     else return an array with the morse translation of the user’s word.

//     if the user enters the word "Hello", the promise resolves with this value ["....", ".", ".-..", ".-..","---"]
//     if the user entered the word "¡Hola!", the promise rejects because the character "¡" doesn't exist in the morse javascript object


// The third function called joinWords(morseTranslation), takes one argument: the morse translation array
//     this function joins the morse translation by using line break and display it on the page (ie. On the DOM)

// Chain the three functions.

const toJs = () => {
    return new Promise ((resolve , reject) => {
        if (morse.includes(':')){
            json = JSON.parse(morse)
            resolve(json) 
        }
        else{
            reject('empty :(')
        }
        
    });
};

const toMorse = (morsejs) => {
    const userstring = prompt('enter a word or sentence')
    return new Promise((resolve , reject) => {
        console.log(morsejs)
        if (Object.keys(morsejs).includes(userstring.split(''))){
            
            resolve('o')
        }
        else{
            reject('x')
        }
    })

}


toJs().then(result1 =>  result1).then(result2 => toMorse(result2).then(result3 => console.log(result3)))

// toMorse(morsejs).then(result => console.log(result))