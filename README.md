# L-System Fractal Architect
**Name:** Piyush Lohia
**Reg No:** 25BCE2527

### Project Overview
This application renders complex L-System fractals using Python. To meet the core constraints, it uses a **Single-Library Tech Stack** (Tkinter + Turtle) without external game engines.

### Key Technical Approaches

**1. The Hybrid GUI Architecture**
Instead of allowing the Turtle module to spawn its own pop-up window, I used `turtle.RawTurtle` to embed the graphics engine directly inside a `tk.Canvas`. This creates a seamless, single-window application where controls and rendering live together.

**2. The Recursive Logic Engine**
To mimic the parallel rewriting nature of L-Systems, I implemented a string expansion function (`expand_string`) that iterates through the axiom `N` times. It constructs the final instruction string character-by-character based on the user-defined Rule Dictionary.

**3. Branching via Stack Data Structure**
To achieve organic, plant-like structures, I implemented a **Push/Pop Stack system**:
* `[` **(Push):** Saves the turtle's current state (position & heading) to a stack.
* `]` **(Pop):** Restores the last saved state, allowing the turtle to "teleport" back to the saved position (i.e. trunk).

**4. Real-Time Optimization**
Rendering thousands of segments is naturally slow in Turtle. I optimized this by disabling the animation loop using `turtle.tracer(0, 0)` and forcing a single frame refresh with `screen.update()` at the end. This allows the engine to render complex fractals (10,000+ characters) instantly without UI lag.
