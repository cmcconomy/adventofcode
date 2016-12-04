var delimiter = "\n";
var input = document.body.textContent.split(delimiter);
input = input.filter((item)=>{return item.length > 0});

var clone = (obj) => {return Object.assign({},obj)};
// input = "";

var enrich = (room) => {
  var matches = room.match(/(.*)-(\d+)\[(\w+)\]/);
  return {
    name: matches[1],
    sectorId: Number(matches[2]),
    checksum: matches[3]
  };
}

input = input.map(enrich);

var count = (input) => {
  var count = input.name.split("").reduce((count,char)=>{
    if(char=="-") {return count;} // skip dashes
    if(count[char]==null) {count[char]=0;}
    count[char]++;
    return count
  },{});
  count = Object.keys(count).reduce((arr,char)=>{
    arr.push({char:char,count:count[char]});
    return arr;
  },[]);
  count = count.sort((a,b)=>{
    // look carefully: I implemented a reverse sort
    if(a.count<b.count){return 1}
    if(a.count>b.count){return -1}
    // we know they're equal in count.. what about alphabet
    if(a.char>b.char){return 1}
    if(a.char<b.char){return -1}
    return 0;
  });

  return count;
}

var isReal = (room) => {
  var calculatedChecksum = count(room).splice(0,5).reduce((str,charCount)=>{return str+charCount.char},"");
  return calculatedChecksum == room.checksum;
}

console.log("Part 1: " + input.filter(isReal).reduce((sum,room)=>{return sum+room.sectorId},0));

var rotateName = (room) => {
  room.realName = room.name.split("").reduce((realName,char) => {
    if(char == "-") { 
      realName += " ";
    }else {
      var realCharCode = char.charCodeAt(0)+room.sectorId%26;
      if( realCharCode > 122 ) {
        realCharCode -= 26;
      }
      realName += String.fromCharCode(realCharCode);
    }

    return realName;
  },"");

  return room;
}

console.log("Part 2: " + input.filter(isReal).map(rotateName).filter((room)=>{return room.realName.substr(0,5)=="north"})[0].sectorId);
