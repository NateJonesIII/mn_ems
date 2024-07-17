/** @type {import('tailwindcss').Config} */
module.exports = {
  future: {
      removeDeprecatedGapUtilities: true,
      purgeLayersByDefault: true,
  },
  purge: {
      enabled: false, //true for production build
      content: [
          '../**/templates/*.html',
          '../**/templates/**/*.html'
      ]
  },
  theme: {
      extend: {
        backgroundImage: {
            // Defined your gradients 
            'gradient-to-br': 'linear-gradient(to bottom right, #38a3a5, #57cc99)',
            'gradient-to-tr': 'linear-gradient(to top right, #38a3a5, #57cc99)',
          },
      },
      colors: {
        transparent: 'transparent',
        current: 'currentColor',
        'white': '#ffffff',
        'midnight': '#121063',
        'metal': '#565584',
        'tahiti': '#3ab7bf',
        'bubble-gum': '#ff77e9',

        'bg-blue-100': '#387E9B'
      },
  },
  safelist: [
    'bg-slate-100',
    'bg-cyan-700',
    'bg-teal-700',
    'bg-pink-500',
    'slate-100',
    'cyan-700',
    'teal-700',
    'pink-500',
  ],
  variants: {
    extend: {
        backgroundImage: ['hover', 'focus'],// incase of enabling hover and focus css features
      },
  },
  plugins: [],
}