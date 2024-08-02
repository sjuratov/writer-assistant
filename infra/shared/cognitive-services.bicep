param name string
param location string

resource CognitiveServices 'Microsoft.CognitiveServices/accounts@2023-05-01' = {
  name: name
  location: location
  sku: {
    name: 'S0'
  }
  kind: 'CognitiveServices'
  identity: {
    type: 'None'
  }
  properties: {
    apiProperties: {}
    customSubDomainName: name
    networkAcls: {
      defaultAction: 'Allow'
      virtualNetworkRules: []
      ipRules: []
    }
    publicNetworkAccess: 'Enabled'
  }
}

output CognitiveServicesName string = CognitiveServices.name
output CognitiveServicesEndpoint string = CognitiveServices.properties.endpoint
