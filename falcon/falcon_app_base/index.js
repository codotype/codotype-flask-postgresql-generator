const Generator = require('../../util/generator')

// // // //

module.exports = class FalconAppBase extends Generator {
  async write () {

    // Defines requisite destination variables
    this.options.build.dest.server.root = this.options.build.dest.root + 'falcon_api/'

    // Ensures presence of client directory
    await this.ensureDir(this.options.build.dest.server.root)

    // Copies application base templates
    await this.copyDir(
      __dirname + '/templates',
      this.options.build.dest.server.root
    )

  }
}

