
function counter(counter = 1){
    return ()=> counter++;
}

const COUNTER = new counter();

console.log(COUNTER);

