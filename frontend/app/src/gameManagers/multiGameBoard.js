import React from "react";
import useGameLogic from "./useGameLogic";
import GameBoard from "./GameBoard";

function MultiGameBoard({ time, allWords }) {
  const gameMode = "multiWord";
  const gameLogic = useGameLogic(time, allWords, gameMode);

  return <GameBoard title="Game Mode 2: Many Words, 30 sec" {...gameLogic} />;
}

export default MultiGameBoard;
