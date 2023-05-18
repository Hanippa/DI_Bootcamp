function compareNumbers(userNumber,computerNumber){
    console.log(computerNumber , userNumber)
    return userNumber == computerNumber ? 'Winner' : userNumber > computerNumber ? 'number is smaller' : 'number is bigger'
}

function isvalidnumber(user_num , limit){
    while(isNaN(user_num) || Number(user_num) > limit || Number(user_num) < 0){
        if(!isNaN(user_num)){
            alert('Sorry it’s not a good number')  
        }
        else{
            alert('Sorry, not a number')
        }
        user_num = prompt('enter a number between 0 and 10')
    }
    return user_num
}

function playTheGame(){
    game:
    if(confirm('would you like to play the game?')){
        const computerNumber = Math.floor(Math.random()*11)
        for(i=0;i < 3;i++){
        const user_num = prompt('enter a number between 0 and 10')
        isvalidnumber(user_num,10)

        if (compareNumbers(user_num,computerNumber) === 'Winner'){
            alert('You win congrats!')
            break game;
        }
        alert(`${compareNumbers(user_num,computerNumber)} attempt ${i+1}`);
        }
        alert('out of attempts')
    }
}

