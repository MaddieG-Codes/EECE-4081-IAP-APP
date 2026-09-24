# ADR-001: Backend/Frontend Communication Pattern

**Status:** Accepted
**Date:** 2026-09-24

## Context

Southern City Explorer is a Flask app where most pages (city selection, category
browsing, location detail) are simple, navigable content: a user clicks through and
the server has everything it needs to render the next full page. But two user
stories break that pattern:

- **Map view** — the map needs to update (pan, re-center, show/hide pins) without
  reloading the whole page, or it feels broken compared to any map a user has ever
  touched.
- **Search/filter** — filtering by category or city needs to update results as the
  user interacts, not on a full page reload, or the interaction reads as sluggish
  and the acceptance criteria for that story (filter results update without a full
  navigation) aren't met.

The rest of the app has no such requirement. Every page beyond those two can be
rendered server-side with no loss of usability.

This is a two-person, time-boxed course project. Whatever pattern gets picked has
to be learnable and shippable inside the remaining sprints — there's no room to
recover from an architecture that turns out to need a rewrite three weeks in.

## The Decision

Use a **hybrid rendering model**:

- Jinja2 server-rendered templates for all standard pages (city list, category
  browse, location detail, static content).
- A small set of JSON API endpoints (`/api/locations`, `/api/search`) that serve
  only the map and search/filter interactions, called via `fetch()` from vanilla
  JS on top of the rendered page.

There is exactly one frontend rendering paradigm at a time per page — no page
is half server-rendered and half client-hydrated. The JSON endpoints exist only
where a user story requires interaction without a page reload.

## Alternatives Considered

**Pure server-rendered (Jinja2 everywhere, no JSON API).**
Simplest possible architecture — one rendering path, no API surface to design,
no client-side state to manage. Rejected because the map and filter stories can't
be honestly satisfied this way. A "filter" that triggers a full page reload
technically works but fails the acceptance criteria in spirit, and demoing a map
that reloads the page to pan would read as a step backward from any commercial
map, undermining the design defense.

**Full JSON API + client-rendered frontend (SPA-style, even without a framework).**
Would have made the map and filter interactions cleaner and more consistent with
each other — one data-fetching pattern for the whole app instead of two. Rejected
because it makes every simple page (which is most of the app) pay the cost of
client-side rendering logic it doesn't need, for a two-person team with a
deadline. It also front-loads a decision — "we're an SPA now" — that the
project's own scope (mostly static content browsing) doesn't justify.

Going the pure-server-rendered route was the real temptation: it's less work
right now, and for a class project "it technically works" is a defensible bar.
Choosing the hybrid instead means carrying two patterns for the rest of the
project, on a team of two, under a deadline — that's the real cost being
accepted here, not a hypothetical one.

## Consequences

**What this makes easy:**
- Most pages stay simple: no client-side state, no loading spinners, no stale-data
  bugs — they're just HTML the server already assembled correctly.
- The map and filter interactions get the responsiveness they actually need,
  without forcing that complexity onto pages that don't need it.
- Each new page defaults to the simpler pattern (Jinja2) unless a user story
  specifically demands otherwise, which keeps scope from creeping toward "let's
  just make everything an API."

**What this makes hard — the part that matters:**
- **Two data paths to keep in sync.** Location data now has two representations:
  the Jinja2 template context and the JSON serialization for `/api/locations`.
  If the data model changes (a new field, a renamed attribute), both paths need
  updating, and nothing enforces that they stay consistent — a bug where the
  map shows a field the detail page doesn't (or vice versa) is now possible in a
  way it wouldn't be in a single-pattern app.
- **No clean path to "just add one more interactive feature."** Every future
  story has to be individually judged: does this need a JSON endpoint, or is it
  fine as a server-rendered page? That judgment call didn't exist under the pure
  server-rendered alternative, and it's a recurring tax on every new feature from
  here forward.
- **Testing burden doubles instead of adding.** The test suite now needs to cover
  full-page rendering (Jinja2 output) and API contract correctness (JSON shape,
  status codes) as genuinely separate concerns, with separate tooling
  expectations, rather than one consistent testing approach across the app.
- **Closes the door on migrating to a frontend framework later without a real
  rewrite.** If a future version of this app wanted to move to React or Vue, the
  Jinja2-rendered pages would need to be fully redone — the hybrid doesn't
  degrade gracefully into a full SPA, it has to be replaced. Choosing pure JSON
  API up front would have kept that door open; this decision closes it for as
  long as this codebase lives.
- **A new contributor has to learn two conventions, not one**, and has to learn
  *when* to use which — that's implicit project knowledge that lives in this ADR
  and in code review, not in the framework itself.
