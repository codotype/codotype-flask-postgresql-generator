const Generator = require('../../util/generator')

// // // //

module.exports = class FlaskResource extends Generator {
  async write () {
    const dest = this.options.build.dest.server.root + 'resources/'

    // Ensures destination directory
    this.ensureDir(dest)

    // Defines resources/__init__.py
    await this.copyTemplate(
      this.templatePath(__dirname, '__init__.py'),
      this.destinationPath(dest + '__init__.py')
    )

    // Defines resources/{{schema.identifier_plural}}.py
    for (let schema of this.options.build.app.schemas) {
      await this.copyTemplate(
        this.templatePath(__dirname, 'resource.py'),
        this.destinationPath(dest + schema.identifier_plural + '.py'),
        { schema: schema }
      )
    }
  }
}
