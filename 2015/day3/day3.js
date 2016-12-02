var delimiter = "";
var input = document.body.textContent.split(delimiter);
input = input.filter((item)=>{return item.length > 0});

var clone = (obj) => {return Object.assign({},obj)};
// input = "";

var move = (output, move) => {
  switch(move) {
    case "^": output.y++; break;
    case ">": output.x--; break;
    case "v": output.y--; break;
    case "<": output.x++; break;
  }
  return output;
}

var giveGifts = (useRobosanta) => {
  return (output, value,i) => {
    var gifter; 
    if( useRobosanta && i%2 == 1 ) {
      gifter = output.robosanta;
      output.robosanta = move(gifter,value);
    } else {
      gifter = output.santa;
      output.santa = move(gifter,value);
    }
    var pos=gifter.x+":"+gifter.y;
    if ( output.visited[pos] == null ) {
      output.visited[pos] = 1;
    } else {
      output.visited[pos]++;
    }

    return output;
    }
}
var output;

output = {santa:{x:0,y:0},robosanta:{x:0,y:0},visited:{"0:0":1}};
output = input.reduce(giveGifts(false), output);
console.log("Part 1: " + Object.keys(output.visited).length);

output = {santa:{x:0,y:0},robosanta:{x:0,y:0},visited:{"0:0":2}};
output = input.reduce(giveGifts(true), output);
console.log("Part 2: " + Object.keys(output.visited).length);
