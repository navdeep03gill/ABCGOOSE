import React from 'react';
import '../css/SimilarityPopup.css';

const SimilarityPopup = ({ isVisible, confidence, isSynonym, onClose }) => {
  if (!isVisible) return null;

  const percentage = (confidence * 100).toFixed(2);
  const message = isSynonym
    ? `Correct! Similarity: ${percentage}%`
    : `Incorrect! Similarity: ${percentage}%`;

  return (
    <div className={`popup ${isSynonym ? 'success' : 'failure'}`}>
      <div className='popup-content'>
        <p>{message}</p>
      </div>
    </div>
  );
};

export default SimilarityPopup;
