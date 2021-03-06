# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "genesysCloud" + os.sep + "libs" + os.sep
sys.path.append(cur_path)
"""
    Obtengo el modulo que fue invocado
"""
from genesys import GenesysCloud

module = GetParams("module")

global genesys, api_client

if module == "setCredentials":
    client_secret = GetParams("client_secret")
    client_id = GetParams("client_id")
    redirect_uri = GetParams("redirect_uri")
    auth_code = GetParams("auth_code")
    try:
        genesys = GenesysCloud(client_id, client_secret, auth_code, redirect_uri)
        api_client = genesys.authorize(cur_path)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "getAllConversations":
    import json
    result = GetParams("result")
    try:
        api_url = api_client.host
        endpoint = "/api/v2/conversations/chats"
        auth_string = 'Bearer ' + api_client.access_token
        header_params = {
            "Authorization": auth_string,
            'Content-Type': 'application/json'
        }
        conversation = api_client.request("GET", api_url + endpoint, headers=header_params)
        conversation_ids = []
        entities = json.loads(conversation.data)
        for conversation in entities['entities']:
            conversation_ids.append(conversation['id'])
        SetVar(result, conversation_ids)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "getAllCalls":
    import json
    result = GetParams("result")
    try:
        api_url = api_client.host
        endpoint = "/api/v2/conversations/calls"
        auth_string = 'Bearer ' + api_client.access_token
        header_params = {
            "Authorization": auth_string,
            'Content-Type': 'application/json'
        }
        conversation = api_client.request("GET", api_url + endpoint, headers=header_params)
        conversation_ids = []
        entities = json.loads(conversation.data)
        for conversation in entities['entities']:
            conversation_ids.append(conversation['id'])
        SetVar(result, conversation_ids)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "getConversationByID":
    import json
    result = GetParams("result")
    id = GetParams("id")
    try:
        api_url = api_client.host
        endpoint = "/api/v2/conversations/chats/{id}".format(id=id)
        auth_string = 'Bearer ' + api_client.access_token
        header_params = {
            "Authorization": auth_string,
            'Content-Type': 'application/json'
        }
        conversation = api_client.request("GET", api_url + endpoint, headers=header_params)
        data_conversation = json.loads(conversation.data)
        SetVar(result, data_conversation)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "getCallByID":
    import json
    result = GetParams("result")
    id = GetParams("id")
    try:
        api_url = api_client.host
        endpoint = "/api/v2/conversations/call/{id}".format(id=id)
        auth_string = 'Bearer ' + api_client.access_token
        header_params = {
            "Authorization": auth_string,
            'Content-Type': 'application/json'
        }
        conversation = api_client.request("GET", api_url + endpoint, headers=header_params)
        data_conversation = json.loads(conversation.data)
        SetVar(result, data_conversation)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "call_history":
    var = GetParams("var")
    try:
        api_url = api_client.host
        endpoint = "/api/v2/conversations/calls/history"
        auth_string = 'Bearer ' + api_client.access_token
        header_params = {
            "Authorization": auth_string,
            'Content-Type': 'application/json'
        }
        conversation = api_client.request("GET", api_url + endpoint, headers=header_params)
        data_conversation = json.loads(conversation.data)
        SetVar(var, data_conversation)
        #call_ids = [call["id"] for call in resp["entities"]]
        #SetVar(var,call_ids)
    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

