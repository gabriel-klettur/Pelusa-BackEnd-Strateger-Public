---
name: Data Design - Template
about: Template of Data Design for Endpoints
title: ''
labels: ''
assignees: Beelzebot777

---

---
name: Data Design
about: Define the database schema and external integrations for the endpoint.
title: "Data Design for [Endpoint Name]"
labels: data-design
assignees: Gaby
---

## **Database Models**
- Example:
```python
class YourModel(Base):
    __tablename__ = "your_table"
    id = Column(Integer, primary_key=True, index=True)
    field1 = Column(String, index=True)
    field2 = Column(Float)
```

## **Database Schema**
Include relationships and constraints.
- Example: Foreign key constraints, unique indexes, etc.

## **External Services**
- List any external services or APIs that the endpoint interacts with.
- Example: BingX API for retrieving trading data.

## **Data Flow Diagram**
- (Optional) Include a diagram showing how data flows through the system.
