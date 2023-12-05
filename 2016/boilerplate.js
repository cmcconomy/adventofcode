var delimiter = "\n";
var input = document.body.textContent.split(delimiter);
input = input.filter((item)=>{return item.length > 0});

var clone = (obj) => {return Object.assign({},obj)};
// input = "";

var transform = (output, value) => {
  // return output + value;
}

var output = {};
output = input.reduce(transform, output);

console.log(output);
