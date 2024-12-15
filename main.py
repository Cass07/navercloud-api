import os
from ApiRequest import ApiRequest

def set_github_action_output(output_key, output_value):
    f = open(os.path.abspath(os.environ["GITHUB_ENV"]), "a")
    f.write(f'{output_key}={output_value}')
    f.close()
    print(f"::set-output name={output_key}::{output_value}")

def main():
    api_base_url = os.environ["INPUT_NC_API_BASE_URL"]
    api_uri = os.environ["INPUT_NC_API_URI"]
    api_key = os.environ["INPUT_NC_ACCESS_KEY"]
    api_secret = os.environ["INPUT_NC_SECRET_KEY"]
    method = os.environ["INPUT_METHOD"]

    apiRequest = ApiRequest(api_base_url, api_uri, api_key, api_secret, method)

    response_body = apiRequest.execute()

    set_github_action_output("response_body", response_body)

if __name__ == "__main__":
    main()