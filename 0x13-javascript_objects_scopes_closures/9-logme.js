#!/usr/bin/node
/* A function that prints the number of arguments already printed
and the new argument value. */
let narg = 0;

exports.logMe = function (item) {
  console.log(narg + ': ' + item);
  narg++;
};
