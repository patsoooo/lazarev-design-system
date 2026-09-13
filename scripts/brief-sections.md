# Lazarev Design System — system brief

Machine-readable summary for generating page designs. Written in English because every
token, class and component name in the system is English. Full documentation, with states,
anatomy and per-component rules, lives at https://github.com/patsoooo/lazarev-design-system

Values marked "no token" are confirmed from design but absent from the Figma export.
Never invent a value that is not listed here.

## 1. Canvas and grid

| Size | Canvas | Side padding | Container |
|---|---|---|---|
| Desktop | 1440px | 48px | **1344px** |
| Tab-md | 844px | 24px | **796px** |
| Mob-sm | 430px | 24px | **382px** |

- Container = canvas minus two side paddings. No token for any of these.
- There is no horizontal column grid. A page is a stack of blocks, each filling the container.
- Blocks lay out their own contents.
- Breakpoint thresholds are UNKNOWN. 1440 / 844 / 430 are canvas widths, not media query values.

## 2. Header

- Fixed. Stays on screen while the page scrolls.
- 24px from the top, 48px from the sides, width 1344px, height 40px.
- Total vertical space it occupies: **88px** = 24 + 40 + 24. Token: `blocks/hero/header-offset`.
- The first block must leave 88px for it.
- On Tab-md the link row collapses into a "Menu" button.

## 3. Vertical rhythm

| Rule | Value | Token |
|---|---|---|
| Every block's top padding | 220px | `primitives.spacing.220px` (not bound semantically) |
| First block, below header | 24px | `primitives.spacing.24px` |
| Section title to content | 56px | `primitives.spacing.56px` |

Spacing is carried by the block's own top padding, never by a gap between blocks.
Blocks have no bottom padding. Block order can change without recalculating distances.

Desktop only — rhythm on Tab-md and Mob-sm is not confirmed.

## 4. Page composition

Pages are assembled freely: there is no fixed recipe per page type.
Every section starts with the **Title block** component (`ds-title-block`): title,
description, optional button. It is the single most repeated element on any page.

Known page types, from breadcrumbs: Home, Industries > [industry], Case studies, Article.

There is no rule for when a block is dark — it is art direction per page.
There are no character limits on titles or descriptions.

## 5. Spacing scale (primitives.spacing)

{{SPACING}}

## 6. Colour tokens (semantic)

{{COLORS}}

## 7. Type scale

Site typography. Headings h1–h4 are Pragati Narrow, h5–h6 and body are Archivo.

| Token | Family | Size / line-height | Weight | Tracking | Case |
|---|---|---|---|---|---|
{{TYPE}}

Article typography is a separate scale. Article h1 and quotes are Instrument Serif —
the only place that face is used. Article body is 20/28, larger than site body 16/20.

| Token | Family | Size / line-height | Weight |
|---|---|---|---|
{{ARTICLE_TYPE}}

Article text is capped at a 640px measure inside its 992px column.
Exceptions that run full width: Article title block, Article table.

## 8. Component index

Quick index. Full markup and every style for each component is in section 9.
{{INVENTORY}}

## 9. Full component specifications

For each component: its exact markup and every CSS rule that applies to it.
All custom properties are resolved to real values, with the variable name kept
as a comment. This is the complete implementation — reproduce it exactly.

Do not invent structure. If a component is here, use its markup as given.
{{SPECS}}

## 10. Known gaps — do not invent these

- Breakpoint threshold values.
- Vertical rhythm on Tab-md and Mob-sm.
- Any container, column or grid width (none exist as tokens).
- Motion: no duration, easing or transition tokens exist.
- Elevation: one shadow only, `effect.shadow.modal`, a green glow.
- Themes: no dark/light theme tokens.
- Focus and z-index: no tokens.
- Input component: not documented, though 9 token groups exist for it.
- States are documented for 11 of 44 components.

## 11. Token file warning

`tokens.json` is a stale export. Padding values across nearly every group are smaller
than the confirmed design values, article spacing is wrong in 6 of 8 places, radius tokens
are bound to `primitives.spacing.*` instead of `primitives.radius.*`, and two conflicting
article type scales exist. **This brief and the documentation are more correct than the
token file.** Do not read tokens.json directly.
