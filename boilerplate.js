var delimiter = ", ";
var input = document.body.textContent.split(delimiter);
// input = "";

var transform = (input) => {
  return input;
}

var transform = (output, value) => {
  // return output + value;
}

var output = {};
output = input.reduce(transform, output);

console.log(output);
