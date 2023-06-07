const {register , login} = require('../modules/users.js');
const hasher = require('p4ssw0rd');




const _register = (req,res) => {
    user_info = {...req.body}
    user_info.password = hasher.hash(user_info.password)
    register(user_info).then(data => {
        res.send(`<h1>registaration seccessful your ID : ${data[0].id}</h1>`)
    }).catch(e => {
        console.log(e)
        res.status(404).json({msg:e.message})
    })
}
const _login = (req,res) => {
   login(req.body).then(data => {
        console.log(data)
        if(data.length > 0){
            res.send(`<h1>login seccessful</h1>`)
        }
        else{
            res.send('failed to login')
        }
        
    }).catch(e => {
        console.log(e)
        res.status(404).json({msg:e.message})
    })
}

module.exports = {
    _register,
    _login
}