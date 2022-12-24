import * as React from 'react';

import Footer from '../components/Footer';
import Header from '../components/Header';

interface LayoutProps {
  children?: React.ReactNode;
}

const Layout = ({children}: LayoutProps) => {
  return (
    <div className="flex flex-col h-screen selection:bg-orange-300">
      <Header />
      <div className="container grow px-3 md:px-5 py-4 mx-auto">{children}</div>
      <Footer />
    </div>
  );
};

export default Layout;
