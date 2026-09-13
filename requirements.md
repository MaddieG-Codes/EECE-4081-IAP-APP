# 🍑 Southern City Explorer - Requirements
## User Stories
### Story 1: Select a City
As a user, I want to select a city from a list, so that I can explore locations within that specific city.
### Acceptance Criteria:
Given the app is launched, when the user views the home screen, then a list of supported cities is displayed.
Given a list of cities, when the user taps/selects a city, then the app navigates to that city's category view.
If no city is selected, the app does not display location data.
The city list reflects only cities currently supported by the initial release.

### Story 2: View Location Details
As a user, I want to view detailed information about a location, so that I can decide whether to visit it.
### Acceptance Criteria:
Given a location list, when the user selects a location, then a detail view opens showing description, address, and category.
If a description is unavailable, a placeholder message is shown instead of a blank field.
The detail view loads without requiring the user to re-select the city or category.


### Story 3: Filter Locations Within a Category
As a user, I want to filter locations within a category (e.g., by distance, rating, or price), so that I can narrow results to what matters most to me.
### Acceptance Criteria:
Given a category location list, when the user applies a filter, then only locations matching the filter criteria are displayed.
Filters can be cleared/reset, returning the full unfiltered list.
Applied filters persist while the user remains on that category screen.


### Story 4: Switch Between Cities
As a user, I want to switch to a different supported city without restarting the app, so that I can explore multiple cities in one session.
### Acceptance Criteria:
Given the user is viewing a city's data, when they select "Change City," then the city selection screen is displayed.
Switching cities clears previously applied filters/search terms from the prior city.
The app does not crash or retain stale data from the previously selected city.


### Story 5: View Location on a Map
As a user, I want to see a location's position on a map, so that I can understand where it is relative to other points of interest.
### Acceptance Criteria:
Given a location detail view, when the user opens the map view, then a map displays a marker at the location's coordinates.
If coordinates are unavailable, the map view is not offered for that location.
The map is centered on the selected location by default.

### Story 6: Search for Locations
As a user, I want to search for locations by name or keyword, so that I can quickly find a specific place without browsing categories.
### Acceptance Criteria:
Given the search feature, when the user enters a search term, then matching locations within the selected city are returned.
Search results update to reflect partial matches (not only exact matches).
If no results match, an appropriate "no results found" message is displayed.
Search results display within a defined response time (see NFR-1).



## 🍑 Southern City Explorer - Non-Requirements

-Performance: Category and search results must load within 2 seconds under normal network conditions (measured via automated load testing on a standard 4G/LTE connection with up to 500 locations per city).

-Availability: The application backend/API must maintain 99.5% uptime measured monthly, verified through uptime monitoring logs.

-Reliability: The application shall process valid searches without crashing for at least 99% of test cases during application testing.
