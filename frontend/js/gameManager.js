class gameManager {
  constructor(time, gameMode) {
    this.messages = document.getElementById("messages");
    this.input = document.getElementById("input");
    this.promptOutput = document.getElementById("definition");
    this.score = document.getElementById("score");
    this.gameMessage = document.getElementById("gameMessage");
    this.playButton = document.getElementById("playAgainButton");
    this.timerText1 = document.getElementById("timerText1");
    this.timerText2 = document.getElementById("timerText2");
    this.sendButton = document.getElementById("sendButton");
    this.gameTime = time;

    this.currIdx = null;

    this.timer;
    this.timeLeft = time;
    this.correctGuesses = [];
    this.allWords = null;
    this.currPrompt = null;
    this.synonymList = null;

    this.gameMode = gameMode;

    this.fetchAllWords();
    this.startEventListener();
  }

  fetchAllWords() {
    let url = "http://127.0.0.1:5000/api/v1/words";
    let username = "admin";
    let password = "SuperSecretPwd";
    let headers = { Authorization: "Basic " + btoa(`${username}:${password}`) };
    fetch(url, { method: "GET", headers: headers })
      .then((response) => response.json())
      .then((data) => {
        this.allWords = data;
        console.log(this.allWords);
      });
  }

  getInput = () => {
    if (this.input.value) {
      var currGuess = input.value;
      this.input.value = "";
      currGuess = currGuess.toLowerCase();
      console.log(currGuess);
      this.evaluateAnswer(currGuess);
    }
  };

  startEventListener = () => {
    $(document).on("keypress", (e) => {
      if (e.which == 13) {
        this.getInput();
      }
    });
  };

  evaluateAnswer(currGuess) {
    console.log(this.currPrompt.synonyms);
    if (this.correctGuesses.includes(currGuess)) {
      this.gameMessage.textContent =
        "You Already Guessed This Word! Keep Trying!";
    } else if (this.synonymList.includes(currGuess)) {
      var addPoints = 100;
      this.score.textContent = (
        parseInt(this.score.textContent) + addPoints
      ).toString();
      this.gameMessage.textContent = "Correct Guess! Next Word:";
      this.correctGuesses.push(currGuess);
      this.getPrompt();
    } else {
      this.gameMessage.textContent = "Incorrect Guess! Keep Trying!";
    }
  }

  resetGame() {
    this.timeLeft = this.gameTime;
    this.gameMessage.textContent = "";
    this.playButton.style.visibility = "hidden";
    this.currPrompt = null;
    this.score.textContent = (0).toString();
    this.correctGuesses = [];
    console.log("game resetted");
    return;
  }

  gameOver = () => {
    // This cancels the setInterval, so the updateTimer stops getting called
    this.playButton.textContent = "Play again!";
    this.playButton.style.visibility = "visible";
    clearInterval(this.timer);
    this.input.style.visibility = "hidden";
    this.sendButton.style.visibility = "hidden";
    this.timerText1.style.visibility = "hidden";
    this.timerText2.style.visibility = "hidden";
    $("#timer").html(null);
    this.showAnswer();
  };

  updateTimer = () => {
    this.timeLeft -= 1;
    if (this.timeLeft >= 0) {
      $("#timer").html(this.timeLeft);
      if (this.timeLeft == 0) this.gameOver();
    } else {
      this.gameOver();
    }
  };

  getPrompt() {
    if (this.gameMode == 2) {
      var max = this.allWords.length;
      var idx = Math.floor(Math.random() * max);
      this.currIdx = idx;
    }
    const newWord = this.allWords[this.currIdx];
    this.synonymList = newWord.synonyms;
    this.currPrompt = {
      word: newWord.word,
      definition: newWord.definition,
      synonyms: this.synonymList,
    };
    console.table(this.currPrompt);
    console.log(this.currPrompt.synonyms);

    this.promptOutput.value =
      "Word: " +
      this.currPrompt.word +
      "\n" +
      "Definition: " +
      this.currPrompt.definition;
  }

  showAnswer() {
    this.gameMessage.textContent = "Time's up!\nPlay Again!\n";
    var output =
      "Time's up! The synonyms for " + this.currPrompt.word + " are:\n";
    console.log(this.currPrompt.synonyms);
    for (const syn of this.currPrompt.synonyms) {
      console.log(syn);
      output += syn + ", ";
    }
    this.promptOutput.value = output.slice(0, -2);
  }

  start() {
    if (this.timeLeft == 0 || this.playButton.textContent == "Play again!") {
      this.resetGame();
    }
    this.getPrompt();
    this.input.style.visibility = "visible";
    this.sendButton.style.visibility = "visible";
    this.gameMessage.textContent = "Make a Guess!";

    this.timerText1.style.visibility = "visible";
    this.timerText2.style.visibility = "visible";

    this.timerText1.textContent = "You have";
    this.timerText2.textContent = " seconds left";

    this.timer = setInterval(this.updateTimer, 1000);

    // It will be a whole second before the time changes, so we'll call the update
    // once ourselves
    this.playButton.style.visibility = "hidden";

    this.updateTimer();
  }

  displayResult(result) {
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "<h2>Result:</h2>";
    for (const wordName in result) {
      const wordInfo = result[wordName];
      resultDiv.innerHTML += `<p><strong>${wordName}</strong></p>`;
      resultDiv.innerHTML += `<p>Definition: ${wordInfo.definition}</p>`;
      if (Object.keys(wordInfo.synonyms).length > 0) {
        resultDiv.innerHTML += "<p>Synonyms:</p>";
        resultDiv.innerHTML += "<ul>";
        for (const synonym in wordInfo.synonyms) {
          const score = wordInfo.synonyms[synonym];
          resultDiv.innerHTML += `<li>${synonym}: ${score}</li>`;
        }
        resultDiv.innerHTML += "</ul>";
      }
    }
  }
  test() {
    console.log("hello world");
  }
}

class singleWordGameManager extends gameManager {
  constructor() {
    super();
  }
  getPrompt() {
    if (this.currIdx == null || this.currIdx >= this.allWords.length) {
      var max = this.allWords.length;
      var idx = Math.floor(Math.random() * max);
      this.currIdx = idx;
    }
    console.log(this.currIdx);

    const newWord = this.allWords[this.currIdx];
    this.synonymList = newWord.synonyms;
    this.currPrompt = {
      word: newWord.word,
      definition: newWord.definition,
      synonyms: this.synonymList,
    };
    console.table(this.currPrompt);
    console.log(this.currPrompt.synonyms);
    this.promptOutput.value =
      "Word: " +
      this.currPrompt.word +
      "\n" +
      "Definition: " +
      this.currPrompt.definition;
  }
}

var gameOn = new gameManager(60, 2);
