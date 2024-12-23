# Global Event Tracker
A web application that visualizes global disaster events on a map, pulling data from the NASA EONET API. Users can filter events by category, country, and date range.

![image](https://github.com/user-attachments/assets/5b91f7e4-33db-4fed-8ba8-861f5800c20d)

## Table of Contents

- [Project Structure](#project-structure)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [API Endpoints](#api-endpoints)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)

## Project Structure

The project is divided into two main directories: `backend` and `frontend`.
-   `backend`: Contains the Django REST Framework application, including the API logic, data models, and database interactions.
-   `frontend`: Contains the React.js application, responsible for rendering the user interface and map.

## Backend Setup

### Prerequisites
    -   Python 3.11 or 3.12
    -   pip (Python package manager)

1.  **Navigate to the `backend` directory:**
    ```bash
    cd backend
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv env
    ```
    -   **Activate the virtual environment:**
        -   On macOS/Linux:
          ```bash
          source env/bin/activate
          ```
        -   On Windows:
          ```bash
          .\env\Scripts\activate
          ```

3.  **Install dependencies:**
    ```bash
    pip install -r ../requirements.txt
    ```

4.  **Apply migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

The API will be available at `http://localhost:8000/api/v1/`.

## Frontend Setup

### Prerequisites
    -   Node.js (>=18)
    -   npm (Node Package Manager)

1.  **Navigate to the `frontend` directory:**
    ```bash
    cd frontend
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Start the development server:**
    ```bash
    npm start
    ```
    The frontend will be available at `http://localhost:3000`.

## Features

-   **Interactive Map:** Displays disaster events on a Leaflet map.
-   **Data Fetching:** Fetches real-time disaster data from the NASA EONET API.
-   **Event Filtering:**
    -   Filter events by country.
    -   Filter events by category (e.g., wildfires, volcanoes).
    -   Filter events by date range.
-   **Event Details:** Displays a popup with event details when clicking on a marker.
-   **Categorized Icons:** Uses unique map marker icons to distinguish different event categories.

## Technologies Used

### Backend

-   **Django REST Framework:** For building the API.
-   **Python:** The core programming language.
-   **geopy:** For geocoding event coordinates to country names.
-   **PostgreSQL:** Used as the main database.
-    **requests:** Used to fetch data from nasa eonet api

### Frontend

-   **React.js:** For building the user interface.
-   **Leaflet:** For the interactive map.
-   **React Leaflet:** For integrating Leaflet with React.
-   **Fetch API:** For making requests to the backend API.
    -   **node.js and npm:** as a dependency manager.

## API Endpoints

-   **`GET /api/v1/`**: Fetches all events from NASA EONET and pushes/updates to the database.
-   **`GET /api/v1/events`**: Retrieves all events, supporting filters through query parameters:
    -   `country`: filter by country.
    -   `category`: filter by event category.
    -   `start_date`: filter events with a start date greater or equal to the value provided.
    -   `end_date`: filter events with an end date lesser or equal to the value provided.
-   **`GET /api/v1/events/<event_id>`**: Retrieves a specific event based on the event ID.
-  **`GET /api/v1/categories`**: Retrieves all event categories.
-   **`GET /api/v1/update_countries/`**: Updates the 'country' field for events with geocoded locations.

## Running the Application

1.  Ensure that you've completed both the [Backend Setup](#backend-setup) and [Frontend Setup](#frontend-setup) steps.
2.  Start the backend server by running `python manage.py runserver` in the `backend` directory.
3.  Start the frontend server by running `npm start` in the `frontend` directory.
4.  Open your browser and go to `http://localhost:3000` to see the map application.

## Testing
1. **To run the backend tests:**
    ```bash
    python manage.py test api.tests
    ```

## Future Enhancements

-   **Implement pagination** for handling larger datasets.
-   **Improve UI/UX**, including better error handling and loading indicators.
-   **Add more filtering options**, such as searching by magnitude.
-   **Implement real-time updates**.
-   **Add user authentication and authorization**.

## Contributing

Feel free to contribute to the Global Event Tracker project! To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and test them thoroughly.
4.  Submit a pull request.

## Contact
For any questions or comments, feel free to reach out to albericoeduardo202@gmail.com
