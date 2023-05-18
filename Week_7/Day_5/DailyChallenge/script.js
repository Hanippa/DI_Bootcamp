let input = prompt('number ')
let counter = 0
for (let i = Number(input); i >= 0; i = i - counter) {
    if (i <= 0 || i-counter < 0){
        console.log(`${i} bottles of beer on the wall \n${i} bottles of beer \nTake ${counter+1} down, pass them around \nno more bottles of beer on the wall`);
    }
    else if (i === 1){
        console.log(`${i} bottles of beer on the wall \n${i} bottles of beer \nTake ${counter+1} down, pass it around \n${i-counter-1} bottles of beer on the wall`);
    }
    else{
        console.log(`${i} bottles of beer on the wall \n${i} bottles of beer \nTake ${counter+1} down, pass them around \n${i-counter-1} bottles of beer on the wall`);
    }
    counter++
};