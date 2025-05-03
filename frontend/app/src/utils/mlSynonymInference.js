let cachedToken = null;

const fetchCachedAuthToken = async () => {
  if (cachedToken) return cachedToken;
  let url = `${process.env.REACT_APP_SSL_BACKEND_URL}/auth/get-auth-token`;
  try {
    const response = await fetch(url, { method: 'GET' });
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const data = await response.json();
    const token = data['auth_token'];
    cachedToken = token;
    return token;
  } catch (error) {
    console.error(error.message);
  }
};

export const checkSynonymsML = async (word1, word2) => {
  let url = `${process.env.REACT_APP_SSL_BACKEND_URL}/ml/get_inference`;
  const auth_token = await fetchCachedAuthToken();
  const ml_headers = {
    Authorization: auth_token,
    'Content-Type': 'application/json',
  };
  const word_guess = {
    word1: word1,
    word2: word2,
  };
  try {
    const response = await fetch(url, {
      method: 'POST',
      body: JSON.stringify(word_guess),
      headers: ml_headers,
    });
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const data = await response.json();
    const formattedData = {
      confidence: data['confidence'],
      isSynonym: data['is_synonym'],
    };
    return formattedData;
  } catch (error) {
    console.error(error.message);
  }
};
