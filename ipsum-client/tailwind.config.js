/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      spacing: {
        88: '24rem',
      },
      screens: {
        sm: '512px',
      },
    },
  },
  plugins: [require('@headlessui/tailwindcss')],
};
