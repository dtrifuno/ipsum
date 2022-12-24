export interface Language {
  name: string;
  code: string;
}

export interface SupportedLanguagesResponse {
  supported_languages: Language[];
}

export interface GenerateValues {
  type: string;
  count: number;
  languageCode?: string;
}
