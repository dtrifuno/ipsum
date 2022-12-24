import * as React from 'react';

const Footer = () => {
  return (
    <footer className="border-t-2 border-black py-2 sm:py-3 text-md font-medium flex justify-center">
      <div className="px-2 flex flex-col sm:flex-row">
        <div className="sm:mr-1">
          <a
            className="font-medium text-orange-500 hover:border-b-2 border-orange-500"
            href="https://trifunovski.me"
          >
            Darko Trifunovski
          </a>{' '}
          © 2022–2023.
        </div>
        <div>
          Source code available on
          <a
            className="font-medium text-orange-500 hover:border-b-2 ml-1 border-orange-500"
            href="https://github.com/dtrifuno/ipsum"
          >
            Github.
          </a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
