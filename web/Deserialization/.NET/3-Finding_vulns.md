## Whitebox
### Funciones potencialmente vulnerables:

| Serializer | ejemplo |
|-----|------|
| BinaryFormatter	| .Deserialize(...)|	
| fastJSON	| JSON.ToObject(...)	|
| JavaScriptSerializer	| .Deserialize(...) |
| Json.NET	| JsonConvert.DeserializeObject(...)	|
| LosFormatter |.Deserialize(...) |	
| NetDataContractSerializer |	.ReadObject(...)	|
| ObjectStateFormatter	| .Deserialize(...) |	
| SoapFormatter |	.Deserialize(...) |	
| XmlSerializer |	.Deserialize(...)	|
| YamlDotNet |	.Deserialize<...>(...)	|


### Viewstate

Aparte de las funciones listadas arriba, hay una feature llamada viewstate que en algunas aplicaciones ASP.NET se usan para mantener el estado de una página. El proceso incluye guardar un parámetro serializado en la cookie "\_\_VIEWSTATE". Muchas veces es posible explotar esto si el server está mal configurado.

#### Ataques:

    https://soroush.me/blog/2019/04/exploiting-deserialisation-in-asp-net-via-viewstate/

    https://notsosecure.com/exploiting-viewstate-deserialization-using-blacklist3r-and-ysoserial-net

---

## Blackbox

Para reconocer posibles puntos de explotación debemos buscar en las requests:

- Base64 strings que inician con AAEAAAD/////
- Strings que contengan $type
- strings que contengan \_\_type
- Strngs que contengan TypeObject
