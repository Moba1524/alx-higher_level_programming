#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body);
    let completed = {};
    data.forEach((element) => {
      if (element.completed && completed[element.userId] === undefined) {
        completed[element.userId] = 1;
      } else if (element.completed) {
        completed[element.userId] += 1;
      }
    });
    console.log(completed);
  }
});
