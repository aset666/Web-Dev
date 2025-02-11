'use strict'
//3.1
function hello(name) {
  let phrase = `Hello, ${name}!`;
//   debugger;
  say(phrase);
}

function say(phrase) {
  alert(`** ${phrase} **`);
}


for (let i = 0; i < 5; i++) {
    console.log("value,", i);
}


// 3.2  
function pow(x,n){
    let result = 1;

    for(let i = 0; i < n; i++){
        result *= x;
    }

    return result;
}

let x = prompt("x?", '')
let n = prompt("n?", '');

if(n <= 0){
    alert(`Power ${n} is not supported,
     please enter an integer number greater than zero`);
} else {
    alert( pow(x,n) );
}




describe("pow", function() {

    function makeTest(x) {
      let expected = x * x * x;
      it(`${x} in the power 3 is ${expected}`, function() {
        assert.equal(pow(x, 3), expected);
      });
    }
  
    for (let x = 1; x <= 5; x++) {
      makeTest(x);
    }
  
});

