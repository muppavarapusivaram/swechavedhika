const BACKEND_URL =
  import.meta.env.VITE_BACKEND_URL || 'http://localhost:8000';

export async function apiFetch(path, { method = 'GET', data, token, headers = {} } = {}) {
  const url = `${BACKEND_URL}${path}`;
  const reqHeaders = {
    'Content-Type': 'application/json',
    ...headers,
  };

  if (token) {
    reqHeaders['Authorization'] = `Bearer ${token}`;
  }

  const config = {
    method,
    headers: reqHeaders,
  };

  if (data !== undefined && method !== 'GET' && method !== 'HEAD') {
    config.body = JSON.stringify(data);
  }

  const response = await fetch(url, config);

  let responseData = null;
  const contentType = response.headers.get('content-type');
  if (contentType && contentType.includes('application/json')) {
    try {
      responseData = await response.json();
    } catch {
      responseData = null;
    }
  } else {
    try {
      responseData = await response.text();
    } catch {
      responseData = null;
    }
  }

  if (!response.ok) {
    const error = new Error(
      responseData?.detail || responseData?.message || `Request failed with status ${response.status}`
    );
    error.status = response.status;
    error.data = responseData;
    throw error;
  }

  return responseData;
}
