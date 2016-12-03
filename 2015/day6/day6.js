var delimiter = "\n";
var input = document.body.textContent.split(delimiter);
input = input.filter((item)=>{return item.length > 0});

var clone = (obj) => {return Object.assign({},obj)};

var enrich = (command) => {
  var matches = command.match(/((\w+ )+)(\d+),(\d+) through (\d+),(\d+)/)
  return {
    command:matches[1].trim(),
    start: {x:matches[3],y:matches[4]},
    end: {x:matches[5],y:matches[6]}
  }
}
input = input.map(enrich);

var partFuncs = (part) => {
  var funcs;
  if( part == "part1" ) {
    funcs = {
      toggle: (grid,x,y) => {
        var label = x+":"+y;
        if( grid[label] == null ) {
          grid[label] = 1;
        } else {
          delete grid[label]; 
        }

        return grid;
      },

      turnOn: (grid,x,y) => {
        grid[x+":"+y] = 1;
        return grid;
      },

      turnOff: (grid,x,y) => {
        var label = x+":"+y;
        if( grid[label] != null ) {
          delete grid[label]; 
        }

        return grid;
      }
    }
  } else if (part == "part2") {
    funcs = {
      toggle: (grid,x,y) => {
        var label = x+":"+y;
        if( grid[label] == null) {grid[label]=0}
        grid[label]++;
        grid[label]++;
        return grid;
      },

      turnOn: (grid,x,y) => {
        var label = x+":"+y;
        if( grid[label] == null) {grid[label]=0}
        grid[label]++;
        return grid;
      },

      turnOff: (grid,x,y) => {
        var label = x+":"+y;
        if( grid[label] == null) {grid[label]=0}
        if( grid[label] > 0 ) {grid[label]--};
        if( grid[label] == 0 ) {delete grid[label]};
        return grid;
      }
    }
  }
  return funcs;
}


var partExecute = (part) => {
  var turnOn = partFuncs(part).turnOn;
  var turnOff = partFuncs(part).turnOff;
  var toggle = partFuncs(part).toggle;
  
  return (command,grid,x,y) => {
    var func;
    switch(command) {
      case "turn on": func = turnOn; break;
      case "turn off": func = turnOff; break;
      case "toggle": func = toggle; break;
    }

    return func(grid,x,y);
  }
}

var partExecuteGrid = (part) => {
  var execute = partExecute(part);
  return (grid,c) => {
    for( var x=Math.min(c.start.x,c.end.x); x<=Math.max(c.start.x,c.end.x); x++) {
      for( var y=Math.min(c.start.y,c.end.y); y<=Math.max(c.start.y,c.end.y); y++) {
        execute(c.command,grid,x,y);
      }
    }
    return grid;
  }
}

grid={};
grid = input.reduce(partExecuteGrid("part1"), grid);
console.log("Part 1: " + Object.keys(grid).length);

grid={};
grid = input.reduce(partExecuteGrid("part2"), grid);
console.log("Part 2: " + Object.keys(grid).reduce((total,val)=>{return total+grid[val]},0));
