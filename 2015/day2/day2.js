var delimiter = "\n";
var input = document.body.textContent.split(delimiter);
input = input.filter((item)=>{return item.length > 0});
input = input.map((gift)=>{var dims=gift.split("x");return {l:Number(dims[0]),w:Number(dims[1]),h:Number(dims[2])}});

var clone = (obj) => {return Object.assign({},obj)};

var getSurfaceAreas = (gift) => {
  return [gift.l*gift.w,gift.w*gift.h,gift.h*gift.l];
}

var getWrapSurface = (gift) => {
  var areas = getSurfaceAreas(gift);
  return 2*areas[0]+2*areas[1]+2*areas[2]+Math.min(areas[0],areas[1],areas[2]);
}

var getRibbonLength = (gift) => {
  let ribbon = 2*gift.l+2*gift.w+2*gift.h - 2*Math.max(gift.l,gift.w,gift.h);
  let bow = gift.l*gift.w*gift.h;
  return ribbon+bow;
}

var process = (output, value) => {
  output.wrap += getWrapSurface(value);
  output.ribbon += getRibbonLength(value);
  return output;
}

var output = {wrap:0,ribbon:0};
output = input.reduce(wrap, output);
output = input.reduce(ribbon, output);

console.log("Solution 1: " + output.wrap);
console.log("Solution 2: " + output.ribbon);
