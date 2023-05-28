section = document.getElementsByTagName('section')[0]
generate_quate = document.getElementsByClassName('generate_quate')[0]
const onePieceQuotes = [
    {
      id: 0,
      author: "Monkey D. Luffy",
      quote: "I will never stop until I reach my dream of becoming the Pirate King!"
    },
    {
      id: 1,
      author: "Roronoa Zoro",
      quote: "In the face of adversity, a true swordsman finds the strength to keep moving forward!"
    },
    {
      id: 2,
      author: "Nami",
      quote: "With every step I take, I draw closer to unlocking the secrets of the world!"
    },
    {
      id: 3,
      author: "Usopp",
      quote: "Believe in yourself, for your spirit is the key to unlocking your true potential!"
    },
    {
      id: 4,
      author: "Sanji",
      quote: "Love and compassion are the spices that make life worth living!"
    },
    {
      id: 5,
      author: "Tony Tony Chopper",
      quote: "No matter how tough the journey gets, never lose sight of the miracles that lie ahead!"
    },
    {
      id: 6,
      author: "Nico Robin",
      quote: "Embrace the gift of life and seize every moment with unwavering determination!"
    },
    {
      id: 7,
      author: "Franky",
      quote: "True freedom lies in pursuing your dreams with all your heart!"
    },
    {
      id: 8,
      author: "Brook",
      quote: "Let your passion for music resonate through your soul and touch the hearts of others!"
    },
    {
      id: 9,
      author: "Jinbe",
      quote: "Even in the face of despair, find the strength to stand tall and protect what you hold dear!"
    },
    {
      id: 10,
      author: "Monkey D. Luffy",
      quote: "I will gather a crew that will inspire the world and leave behind a legacy that lasts for eternity!"
    },
    {
      id: 11,
      author: "Portgas D. Ace",
      quote: "Live life to the fullest, for every moment is a precious gift."
    },
    {
      id: 12,
      author: "Trafalgar D. Water Law",
      quote: "One's heart is the most powerful weapon of all."
    },
    {
      id: 13,
      author: "Boa Hancock",
      quote: "True strength is not just physical prowess but also the ability to love and be loved."
    },
    {
      id: 14,
      author: "Eustass Kid",
      quote: "Aim high and never settle for anything less than greatness!"
    },
    {
      id: 15,
      author: "Donquixote Doflamingo",
      quote: "The world is a stage, and I am the puppeteer pulling the strings."
    },
    {
      id: 16,
      author: "Nefertari Vivi",
      quote: "To bring about change, one must have the courage to challenge the status quo."
    },
    {
      id: 17,
      author: "Buggy the Clown",
      quote: "Laughter is the best medicine, especially when it comes to facing life's absurdities!"
    },
    {
      id: 18,
      author: "Dracule Mihawk",
      quote: "A true swordsman never underestimates their opponent, for even the smallest threat can become formidable."
    },
    {
      id: 19,
      author: "Bartholomew Kuma",
      quote: "Sometimes, the greatest act of kindness is to bear the pain of others."
    },
    {
      id: 20,
      author: "Jango",
      quote: "Dance like nobody's watching, and let your spirit soar!"
    },
    {
      id: 21,
      author: "Shanks",
      quote: "The mark of a true captain is not the strength of their crew, but the strength of their bonds."
    },
    {
      id: 22,
      author: "Crocodile",
      quote: "In the desert of life, only the strong survive."
    },
    {
      id: 23,
      author: "Bartolomeo",
      quote: "Being a fan means never giving up on your idols, no matter what!"
    },
    {
      id: 24,
      author: "Kuzan",
      quote: "The world may be flawed, but that doesn't mean we can't strive for a better future."
    },
    {
      id: 25,
      author: "Smoker",
      quote: "Justice is not just a concept, but a responsibility that we must uphold."
    },
    {
      id: 26,
      author: "Emporio Ivankov",
      quote: "True beauty lies in embracing your uniqueness and being unapologetically yourself."
    },
    {
      id: 27,
      author: "Gol D. Roger",
      quote: "The greatest treasure is not gold or jewels, but the adventures we experience along the way."
    },
    {
      id: 28,
      author: "Silvers Rayleigh",
      quote: "Age is just a number. It's the spirit within that truly defines us."
    },
    {
      id: 29,
      author: "Whitebeard",
      quote: "Even in the face of death, a man's spirit can never be extinguished!"
    }
  ];

let selected = -1 
generate_quate.addEventListener('click' , () => {
    
    try {
        section.getElementsByTagName('h1')[0].remove()
      }
      catch(err) {
        console.log('enjoy!')
      }


    
    let random = Math.floor(Math.random() * 30);
    while(random === selected){
    random = Math.floor(Math.random() * 30);
    console.log(random)}
    selected = random
    const h1 = document.createElement('h1')
    h1.innerText = `quote : ${onePieceQuotes[random].quote} \n author : ${onePieceQuotes[random].author}`
    section.append(h1)
})