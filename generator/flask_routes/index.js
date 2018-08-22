const Generator = require('../../util/generator')

// // // //

module.exports = class FlaskRouter extends Generator {
  async write () {
    await this.copyTemplate(
      this.templatePath(__dirname, 'server.py'),
      this.destinationPath(this.options.build.dest.server.root + 'server.py'),
      { appSchema: this.options.build.app }
    )
  }
}
