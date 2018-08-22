const Generator = require('../util/generator')
const FlaskAppBase = require('./flask_app_base')
const FlaskRoutes = require('./flask_routes')
const FlaskResource = require('./flask_resource')

module.exports = class Flask extends Generator {
  async write () {
    await this.composeWith(FlaskAppBase)
    await this.composeWith(FlaskRoutes)
    await this.composeWith(FlaskResource)    
  }
}
