const Generator = require('@codotype/generator')

// // // //

module.exports = class FlaskResource extends Generator {
  async write ({ blueprint }) {
    const dest = 'src/resources/'

    // Copies models
    await this.copyTemplate(
      this.templatePath('models.py'),
      this.destinationPath('src/models.py')
    )
        
    // Defines resources/{{schema.identifier_plural}}.py
    
    for (let index = 0; index < blueprint.schemas.length; index++) {
      const schema = blueprint.schemas[index];

      await this.copyTemplate(
        this.templatePath('resource.py'),
        this.destinationPath(dest + schema.identifier + '.py'),
        { schema }
      )
    }

  }
}
