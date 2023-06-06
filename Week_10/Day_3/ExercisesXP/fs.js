// Exercise 1 : Reading from a file in Node.JS
// Instructions

//     Create a text file and write something inside (example: ‘Some Text To See’)
//     Create an fs.js file, and inside use the Node JS File System to read the text file and console.log the output in the terminal


// Expected Output:


let fs = require('fs');
fs.readFile('text.txt', 'utf-8', function (err, data) {
    if (err) {
        console.error(err)
        return
    }
    console.log(data);
});

// Exercise 2 : Writing files with Node JS
// Instructions

//     Create an fs.js file, and use the Node js File System to create a new text file and write to it.


fs.writeFile('test.txt', 'Bla bla', (err) => { 
    if (err){ 
        console.log(err);
    }
    else{
        console.log('Write operation complete.');
    }
});

// Use the Node js File System to append some other text to the text file. (Example:”Buy orange juice”)

fs.writeFile('test.txt', 'Bla bla', (err) => { 
    if (err){ 
        console.log(err);
    }
    else{
        console.log('Write operation complete.');
    }
});

fs.appendFile('test.txt' , ' Buy orange juice' , (err) => {
    if(err){
        console.log(err)
    }
    else{
        console.log('text addition complete')
    }
})

// Use the Node js File System to delete the file.

fs.unlink('test.txt', (err) => {
        if(err){
        console.log(err)
    }
    else{
        console.log('deletion complete')
    }
});