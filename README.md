# Naver Cloud API Github Action
- For using Naver Cloud API in Github Action
  - Generate signature automatically

## Usage
Request
```yaml
name: Get Sourcedeploy Projects
on:
  push:
    branches:
      - main
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        
      - name: Naver Cloud API Request
        uses: cass07/navercloud-api@main
        with:
          nc_api_uri: '/api/v1/project'
          nc_api_base_url: 'https://vpcsourcedeploy.apigw.ntruss.com'
          method: 'GET'
          nc_access_key: ${{ secrets.NAVER_CLOUD_API_ACCESS_KEY }}
          nc_secret_key: ${{ secrets.NAVER_CLOUD_API_SECRET_KEY }}
```

## Configuration
| Key               | Value                      | Suggested Type | Required | Default |
|-------------------|----------------------------|----------------|----------|---------|
| `nc_api_base_url` | API Host URL               | `env`          | Yes      | N/A     |
| `nc_api_uri`      | API URI (Except host url)  | `env`          | Yes      | N/A     |
| `method`          | Request Method             | `env`          | Yes      | N/A     |
| `nc_access_key`   | Naver Cloud API Access Key | `secret env`   | Yes      | N/A     |
| `nc_secret_key`   | Naver Cloud API Secret Key | `secret env`   | Yes      | N/A     |
| `request_body`    | Request Body Json String   | `env`          | No       | N/A     |

## Output
| Key               | Value              |
|-------------------|--------------------|
| `response_body`   | Response Body Json |

## Reference
* [Naver Cloud API Docs](https://api.ncloud-docs.com/docs/en/home)