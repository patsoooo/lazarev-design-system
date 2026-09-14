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
| Tablet | 844px | 24px | **796px** |
| Mobile | 430px | 24px | **382px** |

- Container = canvas minus two side paddings. No token for any of these.
- There is no horizontal column grid. A page is a stack of blocks, each filling the container.
- Blocks lay out their own contents.
- There are FOUR responsive modes in Figma: desktop, tab-large, tab, mob. Canvas widths
  are known for three of them; `tab-large` is not documented yet.
- Breakpoint thresholds are UNKNOWN. 1440 / 844 / 430 are canvas widths, not media query values.

## 2. Header

- Fixed. Stays on screen while the page scrolls.
- 24px from the top, 48px from the sides, width 1344px, height 40px.
- Total vertical space it occupies: **88px** = 24 + 40 + 24. Token: `blocks/hero/header-offset`.
- The first block must leave 88px for it.
- On Tablet the link row collapses into a "Menu" button.

## 3. Vertical rhythm

| Rule | Value | Token |
|---|---|---|
| Every block's top padding | 220px | `primitives.spacing.220px` (not bound semantically) |
| First block, below header | 24px | `primitives.spacing.24px` |
| Section title to content | 56px | `primitives.spacing.56px` |

Spacing is carried by the block's own top padding, never by a gap between blocks.
Blocks have no bottom padding. Block order can change without recalculating distances.

Desktop only — rhythm on Tablet and Mobile is not confirmed.

## 4. Page composition

Pages are assembled freely: there is no fixed recipe per page type.
Every section starts with the **Title block** component (`ds-title-block`): title,
description, optional button. It is the single most repeated element on any page.

Known page types, from breadcrumbs: Home, Industries > [industry], Case studies, Article.

Two elements are mandatory on every page:

- **Header** at the top, fixed, leaving 88px for the first block.
- **Footer** at the bottom. Never omit it, whatever the page is.

Breadcrumbs, when present, sit above the first block and are **always centred**
in the container — never flush left.

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

The article scale has FOUR responsive modes in Figma. Sizes:

| Role | desktop | tab-large | tab | mob |
|---|---|---|---|---|
| h1 | 64 | 64 | 56 | 46 |
| lead | 24 | 24 | 18 | 18 |
| body-1 | 20 | 20 | 16 | 16 |
| body-2 | 16 | 16 | 14 | 14 |
| quote | 36 | 36 | 32 | 28 |

The table below is the **desktop** mode. Line heights are known for desktop and mob only.

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
- Vertical rhythm on Tablet and Mobile.
- Any container, column or grid width (none exist as tokens).
- Motion: no duration, easing or transition tokens exist.
- Elevation: one shadow only, `effect.shadow.modal`, a green glow.
- Themes: no dark/light theme tokens.
- Focus and z-index: no tokens.
- Input component: not documented, though 9 token groups exist for it.
- States are documented for 11 of 44 components.

## 11. Token file warning

`tokens.json` is a single-mode export, and the mode is `mob`. Confirmed against
fresh per-mode exports: of the component tokens that vary by mode, 102 of 108 match
the `mob` column and only 3 match `desktop`. The semantic collection matches `mob`
on 35 of 36. Every "export defect" previously recorded in this brief was in fact a
desktop-vs-mobile comparison.

It is also stale: `global-blocks/padding-x` reads 12px there, which matches no mode
(desktop 48, every other mode 24). Section 12 carries the current four-mode values.

Its `primitives` branch is fine, though — that collection is single-mode and has not
changed: 112 tokens then, 112 now.

Two cosmetic defects in Primitives: the group is spelled `font/letter-spasing`
(missing the c), and `font/String` is an empty placeholder variable that should be
deleted. Neither affects rendering.

Radius tokens are also bound to `primitives.spacing.*` instead of `primitives.radius.*`.

**This brief and the documentation carry the desktop values and are more correct than
the token file.** Do not read tokens.json directly.

## 12. Responsive modes

The Semantic and Component collections have FOUR modes: desktop, tab-large, tab, mob.
**Primitives has a single mode** ("default") — a raw 24px is 24px on every screen, so
only the semantic and component layers reskin. Primitives holds 112 tokens:
42 colours, 21 spacing steps, 8 radii, 39 type values, 2 border widths.
Canvas widths: desktop 1440, tab 844, mob 430 (side padding 48 / 24 / 24).
The tab-large canvas width is not documented; its values mostly track desktop.

Everything else in this brief is the **desktop** mode. Below is every token whose
value changes with screen size — 131 of them. Colours never change: the palette is
identical in all four modes.

### Page rhythm

| Token | desktop | tab-large | tab | mob |
|---|---|---|---|---|
| `spacing.global-blocks.padding-x` | 48 | 24 | 24 | 24 |
| `spacing.global-blocks.padding-y` | 220 | 220 | 180 | 128 |
| `spacing.global-blocks.gap` | 56 | 48 | 48 | 40 |
| `spacing.global-blocks.cards-gap` | 16 | 16 | 12 | 8 |

### Site type scale

| Role | desktop | tab-large | tab | mob |
|---|---|---|---|---|
| h1 | 80 / 72 | 56 / 48 | 46 / 40 | 36 / 32 |
| h2 | 56 / 48 | 46 / 40 | 36 / 32 | 32 / 28 |
| h3 | 46 / 40 | 36 / 32 | 32 / 32 | 28 / 28 |
| h4 | 36 / 32 | 32 / 32 | 28 / 28 | 28 / 28 |
| h5 | 24 / 24 | 24 / 24 | 18 / 24 | 16 / 24 |
| h6 | 20 / 24 | 20 / 24 | 16 / 20 | 16 / 20 |
| p1 | 20 / 20 | 18 / 20 | 16 / 20 | 16 / 20 |
| p2 | 18 / 20 | 16 / 20 | 16 / 20 | 14 / 16 |
| p3 | 16 / 20 | 14 / 16 | 14 / 16 | 13 / 16 |
| p4 | 14 / 16 | 14 / 16 | 14 / 16 | 14 / 16 |
| c1 | 16 / 16 | 16 / 16 | 14 / 16 | 14 / 16 |
| c2 | 12 / 12 | 12 / 16 | 12 / 16 | 12 / 16 |
| n1 | 200 / 140 | 200 / 140 | 80 / 72 | 80 / 72 |

### Article type scale

| Role | desktop | tab-large | tab | mob |
|---|---|---|---|---|
| h1 | 64 / 64 | 64 / 64 | 56 / 56 | 46 / 48 |
| lead | 24 / 32 | 24 / 32 | 18 / 28 | 18 / 28 |
| body-1 | 20 / 28 | 20 / 28 | 16 / 24 | 16 / 24 |
| body-2 | 16 / 20 | 16 / 20 | 14 / 20 | 14 / 16 |
| quote | 36 / 36 | 36 / 36 | 32 / 32 | 28 / 32 |

### Component tokens

| Token | desktop | tab-large | tab | mob |
|---|---|---|---|---|
| `avatart.stroke-inverse` | #E9E9E9 | #FFFFFF | #FFFFFF | #FFFFFF |
| `blocks.article.content-gap` | 16 | 16 | 16 | 12 |
| `blocks.article.h2-bottom` | 12 | 12 | 8 | 8 |
| `blocks.article.h2-top` | 64 | 48 | 40 | 32 |
| `blocks.article.h3-top` | 48 | 32 | 24 | 16 |
| `blocks.article.h4-top` | 24 | 16 | 16 | 16 |
| `blocks.article.media-gap-bottom` | 24 | 24 | 24 | 20 |
| `blocks.article.media-gap-top` | 12 | 12 | 12 | 8 |
| `blocks.article.quote-gap-avatar` | 32 | 24 | 16 | 16 |
| `blocks.article.quote-top-bottom` | 32 | 24 | 16 | 16 |
| `blocks.article.section-gap` | 56 | 48 | 40 | 24 |
| `blocks.articles-listing.padding-y` | 128 | 128 | 88 | 64 |
| `blocks.articles-listing.section-gap` | 80 | 64 | 48 | 32 |
| `blocks.articles-listing.title-gap` | 48 | 40 | 32 | 24 |
| `blocks.block-CTA.gap` | 40 | 32 | 24 | 20 |
| `blocks.block-CTA.padding` | 64 | 48 | 40 | 24 |
| `blocks.block-card.option-1.padding` | 24 | 24 | 20 | 16 |
| `blocks.block-case-industry.bullet-point-gap` | 16 | 16 | 12 | 12 |
| `blocks.block-case-industry.content-gap` | 88 | 64 | 40 | 40 |
| `blocks.block-case-industry.media-gap` | 16 | 16 | 16 | 12 |
| `blocks.block-case-industry.padding` | 24 | 16 | 16 | 12 |
| `blocks.block-case-industry.statistik-gap` | 64 | 32 | 32 | 24 |
| `blocks.block-case-industry.text-button-gap` | 32 | 24 | 24 | 20 |
| `blocks.block-case-industry.title-text-gap` | 24 | 16 | 16 | 12 |
| `blocks.block-case-outcomes.container-widht` | 400 | 400 | 400 | 250 |
| `blocks.block-case-outcomes.gap` | 32 | 32 | 24 | 16 |
| `blocks.block-case-outcomes.padding` | 24 | 24 | 20 | 16 |
| `blocks.block-case-outcomes.title-text-gap` | 32 | 32 | 20 | 20 |
| `blocks.block-icon.padding` | 24 | 16 | 16 | 12 |
| `blocks.block-icon.text-gap` | 24 | 24 | 20 | 20 |
| `blocks.block-icon.title-text-gap` | 32 | 32 | 20 | 20 |
| `blocks.block-phrase.gap` | 40 | 32 | 24 | 20 |
| `blocks.block-phrase.inner-padding-x` | 24 | 24 | 20 | 16 |
| `blocks.block-phrase.inner-padding-y` | 64 | 48 | 40 | 24 |
| `blocks.block-phrase.text-block-button-gap` | 32 | 32 | 24 | 24 |
| `blocks.block-text.option-1.gap` | 32 | 32 | 24 | 16 |
| `blocks.block-text.option-1.padding` | 24 | 24 | 20 | 16 |
| `blocks.block-text.option-2.padding` | 24 | 24 | 20 | 16 |
| `blocks.block-text.option-3.padding` | 24 | 24 | 20 | 16 |
| `blocks.case.gap` | 64 | 40 | 40 | 24 |
| `blocks.case.padding` | 24 | 16 | 16 | 12 |
| `blocks.case.statistik-gap` | 64 | 32 | 32 | 24 |
| `blocks.case.text-button-gap` | 32 | 24 | 24 | 20 |
| `blocks.case.title-text-gap` | 24 | 16 | 16 | 12 |
| `blocks.hero.header-offset` | 116 | 116 | 96 | 88 |
| `blocks.hero.label-title-gap` | 24 | 20 | 16 | 12 |
| `blocks.hero.title-action-gap` | 64 | 48 | 40 | 32 |
| `blocks.industry-text-block.bullet-points-gap` | 16 | 16 | 12 | 12 |
| `blocks.industry-text-block.padding` | 24 | 24 | 20 | 16 |
| `blocks.industry-text-block.text-button-gap` | 40 | 40 | 32 | 24 |
| `blocks.outcomes.card-gap` | 24 | 20 | 16 | 12 |
| `blocks.outcomes.padding-y` | 64 | 64 | 56 | 48 |
| `blocks.process.img-text-gap` | 0 | 48 | 0 | 0 |
| `blocks.process.padding` | 24 | 16 | 16 | 12 |
| `blocks.service.gap` | 64 | 32 | 32 | 24 |
| `blocks.service.gap-innfo-blocks` | 40 | 24 | 20 | 20 |
| `blocks.service.padding` | 24 | 16 | 16 | 16 |
| `blocks.service.title-text-gap` | 24 | 20 | 20 | 16 |
| `blocks.title-group.text-button-gap` | 24 | 20 | 16 | 12 |
| `blocks.title-group.title-action-gap` | 640 | 640 | 640 | 382 |
| `blocks.title-group.title-text-gap` | 24 | 20 | 16 | 12 |
| `blocks.title-group.title-width` | 672 | 672 | 672 | 382 |
| `button.button-block.gap` | 80 | 80 | 64 | 32 |
| `button.button-block.padding-left` | 20 | 20 | 16 | 12 |
| `button.button-block.padding-right-top-bottom` | 8 | 8 | 8 | 12 |
| `button.button-block.radius` | 80 | 80 | 80 | 8 |
| `button.button-icon-secondary.padding` | 12 | 12 | 12 | 8 |
| `button.industry.padding-x` | 16 | 16 | 12 | 12 |
| `button.industry.padding-y` | 12 | 12 | 8 | 8 |
| `card.L.gap` | 32 | 32 | 24 | 20 |
| `card.L.padding` | 24 | 16 | 16 | 12 |
| `card.L.text-button-gap` | 32 | 24 | 20 | 20 |
| `card.L.title-text-gap` | 24 | 20 | 20 | 16 |
| `card.bullet-point-card.padding` | 24 | 24 | 16 | 12 |
| `card.card-article-full.avatar-img-gap` | 16 | 16 | 16 | 12 |
| `card.card-article-full.gap` | 32 | 32 | 24 | 20 |
| `card.card-article-full.padding` | 24 | 16 | 16 | 12 |
| `card.card-article-full.tag-text-gap` | 20 | 20 | 16 | 12 |
| `card.card-article-full.title-max-height` | 96 | 96 | 72 | 64 |
| `card.card-article.gap` | 24 | 16 | 16 | 12 |
| `card.card-article.padding` | 16 | 16 | 16 | 12 |
| `card.card-award.gap` | 40 | 40 | 32 | 24 |
| `card.card-award.padding` | 16 | 16 | 16 | 12 |
| `card.card-comparison.gap` | 56 | 48 | 48 | 40 |
| `card.card-comparison.padding` | 24 | 16 | 16 | 12 |
| `card.card-icon.gap` | 80 | 80 | 72 | 56 |
| `card.card-icon.padding` | 24 | 16 | 16 | 12 |
| `card.card-icon.text-gap` | 24 | 24 | 20 | 20 |
| `card.card-number.padding` | 24 | 24 | 16 | 12 |
| `card.card-outcomes-l.padding` | 24 | 24 | 16 | 12 |
| `card.card-outcomes-s.padding` | 16 | 16 | 16 | 12 |
| `card.case-card.gap` | 32 | 32 | 24 | 20 |
| `card.case-card.padding` | 24 | 16 | 16 | 12 |
| `card.case-card.text-button-gap` | 20 | 20 | 16 | 12 |
| `card.case-card.title-text-gap` | 16 | 16 | 16 | 12 |
| `card.case-mini-card.gap` | 12 | 12 | 12 | 8 |
| `card.case-mini-card.padding` | 16 | 16 | 16 | 12 |
| `card.logo-card.gap` | 20 | 20 | 20 | 16 |
| `card.logo-card.padding` | 16 | 16 | 16 | 12 |
| `card.m.gap` | 32 | 32 | 24 | 20 |
| `card.m.padding` | 24 | 16 | 16 | 12 |
| `card.m.text-button-gap` | 20 | 20 | 16 | 12 |
| `card.m.title-text-gap` | 16 | 16 | 16 | 12 |
| `card.s.gap` | 32 | 32 | 24 | 20 |
| `card.s.padding` | 16 | 16 | 16 | 12 |
| `card.s.tag-text-button-gap` | 24 | 24 | 20 | 16 |
| `card.s.text-button-gap` | 16 | 16 | 16 | 12 |
| `card.s.text-gap` | 12 | 12 | 12 | 8 |
| `card.testimonials.padding` | 24 | 24 | 20 | 16 |
| `card.text.padding` | 16 | 16 | 16 | 12 |
| `dropdown.dropdown.gap` | 4 | 4 | 4 | 2 |
| `dropdown.dropdown.padding-y` | 12 | 12 | 8 | 8 |
| `dropdown.gap` | 40 | 40 | 32 | 24 |
| `dropdown.menu.gap` | 12 | 8 | 8 | 8 |
| `dropdown.menu.hover-item` | #E9E9E9 | #FFFFFF | #FFFFFF | #FFFFFF |
| `dropdown.menu.padding-x` | 8 | 12 | 12 | 8 |
| `dropdown.menu.padding-y` | 8 | 12 | 8 | 8 |
| `dropdown.menu.radius` | 8 | 32 | 32 | 32 |
| `dropdown.menu.radius-item` | 4 | 32 | 32 | 32 |
| `dropdown.padding` | 24 | 24 | 20 | 16 |
| `footer.padding` | 24 | 24 | 20 | 16 |
| `heading-menu.header-menu.gap` | 20 | 20 | 16 | 16 |
| `heading-menu.mobile-menu-item.gap` | 16 | 16 | 12 | 12 |
| `heading-menu.submenu.article-gap` | 16 | 16 | 12 | 8 |
| `heading-menu.submenu.menu-item-gap` | 24 | 24 | 20 | 16 |
| `heading-menu.submenu.padding` | 24 | 24 | 16 | 12 |
| `input.padding-left` | 20 | 20 | 16 | 16 |
| `pagination.wrapper.gap-elements` | 24 | 24 | 24 | 20 |
| `spasing.global-blocks.padding-x` | 48 | 24 | 24 | 24 |
| `tab.tab.padding-x` | 12 | 12 | 12 | 8 |
| `tab.tab.padding-y` | 12 | 12 | 8 | 8 |
