curl --location -k --request POST 'https://localhost/mgmt/tm/asm/advanced-settings' --header 'Authorization: Basic YXp1cmV1c2VyOktvc3RhczEyMw==' --header 'Content-Type: application/json' --data-raw '{"value": 1024,"isUserDefined": true,"maxValue": 1073741824,"name": "total_xml_memory3","minValue": 0,"format": "integer","defaultValue": 0,"units": "Bytes"}'
tmsh restart sys service asm
