module.exports = {
  plugins: [
    {
      resolve: `gatsby-theme-garden`, // This is the plugin that does the work
      options: {
        contentPath: `${__dirname}/content/obsidian`, // Where the notes are stored
        rootNote: `/Overview`,
      },
    },
  ],
  siteMetadata: {
    title: `Test Deployment`,
  },
}
