const knex = require('knex')

const db = knex({
    client : 'pg',
    connection : {
        host : 'localhost',
        port : '5432',
        user : 'postgres',
        password : '2144',
        database : 'imdi'
    }
})


db('auth_user')
.select('username' , 'auth_user')
.update({username : 'Squidy'})
.where({username : 'Squid'})
.then(rows => {
    console.log(rows)
})
.catch(err => {
    console.log(err)
})