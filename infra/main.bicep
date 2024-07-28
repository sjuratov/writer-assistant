// ========== main.bicep ========== //
targetScope = 'resourceGroup'

@minLength(3)
@maxLength(6)
@description('Prefix Name')
param solutionPrefix string

param azureAIMultiServiceAccountLocation string = resourceGroup().location

param azureOpenAIServiceLocation string = resourceGroup().location

// ========== Azure AI services multi-service account ========== //
module azAIMultiServiceAccount './deploy_azure_ai_service.bicep' = {
  name: 'deploy_azure_ai_service'
  params: {
    solutionName: solutionPrefix
    solutionLocation: azureAIMultiServiceAccountLocation
  }
} 

// ========== Azure OpenAI ========== //
module azOpenAI './deploy_azure_open_ai.bicep' = {
  name: 'deploy_azure_open_ai'
  params: {
    solutionName: solutionPrefix
    solutionLocation: azureOpenAIServiceLocation
  }
}
