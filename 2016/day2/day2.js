var delimiter = "\n";
var input = document.body.textContent.split(delimiter);
input = input.filter((item)=>{return item.length > 0});

var clone = (obj) => {return Object.assign({},obj)};

var keypads = {
part1: [
  ["1","2","3"],
  ["4","5","6"],
  ["7","8","9"]
],
part2: [
  [".",".","1",".","."],
  [".","2","3","4","."],
  ["5","6","7","8","9"],
  [".","A","B","C","."],
  [".",".","D",".","."]
]};

var moves = (part) => {
  var keypad = keypads[part];
  return (pos,dir) => {
    switch(dir) {
      case "U":
        if(pos.y>0 && keypad[pos.x][pos.y-1] != ".") pos.y -= Number(1);
        break;
      case "R":
        if(pos.x<keypad[0].length-1 && keypad[pos.x+1][pos.y] != ".") pos.x += Number(1);
        break;
      case "D":
        if(pos.y<keypad.length-1 && keypad[pos.x][pos.y+1] != ".") pos.y += Number(1);
        break;
      case "L":
        if(pos.x>0 && keypad[pos.x-1][pos.y] != ".") pos.x -= Number(1);
        break;
    }
    return pos;
  }
}

var startPoses = {part1:{x:1,y:1}, part2:{x:0,y:2}};
var transforms = (part) => {
  var keypad = keypads[part];
  var startPos = startPoses[part];
  var move = moves(part);
  return (bathroomCode, value) => {
    var moves=value.split("");
    var pos=clone(startPos);
    if( bathroomCode.length > 0 ) {
      pos = clone(bathroomCode[bathroomCode.length-1]);
    }
    pos = moves.reduce(move,pos);
    bathroomCode.push(pos);
    return bathroomCode;
  }
}

var translators = (part) => {
  var keypad = keypads[part];
  return (bathroomCode) => {
    return bathroomCode.reduce((code,pos)=>{return code.concat(keypad[pos.y][pos.x])},"");
  }
}

var doit = (part) => {
  var bathroomCode = [];
  var transform = transforms(part);
  bathroomCode = input.reduce(transform, bathroomCode);
  var translate = translators(part);
  console.log("Solution for " + part + ": " + translate(bathroomCode));
}

doit("part1");
doit("part2");
