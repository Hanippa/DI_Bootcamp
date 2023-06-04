const http = require("http");


const { largeNumber , currentdatetime} = require("./main");

console.log(largeNumber)

const b = 5;

console.log(largeNumber + b)



const host = 'localhost';
const port = 3000;

const requestListener = function (req, res) {
    res.setHeader("Content-Type", "text/html");
    res.writeHead(200);

    
    res.end(`<html><h1>Hi there at the frontend</h1><p>My Module is ${largeNumber + b}</p><h2>${currentdatetime()}</h2></html>`);
};

const server = http.createServer(requestListener);
server.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
    
});
