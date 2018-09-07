const Generator = require('@codotype/generator')

// // // //

module.exports = class FlaskAppBase extends Generator {
  async write () {
    // await this.ensureDir(this.options.build.dest.server.root)
    // Copies application base templates
    await this.copyDir(
      this.templatePath(),
      this.destinationPath()
    )
  }
}

