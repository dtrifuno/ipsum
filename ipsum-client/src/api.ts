import axios, {AxiosError} from 'axios';

import {baseApiUrl} from './constants';
import createHTTPError from './createHTTPError';
import {Language, SupportedLanguagesResponse} from './types';

export async function fetchSupportedLanguages(): Promise<Language[]> {
  const url = `${baseApiUrl}/api/v1/supported_languages`;

  try {
    const response = await axios.get<SupportedLanguagesResponse>(url);
    return response.data.supported_languages;
  } catch (exception) {
    return [];
  }
}

async function getOrThrowError<T>(url: string): Promise<T | undefined> {
  try {
    const response = await axios.get<T>(url);
    if (response.status === 200) {
      return response.data;
    }
  } catch (err: unknown) {
    if (err instanceof AxiosError) {
      const status = err.response?.status;
      throw createHTTPError(status || 0);
    }
  }
  return undefined;
}

export async function fetchWords(
  languageCode: string,
  count: number
): Promise<string[]> {
  const url = `${baseApiUrl}/api/v1/generate_words/${languageCode}?count=${count}`;
  const result = await getOrThrowError<string[]>(url);
  return result || [];
}

export async function fetchSentences(
  languageCode: string,
  count: number
): Promise<string[]> {
  const url = `${baseApiUrl}/api/v1/generate_sentences/${languageCode}?count=${count}`;
  const result = await getOrThrowError<string[]>(url);
  return result || [];
}

export async function fetchParagraphs(
  languageCode: string,
  count: number
): Promise<string[]> {
  const url = `${baseApiUrl}/api/v1/generate_paragraphs/${languageCode}?count=${count}`;
  const result = await getOrThrowError<string[]>(url);
  return result || [];
}
