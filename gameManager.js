//const res = require("express/lib/response");

var messages = document.getElementById('messages');
var input = document.getElementById('input');
var promptOutput = document.getElementById('definition');
var score = document.getElementById('score');
var gameMessage = document.getElementById('gameMessage');
var playButton = document.getElementById('playAgainButton');
var timerText1 = document.getElementById('timerText1');
var timerText2 = document.getElementById('timerText2');

var timer; 
var timeLeft = 10;
var currGuess;
var firstApiCall = true;

function resetGame(){
    timeLeft = 10;
    firstApiCall = true;
    gameMessage.textContent = "";
    playAgainButton.style.visibility = "hidden";
    console.log("game resetted");
    return;
}

function updateTimer(){
    timeLeft -= 1;
    if (timeLeft >= 0){
        $("#timer").html(timeLeft);
        if (timeLeft == 0) gameOver();
    }
    else { gameOver(); }
}

// What to do when the timer runs out
// IMPORTANT: run playbutton request before cancelInterval(timer)
function gameOver() {
    // This cancels the setInterval, so the updateTimer stops getting called
    playButton.textContent = "Play again!";
    playButton.style.visibility = "visible";
    clearInterval(timer);
    input.style.visibility = "hidden";
    sendButton.style.visibility = "hidden";
    showAnswer();
}

//show syns for last unguessed word
function showAnswer(){
    gameMessage.textContent = "Time's up!\nPlay Again!\n";
}


function start() {
    // input.style.visibility = "visible";
    // sendButton.style.visibility = "visible";
    // gameMessage.textContent = "Make a Guess!";
    // timerText1.textContent = "You have";
    // timerText2.textContent = " seconds left";

    if (timeLeft == 0 || playAgainButton.textContent == "Play again!"){
        resetGame();
        //location.reload();
    }
    input.style.visibility = "visible";
    sendButton.style.visibility = "visible";
    gameMessage.textContent = "Make a Guess!";
    timerText1.textContent = "You have";
    timerText2.textContent = " seconds left";

    timer = setInterval(updateTimer, 1000);
  
    // It will be a whole second before the time changes, so we'll call the update
    // once ourselves
    playAgainButton.style.visibility = "hidden";
  
    updateTimer(); 
}


