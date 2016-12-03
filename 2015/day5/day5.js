var delimiter = "\n";
var input = document.body.textContent.split(delimiter);
input = input.filter((item)=>{return item.length > 0});

var clone = (obj) => {return Object.assign({},obj)};
// input = "";
var has3vowels = (str) => {
  var matches = str.match(/[aeiou]/g);
  return matches!=null && matches.length >= 3;
}

var containsDoubleLetter = (str) => {
  return str.match(/(.)\1/g) != null;
}

var doesntContain = (str) => {
  return str.match(/ab|cd|pq|xy/) == null;
}

var niceOnesPart1 = input.filter(has3vowels).filter(containsDoubleLetter).filter(doesntContain);

var repeatingCouplet = (str) => {
  return str.match(/(..).*\1/) != null;
}

var mirror = (str) => {
  return str.match(/(.).\1/) != null;
}

var niceOnesPart2 = input.filter(repeatingCouplet).filter(mirror);

console.log("Part 1: " + niceOnesPart1.length);
console.log("Part 2: " + niceOnesPart2.length);
