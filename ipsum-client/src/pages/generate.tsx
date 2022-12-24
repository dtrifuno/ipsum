import clsx from 'clsx';
import {Field, Form, Formik, FormikHelpers} from 'formik';
import * as React from 'react';
import {useEffect, useState} from 'react';
import * as yup from 'yup';

import {
  fetchParagraphs,
  fetchSentences,
  fetchSupportedLanguages,
  fetchWords,
} from '../api';
import DropdownMenu, {DropdownItem} from '../components/DropdownMenu';
import SEO from '../components/SEO';
import {baseUrl} from '../constants';
import {GenerateValues} from '../types';

async function onSubmit(
  {type, languageCode, count}: GenerateValues,
  {setFieldError}: FormikHelpers<GenerateValues>
) {
  try {
    if (type === 'words') {
      const words = await fetchWords(languageCode!, count);
      return <p>{words.join(' ')}</p>;
    } else if (type === 'sentences') {
      const sentences = await fetchSentences(languageCode!, count);
      return <p>{sentences.join(' ')}</p>;
    } else if (type === 'paragraphs') {
      const paragraphs = await fetchParagraphs(languageCode!, count);
      return (
        <>
          {paragraphs.map((paragraph, idx) => (
            <p key={idx} className="pb-1">
              {paragraph}
            </p>
          ))}
        </>
      );
    }
  } catch (err: unknown) {
    if (err instanceof Error) {
      setFieldError('languageCode', err.message);
    }
  }

  return undefined;
}

const generateSchema = yup.object().shape({
  type: yup.string().oneOf(['words', 'sentences', 'paragraphs']).required(),
  languageCode: yup
    .string()
    .length(2, 'ISO 639-1 codes must be two-letters long.')
    .required('Please select a language first.'),
  count: yup
    .number()
    .positive()
    .required()
    .integer()
    .when('type', {
      is: 'words',
      then: schema =>
        schema.max(500, 'Cannot generate more than 500 words at a time.'),
    })
    .when('type', {
      is: 'sentences',
      then: schema =>
        schema.max(150, 'Cannot generate more than 150 sentences at a time.'),
    })
    .when('type', {
      is: 'paragraphs',
      then: schema =>
        schema.max(50, 'Cannot generate more than 50 paragraphs at a time.'),
    }),
});

const Generate = () => {
  const [dropDownOptions, setDropDownOptions] = useState<DropdownItem[]>([]);
  const [generatedText, setGeneratedText] = useState<JSX.Element>();
  const [disableButton, setDisableButton] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      const languages = await fetchSupportedLanguages();
      const items = languages.map(language => ({
        value: language.code,
        label: language.name,
      }));
      setDropDownOptions(items);
      if (items.length > 0) {
        setDisableButton(false);
      }
    };

    fetchData().catch(console.error);
  }, []);

  return (
    <>
      <SEO title="Generate Text • Ipsum" url={`${baseUrl}/generate`} />
      <section className="max-w-5xl mx-auto">
        <Formik
          validateOnChange={false}
          validateOnBlur={false}
          initialValues={{
            count: 5,
            type: 'paragraphs',
            languageCode: undefined,
          }}
          validationSchema={generateSchema}
          onSubmit={async (values: GenerateValues, formikBag) => {
            const result = await onSubmit(values, formikBag);
            setGeneratedText(result);
          }}
        >
          {({errors}) => (
            <Form>
              <>
                <div className="items-baseline text-base sm:text-lg font-semibold border-b-2 pb-2.5 border-black mb-2.5">
                  <div className="flex flex-col md:flex-row items-baseline justify-between">
                    <div className="flex flex-col sm:flex-row items-baseline w-full md:w-auto mb-1 md:my-0">
                      <div className="grow-0 w-full md:w-auto text-center">
                        Ipsum, please generate
                      </div>
                      <div className="grow-0 w-full md:w-auto flex justify-center items-baseline my-1 sm:my-0">
                        <Field
                          type="number"
                          name="count"
                          className="w-14 border-2 border-black outline-none focus:border-orange-500 py-1 pl-2 md:ml-2 mr-2"
                        />
                        <DropdownMenu
                          name="type"
                          items={[
                            {value: 'words', label: 'words'},
                            {value: 'sentences', label: 'sentences'},
                            {value: 'paragraphs', label: 'paragraphs'},
                          ]}
                        />
                        <span className="px-2">of</span>
                      </div>
                    </div>
                    <div className="flex flex-row justify-between grow w-full md:w-auto">
                      <DropdownMenu
                        name="languageCode"
                        items={dropDownOptions}
                        placeholderText="select language"
                      />
                      <button
                        type="submit"
                        disabled={disableButton}
                        className={clsx(
                          'py-1 px-4 border-2 border-black',
                          'hover:text-white hover:bg-orange-500 focus:text-white focus:bg-orange-500',
                          'disabled:cursor-not-allowed disabled:opacity-75'
                        )}
                      >
                        Go!
                      </button>
                    </div>
                  </div>
                </div>
                {errors.languageCode ? (
                  <div className="text-lg font-medium text-orange-500">
                    {errors.languageCode}
                  </div>
                ) : errors.count ? (
                  <div className="text-lg font-medium text-orange-500">
                    {errors.count}
                  </div>
                ) : generatedText ? (
                  <div className="text-lg font-medium border-2 border-black p-2 ">
                    {generatedText}
                  </div>
                ) : undefined}
              </>
            </Form>
          )}
        </Formik>
      </section>
    </>
  );
};

export default Generate;
