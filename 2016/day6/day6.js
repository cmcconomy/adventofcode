var delimiter = "\n";
var input = document.body.textContent.split(delimiter);
input = input.filter((item)=>{return item.length > 0});

var clone = (obj) => {return Object.assign({},obj)};
// input = "";

var transform = (collector, value) => {
  for( var i=0; i<8; i++ ){
    if( collector[i][value.charAt(i)] == null ) {
      collector[i][value.charAt(i)] = 0;
    }
    collector[i][value.charAt(i)]++;
  }
  return collector;
}

var collector = [{},{},{},{},{},{},{},{}];
collector = input.reduce(transform, collector);
var counts = collector.map((col)=>{
  var counts = [];
  Object.keys(col).forEach((key)=>{
    counts.push({key:key,count:col[key]});
  });
  return counts;
});

var countSortDesc = (c1,c2) => {
  if(c1.count>c2.count)return -1;
  if(c1.count<c2.count)return 1;
  return 0;
}

var countSortAsc = (c1,c2) => {
  if(c1.count<c2.count)return -1;
  if(c1.count>c2.count)return 1;
  return 0;
}

counts = counts.map((count)=>{return count.sort(countSortDesc)});
console.log("Part 1: " + counts.map((c)=>{return c[0].key}).join(''));

counts = counts.map((count)=>{return count.sort(countSortAsc)});
console.log("Part 2: " + counts.map((c)=>{return c[0].key}).join(''));
