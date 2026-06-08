# shadcn + Tailwind patterns (Akasha UI)

## Layout

- Page shell: flex column, `min-h-screen`, semantic `<main>`
- Content width: `max-w-*` + responsive padding `px-4 md:px-6`
- Use CSS variables from theme for `--background`, `--foreground`, `--primary`

## Components

- Buttons: primary / secondary / ghost / destructive variants; `disabled:opacity-50`
- Forms: `<Label htmlFor>` + `<Input id>` pairing; describe errors with `aria-describedby`
- Dialogs: focus trap, `DialogTitle`, close on Escape
- Tables: sticky header on long lists; empty state row

## Tailwind conventions

- Spacing scale: 2, 4, 6, 8 for rhythm
- Prefer `gap-*` in flex/grid over manual margins
- Dark mode: `dark:` variants when project supports theme toggle

## File organization

- One component per file when >80 lines
- Colocate `*.test.tsx` if project uses Vitest

## Do not

- Inline styles except dynamic values
- Remove focus rings without replacement
- Import entire icon packs — tree-shake Lucide icons
