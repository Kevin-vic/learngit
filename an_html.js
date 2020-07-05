alert("hello,world");
var x = 0;
x = 1;
if (x >= 2) {
    x = 3;
} else {
    x = 0;
}
var xiaoming = {
    name: "xiaoming",
    age: 15,
    like: "playsomething",
    do_not_like: "study",
}
alert(x);
alert("xiaoming's age is" + xiaoming.age);
var b = new Set([111, 222, 333]);
b.add(123);
console.log(b);

function abs(x) {
    if (typeof x !== "number") {
        throw "not a number";
    }
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
}
console.log(abs(-10));