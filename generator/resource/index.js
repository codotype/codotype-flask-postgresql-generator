const { Generator } = require('codotype-generator')

// // // //

module.exports = class FlaskResource extends Generator {
  async write ({ app }) {
    const dest = 'resources/'

    // Ensures destination directory
    this.ensureDir(dest)

    // Defines resources/__init__.py
    await this.copyTemplate(
      this.templatePath('__init__.py'),
      this.destinationPath(dest + '__init__.py')
    )

    // Defines resources/{{schema.identifier_plural}}.py
    app.schemas.forEach(async (schema) => {
      await this.copyTemplate(
        this.templatePath('resource.py'),
        this.destinationPath(dest + schema.identifier_plural + '.py'),
        { schema }
      )
    })
  }
}
