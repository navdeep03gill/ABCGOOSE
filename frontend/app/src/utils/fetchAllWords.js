import axios from "axios";
import { useState, useEffect } from "react";

const fetchAllWords = () => {
  let url = "http://127.0.0.1:5000/api/v1/words";
  let username = "admin";
  let password = "SuperSecretPwd";
  let headers = { Authorization: "Basic " + btoa(`${username}:${password}`) };
  return fetch(url, { method: "GET", headers: headers })
    .then((response) => response.json())
    .then((data) => {
      // Return the fetched data
      return data;
    });
};

const useFetchWords = () => {
  const [allWords, setAllWords] = useState([]);

  useEffect(() => {
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
        console.error("Error fetching allWords: ", error);
      }
    };
    fetchData();
  }, []);

  console.log("useFetchWords", allWords.length);
  return allWords;
};

export default useFetchWords;
