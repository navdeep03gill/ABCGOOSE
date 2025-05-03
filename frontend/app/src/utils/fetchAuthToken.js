export const fetchAuthToken = async () => {
  const url = `${process.env.REACT_APP_NEW_BACKEND_URL}/auth/get-auth-token`;
  try {
    const response = await fetch(url, { method: 'GET' });
    if (!response.ok) {
      throw new Error(
        `Failed to fetch auth token. Response status: ${response.status}`
      );
    }
    const data = await response.json();
    return data['auth_token'];
  } catch (error) {
    console.error('Error fetching auth token:', error.message);
    throw error; // Re-throw the error to handle it in the calling function
  }
};
