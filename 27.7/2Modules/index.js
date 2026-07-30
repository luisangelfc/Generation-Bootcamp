import * as functions from "./functions.js"
global.functions = functions
functions.printDate()


import * as classes from "./classes.js"
const currentDate = new classes.DateString()
console.log("Hoy es: " + currentDate.getDateString())