// single line comment

/*
Multi-line
Comment
*/

console.log("hello world");

//! DATA TYPES

let dataType = "this is a string"; // string data type

dataType = 1234; // integer data type

dataType = 12.34; // float data type

dataType = true; // boolean data type 

//! VARIABLES

var myFirstName = "Jordan"; // 'var' is used for legacy code

const mySurname = "Darlington"; // 'const' cannot be updated

let myJob = "MFL Teacher";

myJob = "Software Instructor"; // 'let' can be updated

console.log(myJob);

//! IF STATEMENTS

if (myJob === "Software Instructor") {
    console.log("Jordan works at Code Nation");
} else if (myJob === "MFL Teacher") {
    console.log("Jordan teaches Spanish & French");
} else {
    console.log("Jordan has a new job");
}

if (myFirstName === "Jordan" && mySurname === "Darlington") {
    console.log("His name is 'Jordan Darlington'");
} else {
    console.log("I don't know his name");
}

if (myJob === "Software Instructor" || myJob === "MFL Teacher") {
    console.log("Jordan teaches");
} else {
    console.log("Jordan doesn't teach");
}

//! FUNCTIONS

function myFunction() {
    console.log("This is a JavaScript function!");
}
myFunction()

//! STRING INTERPOLATION

console.log(`His name is ${myFirstName} ${mySurname}.`);

//! ARRAYS

let innovateInstructors = ["Jordan", "Katy"];

console.log(innovateInstructors);
console.log(innovateInstructors[1]);

//! LOOPS

let text = "";

for (let i = 0; i < 5; i++) {
    text += "the number is " + i + " ";
} console.log(text);


let i = 1;

while (i < 5) {
    text += "the number is " + i;
    i++;
} console.log(text);

//! SWITCH STATEMENTS

let fruit = "apple";
switch (fruit) {
    case "grape":
        console.log("grape");
        break;
    case "orange":
        console.log("orange");
        break;
    case "apple":
        console.log("apple!");
        break;
    default:
        console.log("I don't like that fruit.")
}

//! ARROW FUNCTIONS

hello = () => {
    console.log("Hello World!");
}
hello()