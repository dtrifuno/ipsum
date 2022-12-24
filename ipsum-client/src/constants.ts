const NODE_ENV = process.env.NODE_ENV;

export const baseUrl =
  NODE_ENV === 'development'
    ? 'http://localhost:3000'
    : 'https://ipsum.trifunovski.me';

export const baseApiUrl =
  NODE_ENV === 'development'
    ? 'http://localhost:8000'
    : 'https://ipsum.trifunovski.me';
