# Vendor Management System with Performance Metrics

This is a Django-based system for managing vendors, purchase orders, and calculating vendor performance metrics.

## Setup Instructions

1. Clone the repository:"https://github.com/shubhamrepe/vendor-managment.git"
2. Install dependencies:
3. Run migrations:
4. Start the development server:


## API Endpoints

- **Vendor Profile Management**
- POST `/api/vendors/`: Create a new vendor.
- GET `/api/vendors/`: List all vendors.
- GET `/api/vendors/{vendor_id}/`: Retrieve a specific vendor's details.
- PUT `/api/vendors/{vendor_id}/`: Update a vendor's details.
- DELETE `/api/vendors/{vendor_id}/`: Delete a vendor.

- **Purchase Order Tracking**
- POST `/api/purchase_orders/`: Create a purchase order.
- GET `/api/purchase_orders/`: List all purchase orders with an option to filter by vendor.
- GET `/api/purchase_orders/{po_id}/`: Retrieve details of a specific purchase order.
- PUT `/api/purchase_orders/{po_id}/`: Update a purchase order.
- DELETE `/api/purchase_orders/{po_id}/`: Delete a purchase order.

- **Vendor Performance Evaluation**
- GET `/api/vendors/{vendor_id}/performance`: Retrieve a vendor's performance metrics.

## Running Tests

Run the test suite using:
