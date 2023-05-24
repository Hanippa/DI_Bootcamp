
const grid_container = document.getElementsByClassName('grid-container')[0]
const color_container = document.getElementsByClassName('color-container')[0]
let grid_width = 50
let grid_height = 25
let color_choice = ''
let hover = false

document.addEventListener('click' , () => {hover ^= true;console.log(hover)})

const colors = ["#ABDEE6" , "#CBAACB" , "#FFFFB5" ,
               "#FFCCB6" , "#F3B0C3" , "#AE7F6C" ,
               "#FA6690" , "#AC2931" , "#6D9A5F" ,
                "#f7626b" , "#FE984D" , "#FAE592",
                 "#E9A7B8" , "#A4D4DC" , "#F4CEB8",
                  "#D3D5D4" , "#5F7880" , "#4B5556",
                "#CAA78D" , "#765285" , "#feb47b"];



for (let color of colors){
    const color_box = document.createElement('div');
    color_box.style.backgroundColor = color
    color_box.classList.add('color')
    color_box.addEventListener('click', () => {color_choice = color} )
    color_container.appendChild(color_box);
}



for(let i=0;i<grid_height;i++){
  const row = document.createElement('div')
  row.classList.add('row')
  for(let j=0;j<grid_width;j++){
    const pixel = document.createElement('div')
    pixel.classList.add('pixel')
    pixel.addEventListener('mousedown' , () => {pixel.style.backgroundColor = color_choice})
    pixel.addEventListener('mouseover' , () => {if(hover){pixel.style.backgroundColor = color_choice}})
    row.appendChild(pixel)
  
  }
  grid_container.appendChild(row)

}

