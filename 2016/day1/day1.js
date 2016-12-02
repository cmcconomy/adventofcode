var input = document.body.textContent.split(", ");

var dirs = ["N", "E", "S", "W"];
var person = {facing:0, x:0, y:0};
var visited = {};
var firstVisit = null;

var turn = (person, turn) => {
  if( turn[0] == "R" ) { person.facing = (person.facing+1)%4;}
  if( turn[0] == "L" ) { person.facing = (person.facing+3)%4;}
  return person;
}

var takeSteps = (person, prop, dist) => {
  var newVal = person[prop] + Number(dist);
  for( var i=Math.min(person[prop],newVal); i<=Math.max(person[prop],newVal); i++ ) {
    if( person[prop] != i) {
      let x,y;
      if( prop == "x" ) {
        x=i;
        y=person.y;
      } else {
        x=person.x;
        y=i;
      }
      if( visited[x+":"+y] == 1 && firstVisit == null) {
        firstVisit = {x:x,y:y};
      }
      visited[x+":"+y] = 1;
    }
  }
  person[prop] = newVal;
  return person;
}

var walk = (person, dist) => {
  switch(person.facing) {
    case 0:
      person = takeSteps(person,"y",dist);
      break;
    case 1:
      person = takeSteps(person,"x",dist);
      break;
    case 2:
      person = takeSteps(person,"y",-dist);
      break;
    case 3:
      person = takeSteps(person,"x",-dist);
      break;
  }

  return person;
}

var move = (person, move) => {
  person = turn(person,move);
  person = walk(person,move.substr(1));
  return person;
};

person = input.reduce(move, person);

console.log("Solution 1: " + (Math.abs(person.x) + Math.abs(person.y)));
console.log("Solution 2: " + (Math.abs(firstVisit.x) + Math.abs(firstVisit.y)));
