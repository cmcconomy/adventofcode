var input = document.body.textContent.split(", ");

var dirs = ["N", "E", "S", "W"];
var person = {facing:0, x:0, y:0};
var visited = {};

var turn = (person, turn) => {
  if( turn[0] == "R" ) { person.facing = (person.facing+1)%4;}
  if( turn[0] == "L" ) { person.facing = (person.facing+3)%4;}
  return person;
}

var takeSteps = (person, prop, dist) => {
  var newVal = person[prop] + Number(dist);
  for( var i=Math.min(person[prop],newVal); i<=Math.max(person[prop],newVal); i++ ) {
    if( person[prop] != i) {
      let label;
      if( prop == "x" ) {
        label=i + ":" + person.y;
      } else {
        label=person.x + ":" + i;
      }
      if( visited[label] == 1 ) {
        console.log(label);
      }
      visited[label] = 1;
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

console.log(person);
