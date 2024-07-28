@minLength(3)
@maxLength(15)
@description('Solution Name')
param solutionName string
param solutionLocation string

param accounts_byc_openai_name string = '${ solutionName }-openai'

resource accounts_byc_openai_name_resource 'Microsoft.CognitiveServices/accounts@2023-05-01' = {
  name: accounts_byc_openai_name
  location: solutionLocation
  sku: {
    name: 'S0'
  }
  kind: 'OpenAI'
  properties: {
    customSubDomainName: accounts_byc_openai_name
    networkAcls: {
      defaultAction: 'Allow'
      virtualNetworkRules: []
      ipRules: []
    }
    publicNetworkAccess: 'Enabled'
  }
}

resource accounts_byc_openai_name_gpt_4o_global 'Microsoft.CognitiveServices/accounts/deployments@2023-05-01' = {
  parent: accounts_byc_openai_name_resource
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

var openaiKey = accounts_byc_openai_name_resource.listKeys().key1

output openAIOutput object = {
openAPIKey : openaiKey
openAPIVersion:accounts_byc_openai_name_resource.apiVersion
openAPIEndpoint: accounts_byc_openai_name_resource.properties.endpoint
openAIAccountName:accounts_byc_openai_name
}
