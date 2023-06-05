
// Create a new folder, name it - node-server
// Create a server file, name it - myserver.js
// In this file, use http to create a server. You should return at least three different lines of HTML to the browser. (Use only HTML tags, no HTML files)
// Your server should run on http://localhost:3000/


let http = require("http");

const host = 'localhost';
let port = 8000;

const user = {firstName: 'Robin',lastName: 'Braze'}

const requestlistener = function (req, res) {
    res.setHeader('Content-Type', 'text/html');
    res.writeHead(200);
    res.end(`<html><h1>${JSON.stringify(user)}</h1><h1>1</h1><h1>2</h1><h1>3</h1></html>`);
};
const server = http.createServer(requestlistener)

server.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
})