# UI Design Guide: Riddhesh C Portfolio (v3)

Welcome to the **Official UI Design & Replication Guide** for the Riddhesh C Portfolio (v3) project. This guide breaks down the premium design systems, custom interactions, high-fidelity styles, and visual assets so you can recreate this exact aesthetic in any other project.

---

## 1. Core Visual Aesthetics & Tokens

The portfolio leverages a minimalist yet dynamic **Light-Mode Premium** aesthetic. It relies on crisp typography, subtle depth via overlay text, raw sketch elements, and rich micro-interactions.

### A. Color Palette
The colors are harmonized between crisp greys and vibrant neon highlights:
* **Background Primary**: `#FFFFFF` (Spotlight glow transitions to `#FAFAFA`)
* **Text Primary**: `#111111` / `#1A1A1A`
* **Text Secondary (Subtles)**: `#555555` / `#666666` / `#888888`
* **Accent Blue**: `#2C64E8` / `#0055FF` (`--accent-blue`) — Used for focus highlights and link underlines.
* **Accent Orange**: `#E85D34` / `#FF5A1F` (`--accent-orange`) — Used for errors and warning highlights.
* **Card Backing**: `#F7F7F7` / `#F3F4F6` (Cool gray border backing)
* **Status Card Accents**:
  * *Purple Accent*: `#9B59B6`
  * *Green Accent*: `#00B894`
  * *Cyan Accent*: `#9B00CE`
  * *Pink Accent*: `#FD79A8`
  * *Dark Red Accent*: `#A50C22`

---

### B. Typography Stack
A contrasting pairing of premium geometric grotesque sans-serif and classical editorial serifs gives the interface an active, designer-crafted feel.

| Font Family | Style / Weight | CSS Variable | Primary Purpose |
| :--- | :--- | :--- | :--- |
| **Inter** | Grotesque Sans (400, 500, 600, 700) | `--font-inter` | Body text, captions, UI tags, buttons, technical labels. |
| **Playfair Display** | Classical Editorial Serif (Italic, 600) | `--font-playfair` | Editorial headings, italicized highlights (`Selected Work`, `computer engineer`), overlap phrases. |
| **Mr De Haviland** | Expressive Script / Handwriting | `--font-mr-de-haviland` | Freehand signature logo overlay. |
| **Nanum Pen Script** | Ink Pen Handwriting | `--font-nanum-pen` | Doodles, informal annotations, arrows, and personal notes. |

---

### C. The Grid Dot Spotlight Background
Rather than a stark solid background, the site layers a **highly subtle dot grid** under a **soft radial spotlight gradient** focusing attention on the center.

```css
body {
  background-color: #ffffff;
  /* Creates a very faint dot pattern */
  background-image: radial-gradient(#e5e5e5 1.5px, transparent 1.5px);
  background-size: 40px 40px;
  /* Adds a subtle spotlight effect to focus on the center */
  background: radial-gradient(circle at center, #ffffff 20%, #fafafa 100%),
              radial-gradient(#e0e0e0 1px, transparent 1px);
  background-size: 100% 100%, 40px 40px;
}
```

---

## 2. Key Components & Interactions

Below are the blueprints, markup guidelines, and CSS parameters for the signature interactive components of the portfolio.

### A. The Dynamic Reveal Project Cards
This is the showcase element of the portfolio. The cards are tall, structured blocks where the media/video layer sits on top, and on hover, slides down dynamically to reveal a project description and blur-backdrop button.

```
+------------------------------------+
|  Modern minimal e-commerce...     |  <- Header (Always Visible)
|  [Wordpress] [SEO] [E-Commerce]    |
+------------------------------------+
| +--------------------------------+ |
| |                                | |  <- Visual Area
| |        Media Video Mockup      | |  
| |        (Slides down on hover)  | |  
| +--------------------------------+ |
| |  Project details and button   | |  <- Revealed content behind
| +--------------------------------+ |
+------------------------------------+
```

#### HTML / React Structure
```tsx
<a href="URL" className="project-card-link">
  <div className="project-card">
    {/* Always Visible Header */}
    <div className="card-header">
      <h4 className="project-title">
        Modern <span className="highlight purple">minimal</span> e-commerce.
      </h4>
      <div className="tags">
        <span className="tag">Wordpress</span>
        <span className="tag">SEO</span>
      </div>
    </div>

    {/* Interactive Container */}
    <div className="card-visual-container purple-bg">
      {/* Behind layer - Text & Actions */}
      <div className="reveal-text-layer">
        <p className="reveal-description">
          A sleek e-commerce platform with advanced SEO.
        </p>
        <div className="view-btn">Click to view ↗</div>
      </div>

      {/* Front sliding layer - Media Mockup */}
      <div className="sliding-image-layer">
        <video src="/clasicraft-mockup.mp4" autoPlay loop muted playsInline />
      </div>
    </div>
  </div>
</a>
```

#### CSS Stylesheet
```css
.project-card {
  background-color: #fff;
  border-radius: 24px;
  border: 1px solid #f0f0f0;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  height: 580px;
  transition: all 0.3s ease;
}

.card-header {
  padding: 40px 30px 20px 30px;
  flex-shrink: 0;
}

.project-title {
  font-size: 2rem;
  font-weight: 800;
  line-height: 1.1;
  color: #1a1a1a;
  margin-bottom: 20px;
}

.project-title span.highlight.purple {
  font-family: 'Playfair Display', serif;
  font-style: italic;
  color: #9b59b6;
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.tag {
  font-size: 0.85rem;
  font-weight: 600;
  color: #555;
  background-color: #f3f4f6;
  padding: 8px 16px;
  border-radius: 20px;
  border: 1px solid #eee;
}

/* Visual Container representing colored card frame */
.card-visual-container {
  flex-grow: 1;
  position: relative;
  margin: 0 20px 20px 20px;
  border-radius: 20px;
  overflow: hidden;
  background-color: #9b59b6; /* fallback */
  cursor: pointer;
}

/* Background options */
.purple-bg { background-color: #9b59b6; }
.green-bg { background-color: #00b894; }
.blue-bg { background-color: #1c64f2; }

/* Hidden text overlay behind */
.reveal-text-layer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 50%;
  padding: 40px 30px;
  color: white;
  opacity: 0;
  transform: translateY(-20px);
  transition: all 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
  z-index: 1;
  display: flex;
  flex-direction: column;
}

.reveal-description {
  font-size: 1.1rem;
  line-height: 1.5;
  font-weight: 500;
  margin-bottom: 20px;
}

.view-btn {
  background-color: rgba(0, 0, 0, 0.3);
  color: white;
  padding: 8px 16px;
  border-radius: 30px;
  font-size: 0.85rem;
  font-weight: 600;
  width: fit-content;
  backdrop-filter: blur(5px);
}

/* Media Layer sitting on top */
.sliding-image-layer {
  position: absolute;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  width: 90%;
  height: 100%;
  background-color: #fff;
  border-radius: 16px 16px 0 0;
  box-shadow: 0 -10px 40px rgba(0, 0, 0, 0.2);
  transition: transform 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
  z-index: 2;
}

.sliding-image-layer video,
.sliding-image-layer img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Hover Mechanics */
.project-card:hover .sliding-image-layer {
  transform: translateX(-50%) translateY(200px); /* Moves down to reveal text */
}

.project-card:hover .reveal-text-layer {
  opacity: 1;
  transform: translateY(0);
}
```

---

### B. Scattered Polaroid Gallery Component
An exceptionally premium component clumping photos together like organic real-life Polaroids. On hover, the hovered photo lifts smoothly above the other stacked photos.

```
       +--------+
       | Memory | (8deg rot)
  +----+--------+----+
  | Memory |    | M  | (-6deg rot)
  | (-12d) |    |    |
  +--------+----+----+
```

#### HTML / React Structure
```tsx
<div className="gallery-container">
  {/* Annotating note */}
  <div className="handwritten-note">
    Some photos <br /> from my life :)
  </div>

  <div className="cards-wrapper">
    <div className="photo-card">
      <img src="/win.jpg" alt="Memory 1" />
    </div>
    <div className="photo-card">
      <img src="/iot.jpg" alt="Memory 2" />
    </div>
    <div className="photo-card">
      <img src="/mine-mount.png" alt="Memory 3" />
    </div>
  </div>
</div>
```

#### CSS Stylesheet
```css
.gallery-container {
  position: relative;
  width: 100%;
  text-align: center;
  padding: 60px 0;
}

.handwritten-note {
  font-family: 'Nanum Pen Script', cursive;
  font-size: 1.8rem;
  color: #6B7280;
  position: absolute;
  top: 0px;
  left: 5%;
  transform: rotate(-6deg);
  pointer-events: none;
}

.cards-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px 0;
}

.photo-card {
  width: 220px;
  height: 280px;
  background-color: #FFFFFF;
  padding: 12px 12px 45px 12px; /* Polaroid wider bottom margin */
  box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.15);
  border-radius: 4px;
  cursor: pointer;
  border: 1px solid rgba(0, 0, 0, 0.02);
  margin: 0 -35px; /* Overlap margins pulls them together */
  
  /* Setup dynamic variables used in hover calculations */
  --rotate: 0deg;
  --y: 0px;
  
  transform: rotate(var(--rotate)) translateY(var(--y));
  transition: transform 0.4s cubic-bezier(0.25, 0.8, 0.25, 1), box-shadow 0.4s ease;
}

.photo-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 2px;
  filter: sepia(15%) contrast(105%) brightness(105%);
  transition: filter 0.3s ease;
}

/* Stack styling definitions */
.photo-card:nth-child(1) { --rotate: -6deg; --y: 15px; z-index: 2; }
.photo-card:nth-child(2) { --rotate: 8deg; --y: -10px; z-index: 1; }
.photo-card:nth-child(3) { --rotate: -12deg; --y: 20px; z-index: 3; }

/* Interactive Hover Lift */
.photo-card:hover {
  transform: rotate(var(--rotate)) translateY(calc(var(--y) - 40px));
  box-shadow: 0 20px 40px -5px rgba(0, 0, 0, 0.2);
}

.photo-card:hover img {
  filter: none;
}
```

---

### C. Technical Skills Grid Component
A grid layout displaying clean cards that rotate and expand slightly on mouse-over.

#### HTML Structure
```html
<div className="skills-grid">
  <div className="skill-card">
    <div className="skill-icon-box">
      <img src="/javascript.svg" alt="JavaScript" />
    </div>
    <div className="skill-info">
      <h4 className="skill-name">JavaScript</h4>
      <p className="skill-desc">React, Node, Express, TS</p>
    </div>
  </div>
</div>
```

#### CSS Stylesheet
```css
.skills-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.skill-card {
  background-color: #fff;
  border: 1px solid #f0f0f0;
  border-radius: 20px;
  padding: 32px;
  display: flex;
  align-items: center;
  gap: 24px;
  transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1), border-color 0.3s;
  min-height: 120px;
}

.skill-card:hover {
  border-color: #e0e0e0;
}

.skill-icon-box {
  width: 70px;
  height: 70px;
  background-color: #fef08a; /* Yellow-themed for JS */
  color: #854d0e;
  border-radius: 16px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
  padding: 12px;
  transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.skill-card:hover .skill-icon-box {
  transform: rotate(6deg); /* Playful tilt */
}

.skill-card:hover .skill-name,
.skill-card:hover .skill-desc {
  transform: translateX(8px); /* Shifts texts rightward */
}

.skill-name {
  font-size: 1.15rem;
  font-weight: 700;
  transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.skill-desc {
  font-size: 0.95rem;
  color: #666;
  transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}
```

---

### D. The Interactive Custom Cursor
For desktop layouts, a gorgeous customized cursor replaces the default mouse pointer. It detects elements dynamically (`data-sticker="true"`, links, inputs) and transitions the pointer to appropriate interactive cursors.

#### React Implementation Code
```tsx
'use client';

import { useEffect, useState, useRef } from 'react';

export default function CustomCursor() {
    const cursorRef = useRef<HTMLDivElement>(null);
    const [isHovering, setIsHovering] = useState(false);
    const [isHoveringWork, setIsHoveringWork] = useState(false);
    const [isHoveringEmail, setIsHoveringEmail] = useState(false);
    const [isHoveringSticker, setIsHoveringSticker] = useState(false);
    const [isDraggingSticker, setIsDraggingSticker] = useState(false);
    const [isHoveringTyping, setIsHoveringTyping] = useState(false);

    useEffect(() => {
        const updatePosition = (e: MouseEvent) => {
            if (cursorRef.current) {
                cursorRef.current.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
            }
        };

        const handleMouseOver = (e: MouseEvent) => {
            const target = e.target as HTMLElement;
            const isProjectCard = target.closest('.project-card') || target.closest('.card-visual-container');
            const isEmailContainer = target.closest('.email-container');
            const isSticker = target.closest('[data-sticker="true"]');
            const isTypingSection = target.closest('[data-typing-section="true"]');

            if (isSticker) {
                setIsHoveringSticker(true);
                setIsHovering(false);
                setIsHoveringWork(false);
                setIsHoveringEmail(false);
                setIsHoveringTyping(false);
            } else if (isTypingSection) {
                setIsHoveringTyping(true);
                setIsHovering(false);
                setIsHoveringWork(false);
                setIsHoveringEmail(false);
                setIsHoveringSticker(false);
            } else if (
                target.tagName === 'A' ||
                target.tagName === 'BUTTON' ||
                target.closest('a') ||
                target.closest('button') ||
                isProjectCard ||
                isEmailContainer
            ) {
                setIsHovering(true);
                setIsHoveringWork(!!isProjectCard);
                setIsHoveringEmail(!!isEmailContainer);
                setIsHoveringSticker(false);
                setIsHoveringTyping(false);
            } else {
                setIsHovering(false);
                setIsHoveringWork(false);
                setIsHoveringEmail(false);
                setIsHoveringSticker(false);
                setIsHoveringTyping(false);
            }
        };

        const handleMouseDown = (e: MouseEvent) => {
            const target = e.target as HTMLElement;
            if (target.closest('[data-sticker="true"]')) {
                setIsDraggingSticker(true);
            }
        };

        const handleMouseUp = () => setIsDraggingSticker(false);

        window.addEventListener('mousemove', updatePosition);
        window.addEventListener('mouseover', handleMouseOver);
        window.addEventListener('mousedown', handleMouseDown);
        window.addEventListener('mouseup', handleMouseUp);

        return () => {
            window.removeEventListener('mousemove', updatePosition);
            window.removeEventListener('mouseover', handleMouseOver);
            window.removeEventListener('mousedown', handleMouseDown);
            window.removeEventListener('mouseup', handleMouseUp);
        };
    }, []);

    return (
        <div ref={cursorRef} className="custom-cursor">
            <img
                src={
                    isDraggingSticker ? '/grabbed.svg'
                    : isHoveringSticker ? '/grab.svg'
                    : isHoveringTyping ? '/text.svg'
                    : isHovering ? '/hover-cursor.svg'
                    : '/cursor.svg'
                }
                alt="cursor"
                width={48}
                height={48}
                style={{ pointerEvents: 'none' }}
            />
            {isHoveringWork && <div className="cursor-label">View Work</div>}
            {isHoveringEmail && <div className="cursor-label">Copy !!</div>}
        </div>
    );
}
```

#### CSS Rules for Cursors
```css
/* Disable default cursor on desktop */
@media (min-width: 769px) {
  body, a, button, input, select, .project-card {
    cursor: none !important;
  }
}

.custom-cursor {
  position: fixed;
  top: 0;
  left: 0;
  width: 48px;
  height: 48px;
  pointer-events: none;
  z-index: 9999;
  will-change: transform;
}

.cursor-label {
  position: absolute;
  top: 52px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #1a1a1a;
  color: white;
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 600;
  white-space: nowrap;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  animation: fadeInLabel 0.2s ease-out;
}

@keyframes fadeInLabel {
  from { opacity: 0; transform: translateX(-50%) translateY(-5px); }
  to { opacity: 1; transform: translateX(-50%) translateY(0); }
}
```

---

## 3. Dynamic Preloading & Staged Reveals

The portfolio implements a highly coordinated loading layout. A **Splash Screen** plays initially, holding back elements until fully loaded, followed by staggered animation reveals (`BlurFade`).

### A. Preloader Splash Screen
Plays a 2.4-second bar animation combined with sliding transitions.

```tsx
import React, { useEffect, useState } from "react";

export default function SplashScreen({ onFinish }: { onFinish: () => void }) {
    useEffect(() => {
        const timer = setTimeout(() => onFinish(), 2400);
        return () => clearTimeout(timer);
    }, [onFinish]);

    return (
        <div id="splash-screen">
            <div className="splash-eyebrow">Hello, I am</div>
            <div className="splash-header">
                Riddhesh<span>.</span>
                <div className="splash-sticker">✱</div>
            </div>
            <div className="splash-loader">
                <div className="loader-fill"></div>
            </div>
        </div>
    );
}
```

#### Splash Styles
```css
#splash-screen {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background-color: #FAFAFA;
  z-index: 9999;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.splash-eyebrow {
  font-family: 'Inter', sans-serif;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.25em;
  color: #6B7280;
  margin-bottom: 5px;
  opacity: 0;
  transform: translateY(15px);
  animation: textFadeIn 0.8s ease forwards 0.2s;
}

.splash-header {
  font-family: 'Playfair Display', serif;
  font-size: 4rem;
  font-weight: 600;
  color: #111;
  position: relative;
  opacity: 0;
  transform: translateY(20px);
  animation: textFadeIn 0.8s cubic-bezier(0.25, 1, 0.5, 1) forwards 0.4s;
}

.splash-header span { color: #2C64E8; }

.splash-sticker {
  position: absolute;
  top: -20px;
  right: -35px;
  font-size: 2rem;
  color: #2C64E8;
  opacity: 0;
  animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.27) forwards 0.9s,
             spinSlow 10s linear infinite 0.9s;
}

.splash-loader {
  width: 180px;
  height: 2px;
  background: #E5E7EB;
  margin-top: 35px;
  border-radius: 2px;
  overflow: hidden;
  opacity: 0;
  animation: simpleFade 0.5s ease forwards 0.6s;
}

.loader-fill {
  height: 100%;
  width: 0%;
  background-color: #111;
  animation: fillBar 2s cubic-bezier(0.22, 1, 0.36, 1) forwards 0.7s;
}

@keyframes textFadeIn { to { opacity: 1; transform: translateY(0); } }
@keyframes popIn { 0% { opacity: 0; transform: scale(0); } 100% { opacity: 1; transform: scale(1); } }
@keyframes simpleFade { to { opacity: 1; } }
@keyframes fillBar { 0% { width: 0%; } 100% { width: 100%; } }
@keyframes spinSlow { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
```

---

### B. Client Stagger Transition (BlurFade)
Instead of importing heavy packages, use lightweight `IntersectionObserver` coupled with CSS transitions.

```tsx
import { useEffect, useRef, useState } from "react";

export default function BlurFade({ children, delay = 0, blur = "10px" }) {
  const [isVisible, setIsVisible] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) {
        setTimeout(() => setIsVisible(true), delay * 1000);
      }
    }, { threshold: 0.1 });
    
    if (ref.current) observer.observe(ref.current);
    return () => { if (ref.current) observer.unobserve(ref.current); };
  }, [delay]);

  return (
    <div
      ref={ref}
      className={`blur-fade ${isVisible ? "blur-fade-visible" : "blur-fade-hidden"}`}
      style={{ "--blur-amount": blur } as React.CSSProperties}
    >
      {children}
    </div>
  );
}
```

```css
.blur-fade {
  transition: opacity 0.6s cubic-bezier(0.4, 0, 0.2, 1),
              filter 0.6s cubic-bezier(0.4, 0, 0.2, 1),
              transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  will-change: opacity, filter, transform;
}

.blur-fade-hidden {
  opacity: 0;
  filter: blur(var(--blur-amount, 10px));
  transform: translateY(20px);
}

.blur-fade-visible {
  opacity: 1;
  filter: blur(0px);
  transform: translateY(0);
}
```

---

## 4. Key Takeaways for Replication

When building your new project with this aesthetic, ensure you preserve these four core design secrets:
1. **Contrasting Serif Overlaps**: Keep some italic Playfair Display titles layered overlapping standard grotesque sans-serif words.
2. **Interactive Motion Stickers**: Place 4-6 colorful sticker PNG/SVG files scattered at absolute angles (`rotate(-10deg)` to `rotate(15deg)`) around your Hero components and make them draggable using Framer Motion (`drag` properties).
3. **Smooth State Cursor Transforms**: Always use custom SVG cursors that dynamically display context cues (e.g. `'View Work'` label above project grids, `'Copy'` label above emails).
4. **Physical Tactility (Hover Rotations)**: Add slight physical rotates, translate offsets, and polaroid styles to make digital cards feel tactile, satisfying, and premium.
