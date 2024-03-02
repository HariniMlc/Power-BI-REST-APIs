# Power BI Dataset Refresh Project

This project uses the Power BI REST API to refresh a dataset in Power BI. It allows you to automate the refresh process and get notified of the refresh status by email.

## Features and Benefits

This project has the following features and benefits:

- It simplifies the task of refreshing a dataset in Power BI by using a simple Python script.
- It supports different notify options to customize the email notification that you receive after the refresh is completed.
- It handles different status codes and errors that may occur during the refresh process and prints them to the console.
- It uses the `requests` library, which is a popular and easy-to-use HTTP library for Python.


## Installation and Usage

To use this project, you need to:

- Clone this repository to your local machine.
- Install the required dependencies, such as requests for Python.
- Obtain an access token from Power BI. You can follow the instructions [https://learn.microsoft.com/en-us/rest/api/power-bi/embed-token/generate-token].
- Edit the `RefreshDataset_main.py` file and replace the placeholders with your access token, workspace ID, and dataset ID.
- Run the `RefreshDataset_main.py` file and check the output.


## Resource File

The resource.md file is a file that contains information about the Power BI REST API that I am using to refresh a dataset in Power BI. It includes the endpoint, the parameters, the headers, and the response of the API. It also provides an example of how to use the API in Python. The resource.md file can help you understand the API and use it in your code. You can find the resource.md file in the root folder of this repository.



## License and Acknowledgements

This project is licensed under the MIT License. See the LICENSE file for details.
This project is based on the Power BI REST API documentation. See [https://learn.microsoft.com/en-us/rest/api/power-bi/] for more information.

