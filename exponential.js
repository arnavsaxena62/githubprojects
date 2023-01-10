
const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


function exponetial(base, exponent) {
    let answer = 1;
    for (let i = 0; i < exponent; i++) {
      answer = answer * base;
    }
    return answer;
}
rl.question("", (base) => {
    rl.question("", (exponent) =>{
        let finalanswer = exponetial(parseInt(base), parseInt(exponent));
        console.log(finalanswer);
        process.exit(0);
    })
})

  