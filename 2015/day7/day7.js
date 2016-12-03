var delimiter = "\n";
var input = document.body.textContent.split(delimiter);
input = input.filter((item)=>{return item.length > 0});

var clone = (obj) => {return Object.assign({},obj)};
// input = "";
var regexs = {
  numAssign: /^(\d+) -> ([a-z]+)$/,
  assign: /^([a-z]+) -> ([a-z]+)$/,
  not: /^NOT ([a-z]+) -> ([a-z]+)$/,
  rshift: /^([a-z]+) RSHIFT (\d+) -> ([a-z]+)$/,
  lshift: /^([a-z]+) LSHIFT (\d+) -> ([a-z]+)$/,
  numAnd: /^(\d+) AND ([a-z]+) -> ([a-z]+)$/,
  and: /^([a-z]+) AND ([a-z]+) -> ([a-z]+)$/,
  or: /^([a-z]+) OR ([a-z]+) -> ([a-z]+)$/
};

// inputs and commands use the same [keys], eg. numAssign
var inputs = {
  numAssign: input.filter((str)=>{return str.match(regexs.numAssign)!=null}).map((command) => {
    var match = command.match(regexs.numAssign);
    return {
      from: match[1],
      to: match[2]
    }
  }),
  assign: input.filter((str)=>{return str.match(regexs.assign)!=null}).map((command) => {
    var match = command.match(regexs.assign);
    return {
      from: match[1],
      to: match[2]
    }
  }),
  not: input.filter((str)=>{return str.match(regexs.not)!=null}).map((command) => {
    var match = command.match(regexs.not);
    return {
      from: match[1],
      to: match[2]
    }
  }),
  rshift: input.filter((str)=>{return str.match(regexs.rshift)!=null}).map((command) => {
    var match = command.match(regexs.rshift);
    return {
      from: match[1],
      shift: match[2],
      to: match[3]
    }
  }),
  lshift: input.filter((str)=>{return str.match(regexs.lshift)!=null}).map((command) => {
    var match = command.match(regexs.lshift);
    return {
      from: match[1],
      shift: match[2],
      to: match[3]
    }
  }),
  numAnd: input.filter((str)=>{return str.match(regexs.numAnd)!=null}).map((command) => {
    var match = command.match(regexs.numAnd);
    return {
      from1: match[1],
      from2: match[2],
      to: match[3]
    }
  }),
  and: input.filter((str)=>{return str.match(regexs.and)!=null}).map((command) => {
    var match = command.match(regexs.and);
    return {
      from1: match[1],
      from2: match[2],
      to: match[3]
    }
  }),
  or: input.filter((str)=>{return str.match(regexs.or)!=null}).map((command) => {
    var match = command.match(regexs.or);
    return {
      from1: match[1],
      from2: match[2],
      to: match[3]
    }
  })
}

var commands = {
  numAssign: (registers, input) => {
    if( input.done != true ) {
      registers[input.to] = Number(input.from);
      input.done = true
    }
    return registers;
  },
  assign: (registers, input) => {
    if( input.done != true && registers[input.from] != null) {
      registers[input.to] = registers[input.from];
      input.done = true
    }
    return registers;
  },
  not: (registers, input) => {
    if( input.done != true && registers[input.from] != null) {
      registers[input.to] = ~ registers[input.from];
      input.done = true
    }
    return registers;
  },
  rshift: (registers, input) => {
    if( input.done != true && registers[input.from] != null) {
      registers[input.to] = registers[input.from] >> input.shift ;
      input.done = true
    }
    return registers;
  },
  lshift: (registers, input) => {
    if( input.done != true && registers[input.from] != null) {
      registers[input.to] = registers[input.from] << input.shift ;
      if(registers[input.to] > 65535) { console.error("Register for lshift reached " + registers[input.to])};
      input.done = true
    }
    return registers;
  },
  numAnd: (registers, input) => {
    if( input.done != true && registers[input.from2] != null) {
      registers[input.to] = Number(input.from1) & registers[input.from2];
      input.done = true
    }
    return registers;
  },
  and: (registers, input) => {
    if( input.done != true && registers[input.from1] != null && registers[input.from2] != null) {
      registers[input.to] = registers[input.from1] & registers[input.from2];
      input.done = true
    }
    return registers;
  },
  or: (registers, input) => {
    if( input.done != true && registers[input.from1] != null && registers[input.from2] != null) {
      registers[input.to] = registers[input.from1] | registers[input.from2];
      input.done = true
    }
    return registers;
  }
}

var remainingInputs = (inputList) => {
  return inputList.filter((input)=>{return !input.done;}).length;
}

var allRemainingInputs = () => {
  return Object.keys(inputs).reduce((count,inputListKey)=>{return count+remainingInputs(inputs[inputListKey])},0);
}

var run = (registers) => {
  while(allRemainingInputs() > 0) {
    Object.keys(inputs).forEach((inputListKey)=>{registers = inputs[inputListKey].reduce(commands[inputListKey],registers);});
  }

  return registers;
}

var registers = run({});
console.log("Part 1: " + registers.a);

Object.keys(inputs).forEach((inputListKey)=>{inputs[inputListKey].forEach((input)=>{delete input.done})});
// since we are setting 'b' ourselves, we need to disable whatever is setting 'b' from the instructions
inputs["numAssign"].filter((input)=>{return input.to=="b"})[0].done=true;
registers = run({b:registers.a});
console.log("Part 2: " + registers.a);
