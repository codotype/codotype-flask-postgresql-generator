const Generator = require('@codotype/generator')

// // // //

module.exports = class FlaskResource extends Generator {
  async write ({ blueprint }) {
    const dest = 'resources/'

    // Ensures destination directory
    this.ensureDir(dest)

    // Defines resources/__init__.py
    await this.copyTemplate(
      this.templatePath('__init__.py'),
      this.destinationPath(dest + '__init__.py')
    )

    // Defines resources/{{schema.identifier_plural}}.py
    for (let index = 0; index < blueprint.schemas.length; index++) {
      const schema = blueprint.schemas[index];

      await this.copyTemplate(
        this.templatePath('resource.py'),
        this.destinationPath(dest + schema.identifier_plural + '.py'),
        { schema }
      )
    }

  }
}
