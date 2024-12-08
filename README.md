
# Payment Processing System Using Factory Method

This Django project demonstrates a **Payment Processing System** where various payment methods are handled dynamically using the **Factory Method Design Pattern**. The goal is to separate the logic of payment processing for different payment methods into dedicated classes, making the system scalable and easy to maintain.

## Features

1. **Supports Multiple Payment Methods**:
   - Credit Card.
   - PayPal.
   - Apple Pay.

2. **Dynamic Payment Handling**:
   - The `PaymentFactory` dynamically chooses the appropriate payment processor based on the payment method.

3. **Scalable Design**:
   - Adding new payment methods requires minimal changes.

4. **REST API Endpoint**:
   - Provides an endpoint to process payments based on their unique ID.

---

## Project Structure

### 1. Models (`models.py`)

Defines the `Payment` model, which includes:
- `amount`: The amount to be processed.
- `payment_method`: The method of payment (Credit Card, PayPal, or Apple Pay).
- `created_at`: Timestamp for when the payment was created.

### 2. Factories (`factories.py`)

Implements the Factory Method Design Pattern:
- **Payment Processor Classes**:
  - `CreditCardPayment`: Processes credit card payments.
  - `PayPalPayment`: Processes PayPal payments.
  - `ApplePayPayment`: Processes Apple Pay payments.
  
- **PaymentFactory**:
  - Dynamically selects the appropriate payment processor based on the `payment_method`.

### 3. Views (`views.py`)

Handles requests to process payments:
- Retrieves the `Payment` object from the database.
- Uses `PaymentFactory` to choose the appropriate payment processor.
- Processes the payment and returns a JSON response with the result.

### 4. URL Configuration (`urls.py`)

Maps the payment processing API to:
```
/payments/process_payment/<int:payment_id>/
```

---

## How It Works

1. **Create a Payment**:
   - Add a payment via Django Admin or directly through the database.
   - Specify the `amount` and `payment_method`.

2. **Process the Payment**:
   - Access the endpoint `/payments/process_payment/<payment_id>/`.
   - The system uses `PaymentFactory` to determine the correct processor for the `payment_method`.
   - Executes the appropriate processing logic for the payment.

3. **Get a Response**:
   - Returns a JSON response indicating the success or failure of the payment processing.

---

## Sample JSON Response

### Credit Card Payment:

```json
{
    "status": "success",
    "message": "Processing credit card payment of $100.00."
}
```

### PayPal Payment:

```json
{
    "status": "success",
    "message": "Processing PayPal payment of $200.00."
}
```

### Apple Pay Payment:

```json
{
    "status": "success",
    "message": "Processing Apple Pay payment of $300.00."
}
```

---

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd payment_project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the server:
   ```bash
   python manage.py runserver
   ```

5. Test the endpoint:
   - Add a payment in Django Admin.
   - Access the endpoint: `/payments/process_payment/<payment_id>/`.

---

## Future Improvements

1. Add support for additional payment methods (e.g., Stripe, Google Pay).
2. Integrate with third-party APIs for real payment processing.
3. Implement authentication and authorization for secure API access.

---
