// TODO - this file should be moved into a test directory
const CodotypeRuntime = require('@codotype/runtime')

// const app = require('codotype-generator/examples/todo-list.json')
const app = require('@codotype/generator/examples/library.json')

// Each stage can accept its own app - this is done to simplify challenges introduc
const build = {
  app: app,
  stages: [{
    generator_id: 'codotype-generator-python-flask',
    configuration: {} // TODO - this will be populated by the UI
  }]
}

// Invoke runtime directly with parameters
const runtime = new CodotypeRuntime()

// Registers this generator via relative path
runtime.registerGenerator({ relative_path: './' })

// Executes the build
runtime.execute({ build })
.then(() => {
  console.log('TEST SUCCESSFUL')
})