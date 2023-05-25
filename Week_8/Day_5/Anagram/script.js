const anagram = (string1 , string2) => {
    let string1array = [...string1.replaceAll(' ' , '').toLowerCase()];
    let string2array = [...string2.replaceAll(' ' , '').toLowerCase()];
    string1array = string1array.sort().toString()
    string2array = string2array.sort().toString()

    return string1array === string2array

}

console.log(anagram("The Morse Code" , "Here come dots"))