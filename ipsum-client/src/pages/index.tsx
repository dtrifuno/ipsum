import clsx from 'clsx';
import * as React from 'react';
import Image from 'next-image-export-optimizer';
import Link from 'next/link';

import SEO from '../components/SEO';
import {baseUrl} from '../constants';

const About = () => {
  return (
    <>
      <SEO url={`${baseUrl}`} />
      <section className="text-black font-semibold max-w-5xl mx-auto">
        <div className="container px-0 mx-auto">
          <div className="h-64">
            <Image
              src="/images/splash.jpg"
              alt=""
              className="object-cover object-bottom h-full w-full"
              width={1024}
              height={256}
              priority
            />
          </div>

          <div className="flex flex-col text-center w-full my-8">
            <p className="lg:w-2/3 mx-auto leading-relaxed text-base">
              If instead you would like to use the Ipsum placeholder text
              generator as a Python library in your own project,{' '}
              <a
                href="https://pypi.org/project/ipsum/"
                className="text-orange-500 hover:border-b-2 border-orange-500"
              >
                check out the Ipsum package on PyPI.
              </a>{' '}
              If you would like to learn more about how Ipsum works, you can
              check out{' '}
              <a
                href="https://github.com/dtrifuno/ipsum"
                className="text-orange-500 hover:border-b-2 border-orange-500"
              >
                the source code on Github,
              </a>{' '}
              or{' '}
              <a
                href="https://trifunovski.me/posts/230225-lorem-ipsum-or-the-procedural-generation-of-typographically-plausible-nonsense"
                className="text-orange-500 hover:border-b-2 border-orange-500"
              >
                read this blog post
              </a>{' '}
              on the movivation behind it.
            </p>
          </div>

          <Link
            className={clsx(
              'flex mx-auto my-6 lg:my-10 text-black font-bold text-xl',
              'border-2 border-black py-2 w-56',
              'focus:outline-none focus:bg-orange-400 focus:text-white',
              'hover:bg-orange-400 hover:text-white justify-center'
            )}
            href="/generate"
          >
            <div className="text-center">Try Ipsum Now</div>
          </Link>

          <div className="flex flex-wrap">
            <div className="xl:w-1/3 lg:w-1/2 md:w-full px-8 py-4 border-l-2 border-black">
              <h2 className="text-lg sm:text-xl text-black font-bold title-font mb-2">
                Why do I need Ipsum?
              </h2>
              <p className="leading-relaxed text-base mb-4">
                Traditional <i>Lorem Ipsum</i> placeholder text generators are
                based on a 1st-century BC Latin text, which does not resemble
                the languages that designers are targeting today.
              </p>
            </div>

            <div className="xl:w-1/3 lg:w-1/2 md:w-full px-8 py-4 border-l-2 border-black">
              <h2 className="text-lg sm:text-xl text-black font-bold title-font mb-2">
                How does it work?
              </h2>
              <p className="leading-relaxed text-base mb-4">
                Ipsum uses Markov chains trained on large corpora of modern
                texts to create placeholder text that is meaningless, but uses
                the alphabet and punctuation of the desired language in a
                typographically plausible way.
              </p>
            </div>

            <div className="xl:w-1/3 lg:w-1/2 md:w-full px-8 py-4 border-l-2 border-black">
              <h2 className="text-lg sm:text-xl text-black font-bold title-font mb-2">
                What languages?
              </h2>
              <p className="leading-relaxed text-base mb-4">
                Ipsum currently supports 12 languages: Albanian, Bulgarian,
                Dutch, English, French, German, Greek, Italian, Macedonian,
                Serbian, Spanish and Swedish.
              </p>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default About;
