const gameInfo = [
 {
   username: "john",
   team: "red",
   score: 5,
   items: ["ball", "book", "pen"]
 },
 {
   username: "becky",
   team: "blue",
   score: 10,
   items: ["tape", "backpack", "pen"]
 },
 {
   username: "susy",
   team: "red",
   score: 55,
   items: ["ball", "eraser", "pen"]
 },
 {
   username: "tyson",
   team: "green",
   score: 1,
   items: ["book", "pen"]
 },
];

const usernames = []
gameInfo.forEach(game => usernames.push(game.username + "!"))

console.log(usernames)

const usernames5 = []
gameInfo.forEach(game => game.score>5 ? usernames5.push(game.username + "!") : "")

console.log(usernames5)

let totalscore = 0
gameInfo.forEach(game => totalscore += game.score)

console.log(totalscore)