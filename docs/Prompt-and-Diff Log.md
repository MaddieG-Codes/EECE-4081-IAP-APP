# Prompt-and-Diff Log — Southern City Explorer

This log tracks the literal prompts issued to the AI tool and the resulting changes (diffs) between drafts, showing the iterative refinement of requirements.

---

## Iteration 1

**Prompt:**
```
I am developing an application called Southern City Explorer.
The concept is:
"Southern City Explorer is a city exploration and navigation application
designed to help users discover cities throughout the Southern United States.
Users will be able to select a city and explore different categories of
locations, including parks, attractions, restaurants, and other points of
interest. The application will organize these locations into searchable
categories and provide useful information such as descriptions, addresses,
and navigation options. The initial version of the application will focus on
a small number of cities and categories, with the goal of eventually
expanding to additional cities and providing personalized recommendations
based on users' interests and locations."

Elicit the functional and non-functional requirements for this application.
Provide:
1. 6–8 user stories.
2. Acceptance criteria for each user story.
3. 3 non-functional requirements that are measurable or testable.

Do not write code. Focus only on requirements.
```

**AI Output (summary):**
Produced 8 user stories in "As a user, I want... so that..." format, each with
3–4 Given/When/Then acceptance criteria, covering: city selection, category
browsing, location detail viewing, search, navigation/directions, filtering,
city switching, and map view. Also produced 3 measurable NFRs covering
performance (2-second load threshold), availability (99.5% monthly uptime),
and scalability (10 cities / 10 categories / 5,000 locations without
degradation).

**Diff from Previous Version:**
Not much was too far off from what i wrote other than the Ai including navigation 


**Action Taken:** Accepted (used as the baseline requirements document)
**Notes:** Output matched the requested format (story count, AC structure,
NFR count) without needing structural correction. Content was reviewed for
domain fit (Southern US cities, POI categories) before being adopted as the
project's requirements.md.
---

## Summary of Total Iterations
- **Total prompts issued:** 1 (initial elicitation) — add more rows as you iterate
- **Net changes accepted without modification:** 1
- **Net changes modified after AI output:** 0
- **Net changes rejected:** 0
