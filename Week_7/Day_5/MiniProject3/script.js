const buttons = document.getElementsByClassName('piece')
const sounds = ['boom' , 'clap' , 'hihat' , 'kick' , 'openhat' , 'ride' , 'snare' , 'tink' , 'tom']
const keys = ['a','s','d','f','g','h','j','k','l']
const soundsaudio = []

for (sound of sounds){
 soundsaudio.push(new Audio(`sounds/${sound}.wav`));
};


let counter = 0
for (piece of buttons){
    let currentcounter = counter;
    const currentButton = piece;
    piece.addEventListener("click", function() {soundsaudio[currentcounter].play(); currentButton.classList.add('active');    setTimeout(function() {currentButton.classList.remove('active');}, 100);});
    counter++
}

  document.addEventListener("keydown", function(event) {
    const key = event.key.toLowerCase();
      event.preventDefault();
      for(let i = 0 ; i<sounds.length;i++){
        if (key === keys[i]){
            buttons[i].click();
        }
      }
  });