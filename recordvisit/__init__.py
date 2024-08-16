{
  "bindings": [
    {
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "authLevel": "anonymous"
    },
    {
      "type": "cosmosDB",
      "direction": "out",
      "name": "document",
      "databaseName": "your-database-name",
      "collectionName": "your-container-name",
      "connectionStringSetting": "CosmosDBConnectionString"
    },
    {
      "type": "http",
      "direction": "out",
      "name": "res"
    }
  ]
}