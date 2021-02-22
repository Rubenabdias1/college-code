var score = 45;    // Score
var msg = '';      // Message

function congratulate() {
  msg += 'Congratulations! ';
}

function hardLuck() {
  msg += 'Jolly bad luck! ';
}

if (score >= 50) {  // If score is 50 or more
  congratulate();
  msg += 'Proceed to the next round.';
} else {
  hardLuck();
  msg+= 'Have another go!';
}

var el = document.getElementById('answer');
el.innerHTML = msg;