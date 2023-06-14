const _hello = (req,res) => {
    res.status(200).json({msg : 'hello from express'})
}

const _hello_post = (req,res) => {
    res.status(200).json({msg : `post request accepted your message : ${JSON.stringify(req.body)}`})
}
module.exports = {
    _hello , _hello_post
}