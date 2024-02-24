# Expense Tracker API

Expense Tracker API is a Flask-based backend application designed to help users manage their daily expenses efficiently. This API provides various functionalities such as user authentication, expense management, analysis, and email notifications.

## Features

1. **User Authentication and Authorization**:
   - Register new users and authenticate existing users securely.
   - Implement role-based access control for managing user permissions.

2. **Password Management**:
   - Allow users to update their passwords securely.

3. **Expense Management**:
   - CRUD operations for managing expenses.
   - Categorize expenses and provide filtering options.

4. **Expense Analysis**:
   - Generate reports and visualizations for expense analysis.
   - Track expenses over time and by category.

5. **Rapid MQ Based Email Notifications**:
   - Send email notifications for various events such as expense creation, password reset, etc.

6. **Swagger Documentation**:
   - Generate interactive API documentation using Swagger/OpenAPI specifications.

## Additional Features

- Multi-factor authentication (MFA)
- User profile management
- Expense categories
- Currency conversion
- Data export/import
- Reminders
- Search and filter
- Data backup and restore

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/expense-tracker-api.git
   cd expense-tracker-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Copy the `.env.example` file to `.env` and update the configurations.

4. Run the application:
   ```bash
   flask run
   ```

## API Documentation

Access the Swagger documentation at `/api/docs` endpoint after running the application.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

