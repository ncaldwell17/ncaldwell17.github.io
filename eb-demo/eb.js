/* exported getData */
/* exported launch_function */
/* global document */
/* global window */

// First, checks if it isn't implemented yet.
if (!String.prototype.format) {
  String.prototype.format = function() {
    var args = arguments;
    return this.replace(/{(\d+)}/g, function(match, number) { 
      return typeof args[number] != 'undefined'
        ? args[number]
        : match
      ;
    });
  };
}

function getData(someInput) {
    someInput = document.getElementById('entryBox').value;
    someInput = someInput.toLowerCase();
    console.log(someInput);
    console.log(typeof(someInput));
    return someInput;
}