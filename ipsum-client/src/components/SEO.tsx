import Head from 'next/head';
import * as React from 'react';

interface SEOProps {
  title?: string;
  description?: string;
  url?: string;
}

const SEO = (props: SEOProps) => {
  const title = props.title || 'Ipsum';
  const description =
    props.description || 'The international placeholder text generator.';
  return (
    <Head>
      {/* Standard metadata tags */}
      <title>{title}</title>
      <meta name="description" content={description} />
      {/* Facebook tags */}
      <meta property="og:type" content="website" />
      <meta property="og:title" content={title} />
      <meta property="og:description" content={description} />
      <meta property="og:image" content="/images/og_image.jpg" />
      {props.url ? <meta property="og:url" content={props.url} /> : undefined}
      {/* Twitter tags */}
      <meta name="twitter:creator" content="@dtrifuno" />
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:title" content={title} />
      <meta name="twitter:description" content={description} />
      <meta name="twitter:image" content="/images/og_image.jpg" />
    </Head>
  );
};

export default SEO;
