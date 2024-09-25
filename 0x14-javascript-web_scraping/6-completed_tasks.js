#!/usr/bin/node
//  a script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

if (!url) {
  process.exit(1);
}

request(url, (err, response, body) => {
  if (err) {
    console.log(`${err}`);
    process.exit(1);
  }

  const data = JSON.parse(body);
  const completedTask = {};

  for (const task of data) {
    if (task.completed) {
      if (!completedTask[task.userId]) {
        completedTask[task.userId] = 0;
      }
      completedTask[task.userId]++;
    }
  }

  for (const x in completedTask) {
    console.log(`${x}: ${completedTask[x]}`);
  }
});
