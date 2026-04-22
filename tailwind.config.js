/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'apple-black': '#000000',
        'apple-gray': '#1d1d1f',
      },
    },
  },
  plugins: [],
}