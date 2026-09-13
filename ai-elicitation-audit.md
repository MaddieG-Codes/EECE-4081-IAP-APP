# IAP M2 — AI Elicitation Audit
**Tool:** [Claude.Ai]

**Date:** [9/8/2026]

**Purpose:** The AI tool was asked to independently elicit functional and non-functional requirements for the Southern City Explorer application.

---

# 1. AI Elicitation Prompt

The following prompt was used to ask an AI tool to generate requirements for the Southern City Explorer application:

> I am developing a Southern U.S. city exploration and navigation application called Southern City Explorer. The application allows users to select a supported city and explore locations within that city. Users should be able to view location details such as descriptions, addresses, and categories. The application should also allow users to filter locations, switch between supported cities, search for locations by name or keyword, and view locations on a map.
>
> Generate 6 user stories with acceptance criteria and 3 measurable non-functional requirements for this application.

---

# 2. Evaluation of AI-Generated User Stories

## Story 1 — Select a City

### AI Suggestion

The AI suggested that users should be able to select a city from a list and view locations associated with that city.

### Decision: KEEP

### Reason

This requirement directly matches the intended functionality of Southern City Explorer. The application is designed around allowing users to explore supported Southern U.S. cities. The requirement is also specific enough to test because the application can be checked for whether a supported city list is displayed and whether selecting a city displays the appropriate city information.

---

## Story 2 — View Location Details

### AI Suggestion

The AI suggested that users should be able to select a location and view information such as its name, description, address, and category.

### Decision: KEEP

### Reason

This matches the intended purpose of the application. Users need location information to determine whether a location is useful or interesting to them. The requirement was kept because the information displayed can be directly verified through testing.

---

## Story 3 — Filter Locations

### AI Suggestion

The AI suggested that users should be able to filter locations based on criteria such as distance, rating, or price.

### Decision: KEEP WITH MODIFICATION

### Reason

The filtering functionality matches the project's goal of helping users narrow down locations. However, the specific filtering options should depend on what information is available in the application's dataset. Therefore, the requirement was kept but should remain flexible rather than requiring every possible filter.

The final requirement allows filtering within a category by criteria such as distance, rating, or price while allowing the implementation to depend on available location data.

---

## Story 4 — Switch Between Cities

### AI Suggestion

The AI suggested that users should be able to return to the city selection screen and switch between supported cities without restarting the application.

### Decision: KEEP

### Reason

This requirement supports the application's purpose of allowing users to explore multiple Southern U.S. cities during one session. The requirement was kept because switching cities is an important part of exploring the application and can be tested by selecting one city, changing cities, and verifying that the new city's information is displayed.

---

## Story 5 — View Location on a Map

### AI Suggestion

The AI suggested that users should be able to view a selected location on a map using its coordinates.

### Decision: KEEP WITH MODIFICATION

### Reason

Map functionality supports the navigation aspect of Southern City Explorer. However, not every location may have coordinate information available. The final requirement therefore specifies that the map should only be offered when coordinates are available.

This prevents the application from attempting to display an invalid map location.

---

## Story 6 — Search for Locations

### AI Suggestion

The AI suggested that users should be able to search for locations by name or keyword and receive matching results within the selected city.

### Decision: KEEP

### Reason

Search functionality is one of the main ways users will discover locations without manually browsing every category. The requirement was kept because partial matching and a no-results message provide clear, testable behavior.

The final requirement also connects search performance to the application's performance NFR.

---

# 3. Evaluation of AI-Generated Non-Functional Requirements

## NFR 1 — Performance

### AI Suggestion

The AI suggested that search results should load quickly, preferably within a few seconds.

### Decision: MODIFY

### Reason

The phrase "within a few seconds" is not precise enough to be tested consistently. The requirement was changed to a specific 2-second limit.

### Final Requirement

> Category and search results must load within 2 seconds under normal network conditions, measured via automated load testing on a standard 4G/LTE connection with up to 500 locations per city.

This version provides a measurable response-time requirement and defines testing conditions.

---

## NFR 2 — Availability

### AI Suggestion

The AI suggested that the application's backend should remain available most of the time and minimize service interruptions.

### Decision: MODIFY

### Reason

The AI suggestion was too vague because "most of the time" does not provide a measurable target. The requirement was changed to a specific uptime percentage and measurement period.

### Final Requirement

> The application backend/API must maintain 99.5% uptime measured monthly, verified through uptime monitoring logs.

This makes availability measurable and provides a method for verifying the requirement.

---

## NFR 3 — Reliability

### AI Suggestion

The AI suggested that the application should handle searches reliably without crashing.

### Decision: MODIFY

### Reason

Although the AI identified an important reliability concern, the phrase "reliably" is subjective. The requirement was changed to include a measurable success rate.

### Final Requirement

> The application shall process valid searches without crashing for at least 99% of test cases during application testing.

This provides a measurable standard that can be verified through testing.

---

# 4. Requirements the AI Missed or Did Not Fully Specify

The AI-generated requirements provided a useful starting point, but some important details had to be added during the requirements-development process.

### 1. Clearing Filters

The AI identified filtering as a feature but did not fully specify what should happen when filters are removed.

The final requirement specifies:

> Filters can be cleared/reset, returning the full unfiltered list.

This provides a clear expected behavior for testing.

### 2. Persistence of Filters

The final requirements specify that applied filters should persist while the user remains on the category screen.

This makes the expected behavior more specific than simply stating that filtering is available.

### 3. Clearing Previous City Data

The final city-switching requirement specifies that changing cities must clear previous filters and search terms and must not retain stale data.

This was added to prevent incorrect information from one city appearing while the user is viewing another city.

### 4. Missing Location Information

The final location-detail requirement specifies that a placeholder message should appear when a description is unavailable rather than displaying a blank field.

This provides a defined behavior for incomplete data.

### 5. Missing Coordinates

The final map requirement specifies that the map option should not be offered when coordinates are unavailable.

This prevents the application from attempting to display a location that cannot be mapped.

---

# 5. AI Requirements That Were Outside the Current Scope

During the review, AI-generated suggestions may include features that could be useful in a future version but are not required for the current release.

Examples include:

* User accounts and login
* Saving favorite locations
* Social sharing
* Personalized recommendations
* Reviews and user-generated ratings
* Real-time traffic information
* Turn-by-turn navigation

These features were not included in the final requirements because the current project focuses on selecting supported cities, exploring categories, searching for locations, viewing location information, filtering results, switching cities, and viewing locations on a map.

---

# 6. Final Audit Conclusion

The AI tool was useful for generating an initial set of possible requirements and identifying major application features. However, the generated requirements were not accepted without review.Several requirements were kept because they directly matched the intended application. Other requirements were modified to make them more specific, measurable, and testable. Features outside the current project scope were not included in the final requirements.
