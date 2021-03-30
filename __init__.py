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
        auth_code = "Y1ELvZruTwQQyXUoP5__v_iB2JfzmNmGn0lh5XnzsuI"
        client_secret = "Cica0GPtUrMO33S1ORzNxrofCA1hxWnRbj9K1ot6q_U"
        client_id = "a33ce1f3-95bf-4fe5-b37a-f9085a7cc867"
        redirect_uri = "http://localhost:5001"
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
