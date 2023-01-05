const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter a binary number: ', (binary) => {
  const decimal = parseInt(binary, 2);
  console.log(`${binary} in decimal is ${decimal}`);
  rl.close();
});
