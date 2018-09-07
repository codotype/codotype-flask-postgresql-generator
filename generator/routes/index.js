const Generator = require('@codotype/generator')

// // // //

module.exports = class FlaskRouter extends Generator {
  async write () {
    await this.copyTemplate(
      this.templatePath('server.py'),
      this.destinationPath('server.py')
    )
  }
}
