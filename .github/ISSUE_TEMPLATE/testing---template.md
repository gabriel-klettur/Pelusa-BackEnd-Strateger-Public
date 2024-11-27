---
name: Testing - Template
about: Template of Testing for Endpoints
title: ''
labels: ''
assignees: ''

---

---
name: Testing
about: Define and execute test cases for the endpoint.
title: "Testing for [Endpoint Name]"
labels: testing
assignees: Gaby
---

## **Testing Frameworks**
- List frameworks and tools used.
  - Example: Pytest, FastAPI TestClient.

## **Test Cases**
- Example:
  - Validate successful creation of a resource.
  - Handle invalid input data gracefully.

## **Sample Test Code**
```python
def test_create_item(client):
    response = client.post("/api/your-endpoint", json={"field1": "value1"})
    assert response.status_code == 201
    assert response.json()["data"]["field1"] == "value1"
```

## **Coverage**
- Report on the percentage of code covered by tests.
  - Example: 90% coverage.
