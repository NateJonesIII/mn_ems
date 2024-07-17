
module.exports = {
  content: [
      './templates/**/*.html'
  ],
  purge: [],
  darkMode: 'media', // or 'media' or 'class'
  theme: {
    extend: {
      backgroundImage: {
      // Defined your gradients 
      'gradient-to-br': 'linear-gradient(to bottom right, #38a3a5, #57cc99)',
      'gradient-to-tr': 'linear-gradient(to top right, #38a3a5, #57cc99)',
    },
  },
  },
  variants: {
    extend: {
      backgroundImage: ['hover', 'focus'],// incase of enabling hover and focus css features
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
  plugins: [],
}