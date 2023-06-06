const express = require('express')
const fs = require('fs')

const app = express()

app.use(express.urlencoded({ extended: true }))

app.listen(3000, () => {
    console.log('server running on http://localhost:3000')
})

const readfile = async (filename) => {
    const filedata = await fs.promises.readFile(filename , 'utf-8');
    return JSON.parse(filedata)

}
const addtofile = async (filename , data) => {
    const filedata = await readfile(filename)
    filedata.items.push(data)
    fs.writeFile(filename , JSON.stringify(filedata, null, 2) ,  'utf-8' , (err) => {
        if (err){
            console.log("err", err)
        }
       
    })

}


app.get('/items',  (req, res)=>{
    readfile('shoppinglist.json').then(response => {
        res.status(200).json(response)
    })
    
  })

  app.get('/items/:id',  (req, res)=>{
    readfile('shoppinglist.json').then(response => {

        if(response.items[req.params.id-1]){
            res.status(200).json(response.items[req.params.id-1])
        }
        else{
            res.status(404).send('item not found')
        }
        
    })
    
  })
  app.get('/',  (req, res)=>{
    res.sendFile(__dirname + '/index.html')
    
  })

app.post('/items',  async (req, res)=>{
    await addtofile('shoppinglist.json' , req.body)
    res.status(200).send('fadsf')
})  
    