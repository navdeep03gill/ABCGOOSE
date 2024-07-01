import React from "react";
import "../css/table.css";

function GameResults({ data }) {
  const classify = (value) => {
    switch (value) {
      case 0:
        return "Incorrect Guess";
      case 1:
        return "Correct Guess";
      case 2:
        return "Already Guessed";
      default:
        return "Unknown";
    }
  };

  return (
    <div className="table-container">
      <table className="responsive-table">
        <thead>
          <tr>
            <th>String</th>
            <th>Classification</th>
          </tr>
        </thead>
        <tbody>
          {data.map(([string, number], index) => (
            <tr key={index}>
              <td>{string}</td>
              <td>{classify(number)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default GameResults;
