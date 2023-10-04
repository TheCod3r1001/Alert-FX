import freecurrencyapi

client = freecurrencyapi.Client('fca_live_9qrkgr3qyOqgzkN9MlFsREydKMen0qTZ7SsQ3kEf')  # Setting up the client with the API Key

def get_currency():
    return client.latest()

if __name__ == '__main__':
    print(get_currency())