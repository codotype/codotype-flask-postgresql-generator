
module.exports = {
  name: 'FalconBase',
  async write () {
    await this.copyDir(
      this.templatePath(),
      this.destinationPath()
    )
  }
}

