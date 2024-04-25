#!/usr/bin/node

exports.esrever = function (list) {
  let listlen = list.length - 1;
  let j = 0;
  while ((listlen - j) > 0) {
    const temp = list[listlen];
    list[listlen] = list[j];
    list[j] = temp;
    j++;
    listlen--;
  }
  return list;
};
