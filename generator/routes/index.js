
module.exports = {
  name: 'FalconRouter',
  async write () {
    await this.copyTemplate(
      this.templatePath('routes.py'),
      this.destinationPath('src/routes.py')
    )
  }
}
