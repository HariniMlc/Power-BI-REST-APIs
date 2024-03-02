# Power BI Dataset Refresh Project

This project uses the Power BI REST API to refresh a dataset in Power BI. The API endpoint is:

`POST https://api.powerbi.com/v1.0/myorg/groups/{groupId}/datasets/{datasetId}/refreshes`

For more information about the API, see [Refresh Dataset].

| Parameter | Type | Description |
|-----------|------|-------------|
| groupId | string | The workspace ID that contains the dataset. |
| datasetId | string | The dataset ID. |
| notifyOption | string | The option to send an email notification when the refresh is completed. Possible values are: `NoNotification`, `MailOnCompletion`, `MailOnFailure`. |

| Header | Value |
|--------|-------|
| Authorization | Bearer {access_token} |
| Content-Type | application/json |

| Response | Description |
|----------|-------------|
| 202 | The refresh request was accepted. |
| 400 | The refresh request was invalid. |
| 401 | The access token was invalid or expired. |
| 403 | The user does not have permission to refresh the dataset. |
| 404 | The dataset or the workspace was not found. |
| 429 | The refresh request was throttled. |
| 500 | An internal server error occurred. |
