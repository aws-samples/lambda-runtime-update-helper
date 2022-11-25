import boto3
from botocore.config import Config

# List runtime needs to be updated here
source_runtime_list = ('nodejs14.x',)

# Target update runtime
target_runtime = 'nodejs16.x'

# Client config
client_config = Config(
    region_name='us-east-1'
)


def runtime_update_handler():
    client = boto3.client('lambda', config=client_config)

    response = client.list_functions(MaxItems=30)

    function_list_for_update = []

    while True:
        function_list = response.get('Functions')
        print('Get ' + str(len(function_list)) + ' functions in response.')

        it = iter(function_list)
        for func in it:
            if func.get('Runtime') in source_runtime_list:
                function_list_for_update.append(func.get('FunctionName'))

        print('Find ' + str(len(function_list_for_update)) + ' function(s) will be updated.')

        if len(function_list_for_update) > 0:
            it_for_update = iter(function_list_for_update)

            for funcName in it_for_update:
                print('Update function:' + funcName)
                client.update_function_configuration(FunctionName=funcName, Runtime=target_runtime)

            function_list_for_update.clear()

        if response.get('NextMarker') is not None:
            response = client.list_functions(Marker=response.get('NextMarker'), MaxItems=30)
        else:
            break

    print('Update completed!')


runtime_update_handler()
