import React, { useState, useEffect } from "react";
import "../css/App.css";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function MultiWordGameBoard({ time, allWords }) {
  const [inputBoxShow, setInputBoxShow] = useState(false);
  const [sendButtonShow, setSendButtonShow] = useState(false);
  const [input, setInput] = useState(null);
  const [promptOutput, setPromptOutput] = useState("");
  const [score, setScore] = useState(0);
  const [gameMessage, setGameMessage] = useState("");
  const [playButton, setPlayButton] = useState("New Game");
  const [showPlayButton, setShowPlayButton] = useState(true);
  const [timerText1, setTimerText1] = useState("");
  const [timerText2, setTimerText2] = useState("");
  const [timeVisible, setTimeVisible] = useState(false);
  const [seconds, setSeconds] = useState(time);
  const [isRunning, setIsRunning] = useState(null);
  const [currPrompt, setCurrPrompt] = useState(null);
  const navigate = useNavigate();

  var currIdx = null;
  var correctGuesses = []; // may need state here, but I doubt it

  useEffect(() => {
    console.log(currPrompt);
    if (currPrompt && currPrompt.word && currPrompt.definition) {
      setPromptOutput(`Word: ${currPrompt.word} \n${currPrompt.definition}`);
    }
  }, [currPrompt]);

  useEffect(() => {
    let interval;
    if (isRunning) {
      interval = setInterval(() => {
        if (seconds > 0) {
          setSeconds((seconds) => seconds - 1);
        }
      }, 1000);
    }
    if (seconds === 0) {
      resetTimer();
      gameOver();
    }
    return () => clearInterval(interval);
  }, [seconds, isRunning]);

  function startTimer() {
    setIsRunning(true);
  }

  function resetTimer() {
    setIsRunning(false);
    setSeconds(0);
  }

  const getInput = () => {
    if (input) {
      var currGuess = input.toLowerCase();
      setInput("");
      evaluateAnswer(currGuess);
    }
  };

  const getPrompt = () => {
    if (currIdx == null || currIdx >= allWords.length) {
      var max = allWords.length;
      var idx = Math.floor(Math.random() * max);
      currIdx = idx;
    }
    const newWord = allWords[currIdx];
    console.log(newWord.synonyms);
    const newPrompt = {
      word: newWord.word,
      definition: newWord.definition,
      synonyms: newWord.synonyms,
    };
    setCurrPrompt(newPrompt);
  };

  const evaluateAnswer = (currGuess) => {
    if (correctGuesses.includes(currGuess)) {
      setGameMessage("You Already Guessed This Word! Keep Trying!");
    } else if (currPrompt.synonyms.includes(currGuess)) {
      setScore(score + 100);
      setGameMessage("Correct Guess! Next Word:");
      correctGuesses.push(currGuess);
      getPrompt();
    } else {
      setGameMessage("Incorrect Guess! Keep Trying!");
    }
  };

  const resetGame = () => {
    console.log("reset game");
    setScore(0);
    setSeconds(time);
    correctGuesses = [];
  };

  const gameOver = () => {
    setGameMessage("");
    setPlayButton("Play Again!");
    setInputBoxShow(false);
    setSendButtonShow(false);
    setShowPlayButton(true);
    showAnswer();
  };

  const showAnswer = () => {
    setGameMessage("Time's up!\nPlay Again!\n");
    var output = "Time's up! The synonyms for " + currPrompt.word + " are:\n";
    for (const syn of currPrompt.synonyms) {
      output += syn + ", ";
    }
    setPromptOutput(output.slice(0, -2));
  };

  const start = () => {
    if (seconds === 0 || seconds < 0 || playButton === "Play Again!") {
      resetGame();
    }
    getPrompt();
    setInputBoxShow(true);
    setSendButtonShow(true);
    setShowPlayButton(false);
    setGameMessage("Make a Guess!");
    setTimerText1("You have");
    setTimerText2(" seconds left");
    setTimeVisible(true);
    startTimer();
  };

  const handleKeyPress = (event) => {
    if (event.key === "Enter") {
      getInput();
    }
  };

  return (
    <div className="container">
      <div className="top-header">
        <h1 className="font-semibold title">ABCGoose</h1>
      </div>
      <div className="grid grid-flow-col grid-rows-2">
        <h2 className="text-2xl">Game Mode 2: Many Words, 30 sec</h2>
      </div>
      {timeVisible ? (
        <div className="flex items-center justify-center space-x-2">
          <p id="timerText1">{timerText1}</p>
          <span id="timer">{seconds}</span>
          <p id="timerText2">{timerText2}</p>
        </div>
      ) : null}
      <div className="grid grid-flow-col grid-rows-2">
        <p class="d-flex justify-content-center">
          Input the best synonym for the word below!
        </p>
      </div>
      <div className="grid grid-flow-col grid-cols-6 gap-1">
        <textarea
          value={promptOutput}
          disabled={true}
          rows="4"
          className="wordpromptarea block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white col-span-6"
        ></textarea>
        <div className="m-4 grid col-span-1 gap-3">
          <div className="grid-rows-1">
            <button
              className="btn-exit btn-blue btn-primary"
              id="playAgainButton"
              onClick={() => {
                navigate(`/`);
              }}
            >
              Exit Game
            </button>
          </div>
          <div>
            {showPlayButton ? (
              <button
                className="btn btn-blue btn-primary"
                id="playAgainButton"
                onClick={() => {
                  start();
                }}
              >
                {playButton}
              </button>
            ) : null}
          </div>
        </div>
      </div>
      <div className="grid grid-flow-col grid-rows-1">
        <h2 className="font-semibold scoretext">
          SCORE: <span>{score}</span>
        </h2>
      </div>
      <div className="grid grid-cols-3 gap-3 justify-center custom-grid">
        <div className="col-span-2 flex justify-end">
          {inputBoxShow ? (
            <input
              value={input}
              onInput={(e) => setInput(e.target.value)}
              className="gameInputBox"
              autocomplete="off"
              onKeyPress={handleKeyPress}
            />
          ) : null}
        </div>
        <div className="flex justify-start">
          {sendButtonShow ? (
            <button
              class="btn btn-blue btn-primary send-button"
              onClick={() => {
                getInput();
              }}
            >
              Send
            </button>
          ) : null}
        </div>
      </div>
      <h3 className="font-semibold game-message">{gameMessage}</h3>
    </div>
  );
}

export default MultiWordGameBoard;
