const createHTTPError = (status: number): Error =>
  new Error(statusCodeToErrorMsg(status));

const statusCodeToErrorMsg = (status: number): string => {
  if (status === 200) {
    return 'OK.';
  } else if (status === 429) {
    return 'You are doing that too often. Please try again in one minute.';
  } else if (status === 504) {
    return 'Server is not responding. Please try again later.';
  } else if (status === 0) {
    return 'Cannot connect to server. Check your internet connection, or try again later.';
  } else {
    return `Received unexpected status code ${status}.`;
  }
};

export default createHTTPError;
