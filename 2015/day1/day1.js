var delimiter = "";
var input = document.body.textContent.split(delimiter);
input = input.filter((item)=>{return item.length > 0});

var clone = (obj) => {return Object.assign({},obj)};

var transform = (output, value, step) => {
  if(value=="(") output.floor++;
  if(value==")") output.floor--;
  if( output.basementStep == null && output.floor<0 ) {
    output.basementStep = step;
  }
  return output;
}

var output = {floor:0};
output = input.reduce(transform, output);

console.log("Solution 1: " + output.floor);
console.log("Solution 2: " + (output.basementStep+1));
