const Generator = require('../util/generator')
const FalconAppBase = require('./falcon_app_base')
const FalconRoutes = require('./falcon_routes')
const FalconResource = require('./falcon_resource')

module.exports = class Falcon extends Generator {
  async write () {
    await this.composeWith(FalconAppBase)
    await this.composeWith(FalconRoutes)
    await this.composeWith(FalconResource)
  }
}
