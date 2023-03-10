import Link from 'next/link';
import {useRouter} from 'next/router';
import * as React from 'react';

interface NavLinkProps {
  activeClassName?: string;
  className?: string;
  href: string;
  children: string;
}

const NavLink = ({
  href,
  className,
  activeClassName,
  children,
}: NavLinkProps) => {
  const {asPath} = useRouter();
  const cleanPath = asPath.split(/[?#]/)[0];

  const actualClassName =
    cleanPath === href ? `${className} ${activeClassName}` : className;

  return (
    <Link className={actualClassName} href={href}>
      {children}
    </Link>
  );
};

export default NavLink;
