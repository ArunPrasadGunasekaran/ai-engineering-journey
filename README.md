# AI Engineering Journey

This repository documents my practical journey toward becoming an AI Engineer.

## Week 1 — Python Fundamentals

Covered Python fundamentals including:
- Variables, data types and control flow
- Lists, dictionaries and sets
- Functions
- String processing
- List comprehensions
- Exception handling
- File handling
- Modules
- JSON data handling

## Week 2 — Python Projects

Built two practical Python projects to apply the fundamentals.

### Student Report Card
- Add student details and subject marks
- Store student data using dictionaries and JSON
- Calculate total, average and grade
- Retrieve student report cards using Student ID

### Personal Expense Tracker
- Add expenses with category and amount
- Store expense records in JSON
- Store date and time for each expense
- Calculate expense statistics
- Filter expenses by category

# Week 3 – Python API Fundamentals

## Overview

This week focused on understanding REST APIs from both sides:

- API Consumer – calling and consuming external APIs using Python
- API Provider – building REST APIs using FastAPI

The goal was to build a strong API foundation before moving into databases and eventually AI application development.

---

## Topics Learned

### 1. HTTP & REST API Fundamentals

- Client and Server architecture
- HTTP request and response
- HTTP methods:
  - GET
  - POST
  - PUT
  - PATCH
  - DELETE
- URL structure
- Path parameters
- Query parameters
- HTTP headers
- Request body
- JSON
- HTTP status codes

### 2. Consuming APIs with Python

Practiced calling external REST APIs using:

- `requests`
- HTTP GET requests
- HTTP POST requests
- Query parameters
- Headers
- JSON request bodies
- JSON response parsing
- Basic API error handling

### 3. FastAPI

Learned how to build REST APIs using FastAPI.

Covered:

- FastAPI application setup
- API routes
- GET and POST endpoints
- Path parameters
- Query parameters
- Request body
- Pydantic models
- Request validation
- Response serialization
- Swagger/OpenAPI documentation
- Running FastAPI using Uvicorn

Example architecture:

Client → FastAPI → Endpoint → Response

### 4. Authentication

Learned basic API authentication concepts:

- Authentication vs Authorization
- API Keys
- Basic Authentication
- `Authorization` header
- `X-API-Key` header
- FastAPI `HTTPBasic`
- `HTTPBasicCredentials`
- FastAPI dependency injection using `Depends()`

### 5. Error Handling

Practiced handling API errors using:

- `HTTPException`
- HTTP status codes
- Request validation errors
- Invalid JSON
- Authentication failures
- Response serialization errors

### 6. Logging & Monitoring

Learned the difference between logging and monitoring.

#### Logging

Used Python's `logging` module to record:

- HTTP method
- API path
- Response status
- Execution time
- Authentication events

#### Monitoring

Covered basic application monitoring concepts:

- Health checks
- Request latency
- HTTP status codes
- Error monitoring
- Basic request monitoring

### 7. FastAPI Middleware

Learned how HTTP middleware works.

Middleware can be used for common processing across API requests, such as:

- Logging
- Request timing
- Correlation IDs
- Response headers
- Authentication-related processing

Request flow:

Client → Middleware → API Endpoint → Middleware → Client

### 8. Correlation ID

Implemented a Correlation ID using FastAPI middleware.

The middleware:

- Checks for an existing `X-Correlation-ID`
- Generates a UUID if one is not provided
- Adds the Correlation ID to the response
- Includes the ID in application logs

Purpose:

Correlation IDs help trace a single request across multiple services and application components.

Example:

Client → FastAPI → Service A → Service B

All components can use the same:

`X-Correlation-ID`

---

## API Design Concepts

Also learned the fundamentals of:

- Resource-oriented API URLs
- Query parameters
- Filtering
- Sorting
- Pagination
- `page`
- `limit`
- Client-side vs server-side pagination

Example:

```text
GET /employees?department=Mendix&page=1&limit=20&sort=name
