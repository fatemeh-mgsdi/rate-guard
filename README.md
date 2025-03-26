# Rate Guard

Rate Guard is a web-based rate limiting management system that allows you to register and manage API providers with configurable rate limits. It provides a user-friendly interface for monitoring and testing rate limits across different providers.

## Features

- Register new API providers with custom rate limits and time windows
- View all registered providers and their configurations
- Test rate limiting by sending requests to providers
- Real-time feedback on rate limit status
- Responsive web interface
- RESTful API endpoints
- Comprehensive API documentation with Swagger/OpenAPI

## Technology Stack

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, JavaScript with jQuery
- **Styling**: Custom CSS with modern design principles
- **Rate Limiting**: Custom implementation using sliding window algorithm
- **API Documentation**: OpenAPI 3.0 (Swagger)

## Project Structure

```
rate_guard/
├── static/
│   └── style.css          # CSS styles for the web interface
├── templates/
│   └── index.html         # Main HTML template
├── app.py                 # Main Flask application
├── provider.py           # Provider class implementation
├── swagger.yaml          # API documentation
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd rate_guard
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## API Documentation

The API documentation is available in OpenAPI 3.0 (Swagger) format. You can view it in several ways:

1. Using Swagger UI locally:
   ```bash
   npm install -g swagger-ui
   swagger-ui swagger.yaml
   ```

2. Using online Swagger Editor:
   - Visit https://editor.swagger.io/
   - Copy the contents of `swagger.yaml`

3. Using Swagger UI:
   - Visit https://swagger.io/tools/swagger-ui/
   - Import the `swagger.yaml` file

## Implementation Details

### Rate Limiting Algorithm
The system implements a sliding window rate limiting algorithm that:
1. Tracks request timestamps for each provider
2. Maintains a rolling window of requests
3. Enforces rate limits based on the configured window duration
4. Provides real-time feedback on rate limit status

### Frontend Implementation
- Modern, responsive design using CSS Grid and Flexbox
- Real-time updates using AJAX
- User-friendly form validation
- Clean and intuitive interface
- Mobile-first approach

### Backend Implementation
- Flask-based REST API
- In-memory storage for provider configurations
- Thread-safe rate limiting implementation
- Error handling and validation
- Asynchronous request processing

## Usage Example

1. Register a new provider:
   - Enter provider name (e.g., "API Provider 1")
   - Set rate limit (e.g., 100 requests)
   - Set window duration (e.g., 60 seconds)
   - Click "Register Provider"

2. Test rate limiting:
   - Find the registered provider in the list
   - Click "Send Request" to test the rate limit
   - Monitor the response for rate limit status

## Development

### Prerequisites
- Python 3.7+
- Node.js (for Swagger UI)
- Modern web browser

### Running Tests
```bash
python -m pytest tests/
```

### Code Style
The project follows PEP 8 guidelines. To check code style:
```bash
flake8 .
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask web framework
- jQuery library
- Inter font family
- OpenAPI/Swagger community 