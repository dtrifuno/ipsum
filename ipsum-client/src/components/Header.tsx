import clsx from 'clsx';
import Image from 'next-image-export-optimizer';
import Link from 'next/link';
import * as React from 'react';

import NavLink from '../components/NavLink';

const links = [
  {href: '/', label: 'About'},
  {href: '/generate', label: 'Generate'},
];

const Header: React.FC = () => {
  return (
    <header className="bg-white md:px-6 py-2 border-b-2 border-black">
      <div className="flex items-center sm:justify-between max-w-5xl mx-auto flex-col md:flex-row justify-between">
        <Link href="/" className="flex items-center mb-0">
          <Image
            src="/logo.svg"
            alt="Ipsum Logo"
            className="w-14 md:w-16 h-10 md:h-12 self-center"
            width={64}
            height={48}
            priority
          />
        </Link>
        <div className="text-sm sm:text-lg md:text-xl font-semibold text-black md:mt-0 mt-2">
          the international placeholder text generator
        </div>
        <nav>
          <ul className="flex flex-wrap items-center text-sm text-black space-x-4 md:space-x-6">
            {links.map(item => (
              <li key={item.href}>
                <NavLink
                  key={item.href}
                  className={clsx(
                    'lowercase text-base sm:text-lg font-semibold border-black',
                    'hover:border-b-2'
                  )}
                  activeClassName="border-b-2 text-orange-500 border-orange-500"
                  href={item.href}
                >
                  {item.label}
                </NavLink>
              </li>
            ))}
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;
