const Generator = require('@codotype/generator')

module.exports = class FlaskApi extends Generator {
  async write () {
    await this.composeWith('./base')
    await this.composeWith('./routes')
    await this.composeWith('./resource')
  }
}
