/*

  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */

function reverseString(str) {
  var new_string = ""
  for (var i = str.length-1; i >= 0; i--) {
    new_string +=  str[i]
  }
  return new_string
}

//TEST CODE FOR REVERSE
console.log(reverseString(str1)) // Expected: erutaerc
console.log(reverseString(str2)) // Expected: god
console.log(reverseString(str3)) // Expected: olleh
console.log(reverseString(str4)) // Expected: ""


// Method 2
// split 
// function reverseString(str) {
//   return str.split("").reverse().join("")
// }

// splitting is splitting each index of the string into an array
// reverse is taking the elements in that array so that the last one comes first
//   doing swap halfway through the array


// Method 3
// function reverseString(str) {
//   let newStr = ""
//   for (let i = 0; i < str.length; i++){
//     new Str = str[i] + newStr
//   }
// }