# Event REST API Manager

The Event REST API Manager is a robust and user-friendly tool for managing event data via a RESTful API. It allows developers to create, read, upstart_time, and delete event-related information through HTTP requests, making it a versatile solution for event management systems.
## Features

- Create new events with details such as kind, start_time, location, and description.
- Retrieve a list of all events or fetch specific events by their unique IDs.
- Update event information, including modifying event details or changing the event date and kind.
- Delete events to keep your event database organized.

## Getting Started

These instructions will help you get a copy of the Event REST API Manager up and running on your local machine for development and testing purposes.

### Prerequisites

- python and pip installed on your local machine.

### Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/falila/event-manager.git
   ```

2. Install the required dependencies:

   ```
   pip install
   ```

3. Start the API server:

   ```
   python3 run
   ```

The API should now be running on `http://localhost:3000`.

## API Endpoints

### Create an Event

- Endpoint: `POST /events`
- Description: Create a new event with the provided details.
- Request Body:

  ```json
  {
    "kind": "Event kind",
    "start_time": "2023-10-20",
    "end_time": "2023-10-28",
    "timestamp": "928932034711002"
  }
  ```

### Get All Events

- Endpoint: `GET /events`
- Description: Retrieve a list of all events.

### Get a Specific Event

- Endpoint: `GET /events/:id`
- Description: Retrieve a specific event by its unique ID.

### Update an Event

- Endpoint: `PUT /events/:id`
- Description: Update event information using the provided details.
- Request Body:

  ```json
  {
    "kind": "Alert",
    "start_time": "2023-10-25",
    "end_time":"2024-01-23",
    "description": "Upstart_timed Event Description"
  }
  ```

### Delete an Event

- Endpoint: `DELETE /events/:id`
- Description: Delete a specific event by its unique ID.

## Usage

You can use tools like `curl`, Postman, or integrate the API into your applications to interact with the Event REST API Manager. Please refer to the API endpoints section for more details on making requests.

## Contributing

Contributions are welcome! If you would like to contribute to the development of this API, please follow our [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

