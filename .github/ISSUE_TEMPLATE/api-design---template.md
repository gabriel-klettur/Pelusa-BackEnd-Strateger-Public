---
name: API Design - Template
about: Template of API Design for Endpoints
title: ''
labels: ''
assignees: ''

---

---
name: API Design
about: Define the structure and behavior of the API endpoint.
title: "API Design for [Endpoint Name]"
labels: api-design
assignees: Gaby
---

## **HTTP Method(s):**
- GET, POST, PUT, DELETE, etc.

## **URL Path:**
- `/api/your-endpoint`

## **Headers:**
- **Authentication:**
  - Example: `Authorization: Bearer [token]`
- **Content-Type:**
  - Example: `application/json`

## **Query Parameters:**
- Example: `?param1=value1&param2=value2`

## **Path Parameters:**
- Example: `/api/your-endpoint/{id}`

## **Request Body Schema:**
```json
{
    "field1": "value1",
    "field2": "value2"
}
```

## **Response Body Schema:**
```json
{
    "status": "success",
    "data": {
        "field1": "value1",
        "field2": "value2"
    }
}
```

## **Response Codes:**
```json
    200 OK - Successful request
    201 Created - Resource created
    400 Bad Request - Validation errors
    401 Unauthorized - Authentication failed
    404 Not Found - Resource not found
    500 Internal Server Error - Server error
```
