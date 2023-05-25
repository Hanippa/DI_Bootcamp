const robots = [
    {
      id: 1,
      name: 'Astro Boy',
      image: 'https://w7.pngwing.com/pngs/206/244/png-transparent-astro-boy-t-shirt-drawing-astro-boy-hand-manga-toddler-thumbnail.png'
    },
    {
      id: 2,
      name: 'Franky',
      image: 'https://static.wikia.nocookie.net/onepiece/images/8/8c/Franky_Anime_Post_Timeskip_Infobox.png'
    },
    {
      id: 3,
      name: 'Ava',
      image: 'https://static.wikia.nocookie.net/non-aliencreatures/images/9/9a/Ava-ExMachina.jpg'
    },
    {
      id: 4,
      name: 'XJ-9',
      image: 'https://static.wikia.nocookie.net/teenagerobot/images/b/b0/Jenny_wiki_icon.png'
    },
    {
      id: 5,
      name: 'Optimus Prime',
      image: 'https://e1.pngegg.com/pngimages/62/642/png-clipart-transformers-s-optimus-prime-transformer.png'
    },
    {
      id: 6,
      name: 'Sharon',
      image: 'https://ic.pics.livejournal.com/fai_dust/4082396/9076/9076_original.jpg'
    },
    {
      id: 7,
      name: 'R2D2',
      image: 'https://png.pngitem.com/pimgs/s/90-908013_transparent-r2d2-c3po-png-star-wars-r2d2-cartoon.png'
    },
    {
      id: 8,
      name: 'Unit-01',
      image: 'https://tvovermind.com/wp-content/uploads/2019/06/Neon-Genesis-Evangelion.jpg'
    },
    {
      id: 9,
      name: 'Atlas',
      image:'https://www.bostondynamics.com/sites/default/files/2021-08/atlas-dynamic.jpg'
    },
    {
      id: 10,
      name: 'P-body',
      image:'https://necaonline.com/wp-content/uploads/2013/06/650h-PBody.jpg'
    }
    ]




    let visible = []

    main_container = document.getElementsByClassName('main-container')[0]
    search = document.getElementsByClassName('search-input')[0]

    robots_container = document.getElementsByClassName('robots-container')[0]


    for(const robot of robots){
        robot_container = document.createElement('div')
        robot_image = document.createElement('img')
        robot_name = document.createElement('h1')
        robot_image.style.backgroundImage = `url(${robot.image})`
        robot_image.classList.add('robot-image')
        robot_name.innerText = robot.name
        robot_name.classList.add('robot-name')
        robot_container.append(robot_image)
        robot_container.append(robot_name)
        robot_container.classList.add('robot-container')
        robots_container.append(robot_container)
        }

    search.addEventListener('input', () => {
        visible = []


        robots_container.remove()
        robots_container = document.createElement('div')
        robots_container.classList.add('robots-container')
        main_container.append(robots_container)
        for(const robot of robots){

            if (robot.name.includes(search.value)){
                visible.push(robot.id)
            }
        }
        for(const robot of robots){

            if (visible.includes(robot.id) || visible.length === 0){
            console.log(robot)
            robot_container = document.createElement('div')
            robot_image = document.createElement('img')
            robot_name = document.createElement('h1')
            robot_image.style.backgroundImage = `url(${robot.image})`
            robot_image.classList.add('robot-image')
            robot_name.innerText = robot.name
            robot_name.classList.add('robot-name')
            robot_container.append(robot_image)
            robot_container.append(robot_name)
            robot_container.classList.add('robot-container')
            robots_container.append(robot_container)
            }
        }
})

