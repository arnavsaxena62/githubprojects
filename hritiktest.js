let base = 2;
let exponent = 2;
let answer = 1;
function exponetial(base, exponent) {
    for (i in exponent){
        answer = answer*base;
        i++
    }
        return answer;}
let finalanswer = exponetial(base,exponent)
console.log ( finalanswer)
