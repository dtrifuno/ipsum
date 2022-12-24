import * as React from 'react';
import Image from 'next-image-export-optimizer';

import SEO from '../components/SEO';
import {baseUrl} from '../constants';

const PageNotFound = () => {
  return (
    <>
      <SEO title="Page Not Found • Ipsum" url={`${baseUrl}/404`} />
      <section className="text-black font-semibold max-w-5xl mx-auto">
        <div className="container mx-auto text-md md:text-lg">
          <div className="text-center xl:mt-5">
            <h1 className="text-5xl font-bold">404</h1>
            <h2 className="text-2xl font-bold uppercase">Page Not Found</h2>
            <Image
              src="/puppy.jpg"
              alt="A close-up photo of a pensive Samoyed puppy leaning on a red brick wall."
              className="object-cover object-bottom h-full w-88 py-1 mx-auto"
              width={384}
              height={576}
            />
            <p>I am so sorry, but I cannot find what you were looking for.</p>
            <p>Please enjoy this magnificent puppy instead.</p>
          </div>
        </div>
      </section>
    </>
  );
};

export default PageNotFound;
