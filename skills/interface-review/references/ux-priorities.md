# UX priority checklist

## P0 — Blockers (fix before merge)

- Keyboard: all interactive elements reachable and operable via keyboard
- Focus visible on every focusable control
- Form inputs have associated labels (`<label>` or `aria-label`)
- Color contrast ≥ WCAG AA for text (flag if only checked visually)
- No information conveyed by color alone without icon/text backup
- Images/icons with meaning have `alt` or `aria-hidden` + text alternative

## P1 — Core UX

- Loading and error states for async actions
- Disabled buttons explain why (tooltip/copy) when non-obvious
- Destructive actions require confirmation
- Consistent navigation/back behavior
- Touch targets ~44px minimum on mobile layouts

## P2 — Layout

- Responsive breakpoints without horizontal scroll on common widths
- Text truncation/overflow handled for long titles
- Z-index stacking: modals above nav

## P3 — Polish

- Consistent spacing scale (Tailwind tokens)
- Heading hierarchy (h1 once per view)
- Empty states with guidance, not blank panels
