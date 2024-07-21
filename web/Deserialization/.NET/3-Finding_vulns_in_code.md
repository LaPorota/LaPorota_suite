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
