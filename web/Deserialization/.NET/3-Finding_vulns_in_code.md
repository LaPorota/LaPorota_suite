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

Aparte de las funciones listadas arriba, hay una feature llamada viewstate que en algunas aplicaciones ASP.NET se usan para mantener el estado de una página. El proceso incluye guardar un parámetro serializado en la cookie "\_\_viewstate"
