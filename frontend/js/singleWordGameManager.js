

var messages = document.getElementById('messages');
var input = document.getElementById('input');
var promptOutput = document.getElementById('definition');
var score = document.getElementById('score');
var gameMessage = document.getElementById('gameMessage');
var playButton = document.getElementById('playAgainButton');
var timerText1 = document.getElementById('timerText1');
var timerText2 = document.getElementById('timerText2');

var timer; 
var timeLeft = 30;
var currGuess;
var currPrompt = null;
var allWords = null;
var synonymList = null;
var currIdx = null;
var correctGuesses = [];


function getInput(){
    if (input.value) {
        currGuess = input.value;
        input.value = '';
        evaluateAnswer();
    }
}

function evaluateAnswer(){
    currGuess = (currGuess).toLowerCase();

    if (correctGuesses.includes(currGuess)){
        gameMessage.textContent = "You Already Guessed This Word! Keep Trying!";
    }
    else if(currPrompt.synonyms.includes(currGuess)){
        console.log(synonymList);

        var currScore = synonymList[currGuess];

        console.log(currScore);

        score.textContent = (parseInt(score.textContent) + currScore).toString();
        gameMessage.textContent = "Correct Guess! Next Word:";
        correctGuesses.push(currGuess);
        getPrompt();
    }
    else {
        gameMessage.textContent = "Incorrect Guess! Keep Trying!";
    }
}

function resetGame(){
    timeLeft = 30;
    gameMessage.textContent = "";
    playAgainButton.style.visibility = "hidden";
    currPrompt = null;
    currGuess = '';
    score.textContent = (0).toString();
    currIdx = Math.floor(Math.random() * allWords.length) ;
    console.log("game resetted");
    // if (currIdx == null || currIdx >= allWords.length){
    //     var max = allWords.length
    //     var idx = Math.floor(Math.random() * max) ;
    //     currIdx = idx;
    // }
    // else{
    //     currIdx += 1;
    // }
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

    timerText1.style.visibility = "hidden";
    timerText2.style.visibility = "hidden";
    
    $("#timer").html(null);
    
    showAnswer();
}


function getPrompt() {
    if (currIdx == null || currIdx >= allWords.length){
        var max = allWords.length
        var idx = Math.floor(Math.random() * max) ;
        currIdx = idx;
    }
    console.log(currIdx);

    const newWord = allWords[currIdx];
    synonymList = newWord.synonyms;
    const newSynList = Object.keys(synonymList);
    synonymList = newWord.synonyms;
    console.log(synonymList);

    currPrompt = {
        word: newWord.word,
        definition: newWord.definition, 
        synonyms: newSynList
    };
    console.table(currPrompt);
    promptOutput.value = currPrompt.word + ":\n" + currPrompt.definition;
}

//show syns for last unguessed word
function showAnswer(){
    gameMessage.textContent = "Time's up!\nPlay Again!\n";
    output = "Time's up! The synonyms for " + currPrompt.word + " are:\n";
    for(syn of currPrompt.synonyms){
        output += syn + ", ";
    }
    promptOutput.style.height = '200px';
    promptOutput.value = output.slice(0,-2);
}


function start() {
    if (timeLeft == 0 || playAgainButton.textContent == "Play again!"){
        resetGame();
    }
    getPrompt();
    promptOutput.style.height = '100px';
    input.style.visibility = "visible";
    sendButton.style.visibility = "visible";
    gameMessage.textContent = "Make a Guess!";

    timerText1.style.visibility = "visible";
    timerText2.style.visibility = "visible";

    timerText1.textContent = "You have";
    timerText2.textContent = " seconds left";

    timer = setInterval(updateTimer, 1000);
  
    // It will be a whole second before the time changes, so we'll call the update
    // once ourselves
    playAgainButton.style.visibility = "hidden";
  
    updateTimer(); 
}

$(document).on("keypress", function(e) {
    if(e.which == 13) {
        console.log("success");
        getInput();
    }
});


function displayResult(result){
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '<h2>Result:</h2>';
    for (const wordName in result) {
        const wordInfo = result[wordName];
        resultDiv.innerHTML += `<p><strong>${wordName}</strong></p>`;
        resultDiv.innerHTML += `<p>Definition: ${wordInfo.definition}</p>`;
        if (Object.keys(wordInfo.synonyms).length > 0) {
            resultDiv.innerHTML += '<p>Synonyms:</p>';
            resultDiv.innerHTML += '<ul>';
            for (const synonym in wordInfo.synonyms) {
                const score = wordInfo.synonyms[synonym];
                resultDiv.innerHTML += `<li>${synonym}: ${score}</li>`;
            }
            resultDiv.innerHTML += '</ul>';
        }
    }
}


function fetchAllWords(){
    fetch(`http://127.0.0.1:5000/api/words`)
        .then((response) => response.json())
        .then((data) => {
            allWords = data;
            //allWords = JSON.stringify(allWords);
            console.log(allWords);
        }
    );
}

fetchAllWords();
