import { useState, useEffect } from 'react';

const fetchAuthToken = async () => {
  let url = 'http://127.0.0.1:5000/get-csrf-token';
  try {
    const response = await fetch(url, { method: 'GET' });
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const data = await response.json();
    const token = data['csrf_token'];
    return token;
  } catch (error) {
    console.error(error.message);
  }
};

const fetchAllWords = async () => {
  const url = 'http://127.0.0.1:5000/thesaurus/get_words';
  const auth_token = await fetchAuthToken();
  const headers = { Authorization: auth_token };
  return fetch(url, { method: 'GET', headers: headers })
    .then((response) => response.json())
    .then((data) => {
      return data;
    });
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
      console.error('Error fetching allWords: ', error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);
  return [allWords, fetchData];
};

export default useFetchWords;
