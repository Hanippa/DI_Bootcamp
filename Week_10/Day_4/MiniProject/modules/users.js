const {db} = require('../config/db.js');
const hasher = require('p4ssw0rd');

const register = (user) => {
    return db('users').insert(user).returning('*')
}

const login = (user) => {
    hashed_password = hasher.hash(user.password)
    return db('users').select('*').where({username:user.username , password:hashed_password})
}




module.exports = {
    register,
    login
}

