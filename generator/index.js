
module.exports = {
  name: 'FalconMongoDbAPI',
  async write () {
    await this.composeWith('./base')
    await this.composeWith('./routes')
    await this.composeWith('./resource')
  }
}
