import { useState, useEffect } from 'react';
import { fetchAuthToken } from './fetchAuthToken';

const fetchAllMLWords = async () => {
  const url = `${process.env.REACT_APP_NEW_BACKEND_URL}/ml/get_ml_words`;
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

const useFetchMLWords = () => {
  const [allWords, setAllWords] = useState([]);
  const fetchData = async () => {
    try {
      const data = await fetchAllMLWords();
      if (data) {
        setAllWords(data);
      } else {
        console.error('fetchAllMLWords returned no data');
      }
    } catch (error) {
      console.error('Error fetching allWords:\n', error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return [allWords, fetchData];
};

export default useFetchMLWords;
