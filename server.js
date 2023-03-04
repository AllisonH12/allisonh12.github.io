const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/vote', function(req, res) {
  const voteValue = req.body.vote;
  fs.appendFile('votes.txt', voteValue + '\n', function(err) {
    if (err) throw err;
    console.log('Vote saved: ' + voteValue);
  });
  res.sendStatus(200);
});

app.listen(8000, function () {
  console.log('Server listening on port 8000');
});
