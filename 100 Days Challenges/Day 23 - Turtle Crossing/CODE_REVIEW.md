# Code Review — Day 23: Turtle Crossing

**Reviewed:** 2026-10-21
**Reviewer:** Claude Opus 5 (via Claude Code)
**Scope:** `project/crossing_objects.py`, `project/main.py`
**Context:** First attempt, written without following any guide, tutorial, or
course solution. Graded against the standard for a CS beginner at this stage.

**Overall: 7 / 10.** Design instincts read intermediate; state management still
reads beginner. Most no-tutorial first attempts at this project land around 4–5.

---

## What's good

**Classes with real behaviour, not just data bags.**
`CarManager` subclasses `turtle.Turtle` and owns its own `move()`, `move_speed`,
and `set_pos()`. The data and the methods that act on it live together — correct
OOP rather than cargo-culted OOP.

**Geometry is derived, not hard-coded.**
`crossing_objects.py:26-31` builds `LANES` and `COLUMNS` from the `X_AXIS` /
`Y_AXIS` constants so cars snap to a grid. The obvious beginner move is
`random.randint(-250, 250)` and ragged traffic. This is a design decision about
the *structure* of the road, and most beginners don't make it.

**Went past the brief.**
Four-direction movement, a lives system, a drawn finish line, per-car speed —
none of it required.

**Applied new knowledge immediately.**
The `if __name__ == '__main__'` guard was added the same day it was learned,
with a comment explaining the reasoning. That habit compounds.

**Correct rendering pattern.**
`tracer(0)` + `screen.update()` is right, and `onkeypress` over `onkey` is
genuinely the better choice for responsive movement.

---

## What's weak

Nearly every flaw traces to **one root cause: one object holding two jobs, or
one fact living in two places.**

### 1. `ScoreBoard` has two unrelated responsibilities

It writes the score text *and* draws the finish line, using a single turtle.
Because `clear()` is per-turtle rather than per-drawing, clearing the text also
erases the finish line.

**Fix:** one turtle, one responsibility. Give the finish line its own turtle or
its own class.

### 2. State and display can drift apart

`increase_score()` (`crossing_objects.py:112`) redraws after mutating.
`decrease_life()` (`crossing_objects.py:109`) does not. The lives counter was
decrementing correctly all along — the screen simply never showed it.

The real problem isn't the missing redraw; it's that every future mutator has to
*remember* to redraw, and one day one won't.

**Fix:** stop making redrawing each method's job. Either call `update_score()`
once per frame from the game loop, or route both mutators through one method.

### 3. Duplicated constants that already disagree

`X_AXIS` / `Y_AXIS` are defined in both files — and `Y_AXIS` is `260` in
`crossing_objects.py:25` but `280` in `main.py:14`. The copies in `main.py` are
never even used. Two sources of truth that already contradict each other is a
bug waiting to be used.

### 4. Redundant state

`self.finsish_line` (`crossing_objects.py:98`) is a misspelled copy of the
`FINISH_LINE_Y` constant that `main.py` could read directly. Indirection with no
payoff.

### 5. The hitbox is a circle around a rectangle

`main.py:43` — `car.distance(tim) < 30` measures centre-to-centre, but cars are
50x20 px. It registers diagonal near-misses and misses real hits on the car's
far end. The `car.xcor() - 10 <= tim.xcor()` clause adds nothing `distance`
doesn't already cover and looks like a leftover.

**Fix:** for rectangles, compare x and y separately.

### 6. Conditions in the wrong scope

`main.py:46-50` — the `lives <= 0` check and the finish-line check sit inside
`for car in cars:`, so they evaluate 16 times per frame. Harmless today, but
these aren't per-car conditions.

### 7. Inconsistent naming

- `up()` / `down()` vs `go_left()` / `go_right()`
- `starting_pos()`, `set_pos()`, `reset_pos()` — three similar names whose jobs
  can't be told apart without reading them, and `set_pos` sits a hair away from
  turtle's built-in `setpos`
- `DEFAULT_LIFE` should be `DEFAULT_LIVES` (it's a count)
- `CarManager` manages nothing — it *is* a car; the managing happens in `main.py`

### 8. Loose ends

- `random as rng` is imported but unused in `main.py`
- `speed_increase()` is never called, so there is no difficulty progression yet
- `main()` in `crossing_objects.py` is a `pass` stub

---

## Assessment

Worth noting which beginner mistakes are **absent**: no scope confusion, no
forgotten `self`, no mutable-default traps, no tangled conditionals, no
200-line script with zero functions.

The bugs here are all "two things that should be one thing." That is a more
sophisticated failure mode than the usual beginner set, and it happens to be the
exact problem that separates people who can write 100 lines of code from people
who can write 10,000.

## The one thing to work on next

**Single source of truth.**

Every issue above is a violation of it — duplicated constants, a duplicated
finish-line value, one turtle doing two jobs, redraw logic duplicated across
mutators. Fix that single habit and six of these problems stop being possible.
