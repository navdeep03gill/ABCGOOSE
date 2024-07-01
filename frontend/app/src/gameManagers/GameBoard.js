// GameBoard.js
import React from "react";
import { useNavigate } from "react-router-dom";
import GameResults from "../components/gameResults";

const GameBoard = ({
  title,
  time,
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
}) => {
  const navigate = useNavigate();

  return (
    <div className="container">
      <div className="top-header">
        <h1 className="font-semibold title">ABCGoose</h1>
      </div>
      <div className="grid grid-flow-col grid-rows-2">
        <h2 className="text-2xl">{title}</h2>
      </div>
      {timeVisible ? (
        <div className="flex items-center justify-center space-x-2">
          <p id="timerText1">{timerText1}</p>
          <span id="timer">{seconds}</span>
          <p id="timerText2">{timerText2}</p>
        </div>
      ) : null}
      <div className="grid grid-flow-col grid-rows-2">
        <p className="d-flex justify-content-center">
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
              className="btn btn-blue btn-primary send-button"
              onClick={getInput}
            >
              Send
            </button>
          ) : null}
        </div>
      </div>
      <h3 className="font-semibold game-message">{gameMessage}</h3>
      {showPlayButton && !pageEntry ? (
        <GameResults data={allGuesses}></GameResults>
      ) : (
        showPlayButton
      )}
    </div>
  );
};

export default GameBoard;
