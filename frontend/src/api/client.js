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

// Event & Attendee APIs
export const getAttendees = (eventId, token) =>
  apiFetch(`/events/${eventId}/attendees`, { token });

export const raiseHand = (eventId, handRaised, token) =>
  apiFetch(`/events/${eventId}/raise-hand`, {
    method: 'POST',
    data: { hand_raised: handRaised },
    token,
  });

export const promoteSpeaker = (eventId, userId, isSpeaker, token) =>
  apiFetch(`/events/${eventId}/promote-speaker`, {
    method: 'POST',
    data: { user_id: userId, is_speaker: isSpeaker },
    token,
  });

// Q&A APIs
export const getQuestions = (eventId, token) =>
  apiFetch(`/events/${eventId}/questions`, { token });

export const submitQuestion = (eventId, content, token) =>
  apiFetch(`/events/${eventId}/questions`, {
    method: 'POST',
    data: { content },
    token,
  });

export const upvoteQuestion = (eventId, questionId, token) =>
  apiFetch(`/events/${eventId}/questions/${questionId}/upvote`, {
    method: 'POST',
    token,
  });

export const markQuestionAnswered = (eventId, questionId, token) =>
  apiFetch(`/events/${eventId}/questions/${questionId}/answer`, {
    method: 'POST',
    token,
  });

// Live Poll APIs
export const getPolls = (eventId, token) =>
  apiFetch(`/events/${eventId}/polls`, { token });

export const createPoll = (eventId, pollData, token) =>
  apiFetch(`/events/${eventId}/polls`, {
    method: 'POST',
    data: pollData,
    token,
  });

export const votePoll = (eventId, pollId, optionIndex, token) =>
  apiFetch(`/events/${eventId}/polls/${pollId}/vote`, {
    method: 'POST',
    data: { option_index: optionIndex },
    token,
  });

// Archive & Multilingual APIs
export const searchArchive = (q = '', language = '') => {
  const params = new URLSearchParams();
  if (q) params.append('q', q);
  if (language) params.append('language', language);
  const queryStr = params.toString() ? `?${params.toString()}` : '';
  return apiFetch(`/archive/search${queryStr}`);
};

export const getCorpus = () => apiFetch('/archive/corpus');

export const populateDemoAi = (eventId, token) =>
  apiFetch(`/archive/${eventId}/populate-demo-ai`, {
    method: 'POST',
    token,
  });

// WhatsApp Bot Simulator API
export const simulateWhatsApp = (message, phone = '+919876543210', name = 'Village Volunteer') =>
  apiFetch('/webhook/whatsapp/simulate', {
    method: 'POST',
    data: { message, phone, name },
  });


// In-Room Live Chat APIs
export const getChatMessages = (eventId, token) =>
  apiFetch(`/events/${eventId}/chat`, { token });

export const sendChatMessage = (eventId, content, token) =>
  apiFetch(`/events/${eventId}/chat`, {
    method: 'POST',
    data: { content },
    token,
  });

// Replay-as-Live & Clock Synchronization
export const startReplay = (eventId, token) =>
  apiFetch(`/events/${eventId}/replay-start`, {
    method: 'POST',
    token,
  });

export const getSyncClock = (eventId) =>
  apiFetch(`/events/${eventId}/sync-clock`);

// Host Heartbeat & Disconnect Failover
export const sendHeartbeat = (eventId, token) =>
  apiFetch(`/events/${eventId}/heartbeat`, {
    method: 'POST',
    token,
  });

export const getFailoverStatus = (eventId) =>
  apiFetch(`/events/${eventId}/failover-status`);

// Offline Pack Download URL
export const getOfflinePackUrl = (eventId) =>
  `${BACKEND_URL}/archive/${eventId}/offline-pack`;
