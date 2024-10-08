// useGameLogic.js
import { useState, useEffect } from 'react';
import { useNumGameContext } from '../utils/numGamesContext';

const useGameLogic = (time, allWords, gameMode) => {
  const [inputBoxShow, setInputBoxShow] = useState(false);
  const [sendButtonShow, setSendButtonShow] = useState(false);
  const [input, setInput] = useState(null);
  const [promptOutput, setPromptOutput] = useState('');
  const [score, setScore] = useState(0);
  const [gameMessage, setGameMessage] = useState('');
  const [playButton, setPlayButton] = useState('New Game');
  const [showPlayButton, setShowPlayButton] = useState(true);
  const [timerText1, setTimerText1] = useState('');
  const [timerText2, setTimerText2] = useState('');
  const [timeVisible, setTimeVisible] = useState(false);
  const [seconds, setSeconds] = useState(time);
  const [isRunning, setIsRunning] = useState(null);
  const [currPrompt, setCurrPrompt] = useState(null);
  const [correctGuesses, setCorrectGuesses] = useState([]);
  const [allGuesses, setAllGuesses] = useState([]);
  const [pageEntry, setPageEntry] = useState(true);

  const { numConsecutiveGames, setNumConsecutiveGames } = useNumGameContext();

  let currIdx = null;

  useEffect(() => {
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

  const startTimer = () => {
    setIsRunning(true);
  };

  const resetTimer = () => {
    setIsRunning(false);
    setSeconds(0);
  };

  const getInput = () => {
    if (input) {
      let currGuess = input.toLowerCase();
      setInput('');
      evaluateAnswer(currGuess);
    }
  };

  const getPrompt = () => {
    let max = allWords.length;
    let idx = Math.floor(Math.random() * max);
    currIdx = idx;
    const newWord = allWords[currIdx];
    const newPrompt = {
      word: newWord.word,
      definition: newWord.definition,
      synonyms: newWord.synonyms,
    };
    setCurrPrompt(newPrompt);
  };

  const evaluateAnswer = (currGuess) => {
    if (!currPrompt.synonyms.includes(currGuess)) {
      setGameMessage('Incorrect Guess! Keep Trying!');
      setAllGuesses((guesses) => [...guesses, [currGuess, currPrompt.word, 0]]);
    } else if (correctGuesses.includes(currGuess)) {
      setGameMessage('You Already Guessed This Word! Keep Trying!');
      setAllGuesses((guesses) => [...guesses, [currGuess, currPrompt.word, 2]]);
    } else {
      setScore(score + 100);
      setGameMessage('Correct Guess! Next Word:');
      setCorrectGuesses((prevItems) => [...prevItems, currGuess]);
      setAllGuesses((guesses) => [...guesses, [currGuess, currPrompt.word, 1]]);
      if (gameMode === 'multiWord') {
        getPrompt();
      }
    }
  };

  const resetGame = () => {
    setScore(0);
    setSeconds(time);
    setCorrectGuesses([]);
    setAllGuesses([]);
    setNumConsecutiveGames(numConsecutiveGames + 1);
  };

  const gameOver = () => {
    setGameMessage('');
    setPlayButton('Play Again!');
    setInputBoxShow(false);
    setSendButtonShow(false);
    setShowPlayButton(true);
    showAnswer();
  };

  const showAnswer = () => {
    let output = `Time's up!\nWord: ${currPrompt.word}\nDefinition: ${currPrompt.definition}\nThe synonyms for ${currPrompt.word} are:\n`;
    for (const syn of currPrompt.synonyms) {
      output += syn + ', ';
    }
    setPromptOutput(output.slice(0, -2));
  };

  const start = () => {
    if (seconds === 0 || seconds < 0 || playButton === 'Play Again!') {
      resetGame();
    }
    getPrompt();
    setInputBoxShow(true);
    setSendButtonShow(true);
    setShowPlayButton(false);
    setGameMessage('Make a Guess!');
    setTimerText1('You have');
    setTimerText2(' seconds left');
    setTimeVisible(true);
    startTimer();
    setPageEntry(false);
    setInput('');
  };

  const handleKeyPress = (event) => {
    if (event.key === 'Enter') {
      getInput();
    }
  };

  return {
    inputBoxShow,
    sendButtonShow,
    input,
    setInput,
    promptOutput,
    score,
    gameMessage,
    playButton,
    showPlayButton,
    timerText1,
    timerText2,
    timeVisible,
    seconds,
    start,
    getInput,
    handleKeyPress,
    pageEntry,
    allGuesses,
  };
};

export default useGameLogic;
