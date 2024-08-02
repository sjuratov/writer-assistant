param name string
param location string

resource CognitiveServicesOpenAI 'Microsoft.CognitiveServices/accounts@2023-05-01' = {
  name: name
  location: location
  sku: {
    name: 'S0'
  }
  kind: 'OpenAI'
  properties: {
    customSubDomainName: name
    networkAcls: {
      defaultAction: 'Allow'
      virtualNetworkRules: []
      ipRules: []
    }
    publicNetworkAccess: 'Enabled'
  }
}

resource CognitiveServicesOpenAIDeployment 'Microsoft.CognitiveServices/accounts/deployments@2023-05-01' = {
  parent: CognitiveServicesOpenAI
  name: 'gpt-4o-global'
  sku: {
    name: 'GlobalStandard' 
    capacity: 30
  }
  properties: {
    model: {
      format: 'OpenAI'
      name: 'gpt-4o'
      version: '2024-05-13'
    }
    versionUpgradeOption: 'OnceNewDefaultVersionAvailable'
    raiPolicyName: 'Microsoft.Default'
  }
}

output CognitiveServicesOpenAIVersion string = CognitiveServicesOpenAI.apiVersion
output CognitiveServicesOpenAIEndpoint string = CognitiveServicesOpenAI.properties.endpoint
output CognitiveServicesOpenAIName string = name
output CognitiveServicesOpenAIDeploymentName string = CognitiveServicesOpenAIDeployment.name
