let aocDoc;
fetch("https://adventofcode.com/2021/day/1/input")
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
depths = document.body
  .querySelectorAll("pre")[0]
  .innerHTML.trim()
  .split("\n")
  .map((x) => +x);

x = 0;
depths.reduce((prev, curr, idx, arr) => {
  if (idx != 0 && curr > prev) x++;
  return curr;
});
console.log(x);

let sum = (x, a) => a[x - 2] + a[x - 1] + a[x];
let counter = 0;
for (let i = 3; i < depths.length; i++) {
  if (sum(i, depths) > sum(i - 1, depths)) counter++;
}
