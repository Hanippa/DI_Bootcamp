const plus = () => {
    return {
        type: "PLUS",
    }
}

//to go back to the previous day
const minus = () => {
    return {
        type: "MINUS",
    }
}

//we export the two functions
export {
    plus,
    minus
}