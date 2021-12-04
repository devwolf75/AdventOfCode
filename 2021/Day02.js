let aocDoc;
fetch("https://adventofcode.com/2021/day/2/input")
  .then(function (response) {
    return response.text();
  })
  .then(function (html) {
    var parser = new DOMParser();
    aocDoc = parser.parseFromString(html, "text/html");
  })
  .catch(function (err) {
    console.error(err);
  });

// https://adventofcode.com/2021/day/1/input
directions = document.body
  .querySelectorAll("pre")[0]
  .innerHTML.trim()
  .split("\n")
  .map((x) => {
    x = x.split(" ");
    x[1] = +x[1];
    return x;
  });

testDirections = [
  "forward 5",
  "down 5",
  "forward 8",
  "up 3",
  "down 8",
  "forward 2",
];

testDirections = testDirections.map((x) => {
  x = x.split(" ");
  x[1] = +x[1];
  return x;
});

// Part 1
horiz = 0;
depth = 0;
directions.forEach(([position, amount]) => {
  switch (position) {
    case "forward":
      horiz += amount;
      break;
    case "up":
      depth -= amount;
      break;
    case "down":
      depth += amount;
      break;
  }
});
console.log(horiz * depth);

// Part 2
horiz = 0;
depth = 0;
aim = 0;
directions.forEach(([position, amount]) => {
  switch (position) {
    case "forward":
      horiz += amount;
      depth += aim * amount;
      break;
    case "up":
      aim -= amount;
      break;
    case "down":
      aim += amount;
      break;
  }
});
console.log(horiz * depth);
