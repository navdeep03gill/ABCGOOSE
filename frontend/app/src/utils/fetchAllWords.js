import { useState, useEffect } from 'react';
import { fetchAuthToken } from './fetchAuthToken';

const fetchAllWords = async () => {
  const url = `${process.env.REACT_APP_NEW_BACKEND_URL}/thesaurus/get_words`;
  const auth_token = await fetchAuthToken();
  const headers = { Authorization: auth_token };

  try {
    const response = await fetch(url, { method: 'GET', headers: headers });
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error(error.message);
  }
};

const useFetchWords = () => {
  const [allWords, setAllWords] = useState([]);
  const fetchData = async () => {
    try {
      const data = await fetchAllWords();
      let improvedData = data.map((word) => {
        return {
          ...word,
          synonyms: word.synonyms.map((synonym) => synonym.toLowerCase()),
        };
      });
      setAllWords(improvedData);
    } catch (error) {
      console.error('Error fetching allWords:\n', error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return [allWords, fetchData];
};

export default useFetchWords;
