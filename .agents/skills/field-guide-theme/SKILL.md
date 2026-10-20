---
name: field-guide-theme
description: >-
  Enterprise Architect Field Guide Design System & Theme.
  Use whenever creating, updating, styling, or refactoring single-file HTML/CSS/JS field guides,
  technical interview manuals, architecture cheatsheets, or interactive documentation.
---

# Enterprise Architect Field Guide Design System (2026 Edition)

> Complete design system, CSS architecture, component library, and interactive JavaScript engine
> for single-file HTML guides (React Performance Field Guide, MERN + TypeScript Ultimate Guide, etc.).

---

## 1. Design Aesthetics & Core Principles

- **Visual Tone:** Deep, immersive dark space background (`#060913`) with cyan (`#38bdf8`), teal (`#2dd4bf`), purple (`#a855f7`), and amber (`#f59e0b`) glowing accents.
- **Glassmorphism:** Multi-layered blurred surfaces (`backdrop-filter: blur(20–25px)`), translucent card backgrounds, subtle 1px border lines, and top highlight borders.
- **Depth & Lighting:** Fixed radial mesh orbs (`.ambient-glow`) with `orbFloat` keyframe animation.
- **Typography:**
  - Display / Headings: `'Outfit', 'Space Grotesk', sans-serif`
  - Body: `'Inter', sans-serif`
  - Mono / Code / Labels: `'JetBrains Mono', 'DM Mono', monospace`
- **Icons:** FontAwesome 6.4.0 via CDN.
- **Always import these Google Fonts:**
  ```html
  <link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&family=Outfit:wght@500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  ```

---

## 2. Design Tokens & CSS Variables

### 2.1 Core Surface, Color & Typography Tokens

```css
:root {
  /* ── Surfaces ── */
  --bg-base: #060913;
  --bg-surface: rgba(15, 23, 42, 0.75);
  --bg-elevated: rgba(24, 33, 54, 0.85);
  --bg-card-3d: rgba(13, 20, 36, 0.8);
  --surface-hover: rgba(30, 41, 68, 0.9);
  --border-glass: rgba(255, 255, 255, 0.08);
  --border-glow: rgba(56, 189, 248, 0.35);

  /* ── Accent Palette ── */
  --cyan-glow: #38bdf8;
  --teal: #2dd4bf;
  --teal-glow: rgba(45, 212, 191, 0.25);
  --react-blue: #61dafb;
  --emerald-glow: #10b981;
  --amber-glow: #f59e0b;
  --rose-glow: #f43f5e;
  --purple-glow: #a855f7;
  --indigo-glow: #818cf8;

  /* ── Text Scale ── */
  --text-main: #f8fafc;
  --text-muted: #94a3b8;
  --text-dim: #cbd5e1;

  /* ── Shadows ── */
  --shadow-3d: 0 20px 40px -15px rgba(0, 0, 0, 0.75),
               0 0 25px -5px rgba(56, 189, 248, 0.15);
  --shadow-card: 0 10px 30px -10px rgba(0, 0, 0, 0.6),
                 inset 0 1px 0 rgba(255, 255, 255, 0.1);

  /* ── Fonts ── */
  --font-body: 'Inter', sans-serif;
  --font-display: 'Outfit', 'Space Grotesk', sans-serif;
  --font-mono: 'JetBrains Mono', 'DM Mono', monospace;

  /* ── Radius ── */
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 14px;
  --radius-xl: 18px;
  --radius-2xl: 24px;
  --radius-full: 999px;
}
```

**Light mode overrides:**

```css
[data-theme="light"] {
  --bg-base: #f8fafc;
  --bg-surface: rgba(255, 255, 255, 0.9);
  --bg-elevated: rgba(241, 245, 249, 0.95);
  --bg-card-3d: rgba(255, 255, 255, 0.95);
  --surface-hover: rgba(226, 232, 240, 0.95);
  --border-glass: rgba(0, 0, 0, 0.08);
  --border-glow: rgba(2, 132, 199, 0.35);
  --cyan-glow: #0284c7;
  --teal: #0d9488;
  --text-main: #0f172a;
  --text-muted: #64748b;
  --text-dim: #334155;
  --shadow-3d: 0 20px 40px -15px rgba(0, 0, 0, 0.08),
               0 0 20px rgba(2, 132, 199, 0.1);
  --shadow-card: 0 10px 25px -5px rgba(0, 0, 0, 0.06),
                 inset 0 1px 0 rgba(255, 255, 255, 0.9);
}
```

---

### 2.2 Spacing Scale

All spacing uses a consistent scale. **Never hardcode arbitrary pixel values** — use these tokens:

```css
:root {
  --space-2xs: 2px;    /* badge vertical padding                        */
  --space-xs:  4px;     /* badge padding, runner-header pb, tight gaps   */
  --space-sm:  8px;     /* tag gaps, search-result gaps, nav-link mb     */
  --space-md:  12px;    /* card-title mb, cheat-header py, eyebrow mb    */
  --space-lg:  16px;    /* pre padding, hero-stats gap, section-header pb*/
  --space-xl:  20px;    /* cheat-body padding, demo-body padding         */
  --space-2xl: 24px;    /* card padding, sidebar top-padding, hero-tags mt*/
  --space-3xl: 28px;    /* section-header mb, demo-widget my             */
  --space-4xl: 32px;    /* lede mb, level-head mt                        */
  --space-5xl: 36px;    /* hero padding-x, glass-author-bar mb           */
  --space-6xl: 44px;    /* hero padding-y                                */
  --space-7xl: 48px;    /* hero mb, content padding-x                    */
  --space-8xl: 64px;    /* section mb (biggest vertical rhythm)          */
}
```

---

### 2.3 Transition & Animation Tokens

```css
:root {
  /* ── Easing ── */
  --ease-default: ease;
  --ease-smooth: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);

  /* ── Durations ── */
  --duration-fast: 0.15s;    /* nav-link, copy-btn hover              */
  --duration-normal: 0.2s;   /* search-input focus, header-btn hover  */
  --duration-slow: 0.25s;    /* card hover, sidebar slide             */
  --duration-theme: 0.3s;    /* body bg/color theme transition        */
  --duration-toast: 0.3s;    /* toast & backToTop appear/disappear    */
}
```

**Standard transitions applied:**

```css
body { transition: background var(--duration-theme), color var(--duration-theme); }
.card, .cheat-block { transition: all var(--duration-slow) var(--ease-smooth); }
.nav-link { transition: all var(--duration-fast); }
.search-input { transition: all var(--duration-normal); }
.social-pill { transition: all var(--duration-normal); }
.sidebar { transition: transform var(--duration-slow) var(--ease-default); }
#backToTop, #toast { transition: all var(--duration-toast); }
```

**Keyframe animations:**

```css
@keyframes orbFloat {
  0%   { transform: translate(0, 0) scale(1); }
  50%  { transform: translate(50px, 35px) scale(1.12); }
  100% { transform: translate(-35px, 70px) scale(0.92); }
}

@keyframes pulseGlow {
  0%, 100% { box-shadow: 0 0 8px var(--emerald-glow); }
  50%      { box-shadow: 0 0 16px var(--emerald-glow), 0 0 24px rgba(16, 185, 129, 0.3); }
}
/* Used on .live-status-dot */
.live-status-dot { animation: pulseGlow 2s ease-in-out infinite; }
```

**Reduced-motion respect:**

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
  }
}
```

---

### 2.4 Content Heading Hierarchy & Tokens

All headings follow a strict color hierarchy for visual rhythm and scanability:

```css
:root {
  /* ── H2: Section Header (major chapters) ── */
  --heading-section-gradient: linear-gradient(135deg, #38bdf8, #2dd4bf);
  --heading-section-size: 26px;
  --heading-section-weight: 800;
  --heading-section-icon-bg: rgba(56, 189, 248, 0.12);
  --heading-section-icon-border: rgba(56, 189, 248, 0.3);

  /* ── H3: Level Head (sub-topics) ── */
  --heading-level-gradient: linear-gradient(135deg, #a855f7, #818cf8);
  --heading-level-size: 20px;
  --heading-level-weight: 700;
  --heading-level-accent: #a855f7;

  /* ── H4: Card Title ── */
  --heading-card-color: var(--text-main);
  --heading-card-size: 16px;
  --heading-card-weight: 700;

  /* ── H5: Inline Sub-heading ("Why?", "Gotcha:", "Pattern:") ── */
  --heading-inline-color: var(--teal);
  --heading-inline-size: 14px;
  --heading-inline-weight: 700;
  --heading-inline-transform: uppercase;
  --heading-inline-tracking: 0.08em;
}

[data-theme="light"] {
  --heading-section-gradient: linear-gradient(135deg, #0284c7, #0d9488);
  --heading-section-icon-bg: rgba(2, 132, 199, 0.1);
  --heading-section-icon-border: rgba(2, 132, 199, 0.25);
  --heading-level-gradient: linear-gradient(135deg, #7c3aed, #6366f1);
  --heading-level-accent: #7c3aed;
  --heading-inline-color: #0d9488;
}
```

**CSS for each level:**

```css
/* ── H2: Section Header ── */
.section-header {
  display: flex; align-items: center; gap: 14px;
  margin-bottom: var(--space-3xl); padding-bottom: var(--space-lg);
  border-bottom: 1px solid var(--border-glass);
}
.section-icon {
  width: 42px; height: 42px; border-radius: var(--radius-lg);
  display: flex; align-items: center; justify-content: center;
  font-size: 20px; flex-shrink: 0;
  background: var(--heading-section-icon-bg);
  border: 1px solid var(--heading-section-icon-border);
}
.section-title {
  font-family: var(--font-display);
  font-size: var(--heading-section-size);
  font-weight: var(--heading-section-weight);
  background: var(--heading-section-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.section-subtitle { font-size: 14px; color: var(--text-muted); margin-top: var(--space-2xs); }

/* ── H3: Level Head ── */
.level-head {
  font-family: var(--font-display);
  font-size: var(--heading-level-size);
  font-weight: var(--heading-level-weight);
  background: var(--heading-level-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: var(--space-4xl) 0 var(--space-lg);
  padding-left: 14px;
  border-left: 3px solid var(--heading-level-accent);
}

/* ── H4: Card Title ── */
.card-title {
  font-family: var(--font-display);
  font-size: var(--heading-card-size);
  font-weight: var(--heading-card-weight);
  color: var(--heading-card-color);
  margin-bottom: var(--space-md);
}

/* ── H5: Inline Sub-heading ── */
.inline-head {
  font-family: var(--font-mono);
  font-size: var(--heading-inline-size);
  font-weight: var(--heading-inline-weight);
  color: var(--heading-inline-color);
  text-transform: var(--heading-inline-transform);
  letter-spacing: var(--heading-inline-tracking);
  margin: var(--space-xl) 0 var(--space-sm);
}
```

**HTML pattern:**

```html
<!-- H2: Section Header -->
<div class="section-header" id="section-id">
  <div class="section-icon"><i class="fa-solid fa-icon-name"></i></div>
  <div>
    <h2 class="section-title">Section Title</h2>
    <p class="section-subtitle">Brief description of this section</p>
  </div>
</div>

<!-- H3: Level Head -->
<h3 class="level-head">Sub-Topic Title</h3>

<!-- H4: Card Title (inside .card or .cheat-block) -->
<h4 class="card-title">Concept / Pattern Name</h4>

<!-- H5: Inline Sub-heading (inside a card body) -->
<h5 class="inline-head">Why This Matters</h5>
```

---

### 2.5 Code Snippet & Syntax Highlighting Tokens

**Do not use flat monochrome text for code.** Every code block must apply these token colors via `<span>` wrapping.

```css
:root {
  /* ── Code Block Chrome ── */
  --code-bg: rgba(8, 12, 22, 0.95);
  --code-text: #e2e8f0;
  --code-border: var(--border-glass);
  --code-radius: var(--radius-lg);
  --code-font-size: 13px;
  --code-line-height: 1.65;

  /* ── Syntax Token Colors (Dark Mode) ── */
  --syn-keyword:     #c084fc;   /* purple-400 — import, const, return, if, async   */
  --syn-string:      #34d399;   /* emerald-400 — 'hello', "world", `template`      */
  --syn-number:      #fbbf24;   /* amber-400 — 42, 3.14, 0xFF                      */
  --syn-function:    #60a5fa;   /* blue-400 — functionName(), useEffect             */
  --syn-type:        #38bdf8;   /* cyan — Interface, Type, React.FC, Promise        */
  --syn-comment:     #64748b;   /* slate-500 — // comments, /* block */             */
  --syn-operator:    #f472b6;   /* pink-400 — =, =>, ===, &&, ||, ??               */
  --syn-tag:         #f43f5e;   /* rose-500 — <div>, <Component />                  */
  --syn-attr:        #a78bfa;   /* violet-400 — className=, onClick=                */
  --syn-attr-value:  #34d399;   /* emerald-400 (same as strings)                    */
  --syn-punctuation: #94a3b8;   /* slate-400 — {}, (), [], ;, :                     */
  --syn-decorator:   #fb923c;   /* orange-400 — @Injectable, @Query                 */
  --syn-builtin:     #2dd4bf;   /* teal — console, document, window, Math           */
  --syn-regex:       #fbbf24;   /* amber-400 — /pattern/g                           */
  --syn-deleted:     #fca5a5;   /* red-300 — diff deleted lines                     */
  --syn-inserted:    #86efac;   /* green-300 — diff inserted lines                  */
}

[data-theme="light"] {
  --code-bg: #0f172a;           /* code bg stays dark in light mode                 */
  --code-text: #f1f5f9;
  --syn-keyword:   #d8b4fe;     /* purple-300                                       */
  --syn-string:    #6ee7b7;     /* emerald-300                                      */
  --syn-function:  #93c5fd;     /* blue-300                                         */
  --syn-type:      #67e8f9;     /* cyan-300                                         */
  --syn-comment:   #64748b;     /* slate-500 (same)                                 */
  --syn-tag:       #fda4af;     /* rose-300                                         */
}
```

**Reusable shorthand classes:**

```css
.kw  { color: var(--syn-keyword); }
.s   { color: var(--syn-string); }
.n   { color: var(--syn-number); }
.fn  { color: var(--syn-function); }
.tp  { color: var(--syn-type); }
.cm  { color: var(--syn-comment); font-style: italic; }
.op  { color: var(--syn-operator); }
.tg  { color: var(--syn-tag); }
.at  { color: var(--syn-attr); }
.av  { color: var(--syn-attr-value); }
.p   { color: var(--syn-punctuation); }
.dc  { color: var(--syn-decorator); }
.bi  { color: var(--syn-builtin); }
.del { color: var(--syn-deleted);  background: rgba(248, 113, 113, 0.1); }
.ins { color: var(--syn-inserted); background: rgba(74, 222, 128, 0.1); }
```

**Code block styling:**

```css
pre {
  background: var(--code-bg);
  border: 1px solid var(--code-border);
  border-radius: var(--code-radius);
  padding: var(--space-lg) var(--space-xl);
  margin: 14px 0;
  overflow-x: auto;
  font-family: var(--font-mono);
  font-size: var(--code-font-size);
  line-height: var(--code-line-height);
  color: var(--code-text);
  position: relative;
}

code:not(pre code) {
  background: rgba(56, 189, 248, 0.1);
  color: var(--cyan-glow);
  border: 1px solid rgba(56, 189, 248, 0.25);
  padding: var(--space-2xs) var(--space-sm);
  border-radius: var(--radius-sm);
  font-family: var(--font-mono);
  font-size: 0.85em;
}

.cheat-body {
  padding: var(--space-xl);
  background: var(--code-bg);
  overflow-x: auto;
}
.cheat-body pre {
  margin: 0; border: none; padding: 0;
  background: transparent;
  font-size: var(--code-font-size);
  line-height: var(--code-line-height);
  color: var(--code-text);
}
```

**Example syntax-highlighted code:**

```html
<pre><span class="cm">// React hook with TypeScript</span>
<span class="kw">import</span> <span class="p">{</span> <span class="fn">useState</span><span class="p">,</span> <span class="fn">useEffect</span> <span class="p">}</span> <span class="kw">from</span> <span class="s">'react'</span><span class="p">;</span>

<span class="kw">const</span> <span class="fn">useDebounce</span> <span class="op">=</span> <span class="p">(</span>value<span class="op">:</span> <span class="tp">string</span><span class="p">,</span> delay<span class="op">:</span> <span class="tp">number</span><span class="p">)</span> <span class="kw">=></span> <span class="p">{</span>
  <span class="kw">const</span> <span class="p">[</span>debounced<span class="p">,</span> setDebounced<span class="p">]</span> <span class="op">=</span> <span class="fn">useState</span><span class="p">(</span>value<span class="p">);</span>
  <span class="kw">return</span> debounced<span class="p">;</span>
<span class="p">};</span></pre>
```

---

### 2.6 Cheat Block Language Badge

```css
.cheat-lang-badge {
  font-family: var(--font-mono);
  font-size: 10px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.1em;
  padding: var(--space-2xs) var(--space-sm);
  border-radius: var(--radius-sm);
  background: rgba(168, 85, 247, 0.15);
  color: var(--purple-glow);
  border: 1px solid rgba(168, 85, 247, 0.3);
}

/* Per-language colors */
.cheat-lang-badge[data-lang="ts"],
.cheat-lang-badge[data-lang="typescript"] { background: rgba(56, 189, 248, 0.15);  color: var(--cyan-glow);    border-color: rgba(56, 189, 248, 0.3); }
.cheat-lang-badge[data-lang="tsx"],
.cheat-lang-badge[data-lang="jsx"]        { background: rgba(97, 218, 251, 0.15);  color: #61dafb;             border-color: rgba(97, 218, 251, 0.3); }
.cheat-lang-badge[data-lang="bash"],
.cheat-lang-badge[data-lang="shell"]      { background: rgba(16, 185, 129, 0.15);  color: var(--emerald-glow); border-color: rgba(16, 185, 129, 0.3); }
.cheat-lang-badge[data-lang="json"]       { background: rgba(251, 191, 36, 0.15);  color: var(--amber-glow);   border-color: rgba(251, 191, 36, 0.3); }
.cheat-lang-badge[data-lang="css"]        { background: rgba(244, 63, 94, 0.15);   color: var(--rose-glow);    border-color: rgba(244, 63, 94, 0.3); }
.cheat-lang-badge[data-lang="html"]       { background: rgba(251, 146, 60, 0.15);  color: #fb923c;             border-color: rgba(251, 146, 60, 0.3); }
.cheat-lang-badge[data-lang="sql"]        { background: rgba(129, 140, 248, 0.15); color: var(--indigo-glow);  border-color: rgba(129, 140, 248, 0.3); }
```

```html
<div class="cheat-header">
  <span class="cheat-label">useDebounce Hook</span>
  <div class="cheat-actions">
    <span class="cheat-lang-badge" data-lang="tsx">TSX</span>
    <button class="run-btn">▶ Run</button>
    <button class="copy-btn">Copy</button>
  </div>
</div>
```

---

### 2.7 Callout / Alert Blocks

Use for tips, warnings, gotchas, and pro-tips inside cards:

```css
.callout {
  border-radius: var(--radius-md);
  padding: var(--space-md) var(--space-lg);
  margin: var(--space-lg) 0;
  font-size: 13.5px;
  line-height: 1.6;
  border-left: 4px solid;
  display: flex;
  align-items: flex-start;
  gap: var(--space-md);
}
.callout-icon { font-size: 16px; flex-shrink: 0; margin-top: 2px; }

/* ── Variants ── */
.callout-tip {
  background: rgba(45, 212, 191, 0.08);
  border-color: var(--teal);
  color: var(--teal);
}
.callout-tip .callout-icon { color: var(--teal); }

.callout-warning {
  background: rgba(251, 191, 36, 0.08);
  border-color: var(--amber-glow);
  color: var(--amber-glow);
}
.callout-warning .callout-icon { color: var(--amber-glow); }

.callout-danger {
  background: rgba(244, 63, 94, 0.08);
  border-color: var(--rose-glow);
  color: var(--rose-glow);
}
.callout-danger .callout-icon { color: var(--rose-glow); }

.callout-info {
  background: rgba(56, 189, 248, 0.08);
  border-color: var(--cyan-glow);
  color: var(--cyan-glow);
}
.callout-info .callout-icon { color: var(--cyan-glow); }

.callout p { color: var(--text-dim); margin: 0; }
.callout strong { color: var(--text-main); }
```

```html
<div class="callout callout-tip">
  <span class="callout-icon"><i class="fa-solid fa-lightbulb"></i></span>
  <div><strong>Pro Tip:</strong><p>Always memoize expensive computations with useMemo.</p></div>
</div>

<div class="callout callout-warning">
  <span class="callout-icon"><i class="fa-solid fa-triangle-exclamation"></i></span>
  <div><strong>Gotcha:</strong><p>useEffect cleanup runs before re-execution, not on unmount.</p></div>
</div>

<div class="callout callout-danger">
  <span class="callout-icon"><i class="fa-solid fa-circle-xmark"></i></span>
  <div><strong>Anti-Pattern:</strong><p>Never mutate state directly — always use setState.</p></div>
</div>

<div class="callout callout-info">
  <span class="callout-icon"><i class="fa-solid fa-circle-info"></i></span>
  <div><strong>Note:</strong><p>This pattern works in React 18+ with concurrent features.</p></div>
</div>
```

---

### 2.8 Table Styling

For comparison tables, API references, and config breakdowns inside cards:

```css
.guide-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
  margin: var(--space-lg) 0;
}
.guide-table th {
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--cyan-glow);
  text-align: left;
  padding: var(--space-sm) var(--space-md);
  border-bottom: 2px solid rgba(56, 189, 248, 0.2);
  background: rgba(56, 189, 248, 0.05);
}
.guide-table td {
  padding: var(--space-sm) var(--space-md);
  border-bottom: 1px solid var(--border-glass);
  color: var(--text-dim);
}
.guide-table tr:hover td {
  background: rgba(56, 189, 248, 0.04);
}
.guide-table code {
  font-size: 12px;
}
```

---

## 3. Global Styles & Reset

```css
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; scroll-padding-top: 85px; -webkit-font-smoothing: antialiased; }
body {
  background: var(--bg-base); color: var(--text-main);
  font-family: var(--font-body); font-size: 14.5px;
  line-height: 1.7; min-height: 100dvh;
  overflow-x: hidden;
  transition: background var(--duration-theme), color var(--duration-theme);
}

/* ── Scrollbars ── */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: rgba(6, 9, 19, 0.8); }
::-webkit-scrollbar-thumb { background: rgba(56, 189, 248, 0.25); border-radius: 4px; border: 1px solid rgba(255, 255, 255, 0.05); }
::-webkit-scrollbar-thumb:hover { background: rgba(56, 189, 248, 0.5); }

/* ── Focus States (a11y) ── */
:focus-visible {
  outline: 2px solid var(--cyan-glow);
  outline-offset: 2px;
  border-radius: var(--radius-sm);
}

/* ── Selection ── */
::selection {
  background: rgba(56, 189, 248, 0.3);
  color: var(--text-main);
}
```

---

## 4. Structural Components

### 4.1 Ambient Glow Background

```css
.ambient-glow {
  position: fixed; width: 550px; height: 550px; border-radius: 50%;
  pointer-events: none; z-index: 0; filter: blur(130px); opacity: 0.18;
  animation: orbFloat 20s ease-in-out infinite alternate;
}
.orb-1 { top: -100px; left: 15%;  background: radial-gradient(circle, #38bdf8, #0284c7); }
.orb-2 { bottom: -120px; right: 10%; background: radial-gradient(circle, #2dd4bf, #06b6d4); animation-duration: 24s; animation-delay: -6s; }
.orb-3 { top: 45%; right: 35%;  background: radial-gradient(circle, #a855f7, #6366f1); animation-duration: 28s; animation-delay: -12s; }
```

```html
<div class="ambient-glow orb-1"></div>
<div class="ambient-glow orb-2"></div>
<div class="ambient-glow orb-3"></div>
```

### 4.2 Top Sticky Header (64px)

Fixed, blurred, with logo badge, title, edition badge, search, sidebar toggle, theme switch.

### 4.3 Scroll Progress Bar

```css
.progress-bar-line {
  position: fixed; top: 64px; left: 0; height: 3px;
  background: linear-gradient(90deg, #38bdf8, #2dd4bf, #a855f7, #f59e0b);
  z-index: 101; width: 0%;
  transition: width 0.1s;
  box-shadow: 0 0 10px rgba(56, 189, 248, 0.5);
}
```

### 4.4 Left Fixed Sidebar (290px)

- Fixed width, custom slim scrollbar
- `.nav-group-title` — mono, uppercase, tracked, muted
- `.nav-link` with `.dot` indicator — cyan glow when `.active`
- Active link gets `border-left: 3px solid var(--cyan-glow)`

### 4.5 Author Glass Bar

Glassmorphic banner with avatar + live-status-dot, author name, and social pills (LinkedIn, GitHub, Portfolio, Instagram).

### 4.6 Hero Banner

- `.eyebrow` — teal mono uppercase
- `h1 em` — cyan→teal gradient text
- `.lede` — description paragraph
- `.hero-stats` — responsive grid of stat counters
- `.hero-tags` — pill tags for technologies

### 4.7 3D Glass Cards & Cheat Blocks

```css
.card, .cheat-block {
  background: var(--bg-card-3d);
  backdrop-filter: blur(20px);
  border: 1px solid var(--border-glass);
  border-top: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: var(--radius-lg);
  padding: var(--space-2xl) 26px;
  margin-bottom: var(--space-2xl);
  box-shadow: var(--shadow-card);
  transition: all var(--duration-slow) var(--ease-smooth);
  position: relative;
}
.cheat-block { padding: 0; overflow: hidden; }

.card:hover, .cheat-block:hover {
  border-color: rgba(56, 189, 248, 0.35);
  box-shadow: 0 16px 36px -10px rgba(0, 0, 0, 0.65),
              0 0 20px rgba(56, 189, 248, 0.12);
  transform: translateY(-2px);
}
```

**Cheat block structure:**

```html
<div class="cheat-block">
  <div class="cheat-header">
    <span class="cheat-label">SNIPPET TITLE</span>
    <div class="cheat-actions">
      <span class="cheat-lang-badge" data-lang="ts">TS</span>
      <button class="run-btn" onclick="runCode(this)">▶ Run</button>
      <button class="copy-btn" onclick="copyCode(this)">Copy</button>
    </div>
  </div>
  <div class="cheat-body">
    <pre><!-- syntax highlighted code here --></pre>
  </div>
  <div class="cheat-runner-panel" id="runner-X">
    <div class="cheat-runner-header">
      <span>Console Output</span><span class="runner-time"></span>
    </div>
    <div class="cheat-runner-body"></div>
  </div>
</div>
```

### 4.8 Code Runner Console

```css
.cheat-runner-panel {
  display: none;
  background: rgba(6, 9, 19, 0.98);
  border-top: 1px solid var(--border-glow);
  padding: 14px 18px;
  font-family: var(--font-mono);
  font-size: 12px;
}
.cheat-runner-panel.open { display: block; }
.cheat-runner-header {
  display: flex; justify-content: space-between; align-items: center;
  color: var(--teal); font-size: 11px; font-weight: 700;
  margin-bottom: var(--space-sm);
  border-bottom: 1px solid var(--border-glass);
  padding-bottom: var(--space-xs);
}
.cheat-runner-body {
  color: #34d399;
  max-height: 220px; overflow-y: auto;
  white-space: pre-wrap;
}
```

### 4.9 Interactive Demo Widget

```css
.demo-widget {
  background: var(--bg-card-3d);
  border: 1px solid var(--border-glass);
  border-left: 4px solid var(--cyan-glow);
  border-radius: var(--radius-lg);
  margin: var(--space-3xl) 0;
  overflow: hidden;
  box-shadow: var(--shadow-3d);
}
```

Border-left color variants: `--cyan-glow` (default), `--teal`, `--purple-glow`, `--amber-glow`.

### 4.10 Toast & Back-to-Top

```css
#backToTop {
  position: fixed; bottom: var(--space-2xl); right: var(--space-2xl);
  width: 44px; height: 44px; border-radius: var(--radius-lg);
  background: var(--bg-surface); backdrop-filter: blur(15px);
  border: 1px solid var(--cyan-glow); color: var(--cyan-glow);
  display: flex; align-items: center; justify-content: center;
  font-size: 1.1rem; cursor: pointer; z-index: 99;
  opacity: 0; transform: translateY(20px);
  transition: all var(--duration-toast);
  pointer-events: none;
}
#backToTop.show { opacity: 1; transform: translateY(0); pointer-events: auto; }

#toast {
  position: fixed; bottom: var(--space-3xl); left: 50%;
  transform: translateX(-50%) translateY(100px);
  background: rgba(15, 23, 42, 0.95); backdrop-filter: blur(20px);
  border: 1px solid var(--cyan-glow); color: #fff;
  padding: var(--space-md) var(--space-xl);
  border-radius: var(--radius-full);
  font-size: 0.82rem; font-weight: 600;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
  z-index: 9999; opacity: 0;
  transition: all var(--duration-toast);
  pointer-events: none;
}
#toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }
```

---

## 5. Responsive Breakpoints

```css
/* ── Tablet & below (≤900px) ── */
@media (max-width: 900px) {
  .sidebar {
    position: fixed; top: 64px; left: 0; width: 290px;
    transform: translateX(-100%); z-index: 200;
  }
  body.mobile-sidebar-open .sidebar { transform: translateX(0); }
  .content { margin-left: 0 !important; width: 100% !important; padding: var(--space-2xl) var(--space-lg) 60px; }
  .hero h1 { font-size: clamp(1.6rem, 5vw, 2.4rem); }
  .hero-stats { grid-template-columns: repeat(2, 1fr); }
  .glass-author-bar { flex-direction: column; align-items: flex-start; }
  .search-container { width: 200px; }
}

/* ── Mobile (≤600px) ── */
@media (max-width: 600px) {
  .search-container { display: none; }
  .hero { padding: var(--space-2xl) var(--space-lg); }
  .hero-stats { grid-template-columns: 1fr 1fr; }
  .section-header { flex-direction: column; align-items: flex-start; gap: var(--space-sm); }
}
```

---

## 6. JavaScript Interactive Engine

### 6.1 Theme Switcher

```javascript
function initTheme() {
  const saved = localStorage.getItem('guideTheme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);
  document.body.className = saved;
  const el = document.getElementById('themeToggleText');
  if (el) el.innerText = saved === 'dark' ? '☀️ Light Mode' : '🌙 Dark Mode';
}

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme') || 'dark';
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  document.body.className = next;
  localStorage.setItem('guideTheme', next);
  const el = document.getElementById('themeToggleText');
  if (el) el.innerText = next === 'dark' ? '☀️ Light Mode' : '🌙 Dark Mode';
}
```

### 6.2 Toast Notification

```javascript
function showToast(msg) {
  const t = document.getElementById('toast');
  document.getElementById('toastText').innerText = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2000);
}
```

### 6.3 Code Copy

```javascript
function copyCode(btn) {
  const pre = btn.closest('.cheat-block').querySelector('pre');
  navigator.clipboard.writeText(pre.innerText)
    .then(() => showToast('Copied to clipboard!'));
}
```

### 6.4 Live Code Runner

```javascript
function runCode(btn) {
  const block = btn.closest('.cheat-block');
  const pre = block.querySelector('pre');
  const panel = block.querySelector('.cheat-runner-panel');
  const body = panel.querySelector('.cheat-runner-body');
  const timeEl = panel.querySelector('.runner-time');

  panel.classList.add('open');
  body.innerText = '';

  // Strip TypeScript annotations for browser execution
  let code = pre.innerText
    .replace(/:\s*(string|number|boolean|any|void|never|unknown|object|Record|Array|Promise|React\.\w+|[\w<>,\s|&\[\]]+)\s*(=|,|\)|\{|;|\n)/g, '$2')
    .replace(/\b(interface|type|enum)\s+\w+[^}]*\}/g, '')
    .replace(/<[A-Z][\w<>,\s]*>/g, '');

  const logs = [];
  const fakeConsole = { log: (...a) => logs.push(a.map(String).join(' ')),
                        error: (...a) => logs.push('❌ ' + a.map(String).join(' ')) };

  const t0 = performance.now();
  try {
    new Function('console', code)(fakeConsole);
  } catch (e) {
    logs.push('❌ ' + e.message);
  }
  const elapsed = (performance.now() - t0).toFixed(2);

  body.innerText = logs.join('\n') || '(no output)';
  if (timeEl) timeEl.innerText = elapsed + ' ms';
}
```

### 6.5 Scroll Progress & Back-to-Top

```javascript
window.addEventListener('scroll', () => {
  const docH = document.documentElement.scrollHeight - window.innerHeight;
  document.getElementById('scrollProgressBar').style.width = ((window.scrollY / docH) * 100) + '%';
  const b = document.getElementById('backToTop');
  if (window.scrollY > 400) b.classList.add('show'); else b.classList.remove('show');
});
```

### 6.6 Sidebar Toggle

```javascript
document.getElementById('sidebar-toggle')?.addEventListener('click',
  () => document.body.classList.toggle('mobile-sidebar-open'));
```

### 6.7 Keyboard Shortcuts

```javascript
document.addEventListener('keydown', (e) => {
  // "/" or Ctrl+K → focus search
  if ((e.key === '/' || (e.ctrlKey && e.key === 'k')) && document.activeElement.tagName !== 'INPUT') {
    e.preventDefault();
    document.getElementById('search-input')?.focus();
  }
  // Ctrl+B → toggle sidebar
  if (e.ctrlKey && e.key === 'b') {
    e.preventDefault();
    document.body.classList.toggle('mobile-sidebar-open');
  }
  // Escape → close search / sidebar
  if (e.key === 'Escape') {
    document.getElementById('search-input')?.blur();
    document.getElementById('search-results').style.display = 'none';
    document.body.classList.remove('mobile-sidebar-open');
  }
});
```

---

## 7. Quick-Reference Tables

### Heading Hierarchy

| Level | Class            | Element | Gradient / Color                         | Size   | Use Case                      |
|-------|------------------|---------|------------------------------------------|--------|-------------------------------|
| H1    | `.hero h1 em`    | `<h1>`  | `cyan → teal` gradient                   | clamp  | Hero title (one per page)     |
| H2    | `.section-title` | `<h2>`  | `cyan → teal` gradient                   | 26px   | Major section chapters        |
| H3    | `.level-head`    | `<h3>`  | `purple → indigo` gradient + left border | 20px   | Sub-topics within a section   |
| H4    | `.card-title`    | `<h4>`  | `--text-main` (solid)                    | 16px   | Card or cheat-block title     |
| H5    | `.inline-head`   | `<h5>`  | `--teal` (solid)                         | 14px   | In-card labels: "Why?"        |
| Label | `.cheat-label`   | `<span>`| `--cyan-glow` (solid)                    | 11.5px | Cheat block header label      |

### Syntax Token Colors

| Token        | Class  | Dark Color | Purpose                          |
|--------------|--------|------------|----------------------------------|
| Keyword      | `.kw`  | `#c084fc`  | `import`, `const`, `return`      |
| String       | `.s`   | `#34d399`  | `'text'`, `"text"`, templates    |
| Number       | `.n`   | `#fbbf24`  | `42`, `3.14`                     |
| Function     | `.fn`  | `#60a5fa`  | `useState()`, `map()`            |
| Type         | `.tp`  | `#38bdf8`  | `string`, `React.FC`             |
| Comment      | `.cm`  | `#64748b`  | `// comment`                     |
| Operator     | `.op`  | `#f472b6`  | `=>`, `===`, `&&`                |
| Tag          | `.tg`  | `#f43f5e`  | `<div>`, `<Component />`         |
| Attribute    | `.at`  | `#a78bfa`  | `className=`, `onClick=`         |
| Punctuation  | `.p`   | `#94a3b8`  | `{}`, `()`, `[]`, `;`            |
| Decorator    | `.dc`  | `#fb923c`  | `@Injectable`, `@Query`          |
| Built-in     | `.bi`  | `#2dd4bf`  | `console`, `document`            |
| Diff Delete  | `.del` | `#fca5a5`  | Removed lines                    |
| Diff Insert  | `.ins` | `#86efac`  | Added lines                      |

### Spacing Scale

| Token        | Size  | Common Usage                                    |
|--------------|-------|-------------------------------------------------|
| `--space-2xs`| 2px   | Badge vertical padding                          |
| `--space-xs` | 4px   | Badge padding, tight gaps                        |
| `--space-sm` | 8px   | Tag gaps, nav-link margin-bottom                 |
| `--space-md` | 12px  | Card-title mb, cheat-header py, eyebrow mb       |
| `--space-lg` | 16px  | Pre padding, hero-stats gap, section-header pb   |
| `--space-xl` | 20px  | Cheat-body padding, demo-body padding            |
| `--space-2xl`| 24px  | Card padding, sidebar top-padding                |
| `--space-3xl`| 28px  | Section-header mb, demo-widget my                |
| `--space-4xl`| 32px  | Lede mb, level-head mt                           |
| `--space-5xl`| 36px  | Hero padding-x, glass-author-bar mb              |
| `--space-6xl`| 44px  | Hero padding-y                                   |
| `--space-7xl`| 48px  | Hero mb, content padding-x                       |
| `--space-8xl`| 64px  | Section mb (biggest vertical rhythm)             |

### Callout Variants

| Variant    | Class             | Icon                           | Border Color     | Use Case                |
|------------|-------------------|--------------------------------|------------------|-------------------------|
| Tip        | `.callout-tip`    | `fa-lightbulb`                 | `--teal`         | Pro tips, best practices|
| Warning    | `.callout-warning`| `fa-triangle-exclamation`      | `--amber-glow`   | Gotchas, edge cases     |
| Danger     | `.callout-danger` | `fa-circle-xmark`              | `--rose-glow`    | Anti-patterns, errors   |
| Info       | `.callout-info`   | `fa-circle-info`               | `--cyan-glow`    | Notes, context          |

### Language Badge Colors

| Language   | `data-lang` | Badge Color      |
|------------|-------------|------------------|
| TypeScript | `ts`        | Cyan `#38bdf8`   |
| TSX / JSX  | `tsx`       | React `#61dafb`  |
| Bash       | `bash`      | Emerald `#10b981`|
| JSON       | `json`      | Amber `#f59e0b`  |
| CSS        | `css`       | Rose `#f43f5e`   |
| HTML       | `html`      | Orange `#fb923c` |
| SQL        | `sql`       | Indigo `#818cf8` |

---

## 8. Starter Template

A production-ready starter template lives at:
- `C:\Users\xTheDaDx\Downloads\html guides\template-architect-field-guide.html`
- `F:\0. bank\gemini upgrade\template-architect-field-guide.html`

When creating or upgrading a guide, copy the template and insert domain-specific sections while keeping layout and scripts intact.
