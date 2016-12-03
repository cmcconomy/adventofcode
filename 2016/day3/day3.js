var delimiter = "\n";
var input = document.body.textContent.split(delimiter);
input = input.filter((item)=>{return item.length > 0});
input = input.map((sides)=>{return sides.split(" ").filter((item)=>{return item.length > 0}).map((i)=>{return Number(i)})});

var goodTriangle = (sides) => {
  var max=Math.max(sides[0],sides[1],sides[2]); 
  return (sides[0]+sides[1]+sides[2]-max) > max;  
}

var good = input.filter(goodTriangle);
console.log("Part 1: " + good.length);

var input2=[];
for( var i=0; i<input.length-2; i+=3 ) {
  input2[i] = [input[i][0],input[i+1][0],input[i+2][0]];
  input2[i+1] = [input[i][1],input[i+1][1],input[i+2][1]];
  input2[i+2] = [input[i][2],input[i+1][2],input[i+2][2]];
}
var good2 = input2.filter(goodTriangle);
console.log("Part 2: " + good2.length);
