
module.exports = {
  name: 'FalconRouter',
  async write () {
    function makeResources (schema){
      let resources = []
      resources.push(schema.class_name + "CollectionResource")
      resources.push(schema.class_name + "ModelResource")
      /* """Iterates over each schema in blueprint""" */
      schema.relations.forEach((rel) => {
        if (rel.type === 'BELONGS_TO' || rel.type === "HAS_ONE") {
          resources.push(schema.class_name + "Related" + rel.alias.class_name + "Resource")
        } else {
          resources.push(schema.class_name + "Related" + rel.alias.class_name_plural + "Resource")
        }
      })
      return resources.join(", ")
    }

    await this.copyTemplate(
      this.templatePath('routes.py'),
      this.destinationPath('src/routes.py'),
      { makeResources }
    )
  }
}
