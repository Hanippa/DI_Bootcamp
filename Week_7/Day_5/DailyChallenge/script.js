user_num = prompt('number of beers')
if (confirm('Lets start counting beers!')){
    let counter = 1
for (let i=user_num ; i >= 0 ; i--){
    console.log(`${i} bottles of beer on the wall`)
    console.log(`${i} bottles of beer`)
    if (i === 1){
    console.log(`take ${counter} down, pass it around`)
    }
    else{
        console.log(`take ${counter} down, pass them around`)
    }
    counter++
}
}