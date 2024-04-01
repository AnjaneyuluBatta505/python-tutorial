# Python3 - `json` module

* **JSON** - **J**ava**S**cript **O**bject **N**otation
* A standardized format commonly used to transfer data
* Frequently used in API's and databases

## Data type comparison

| JSON Data Type      | Python Data Type |
| ------------------- | ---------------- |
| Object              | dict             |
| Array               | list             |
| String              | str              |
| Number              | int or float     |
| Boolean true, false | bool True, False |
| Null                | None             |

## JSON - example

```json
{
  "name": "John Doe",
  "age": 25,
  "city": "Exampleville",
  "is_student": true,
  "grades": [85, 90, 88],
  "address": {
    "street": "456 Oak St",
    "zipcode": "54321"
  }
}
```

## Vocabulary

* **Serialization**: converting python data to JSON format
* **Deserialization**: converting JSON data to python object

## json - module

* it allows to serialize and deserialize the data to/from JSON
* methods
  * `json.dumps(obj, indent=None)`
  * `json.dump(obj, fp, indent=None)`
  * `json.loads(s)`
  * `json.load(fp)`

## Custom encoder

```python
import json

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return super().default(obj)

data = {"names": {"John", "Alice", "Bob"}}
json_string = json.dumps(data, cls=CustomEncoder, indent=2)
print(json_string)

```

## Problems

* Convert JSON data to python data

  * '{"name": "John", "age": 30, "city": "New York", "is_valid": true}'
* Convert python data to JSON

  * {"name": "John", "age": 30.5, fruits: ["apple","banana"]}
