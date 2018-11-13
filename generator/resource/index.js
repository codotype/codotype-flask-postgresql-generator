
module.exports = {
  name: 'FalconResources',
  async write ({ blueprint }) {
    await this.renderComponent({ src: 'models.py', dest: 'src/models.py' })
  },
  async forEachSchema({ blueprint, configuration, schema }) {
    const dest = 'src/resources/'

    await this.copyTemplate(
      this.templatePath('resource.py'),
      this.destinationPath(dest + schema.identifier + '.py'),
      { schema }
    )
  }
}
