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

0, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 116, 128, 180, 220

## 6. Colour tokens (semantic)

| `color/action/bg-hover` | #e9e9e9ff |
| `color/action/border-hover` | #bbc2ccff |
| `color/action/brand-hover` | #0da34eff |
| `color/action/brand-pressed` | #0a783aff |
| `color/action/danger` | #dc2626ff |
| `color/action/danger-hover` | #ef4444ff |
| `color/action/danger-pressed` | #b91c1cff |
| `color/action/inactive` | #697382ff |
| `color/action/inactive-content` | #cdd4deff |
| `color/action/primary` | #000000ff |
| `color/action/primary-hover` | #0f9549ff |
| `color/action/primary-invers` | #ffffffff |
| `color/action/primary-pressed` | #222222ff |
| `color/action/warning` | #eab308ff |
| `color/action/warning-hover` | #facc15ff |
| `color/action/warning-pressed` | #ca8a04ff |
| `color/background/block` | #ffffffff |
| `color/background/elements` | #2a2a2aff |
| `color/background/gray-block` | #f4f4f4ff |
| `color/background/inverse` | #000000ff |
| `color/background/page` | #e9e9e9ff |
| `color/background/white-opacity-10%` | #ffffff1a |
| `color/border/danger` | #dc2626ff |
| `color/border/default` | #e9e9e9ff |
| `color/border/subtle` | #d9d9d9ff |
| `color/border/warning` | #eab308ff |
| `color/border/white` | #ffffffff |
| `color/border/white-30%` | #ffffff4d |
| `color/gradient/brand/end` | #c2cddeff |
| `color/gradient/brand/mid` | #0f9549ff |
| `color/gradient/brand/start` | #1e1e1eff |
| `color/icon/border` | #ffffff4d |
| `color/icon/brand` | #0f9549ff |
| `color/icon/danger` | #dc2626ff |
| `color/icon/default` | #000000ff |
| `color/icon/inverse` | #ffffffff |
| `color/icon/secondary` | #697382ff |
| `color/icon/warning` | #eab308ff |
| `color/illustration/bg-white-opacity-10%` | #ffffff1a |
| `color/illustration/bg-white-opacity-30%` | #ffffff4d |
| `color/illustration/border-white` | #ffffffff |
| `color/illustration/elements` | #ffffffff |
| `color/overlay/default` | #00000099 |
| `color/text/danger` | #dc2626ff |
| `color/text/inverse` | #ffffffff |
| `color/text/on-dark` | #e9e9e9ff |
| `color/text/placeholder` | #697382ff |
| `color/text/primary` | #000000ff |
| `color/text/secondary` | #697382ff |
| `color/text/tertiary` | #bbc2ccff |
| `color/text/text-attention` | #0f9549ff |
| `color/text/warning` | #ca8a04ff |

## 7. Type scale

Site typography. Headings h1–h4 are Pragati Narrow, h5–h6 and body are Archivo.

| Token | Family | Size / line-height | Weight | Tracking | Case |
|---|---|---|---|---|---|
| `font.caption.c1-16` | Pragati Narrow | 16 / 16 | 400 | -0.5 | uppercase |
| `font.caption.c2-12` | Archivo | 12 / 12 | 400 | 0 | none |
| `font.caption.c2-med-12` | Archivo | 12 / 12 | 500 | 0 | none |
| `font.heading.h1-80` | Pragati Narrow | 80 / 72 | 400 | -1.5 | none |
| `font.heading.h2-56` | Pragati Narrow | 56 / 48 | 400 | -0.5 | none |
| `font.heading.h3-46` | Pragati Narrow | 46 / 40 | 400 | -0.5 | none |
| `font.heading.h4-36` | Pragati Narrow | 36 / 32 | 400 | -0.5 | none |
| `font.heading.h5-24` | Archivo | 24 / 24 | 500 | -0.5 | none |
| `font.heading.h6-20` | Archivo | 20 / 24 | 500 | -0.5 | none |
| `font.number.n1-200` | Pragati Narrow | 200 / 140 | 400 | -1.5 | none |
| `font.paragraph.p1-20` | Archivo | 20 / 20 | 400 | 0 | none |
| `font.paragraph.p2-18` | Archivo | 18 / 20 | 400 | 0 | none |
| `font.paragraph.p3-16` | Archivo | 16 / 20 | 400 | 0 | none |
| `font.paragraph.p4-14` | Archivo | 14 / 16 | 500 | 0 | none |

Article typography is a separate scale. Article h1 and quotes are Instrument Serif —
the only place that face is used. Article body is 20/28, larger than site body 16/20.

| Token | Family | Size / line-height | Weight |
|---|---|---|---|
| `article.body.b1-bold-20` | Archivo | 20 / 28 | 700 |
| `article.body.b1-regular-20` | Archivo | 20 / 28 | 400 |
| `article.body.b2-bold-16` | Archivo | 16 / 20 | 700 |
| `article.body.b2-regular-16` | Archivo | 16 / 20 | 400 |
| `article.heading.h1-64` | Instrument Serif | 64 / 64 | 400 |
| `article.lead.lead-24` | Archivo | 24 / 32 | 500 |
| `article.link.link p3` | Archivo | 20 / 28 | 400 |
| `article.quote.quote-40` | Instrument Serif | 36 / 36 | 400 |

Article text is capped at a 640px measure inside its 992px column.
Exceptions that run full width: Article title block, Article table.

## 8. Component index

Quick index. Full markup and every style for each component is in section 9.

### Components

| Component | CSS class | Size | Purpose |
|---|---|---|---|
| Icons | `.ds-icon` | 16px · h 16px | CSS-mask icons; colour comes from currentColor. Sizes 16px in buttons, 24px elsewhere |
| Point marker | `.ds-point` | 32px · h 32px | 32px ring with a 6px dot; --green variant uses the brand colour |
| Accordion | `.ds-accordion` | min 1344px | FAQ list, one row open at a time |
| Avatar | `.ds-avatar` | fluid | Photo with name and job title; sizes S 40 / M 56 |
| Breadcrumbs | `.ds-bc` | fluid | Page path, current item last |
| Button | `.ds-btn` | h 40px | 9 variants: primary, secondary, industry, link, play, icon-primary, icon-secondary, plus, block |
| Checkbox | `.ds-cb` | 24px · h 24px | Square check, also used as dropdown list item |
| Chips | `.ds-chip` | h 40px | Outlined filter pill with trailing arrow |
| Dropdown | `.ds-dd` | h 40px | Trigger plus menu of checkbox items |
| Input | — | — | NOT DOCUMENTED — 9 token groups exist, page is empty |
| Links | `.ds-link` | h 16px | Navigation link, plain variant has no arrow |
| Links group | `.ds-header-menu` | fluid | Bordered row of header links |
| Media | `.ds-media` | fluid | Image placeholder, sizes S/M/L, ratio 1.504 |
| Pagination | `.ds-pagi` | 40px · h 40px | Page numbers in a pill with arrow buttons |
| Tab | `.ds-tab` | h 40px | Segmented control, one active |
| Tag | `.ds-tag` | fluid | Uppercase label with hairline separator |
| Toggle | `.ds-toggle` | 28px · h 16px | Binary switch, applies immediately |

### Cards

| Component | CSS class | Size | Purpose |
|---|---|---|---|
| Article | `.ds-article-card` | 312px | Article teaser; S 312 / M 388 / L 616 |
| Article menu | `.ds-card-am` | fluid | Article teaser inside the header menu |
| Award | `.ds-award-card` | 324px | Award name, year, project |
| Bullet point | `.ds-bullet-card` | 400px | Green dot marker plus one paragraph |
| Case | `.ds-case-card` | 312px | Case teaser; S 312 / L 616 |
| Number | `.ds-number-card` | 332px | Numbered step with badge |
| Outcomes | `.ds-outcomes-card` | 272px · h 272px | Metric card, dark, translucent; needs a dark parent |
| Outcomes L | `.ds-outcomes-card--l` | 332px · h 400px | Large metric card, light, with client logo |
| Testimonials | `.ds-testimonial` | 664px · h 604px | Quote with author and rating |
| Text | `.ds-text-card` | 332px · h 416px | Title over gradient plus body |

### Blocks

| Component | CSS class | Size | Purpose |
|---|---|---|---|
| Title block | `.ds-title-block` | fluid | Section header: title, description, optional button. Starts nearly every section |
| Case | `.ds-case-block` | min 1344px | Case study block; desktop / tablet / mobile |
| Case outcomes | `.ds-case-outcomes-block` | min 1344px | Case metrics row |
| CTA | `.ds-cta-block` | min 1344px | Closing call to action with two buttons |
| Icon | `.ds-icon-block` | min 1344px | Icon, text and optional button; desktop and responsive |
| Outcomes | `.ds-outcomes-block` | min 1344px | Dark block holding Outcomes cards |
| Process | `.ds-process-block` | min 1344px | One process step: image, title, text, button |
| Service | `.ds-service-block` | min 1344px | Service offering; wide and narrow layouts |
| Text | `.ds-text-block` | min 1344px | Grid of Text cards |
| Menu | `.ds-menu` | 1342px | Full header menu panel |

### Layout

| Component | CSS class | Size | Purpose |
|---|---|---|---|
| Header | `.ds-header` | min 1344px | Fixed top bar: logo, links, button |
| Footer | `.ds-footer` | 1342px | Three stacked blocks: contacts, services, legal |

### Pages

| Component | CSS class | Size | Purpose |
|---|---|---|---|
| Grid | `.ds-page` | 1440px | Page layout schematic: canvas, container, block rhythm |

### Article

| Component | CSS class | Size | Purpose |
|---|---|---|---|
| Layout | `.ds-article-grid` | min 1344px | Two columns: 992 body, 336 aside, gap 16 |
| Typography | `.ds-art-` | — | h2/h3/h4, lead, body, bullet, number list — each carries its own padding |
| Title block | `.ds-article-title` | min 992px | Article header: tag, date, h1, author, reading time |
| Attention block | `.ds-attention-block` | fluid | Callout with a green hairline on the left |
| Quote | `.ds-art-quote-block` | fluid | Serif quote with author |
| Table | `.ds-art-table` | min 992px | Header row plus data rows, 2px apart |
| Navigation | `.ds-toc` | 336px | Table of contents with reading progress |

## 9. Full component specifications

For each component: its exact markup and every CSS rule that applies to it.
All custom properties are resolved to real values, with the variable name kept
as a comment. This is the complete implementation — reproduce it exactly.

Do not invent structure. If a component is here, use its markup as given.

### Design tokens as CSS variables

Every value below is resolved inline in the rules that follow. This block is the map from Figma token to value.

```css
:root {
  /* --- Кольори: semantic.color.action.* --- */
  --color-action-primary: #000000ff;           /* → primitives.color.black.1000 */
  --color-action-primary-hover: #0f9549ff;     /* → primitives.color.green.500 */
  --color-action-brand-pressed: #0a783aff;     /* → primitives.color.green.600 */
  --color-action-inactive: #697382ff;          /* → primitives.color.gray.600 */
  --color-action-inactive-content: #cdd4deff;  /* → primitives.color.gray.300 */
  --color-action-primary-invers: #ffffffff;    /* → primitives.color.white.1000 */

  --color-action-bg-hover: #e9e9e9ff;           /* → primitives.color.gray.100 */

  /* --- Кольори: semantic.color.text.* / icon.* --- */
  --color-icon-secondary: #697382ff;           /* → primitives.color.gray.600 */
  --color-text-primary: #000000ff;             /* → primitives.color.black.1000 */
  --color-text-inverse: #ffffffff;             /* → primitives.color.white.1000 */
  --color-text-secondary: #697382ff;           /* → primitives.color.gray.600 */
  --color-icon-default: #000000ff;             /* → primitives.color.black.1000 */
  --color-icon-inverse: #ffffffff;             /* → primitives.color.white.1000 */
  --color-icon-brand: #0f9549ff;               /* → primitives.color.green.500 */

  --color-action-brand-hover: #0da34eff;        /* → primitives.color.green.400 */

  /* --- Кольори: semantic.color.border.* / background.* --- */
  --color-background-elements: #2a2a2aff;      /* → primitives.color.black.800 */
  --color-border-default: #e9e9e9ff;           /* → primitives.color.gray.100 */
  --color-border-subtle: #d9d9d9ff;            /* → primitives.color.gray.200 */
  --color-border-white: #ffffffff;             /* → primitives.color.white.1000 */
  --color-text-tertiary: #bbc2ccff;            /* → primitives.color.gray.400 */
  --color-text-attention: #0f9549ff;           /* → primitives.color.green.500 */
  --color-background-white-10: #ffffff1a;      /* → primitives.color.white.1000-10% */
  --color-border-white-30: #ffffff4d;          /* → primitives.color.white.1000-30% */
  --color-background-block: #ffffffff;         /* → primitives.color.white.1000 */
  --color-background-page: #e9e9e9ff;          /* → primitives.color.gray.100 */
  --color-background-inverse: #000000ff;       /* → primitives.color.black.1000 */
  --color-text-placeholder: #697382ff;         /* → primitives.color.gray.600 */
  /* Стаття прив'язана до примітивів напряму, повз семантику */
  --color-gray-50: #f4f4f4ff;                  /* → primitives.color.gray.50 */
  --color-gray-100: #e9e9e9ff;                 /* → primitives.color.gray.100 */
  --color-gray-300: #cdd4deff;                 /* → primitives.color.gray.300 */

  /* --- Розміри: primitives.spacing.* --- */
  --spacing-2: 2px;
  --spacing-4: 4px;
  --spacing-8: 8px;
  --spacing-12: 12px;
  --spacing-16: 16px;
  --spacing-20: 20px;
  --spacing-25: 25px; /* поза шкалою primitives.spacing */
  --spacing-24: 24px;
  --spacing-28: 28px;
  --spacing-32: 32px;
  --spacing-40: 40px;
  --spacing-56: 56px;
  --spacing-64: 64px;
  --spacing-72: 72px;
  --spacing-128: 128px;
  --spacing-48: 48px;

  /* --- Радіуси: primitives.radius.* --- */
  --radius-4: 4px;
  --radius-8: 8px;
  --radius-12: 12px;
  --radius-32: 32px;
  --radius-80: 80px;

  /* --- Межі: primitives.border-width.* --- */
  --border-width-1: 1px;

  /* --- Висота: component.button.primary.height → primitives.spacing.40px --- */
  --button-height: 40px;

  /* --- Родини шрифтів: primitives.font.family.* --- */
  /* Жоден із трьох не має кириличного набору — український текст піде у фолбек */
  --font-pragati: "Pragati Narrow", "Arial Narrow", Arial, sans-serif;
  --font-archivo: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-instrument: "Instrument Serif", Georgia, "Times New Roman", serif;

  /* --- Ролі шрифтів: semantic.font.font-family.* --- */
  --font-heading: var(--font-pragati);            /* h1–h4 */
  --font-heading-small: var(--font-archivo);      /* h5–h6 */
  --font-body: var(--font-archivo);               /* p1–p4 */
  --font-caption-c1: var(--font-pragati);
  --font-caption-c2: var(--font-archivo);
  --font-article-heading: var(--font-instrument); /* article h1, quote */
  --font-article-body: var(--font-archivo);       /* article body, lead */

  /* --- Типографіка лейбла кнопки --- */
  /* Типово Paragraph p4 — font.paragraph.p4-14: Archivo 14/16, вага 500.
     Industry — виняток: Paragraph p3 (font.paragraph.p3-16), Archivo 16/20, вага 400.
     У Figma це поки не токени: у component.button.* немає жодної змінної шрифту. */
  --button-font-family: var(--font-archivo);
  --button-font-size: 14px;
  --button-line-height: 16px;
  --button-font-weight: 500;

  --button-font-size-lg: 16px;
  --button-line-height-lg: 20px;
  --button-font-weight-lg: 400;

  /* --- Розмір іконок --- */
  /* Підтверджено з дизайном; окремого токена в експорті немає */
  --icon-size: 16px;

  /* --- Градієнти --- */
  --gradient-horizontal-2: linear-gradient(180deg, #1e1e1eff 0%, #0f9549ff 45%, #c2cddeff 100%);
  --gradient-horizontal-dark: linear-gradient(180deg, #3e4f7fff 0%, #0c0f19ff 30%, #0c0f19ff 65%, #0f9549ff 94%);
  --gradient-vertical-3: linear-gradient(314.967deg, #1e1e1eff 0%, #0da34eff 54%, #0a783aff 60%, #1e1e1eff 65%, #c2cddeff 68%, #0da34eff 74%, #c2cddeff 84%, #1e1e1eff 100%);

  /* --- Іконки (SVG з Figma), описані на сторінці Foundations → Icons --- */
  --icon-caret: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E%3Cpath d='M8.00373 10L5 6H11L8.00373 10Z' fill='black'/%3E%3C/svg%3E");
  --icon-burger: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E%3Cpath d='M2 3H14' stroke='black' stroke-linecap='round'/%3E%3Cpath d='M2 8H14' stroke='black' stroke-linecap='round'/%3E%3Cpath d='M2 13H14' stroke='black' stroke-linecap='round'/%3E%3C/svg%3E");
  --icon-arrow-side: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M10 8.00373L6 5L6 11L10 8.00373Z' fill='black'/%3E %3C/svg%3E");
  --icon-placeholder: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M2 14L14 2' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3Cpath d='M14 14L2 2' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3Crect x='1.5' y='1.5' width='13' height='13' stroke='black'/%3E %3C/svg%3E");
  --icon-arrow-up-right: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M4 12L12 4' stroke='white' stroke-linecap='round' stroke-linejoin='round'/%3E %3Cpath d='M4 4H12V12' stroke='white' stroke-linecap='round' stroke-linejoin='round'/%3E %3C/svg%3E");
  --icon-close: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M4 11.6569L12 3.65686' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3Cpath d='M4 3.65685L12 11.6569' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3C/svg%3E");
  --icon-check: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M4 8L6.78261 11L12 5' stroke='black' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'/%3E %3C/svg%3E");

  /* --- Висоти кнопок (підтверджено з дизайном) --- */
  --button-height-industry: 44px;
  --button-height-play: 28px;
}
```


### Components — Icons

CSS-mask icons; colour comes from currentColor. Sizes 16px in buttons, 24px elsewhere

Styles:

```css
.ds-icon-card {
  display: inline-flex;
  align-items: center;
  gap: 12px; /* --spacing-12 */
  padding: 12px 16px; /* --spacing-12, --spacing-16 */
  border: 1px solid #d9d9d9ff; /* --border-width-1, --color-border-subtle */
  border-radius: 8px; /* --radius-8 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  font-size: 12px;
  line-height: 16px;
}
.ds-icon {
  display: inline-block;
  flex: none;
  width: 16px; /* --icon-size */
  height: 16px; /* --icon-size */
  background-color: currentColor;
  -webkit-mask-repeat: no-repeat;
  mask-repeat: no-repeat;
  -webkit-mask-position: center;
  mask-position: center;
  -webkit-mask-size: contain;
  mask-size: contain;
}
.ds-icon--caret {
  -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E%3Cpath d='M8.00373 10L5 6H11L8.00373 10Z' fill='black'/%3E%3C/svg%3E"); /* --icon-caret */
  mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E%3Cpath d='M8.00373 10L5 6H11L8.00373 10Z' fill='black'/%3E%3C/svg%3E"); /* --icon-caret */
}
.ds-icon--burger {
  -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E%3Cpath d='M2 3H14' stroke='black' stroke-linecap='round'/%3E%3Cpath d='M2 8H14' stroke='black' stroke-linecap='round'/%3E%3Cpath d='M2 13H14' stroke='black' stroke-linecap='round'/%3E%3C/svg%3E"); /* --icon-burger */
  mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E%3Cpath d='M2 3H14' stroke='black' stroke-linecap='round'/%3E%3Cpath d='M2 8H14' stroke='black' stroke-linecap='round'/%3E%3Cpath d='M2 13H14' stroke='black' stroke-linecap='round'/%3E%3C/svg%3E"); /* --icon-burger */
}
.ds-icon--arrow-side {
  -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M10 8.00373L6 5L6 11L10 8.00373Z' fill='black'/%3E %3C/svg%3E"); /* --icon-arrow-side */
  mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M10 8.00373L6 5L6 11L10 8.00373Z' fill='black'/%3E %3C/svg%3E"); /* --icon-arrow-side */
}
.ds-icon--placeholder {
  -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M2 14L14 2' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3Cpath d='M14 14L2 2' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3Crect x='1.5' y='1.5' width='13' height='13' stroke='black'/%3E %3C/svg%3E"); /* --icon-placeholder */
  mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M2 14L14 2' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3Cpath d='M14 14L2 2' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3Crect x='1.5' y='1.5' width='13' height='13' stroke='black'/%3E %3C/svg%3E"); /* --icon-placeholder */
}
.ds-icon--arrow-up-right {
  -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M4 12L12 4' stroke='white' stroke-linecap='round' stroke-linejoin='round'/%3E %3Cpath d='M4 4H12V12' stroke='white' stroke-linecap='round' stroke-linejoin='round'/%3E %3C/svg%3E"); /* --icon-arrow-up-right */
  mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M4 12L12 4' stroke='white' stroke-linecap='round' stroke-linejoin='round'/%3E %3Cpath d='M4 4H12V12' stroke='white' stroke-linecap='round' stroke-linejoin='round'/%3E %3C/svg%3E"); /* --icon-arrow-up-right */
}
.ds-icon--close {
  -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M4 11.6569L12 3.65686' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3Cpath d='M4 3.65685L12 11.6569' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3C/svg%3E"); /* --icon-close */
  mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M4 11.6569L12 3.65686' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3Cpath d='M4 3.65685L12 11.6569' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3C/svg%3E"); /* --icon-close */
}
.ds-icon--check {
  -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M4 8L6.78261 11L12 5' stroke='black' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'/%3E %3C/svg%3E"); /* --icon-check */
  mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M4 8L6.78261 11L12 5' stroke='black' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'/%3E %3C/svg%3E"); /* --icon-check */
}
.ds-icon--rotate-180 {
  transform: rotate(180deg);
}
.ds-icon--rotate-270 {
  transform: rotate(-90deg);
}
.ds-btn-block__text .ds-icon {
  width: 16px; /* --icon-size */
  height: 16px; /* --icon-size */
}
```


### Components — Point marker

32px ring with a 6px dot; --green variant uses the brand colour

Markup:

```html
<span class="ds-bullet-card">
  <span class="ds-point" />
  <span class="ds-bullet-card__text">text</span>
</span>
```

Styles:

```css
.ds-point {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex: none;
  width: 32px;
  height: 32px;
}
.ds-point::before {
  content: "";
  position: absolute;
  width: 28px;
  height: 28px;
  border: 1px dashed #697382ff; /* --border-width-1, --color-icon-secondary */
  border-radius: 50%;
}
.ds-point--green::after {
  background: #0f9549ff; /* --color-icon-brand */
}
.ds-point::after {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #000000ff; /* --color-icon-default */
}
```


### Components — Accordion

FAQ list, one row open at a time

Markup:

```html
<span class="ds-accordion"><span class="ds-accordion__head"><span class="ds-accordion__title">Title</span><span class="ds-btn ds-btn--plus is-default">+</span></span><span class="ds-accordion__body">text</span></span>
```

Styles:

```css
.ds-accordion {
  display: block;
  box-sizing: border-box;
  width: 100%;
  min-width: 1344px;
  padding: 24px; /* --spacing-24 */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-accordion__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px; /* --spacing-24 */
}
.ds-accordion__title {
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.heading.h5-24 — Archivo 24/24, вага 500 */
  font-size: 24px;
  line-height: 24px;
  font-weight: 500;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
}
.ds-accordion__body {
  display: block;
  margin-top: 24px; /* --spacing-24 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p3-16 — Archivo 16/20 */
  font-size: 16px;
  line-height: 20px;
  font-weight: 400;
  color: #000000ff; /* --color-text-primary */
}
```


### Components — Avatar

Photo with name and job title; sizes S 40 / M 56

Markup:

```html
<span class="ds-avatar-info"><span class="ds-avatar-info__photos"><span class="ds-avatar ds-avatar--m" /><span class="ds-avatar ds-avatar--m" /></span><span class="ds-avatar-info__text"><span class="ds-avatar-info__name">Name</span><span class="ds-avatar-info__job">Job title</span></span></span>
```

Styles:

```css
.ds-avatar {
  display: block;
  flex: none;
  box-sizing: border-box;
  border-radius: 32px; /* --radius-32 */
  border: 1px solid #e9e9e9ff; /* --border-width-1, --color-border-default */
  background: repeating-conic-gradient(#f4f4f4 0% 25%, #fbfbfb 0% 50%) 0 0 / 12px 12px;
}
.ds-avatar--m {
  width: 56px;
  height: 56px;
}
.ds-avatar--s {
  width: 40px;
  height: 40px;
}
.ds-avatar--inverse {
  border-color: #ffffffff; /* --color-border-white */
}
.ds-avatar-info {
  display: inline-flex;
  align-items: center;
  gap: 16px; /* --spacing-16 */
}
.ds-avatar-info--s {
  gap: 12px; /* --spacing-12 */
}
.ds-avatar-info__photos {
  display: flex;
  gap: 4px; /* --spacing-4 */
}
.ds-avatar-info__text {
  display: flex;
  flex-direction: column;
  gap: 8px; /* --spacing-8 */
  min-width: 0;
}
.ds-avatar-info--s .ds-avatar-info__text {
  gap: 4px; /* --spacing-4 */
}
.ds-avatar-info__name {
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p3-16 — Archivo 16/20 */
  font-size: 16px;
  line-height: 20px;
  font-weight: 400;
  color: #000000ff; /* --color-text-primary */
}
.ds-avatar-info__job {
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.caption.c1-16 — Pragati Narrow 16/16, uppercase. TODO: звірити з Figma */
  font-size: 16px;
  line-height: 16px;
  font-weight: 400;
  letter-spacing: -0.5px;
  text-transform: uppercase;
  color: #697382ff; /* --color-text-secondary */
}
.ds-avatar-info--inverse .ds-avatar-info__name {
  color: #ffffffff; /* --color-text-inverse */
}
.ds-avatar-info--inverse .ds-avatar-info__job {
  color: #bbc2ccff; /* --color-text-tertiary */
}
```


### Components — Breadcrumbs

Page path, current item last

Markup:

```html
<span class="ds-bc"><span class="ds-bc-item is-inactive">label</span><span class="ds-bc-item is-inactive">label</span><span class="ds-bc-item is-active">label</span></span>
```

Styles:

```css
.ds-bc-item {
  display: inline-flex;
  align-items: center;
  gap: 8px; /* --spacing-8 */
  padding-right: 8px; /* --spacing-8 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.caption.c2-12 — Archivo 12/12, вага 400 */
  font-size: 12px;
  line-height: 12px;
  font-weight: 400;
  white-space: nowrap;
  user-select: none;
}
.ds-bc-item::after {
  content: "";
  flex: none;
  width: 12px;
  height: 12px;
  background-color: #000000ff; /* --color-action-primary */
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M10 8.00373L6 5L6 11L10 8.00373Z' fill='black'/%3E %3C/svg%3E") no-repeat center / contain; /* --icon-arrow-side */
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M10 8.00373L6 5L6 11L10 8.00373Z' fill='black'/%3E %3C/svg%3E") no-repeat center / contain; /* --icon-arrow-side */
}
.ds-bc-item.is-inactive {
  color: #697382ff; /* --color-action-inactive */
}
.ds-bc {
  display: inline-flex;
  align-items: center;
  gap: 8px; /* --spacing-8 */
  padding: 8px; /* --spacing-8 */
}
```


### Components — Button

9 variants: primary, secondary, industry, link, play, icon-primary, icon-secondary, plus, block

Markup:

```html
<span class="ds-btn ds-btn--primary is-default">Button label</span>
```

Styles:

```css
.ds-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px; /* --spacing-8 */
  box-sizing: border-box;
  height: 40px; /* --button-height */
  padding: 0 16px; /* --spacing-16 */
  border: 1px solid transparent; /* --border-width-1 */
  border-radius: 32px; /* --radius-32 */
  font-family: var(--font-archivo); /* --button-font-family */
  font-size: 14px; /* --button-font-size */
  font-weight: 500; /* --button-font-weight */
  line-height: 16px; /* --button-line-height */
  white-space: nowrap;
  user-select: none;
}
.ds-btn::after {
  content: "";
  flex: none;
  width: 16px; /* --icon-size */
  height: 16px; /* --icon-size */
  background-color: currentColor;
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M4 12L12 4' stroke='white' stroke-linecap='round' stroke-linejoin='round'/%3E %3Cpath d='M4 4H12V12' stroke='white' stroke-linecap='round' stroke-linejoin='round'/%3E %3C/svg%3E") no-repeat center / contain; /* --icon-arrow-up-right */
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M4 12L12 4' stroke='white' stroke-linecap='round' stroke-linejoin='round'/%3E %3Cpath d='M4 4H12V12' stroke='white' stroke-linecap='round' stroke-linejoin='round'/%3E %3C/svg%3E") no-repeat center / contain; /* --icon-arrow-up-right */
}
.ds-btn--primary {
  background: #000000ff; /* --color-action-primary */
  color: #ffffffff; /* --color-text-inverse */
}
.ds-btn--primary.is-inactive {
  background: #697382ff; /* --color-action-inactive */
  color: #cdd4deff; /* --color-action-inactive-content */
}
.ds-btn--secondary {
  background: transparent;
  border-color: #d9d9d9ff; /* --color-border-subtle */
  color: #000000ff; /* --color-text-primary */
}
.ds-btn--secondary.is-inactive {
  border-color: #d9d9d9ff; /* --color-border-subtle */
  color: #697382ff; /* --color-action-inactive */
}
.ds-btn--industry {
  background: #ffffffff; /* --color-action-primary-invers */
  color: #000000ff; /* --color-action-primary */
  height: 44px; /* --button-height-industry */
  padding: 0 12px; /* --spacing-12 */
  font-size: 16px; /* --button-font-size-lg */
  line-height: 20px; /* --button-line-height-lg */
  font-weight: 400; /* --button-font-weight-lg */
}
.ds-btn--industry::before {
  content: "";
  flex: none;
  width: 16px; /* --icon-size */
  height: 16px; /* --icon-size */
  background-color: currentColor;
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M2 14L14 2' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3Cpath d='M14 14L2 2' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3Crect x='1.5' y='1.5' width='13' height='13' stroke='black'/%3E %3C/svg%3E") no-repeat center / contain; /* --icon-placeholder */
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M2 14L14 2' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3Cpath d='M14 14L2 2' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3Crect x='1.5' y='1.5' width='13' height='13' stroke='black'/%3E %3C/svg%3E") no-repeat center / contain; /* --icon-placeholder */
}
.ds-btn--industry.is-inactive {
  background: #697382ff; /* --color-action-inactive */
  color: #cdd4deff; /* --color-action-inactive-content */
}
.ds-btn--link {
  background: transparent;
  border-color: transparent;
  padding: 0;
  height: auto;
  color: #000000ff; /* --color-action-primary */
  text-transform: uppercase; /* TODO: звірити з Figma — стиль тексту не визначений */
}
.ds-btn--play {
  background: transparent;
  border-color: #ffffffff; /* --color-action-primary-invers */
  color: #ffffffff; /* --color-action-primary-invers */
  height: 28px; /* --button-height-play */
  gap: 4px; /* --spacing-4 */
  padding: 0 8px; /* --spacing-8 */
}
.ds-btn--play::before {
  content: "▶";
  flex: none;
  font-size: 16px; /* --icon-size */
  line-height: 16px; /* --icon-size */
}
.ds-btn--play::after {
  content: none;
}
.ds-btn--icon,
.ds-btn--icon-outline {
  width: 40px; /* --button-height */
  height: 40px; /* --button-height */
  padding: 0;
  border-radius: 32px; /* на боксі 40px обрізається до кола */
  font-size: 16px; /* --icon-size */
  line-height: 16px; /* --icon-size */
  gap: 0;
}
.ds-btn--icon::after,
.ds-btn--icon-outline::after {
  content: none;
}
.ds-btn--icon {
  background: #000000ff; /* --color-action-primary */
  color: #ffffffff; /* --color-icon-inverse */
}
.ds-btn--icon.is-inactive {
  background: #697382ff; /* --color-action-inactive */
  color: #cdd4deff; /* --color-action-inactive-content */
}
.ds-btn--icon-outline {
  background: transparent;
  border-color: #d9d9d9ff; /* --color-border-subtle */
  color: #000000ff; /* --color-icon-default */
}
.ds-btn--icon-outline.is-inactive {
  border-color: #d9d9d9ff; /* --color-border-subtle */
  color: #697382ff; /* --color-action-inactive */
}
.ds-btn--plus {
  width: 40px; /* --button-height */
  height: 40px; /* --button-height */
  padding: 0;
  border-radius: 32px; /* --radius-32 */
  background: transparent;
  border-color: #d9d9d9ff; /* TODO: звірити з Figma */
  color: #000000ff; /* --color-icon-default */
  font-size: 16px; /* --icon-size */
  line-height: 16px; /* --icon-size */
  gap: 0;
}
.ds-btn--plus::after {
  content: none;
}
.ds-btn--plus.is-inactive {
  border-color: #697382ff; /* TODO: звірити з Figma */
}
.ds-btn--plus.is-close {
  border-color: #d9d9d9ff; /* TODO: звірити з Figma */
}
.ds-btn--icon.is-loading {
  background: #000000ff; /* --color-action-primary */
  color: transparent;
  position: relative;
}
.ds-btn--icon.is-loading::before {
  content: "";
  position: absolute;
  width: 16px; /* --icon-size */
  height: 16px; /* --icon-size */
  border-radius: 80px; /* --radius-80 */
  border: 2px solid #ffffff4d; /* --color-border-white-30 */
  border-top-color: #ffffffff; /* --color-action-primary-invers */
  animation: ds-btn-spin 0.8s linear infinite;
}
.ds-btn-block {
  display: inline-flex;
  align-items: center;
  gap: 48px; /* --spacing-48 */
  box-sizing: border-box;
  padding: 8px 8px 8px 16px; /* --spacing-8, --spacing-16 */
  border-radius: 80px; /* --radius-80 */
  background: #ffffffff; /* --color-background-block */
  color: #000000ff; /* --color-text-primary */
}
.ds-btn-block__text {
  display: inline-flex;
  align-items: center;
  gap: 8px; /* --spacing-8 */
  font-family: var(--font-archivo); /* --button-font-family */
  font-size: 14px; /* --button-font-size */
  line-height: 1;
}
.ds-btn-block__actions {
  display: inline-flex;
  align-items: center;
  gap: 8px; /* --spacing-8 */
}
```


### Components — Checkbox

Square check, also used as dropdown list item

Markup:

```html
<span class="ds-cb is-checked" />
```

Styles:

```css
.ds-cb {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex: none;
  box-sizing: border-box;
  width: 24px; /* TODO: звірити з Figma */
  height: 24px; /* TODO: звірити з Figma */
  border: 1px solid #d9d9d9ff; /* --border-width-1, --color-border-subtle */
  border-radius: 8px; /* --radius-8 */
  color: #000000ff; /* --color-icon-default */
  font-size: 14px;
  line-height: 1;
}
.ds-cb.is-checked::before,
.ds-dd-item.is-selected .ds-cb::before {
  content: "";
  flex: none;
  width: 16px; /* --icon-size */
  height: 16px; /* --icon-size */
  background-color: currentColor;
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M4 8L6.78261 11L12 5' stroke='black' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'/%3E %3C/svg%3E") no-repeat center / contain; /* --icon-check */
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M4 8L6.78261 11L12 5' stroke='black' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'/%3E %3C/svg%3E") no-repeat center / contain; /* --icon-check */
}
```


### Components — Chips

Outlined filter pill with trailing arrow

Markup:

```html
<span class="ds-chip is-default">Chip label</span>
```

Styles:

```css
.ds-chip {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  gap: 8px; /* --spacing-8 */
  height: 40px; /* --button-height */
  padding: 0 16px; /* --spacing-16 */
  border: 1px solid transparent; /* --border-width-1 */
  border-radius: 32px; /* --radius-32 */
  font-family: var(--font-archivo); /* --button-font-family */
  font-size: 14px; /* --button-font-size */
  font-weight: 500; /* --button-font-weight */
  line-height: 16px; /* --button-line-height */
  white-space: nowrap;
  user-select: none;
}
.ds-chip::after {
  content: "";
  flex: none;
  width: 16px; /* --icon-size */
  height: 16px; /* --icon-size */
  background-color: currentColor;
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M4 12L12 4' stroke='white' stroke-linecap='round' stroke-linejoin='round'/%3E %3Cpath d='M4 4H12V12' stroke='white' stroke-linecap='round' stroke-linejoin='round'/%3E %3C/svg%3E") no-repeat center / contain; /* --icon-arrow-up-right */
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M4 12L12 4' stroke='white' stroke-linecap='round' stroke-linejoin='round'/%3E %3Cpath d='M4 4H12V12' stroke='white' stroke-linecap='round' stroke-linejoin='round'/%3E %3C/svg%3E") no-repeat center / contain; /* --icon-arrow-up-right */
}
.ds-chip.is-default {
  background: transparent;
  border-color: #000000ff; /* --color-action-primary */
  color: #000000ff; /* --color-text-primary */
}
.ds-chip.is-inactive {
  background: transparent;
  border-color: #d9d9d9ff; /* --color-border-subtle */
  color: #697382ff; /* --color-action-inactive */
}
```


### Components — Dropdown

Trigger plus menu of checkbox items

Markup:

```html
<span class="ds-dd-menu"><span class="ds-dd-menu__list"><span class="ds-dd-item"><span class="ds-cb" />Item label</span><span class="ds-dd-item is-selected"><span class="ds-cb" />Item label</span><span class="ds-dd-item"><span class="ds-cb" />Item label</span></span></span>
```

Styles:

```css
.ds-dd {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  gap: 8px; /* --spacing-8 */
  height: 40px; /* --button-height */
  /* 12 / 12 / 12 / 10 — лівий відступ 10px поза шкалою primitives.spacing */
  padding: 12px 12px 12px 10px; /* --spacing-12 */
  border-radius: 32px; /* --radius-32 */
  font-family: var(--font-archivo); /* --button-font-family */
  font-size: 14px; /* --button-font-size */
  font-weight: 500; /* --button-font-weight */
  line-height: 16px; /* --button-line-height */
  white-space: nowrap;
  user-select: none;
}
.ds-dd::after {
  content: "";
  flex: none;
  width: 16px; /* --icon-size */
  height: 16px; /* --icon-size */
  background-color: currentColor;
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E%3Cpath d='M8.00373 10L5 6H11L8.00373 10Z' fill='black'/%3E%3C/svg%3E") no-repeat center / contain; /* --icon-caret */
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E%3Cpath d='M8.00373 10L5 6H11L8.00373 10Z' fill='black'/%3E%3C/svg%3E") no-repeat center / contain; /* --icon-caret */
}
.ds-dd.is-open::after {
  transform: rotate(180deg);
}
.ds-dd.is-default {
  background: #ffffffff; /* TODO: звірити з Figma */
  color: #000000ff; /* --color-text-primary */
}
.ds-dd.is-disabled {
  background: #697382ff; /* TODO: звірити з Figma */
  color: #cdd4deff; /* --color-action-inactive-content */
}
.ds-dd__count {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex: none;
  width: 24px; /* TODO: звірити з Figma */
  height: 24px; /* TODO: звірити з Figma */
  border-radius: 32px; /* --radius-32 */
  background: #000000ff; /* TODO: звірити з Figma */
  color: #ffffffff; /* TODO: звірити з Figma */
  font-size: 12px;
}
.ds-dd-menu {
  display: block;
  box-sizing: border-box;
  width: 280px; /* TODO: звірити з Figma */
  padding: 16px; /* --spacing-16 */
  border: 1px solid #e9e9e9ff; /* --border-width-1, --color-border-default */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-dd-menu__list {
  display: flex;
  flex-direction: column;
  gap: 8px; /* TODO: звірити з Figma — dropdown/gap дорівнює 24px */
}
.ds-dd-item {
  display: flex;
  align-items: center;
  gap: 12px; /* TODO: звірити з Figma */
  padding: 8px; /* --spacing-8 */
  border-radius: 8px; /* --radius-8 */
  font-family: var(--font-archivo); /* --button-font-family */
  font-size: 14px; /* --button-font-size */
  line-height: 16px; /* --button-line-height */
  color: #000000ff; /* --color-text-primary */
}
.ds-dd-group {
  display: inline-flex;
  align-items: center;
  gap: 2px; /* TODO: звірити з Figma */
  padding: 4px; /* TODO: звірити з Figma */
  border-radius: 32px; /* --radius-32 */
  background: #e9e9e9ff; /* TODO: звірити з Figma */
}
```


### Components — Links

Navigation link, plain variant has no arrow

Markup:

```html
<span class="ds-link is-default">Label</span>
```

Styles:

```css
.ds-link--plain::after {
  content: none;
}
.ds-link {
  display: inline-flex;
  align-items: center;
  gap: 0;
  padding: 0;
  height: 16px;
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p4-14 — 14 / 16 */
  font-size: 14px; /* --button-font-size */
  line-height: 16px; /* --button-line-height */
  font-weight: 500; /* --button-font-weight */
  white-space: nowrap;
  user-select: none;
}
.ds-link::after {
  content: "";
  flex: none;
  width: 16px; /* --icon-size */
  height: 16px; /* --icon-size */
  background-color: currentColor;
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E%3Cpath d='M8.00373 10L5 6H11L8.00373 10Z' fill='black'/%3E%3C/svg%3E") no-repeat center / contain; /* --icon-caret */
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E%3Cpath d='M8.00373 10L5 6H11L8.00373 10Z' fill='black'/%3E%3C/svg%3E") no-repeat center / contain; /* --icon-caret */
}
.ds-link.is-active::after {
  transform: rotate(180deg);
}
.ds-link.is-default {
  color: #000000ff; /* --color-action-primary */
}
.ds-link.is-inactive {
  color: #697382ff; /* --color-action-inactive */
}
```


### Components — Links group

Bordered row of header links

Markup:

```html
<span class="ds-header-menu"><span class="ds-link is-default">Product design</span><span class="ds-link is-default">AI visibility</span><span class="ds-link ds-link--plain is-default">Outcomes</span><span class="ds-link is-default">About us</span></span>
```

Styles:

```css
.ds-header-menu {
  display: inline-flex;
  align-items: center;
  box-sizing: border-box;
  gap: 20px; /* --spacing-20 */
  padding: 12px 16px; /* --spacing-12, --spacing-16 */
  border: 1px solid #d9d9d9ff; /* --border-width-1, --color-border-subtle */
  border-radius: 4px; /* --radius-4 */
  background: #ffffffff; /* --color-background-block */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  font-size: 14px; /* --button-font-size */
  line-height: 16px; /* --button-line-height */
  font-weight: 500; /* --button-font-weight */
  color: #000000ff; /* --color-action-primary */
}
```


### Components — Media

Image placeholder, sizes S/M/L, ratio 1.504

Markup:

```html
<span class="ds-media ds-media--m" />
```

Styles:

```css
.ds-media {
  display: block;
  max-width: 100%;
  border-radius: 4px; /* --radius-4 */
  background: repeating-conic-gradient(#f4f4f4 0% 25%, #fbfbfb 0% 50%) 0 0 / 46px 46px;
}
.ds-media--s {
  width: 280px;
  aspect-ratio: 280 / 186;
}
.ds-media--m {
  width: 388px;
  aspect-ratio: 388 / 258;
}
.ds-media--l {
  width: 616px;
  aspect-ratio: 616 / 410;
}
```


### Components — Pagination

Page numbers in a pill with arrow buttons

Markup:

```html
<span class="ds-pagination"><span class="ds-btn ds-btn--icon is-default">←</span><span class="ds-pagination__numbers"><span class="ds-pagi is-active">1</span><span class="ds-pagi is-inactive">2</span><span class="ds-pagi is-inactive">3</span><span class="ds-pagi ds-pagi--dots">…</span><span class="ds-pagi is-inactive">7</span></span><span class="ds-btn ds-btn--icon is-default">→</span></span>
```

Styles:

```css
.ds-pagi {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  width: 40px; /* --button-height */
  height: 40px; /* --button-height */
  border-radius: 32px; /* --radius-32 */
  font-family: var(--font-archivo); /* --button-font-family */
  font-size: 14px; /* --button-font-size */
  font-weight: 500; /* --button-font-weight */
  line-height: 16px; /* --button-line-height */
  user-select: none;
}
.ds-pagi.is-inactive {
  background: #ffffffff; /* --color-action-primary-invers */
  color: #000000ff; /* --color-action-primary */
}
.ds-pagi--dots {
  background: none;
  color: #000000ff; /* --color-action-primary */
}
.ds-pagination {
  display: inline-flex;
  align-items: center;
  gap: 24px; /* --spacing-24 */
  padding: 4px; /* --spacing-4 */
  border-radius: 32px; /* --radius-32 */
  background: #e9e9e9ff; /* --color-background-page */
}
.ds-pagination__numbers {
  display: inline-flex;
  align-items: center;
  gap: 2px; /* --spacing-2 */
}
```


### Components — Tab

Segmented control, one active

Markup:

```html
<span class="ds-tabs"><span class="ds-tab ds-tab--plain is-active">Acquired</span><span class="ds-tab ds-tab--plain is-default">Unicorns</span><span class="ds-tab ds-tab--plain is-default">Growth</span></span>
```

Styles:

```css
.ds-tab {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  gap: 8px; /* --spacing-8 */
  height: 40px; /* --button-height */
  padding: 0 12px; /* --spacing-12 */
  border: none;
  border-radius: 32px; /* --radius-32 */
  font-family: var(--font-archivo); /* --button-font-family */
  font-size: 14px; /* --button-font-size */
  font-weight: 500; /* --button-font-weight */
  line-height: 16px; /* --button-line-height */
  white-space: nowrap;
  user-select: none;
}
.ds-tab::before {
  content: "";
  flex: none;
  width: 16px; /* --icon-size */
  height: 16px; /* --icon-size */
  background-color: currentColor;
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M2 14L14 2' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3Cpath d='M14 14L2 2' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3Crect x='1.5' y='1.5' width='13' height='13' stroke='black'/%3E %3C/svg%3E") no-repeat center / contain; /* --icon-placeholder */
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16' fill='none'%3E %3Cpath d='M2 14L14 2' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3Cpath d='M14 14L2 2' stroke='black' stroke-linecap='round' stroke-linejoin='round'/%3E %3Crect x='1.5' y='1.5' width='13' height='13' stroke='black'/%3E %3C/svg%3E") no-repeat center / contain; /* --icon-placeholder */
}
.ds-tab--plain::before {
  content: none;
}
.ds-tab.is-default {
  background: #ffffffff; /* --color-action-primary-invers */
  color: #000000ff; /* --color-action-primary */
}
.ds-tab.is-inactive {
  background: #697382ff; /* --color-action-inactive */
  color: #cdd4deff; /* --color-action-inactive-content */
}
.ds-tabs {
  display: inline-flex;
  align-items: center;
  gap: 2px; /* --spacing-2 */
  padding: 4px; /* --spacing-4 */
  border-radius: 32px; /* --radius-32 */
  background: #e9e9e9ff; /* --color-background-page */
}
```


### Components — Tag

Uppercase label with hairline separator

Markup:

```html
<span class="ds-card-meta"><span class="ds-tag is-default">Tag</span></span>
```

Styles:

```css
.ds-tag {
  display: inline-flex;
  align-items: center;
  gap: 16px; /* --spacing-16 */
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.caption.c1-16 — Pragati Narrow 16/16, uppercase */
  font-size: 16px;
  line-height: 16px;
  font-weight: 400;
  letter-spacing: -0.5px;
  text-transform: uppercase;
  white-space: nowrap;
  user-select: none;
}
.ds-tag::before,
.ds-tag::after {
  content: "";
  flex: none;
  width: 1px;
  height: 11px;
  background: #697382ff; /* --color-text-secondary */
}
.ds-tag:first-child::before {
  content: none;
}
.ds-tag + .ds-tag::before {
  content: none;
}
.ds-tag.is-default {
  color: #697382ff; /* --color-action-inactive */
}
```


### Components — Toggle

Binary switch, applies immediately

Markup:

```html
<span class="ds-toggle is-active"><span class="ds-toggle__knob" /></span>
```

Styles:

```css
.ds-toggle {
  display: inline-flex;
  align-items: center;
  box-sizing: border-box;
  width: 28px;
  height: 16px;
  padding: 1px;
  border-radius: 32px; /* --radius-32 */
  background: #2a2a2aff; /* --color-background-elements */
}
.ds-toggle__knob {
  width: 14px;
  height: 14px;
  border-radius: 32px; /* --radius-32 */
}
.ds-toggle.is-default .ds-toggle__knob {
  background: #697382ff; /* --color-action-inactive */
}
.ds-toggle.is-active {
  justify-content: flex-end;
}
.ds-toggle.is-active .ds-toggle__knob {
  background: #0da34eff; /* --color-action-brand-hover */
}
```


### Cards — Article

Article teaser; S 312 / M 388 / L 616

Markup:

```html
<span class="ds-article-card"><span class="ds-card-meta"><span class="ds-tag is-default">Tag</span><span class="ds-card-date">04 May 2026</span></span><span class="ds-article-card__title">MVP landing page: how to build one to validate your business idea</span><span class="ds-article-card__desc">AI roadmap is real, adoption isn't.</span><span class="ds-article-card__action"><span class="ds-btn ds-btn--secondary is-default">Button label</span></span><span class="ds-article-card__img" /></span>
```

Styles:

```css
.ds-article-card {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  width: 312px;
  max-width: 100%;
  padding: 16px; /* --spacing-16 */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-article-card__title {
  margin-top: 25px; /* --spacing-25 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.heading.h6-20 — Archivo 20/24, вага 500 */
  font-size: 20px;
  line-height: 24px;
  font-weight: 500;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.ds-article-card__desc {
  display: block;
  margin-top: 12px; /* --spacing-12 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p3-16 — Archivo 16/20 */
  font-size: 16px;
  line-height: 20px;
  font-weight: 400;
  color: #000000ff; /* --color-text-primary */
}
.ds-article-card__action {
  display: block;
  margin-top: 16px; /* --spacing-16 */
}
.ds-article-card__img {
  display: block;
  margin-top: 32px; /* --spacing-32 */
  width: 100%;
  height: 176px;
  border-radius: 4px; /* --radius-4 */
  background: repeating-conic-gradient(#f4f4f4 0% 25%, #fbfbfb 0% 50%) 0 0 / 46px 46px;
}
.ds-article-card--m {
  width: 436px;
  padding: 24px; /* --spacing-24 */
}
.ds-article-card--m .ds-article-card__title {
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.heading.h4-36 — Pragati Narrow 36/32, вага 400 */
  font-size: 36px;
  line-height: 32px;
  font-weight: 400;
}
.ds-article-card--m .ds-article-card__desc {
  margin-top: 16px; /* --spacing-16 */
}
.ds-article-card--m .ds-article-card__action {
  margin-top: 20px; /* --spacing-20 */
}
.ds-article-card--m .ds-article-card__img {
  height: 244px;
}
.ds-article-card--l {
  width: 664px;
  padding: 24px; /* --spacing-24 */
}
.ds-article-card--l .ds-article-card__title {
  margin-top: 0;
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.heading.h3-46 — Pragati Narrow 46/40, вага 400 */
  font-size: 46px;
  line-height: 40px;
  font-weight: 400;
}
.ds-article-card__row {
  display: flex;
  align-items: center;
  gap: 32px; /* --spacing-32 */
  margin-top: 25px; /* --spacing-25 */
}
.ds-article-card__row .ds-article-card__desc {
  flex: 1;
  min-width: 0;
  margin-top: 0;
}
.ds-article-card__row .ds-article-card__action {
  flex: none;
  margin-top: 0;
}
.ds-article-card--l .ds-article-card__img {
  height: 387px;
}
```


### Cards — Article menu

Article teaser inside the header menu

Markup:

```html
<span class="ds-card-am">
  <span class="ds-media ds-media--s" />
  <span class="ds-card-am__title">Title</span>
  <span class="ds-btn ds-btn--icon-outline is-default"><span class="ds-icon ds-icon--arrow-up-right" /></span>
</span>
```

Styles:

```css
.ds-card-am {
  display: flex;
  align-items: flex-start;
  box-sizing: border-box;
  gap: 24px; /* --spacing-24 */
  width: 100%;
  padding: 16px; /* --spacing-16 */
  border: 1px solid #e9e9e9ff; /* --border-width-1, --color-border-default */
  border-radius: 4px; /* --radius-4 */
  background: #ffffffff; /* --color-background-block */
}
.ds-card-am .ds-media {
  flex: none;
  width: 159px;
  aspect-ratio: 159 / 100;
}
.ds-card-am__title {
  flex: 1;
  min-width: 0;
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.heading.h6-20 — Archivo 20/24, вага 500, трекінг -0.5 */
  font-size: 20px;
  line-height: 24px;
  font-weight: 500;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```


### Cards — Award

Award name, year, project

Markup:

```html
<span class="ds-award-card">
  <span class="ds-award-card__logo" />
  <span class="ds-award-card__title">Title</span>
</span>
```

Styles:

```css
.ds-award-card {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  gap: 40px; /* --spacing-40 */
  width: 324px;
  max-width: 100%;
  padding: 16px; /* --spacing-16 */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-award-card__logo {
  flex: none;
  box-sizing: border-box;
  width: 160px;
  height: 60px;
  border: 1px dashed #d9d9d9ff; /* --border-width-1, --color-border-subtle */
  border-radius: 4px; /* --radius-4 */
}
.ds-award-card__title {
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.heading.h6-20 — Archivo 20/24, вага 500 */
  font-size: 20px;
  line-height: 24px;
  font-weight: 500;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
}
```


### Cards — Bullet point

Green dot marker plus one paragraph

Markup:

```html
<span class="ds-bullet-card">
  <span class="ds-point" />
  <span class="ds-bullet-card__text">text</span>
</span>
```

Styles:

```css
.ds-bullet-card {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  box-sizing: border-box;
  gap: 8px; /* --spacing-8 */
  width: 400px;
  max-width: 100%;
  padding: 24px; /* --spacing-24 */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-bullet-card__text {
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p3-16 — Archivo 16/20 */
  font-size: 16px;
  line-height: 20px;
  font-weight: 400;
  color: #000000ff; /* --color-text-primary */
}
```


### Cards — Case

Case teaser; S 312 / L 616

Markup:

```html
<span class="ds-case-card"><span class="ds-case-card__img" /><span><span class="ds-card-meta"><span class="ds-tag is-default">Tag</span><span class="ds-card-date">04 May 2026</span></span><span class="ds-case-card__title">Project name</span><span class="ds-case-card__action"><span class="ds-btn ds-btn--secondary is-default">Button label</span></span></span></span>
```

Styles:

```css
.ds-case-card {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  gap: 12px; /* --spacing-12 */
  width: 312px;
  max-width: 100%;
  padding: 16px; /* --spacing-16 */
  border: 1px solid #e9e9e9ff; /* --border-width-1, --color-border-default */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-case-card__img {
  display: block;
  width: 100%;
  aspect-ratio: 280 / 176;
  border-radius: 4px; /* --radius-4 */
  background: repeating-conic-gradient(#f4f4f4 0% 25%, #fbfbfb 0% 50%) 0 0 / 46px 46px;
}
.ds-case-card__title {
  margin-top: 12px; /* --spacing-12 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.heading.h6-20 — Archivo 20/24, вага 500 */
  font-size: 20px;
  line-height: 24px;
  font-weight: 500;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.ds-case-card__action {
  display: block;
  margin-top: 16px; /* --spacing-16 */
}
.ds-case-card--l {
  gap: 0;
  width: 436px;
  height: 693px;
  padding: 24px; /* --spacing-24 */
}
.ds-case-card--l .ds-case-card__img {
  margin-top: auto;
  aspect-ratio: 388 / 258;
}
.ds-case-card__desc {
  display: block;
  margin-top: 16px; /* --spacing-16 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p3-16 — Archivo 16/20. TODO: звірити з Figma */
  font-size: 16px;
  line-height: 20px;
  font-weight: 400;
  color: #000000ff; /* --color-text-primary */
}
.ds-case-card--l .ds-case-card__action {
  margin-top: 20px; /* --spacing-20 */
}
.ds-case-card--l .ds-case-card__title {
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.heading.h4-36 — Pragati Narrow 36/32, вага 400 */
  font-size: 36px;
  line-height: 32px;
  font-weight: 400;
}
```


### Cards — Number

Numbered step with badge

Markup:

```html
<span class="ds-number-card">
  <span class="ds-badge">01</span>
  <span class="ds-number-card__title">00</span>
  <span class="ds-number-card__text">text</span>
</span>
```

Styles:

```css
.ds-number-card {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  box-sizing: border-box;
  width: 332px;
  max-width: 100%;
  padding: 24px; /* --spacing-24 */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-number-card__title {
  margin-top: 32px; /* --spacing-32 */
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.heading.h1-80 — Pragati Narrow 80/72, вага 400 */
  font-size: 80px;
  line-height: 72px;
  font-weight: 400;
  letter-spacing: -1.5px;
  color: #000000ff; /* --color-text-primary */
}
.ds-number-card__text {
  margin-top: 20px; /* --spacing-20 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.heading.h6-20 — Archivo 20/24, вага 500 */
  font-size: 20px;
  line-height: 24px;
  font-weight: 500;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
}
```


### Cards — Outcomes

Metric card, dark, translucent; needs a dark parent

Markup:

```html
<span class="ds-outcomes-card">
  <span class="ds-outcomes-card__logo" />
  <span class="ds-outcomes-card__text">text</span>
  <span class="ds-outcomes-card__number">number</span>
  <span class="ds-outcomes-card__period">period</span>
</span>
```

Styles:

```css
.ds-outcomes-card {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  /* вирівнювання задаємо явно: батьківський блок центрований */
  text-align: left;
  width: 272px;
  max-width: 100%;
  height: 272px;
  padding: 16px; /* --spacing-16 */
  border-radius: 8px; /* --radius-8 */
  background: #ffffff1a; /* --color-background-white-10 */
}
.ds-outcomes-card__logo {
  flex: none;
  box-sizing: border-box;
  width: 120px; /* TODO: звірити з Figma */
  height: 32px;
  border: 1px dashed #ffffff4d; /* --border-width-1, --color-border-white-30 */
  border-radius: 4px; /* --radius-4 */
}
.ds-outcomes-card__text {
  margin-top: 12px; /* --spacing-12 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p3-16 — Archivo 16/20 */
  font-size: 16px;
  line-height: 20px;
  font-weight: 400;
  color: #ffffffff; /* --color-text-inverse */
}
.ds-outcomes-card__number {
  margin-top: auto;
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.heading.h2-56 — Pragati Narrow 56/48, вага 400 */
  font-size: 56px;
  line-height: 48px;
  font-weight: 400;
  letter-spacing: -0.5px;
  color: #ffffffff; /* --color-text-inverse */
}
.ds-outcomes-card--l {
  width: 332px;
  height: 400px;
  padding: 24px; /* --spacing-24 */
  border: 1px solid #d9d9d9ff; /* --border-width-1, --color-border-subtle */
  background: #ffffffff; /* --color-background-block */
}
.ds-outcomes-card--l .ds-outcomes-card__number {
  margin-top: 0;
  /* font.heading.h1-80 — Pragati Narrow 80/72, вага 400 */
  font-size: 80px;
  line-height: 72px;
  letter-spacing: -1.5px;
  color: #000000ff; /* --color-text-primary */
}
.ds-outcomes-card--l .ds-outcomes-card__text {
  margin-top: 16px; /* --spacing-16 */
  /* font.heading.h6-20 — Archivo 20/24, вага 500 */
  font-size: 20px;
  line-height: 24px;
  font-weight: 500;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
}
.ds-outcomes-card--l .ds-outcomes-card__logo {
  margin-top: auto;
  width: 156px;
  height: 44px;
  border-color: #d9d9d9ff; /* --color-border-subtle */
}
.ds-outcomes-card__paragraph {
  display: block;
  margin-top: auto;
  height: 48px;
  overflow: hidden;
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p4-14 — Archivo 14/16, вага 500 */
  font-size: 14px;
  line-height: 16px;
  font-weight: 500;
  color: #000000ff; /* --color-text-primary */
}
.ds-outcomes-card__period {
  margin-top: 4px; /* --spacing-4 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p3-16 — Archivo 16/20 */
  font-size: 16px;
  line-height: 20px;
  font-weight: 400;
  color: #0f9549ff; /* --color-text-attention */
}
```


### Cards — Testimonials

Quote with author and rating

Markup:

```html
<span class="ds-testimonial">
  <span class="ds-testimonial__top">
    <span class="ds-testimonial__quote">“</span>
    <span class="ds-testimonial__rating" />
  </span>
  <span class="ds-testimonial__text">Thanks to Grand Founders and its unique community of Ambassadors, I've gained access to opportunities for expanding my business in Ukraine and have also grown my capital raising capabilities.</span>
  <span class="ds-testimonial__bottom">
    <span class="ds-avatar-info">
      <span class="ds-avatar-info__photos"><span class="ds-avatar ds-avatar--m" /><span class="ds-avatar ds-avatar--m" /></span>
      <span class="ds-avatar-info__text"><span class="ds-avatar-info__name">Name</span><span class="ds-avatar-info__job">Job title</span></span>
    </span>
    <span class="ds-btn ds-btn--primary is-default">View Case Study</span>
  </span>
</span>
```

Styles:

```css
.ds-testimonial {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  width: 664px;
  max-width: 100%;
  height: 604px;
  /* по боках 24px — підтверджено з дизайном; по вертикалі 16px із card/testimonials/padding */
  padding: 16px 24px; /* --spacing-16, --spacing-24 */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-testimonial__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px; /* --spacing-16 */
}
.ds-testimonial__quote {
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.heading.h1-80 — Pragati Narrow 80/72 */
  font-size: 80px;
  line-height: 72px;
  font-weight: 400;
  letter-spacing: -1.5px;
  color: #000000ff; /* --color-text-primary */
}
.ds-testimonial__rating {
  flex: none;
  box-sizing: border-box;
  width: 165px;
  height: 72px;
  border: 1px dashed #d9d9d9ff; /* --border-width-1, --color-border-subtle */
  border-radius: 4px; /* --radius-4 */
}
.ds-testimonial__text {
  margin-top: 64px; /* --spacing-64 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.heading.h5-24 — Archivo 24/24, вага 500 */
  font-size: 24px;
  line-height: 24px;
  font-weight: 500;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
}
.ds-testimonial__bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px; /* --spacing-16 */
  margin-top: auto;
}
```


### Cards — Text

Title over gradient plus body

Markup:

```html
<span class="ds-text-card">
  <span class="ds-text-card__title">Title</span>
  <span class="ds-text-card__rule" />
  <span class="ds-text-card__text">text</span>
</span>
```

Styles:

```css
.ds-text-card {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  width: 332px;
  max-width: 100%;
  height: 416px;
  padding: 16px; /* --spacing-16 */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-text-card__title {
  height: 136px;
  overflow: hidden;
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.heading.h4-36 — Pragati Narrow 36/32, вага 400 */
  font-size: 36px;
  line-height: 32px;
  font-weight: 400;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
}
.ds-text-card__rule {
  flex: none;
  margin-top: 8px; /* --spacing-8 */
  height: 8px;
  border-radius: 2px;
  background: linear-gradient(314.967deg, #1e1e1eff 0%, #0da34eff 54%, #0a783aff 60%, #1e1e1eff 65%, #c2cddeff 68%, #0da34eff 74%, #c2cddeff 84%, #1e1e1eff 100%); /* --gradient-vertical-3 */
}
.ds-text-card__text {
  margin-top: auto;
  max-height: 215px;
  overflow: hidden;
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p3-16 — Archivo 16/20 */
  font-size: 16px;
  line-height: 20px;
  font-weight: 400;
  color: #000000ff; /* --color-text-primary */
}
```


### Blocks — Title block

Section header: title, description, optional button. Starts nearly every section

Markup:

```html
<span class="ds-title-block">
  <span class="ds-title-block__title">Title</span>
  <span class="ds-title-block__desc">Description</span>
  <span class="ds-title-block__action"><span class="ds-btn ds-btn--primary is-default">All case studies</span></span>
</span>
```

Styles:

```css
.ds-title-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}
.ds-title-block__title {
  max-width: 672px;
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.heading.h2-56 — Pragati Narrow 56/48, вага 400 */
  font-size: 56px;
  line-height: 48px;
  font-weight: 400;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.ds-title-block__desc {
  max-width: 640px;
  margin-top: 24px; /* --spacing-24 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.heading.h6-20 — Archivo 20/24, вага 500 */
  font-size: 20px;
  line-height: 24px;
  font-weight: 500;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
  display: -webkit-box;
  -webkit-line-clamp: 6;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.ds-title-block__action {
  display: block;
  margin-top: 24px; /* --spacing-24 */
}
```


### Blocks — Case

Case study block; desktop / tablet / mobile

Markup:

```html
<span class="ds-case-block"><span class="ds-case-block__main"><span class="ds-card-meta"><span class="ds-tag is-default">Tag</span><span class="ds-card-date">04 May 2026</span></span><span class="ds-case-block__title">Title</span><span class="ds-case-block__paragraph">paragraph</span><span class="ds-case-block__action"><span class="ds-btn ds-btn--primary is-default">View case</span></span></span><span class="ds-case-block__media" /></span>
```

Styles:

```css
.ds-case-block {
  display: flex;
  box-sizing: border-box;
  gap: 40px; /* --spacing-40 */
  width: 100%;
  min-width: 1344px;
  padding: 24px; /* --spacing-24 */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-case-block__main {
  display: flex;
  flex-direction: column;
  flex: 1 1 0;
  min-width: 0;
}
.ds-case-block__title {
  margin-top: 12px; /* --spacing-12 */
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.heading.h3-46 — Pragati Narrow 46/40, вага 400 */
  font-size: 46px;
  line-height: 40px;
  font-weight: 400;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
}
.ds-case-block__paragraph {
  display: block;
  margin-top: 24px; /* --spacing-24 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p3-16 — Archivo 16/20 */
  font-size: 16px;
  line-height: 20px;
  font-weight: 400;
  color: #000000ff; /* --color-text-primary */
}
.ds-case-block__action {
  display: block;
  margin-top: auto;
  padding-top: 24px; /* --spacing-24 */
}
.ds-case-block__media {
  flex: none;
  width: 672px;
  aspect-ratio: 672 / 432;
  border-radius: 4px; /* --radius-4 */
  background: repeating-conic-gradient(#f4f4f4 0% 25%, #fbfbfb 0% 50%) 0 0 / 46px 46px;
}
.ds-case-block--tablet,
.ds-case-block--mobile {
  flex-direction: column;
}
.ds-case-block--tablet .ds-case-block__media,
.ds-case-block--mobile .ds-case-block__media {
  width: 100%;
}
.ds-case-block--tablet .ds-case-block__action,
.ds-case-block--mobile .ds-case-block__action {
  margin-top: 24px; /* --spacing-24 */
  padding-top: 0;
}
.ds-case-block--tablet {
  width: 796px;
  min-width: 796px;
  gap: 40px; /* --spacing-40 */
  padding: 16px; /* --spacing-16 */
}
.ds-case-block--mobile {
  width: 382px;
  min-width: 382px;
  gap: 24px; /* --spacing-24 */
  padding: 12px; /* --spacing-12 */
}
```


### Blocks — Case outcomes

Case metrics row

Markup:

```html
<span class="ds-case-outcomes-block">
  <span class="ds-case-outcomes-block__head">
    <span class="ds-case-outcomes-block__half"><span class="ds-case-outcomes-block__title">Title</span></span>
    <span class="ds-case-outcomes-block__half"><span class="ds-case-outcomes-block__paragraph">Paragraph</span></span>
  </span>
  <span class="ds-case-outcomes-block__controls">
    <span class="ds-case-outcomes-block__half">
      <span class="ds-tabs">
        <span class="ds-tab ds-tab--plain is-active">Acquired</span>
        <span class="ds-tab ds-tab--plain is-default">Unicorns</span>
        <span class="ds-tab ds-tab--plain is-default">Growth</span>
      </span>
    </span>
    <span class="ds-case-outcomes-block__half">
      <span class="ds-case-outcomes-block__actions">
        <span class="ds-btn ds-btn--primary is-default">Read more</span>
        <span class="ds-btn ds-btn--secondary is-default">Button label</span>
      </span>
    </span>
  </span>
  <span class="ds-case-outcomes-block__cards">
    <span class="ds-case-card">
      <span class="ds-case-card__img" />
      <span>
        <span class="ds-card-meta">
          <span class="ds-tag is-default">Tag</span>
          <span class="ds-card-date">04 May 2026</span>
        </span>
        <span class="ds-case-card__title">Project name</span>
        <span class="ds-case-card__action"><span class="ds-btn ds-btn--secondary is-default">Button label</span></span>
      </span>
    </span>
    <span class="ds-case-card">
      <span class="ds-case-card__img" />
      <span>
        <span class="ds-card-meta">
          <span class="ds-tag is-default">Tag</span>
          <span class="ds-card-date">04 May 2026</span>
        </span>
        <span class="ds-case-card__title">Project name</span>
        <span class="ds-case-card__action"><span class="ds-btn ds-btn--secondary is-default">Button label</span></span>
      </span>
    </span>
    <span class="ds-case-card">
      <span class="ds-case-card__img" />
      <span>
        <span class="ds-card-meta">
          <span class="ds-tag is-default">Tag</span>
          <span class="ds-card-date">04 May 2026</span>
        </span>
        <span class="ds-case-card__title">Project name</span>
        <span class="ds-case-card__action"><span class="ds-btn ds-btn--secondary is-default">Button label</span></span>
      </span>
    </span>
    <span class="ds-case-card">
      <span class="ds-case-card__img" />
      <span>
        <span class="ds-card-meta">
          <span class="ds-tag is-default">Tag</span>
          <span class="ds-card-date">04 May 2026</span>
        </span>
        <span class="ds-case-card__title">Project name</span>
        <span class="ds-case-card__action"><span class="ds-btn ds-btn--secondary is-default">Button label</span></span>
      </span>
    </span>
  </span>
</span>
```

Styles:

```css
.ds-case-outcomes-block {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  width: 100%;
  min-width: 1344px;
  padding: 24px; /* --spacing-24 */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-case-outcomes-block__head,
.ds-case-outcomes-block__controls {
  display: flex;
  align-items: flex-start;
}
.ds-case-outcomes-block__controls {
  align-items: center;
  margin-top: 32px; /* --spacing-32 */
}
.ds-case-outcomes-block__half {
  flex: 1 1 0;
  min-width: 0;
}
.ds-case-outcomes-block__title {
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.heading.h3-46 — Pragati Narrow 46/40, вага 400 */
  font-size: 46px;
  line-height: 40px;
  font-weight: 400;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
}
.ds-case-outcomes-block__paragraph {
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p3-16 — Archivo 16/20 */
  font-size: 16px;
  line-height: 20px;
  font-weight: 400;
  color: #000000ff; /* --color-text-primary */
}
.ds-case-outcomes-block__actions {
  display: flex;
  gap: 8px; /* --spacing-8 */
}
.ds-case-outcomes-block__cards {
  display: flex;
  gap: 16px; /* --spacing-16 */
  margin-top: 32px; /* TODO: звірити з Figma */
}
```


### Blocks — CTA

Closing call to action with two buttons

Markup:

```html
<span class="ds-cta-block">
  <span class="ds-cta-block__desc">Let's talk about your AI adoption challenge</span>
  <span class="ds-cta-block__title">Tell us where adoption stalls. You'll hear back from a senior product and UX lead with a practical action plan.</span>
  <span class="ds-cta-block__actions">
    <span class="ds-btn-block">
      <span class="ds-btn-block__text"><span class="ds-icon ds-icon--placeholder" />Response within one business day</span>
      <span class="ds-btn-block__actions">
        <span class="ds-btn ds-btn--primary is-default">Talk to us</span>
        <span class="ds-btn ds-btn--secondary is-default">Explore our services</span>
      </span>
    </span>
  </span>
</span>
```

Styles:

```css
.ds-cta-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  box-sizing: border-box;
  width: 100%;
  /* Проєктна ширина 1344px. У вужчій колонці документації приклад
  не стискається, а прокручується всередині блоку. */
  min-width: 1344px;
  padding: 64px 0; /* --spacing-64 */
  border-radius: 8px; /* --radius-8 */
  background: linear-gradient(180deg, #3e4f7fff 0%, #0c0f19ff 30%, #0c0f19ff 65%, #0f9549ff 94%); /* --gradient-horizontal-dark */
  text-align: center;
}
.ds-cta-block__desc {
  display: block;
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.heading.h6-20 — Archivo 20/24, вага 500 */
  font-size: 20px;
  line-height: 24px;
  font-weight: 500;
  letter-spacing: -0.5px;
  color: #ffffffff; /* --color-text-inverse */
}
.ds-cta-block__title {
  display: block;
  margin-top: 128px; /* --spacing-128 */
  max-width: 1008px;
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.heading.h1-80 — Pragati Narrow 80/72, вага 400 */
  font-size: 80px;
  line-height: 72px;
  font-weight: 400;
  letter-spacing: -1.5px;
  color: #ffffffff; /* --color-text-inverse */
}
.ds-cta-block__actions {
  display: block;
  margin-top: 40px; /* --spacing-40 */
}
```


### Blocks — Icon

Icon, text and optional button; desktop and responsive

Markup:

```html
<span class="ds-icon-block ds-icon-block--responsive"><span class="ds-icon-block__badges"><span class="ds-badge">00</span><span class="ds-badge"><span class="ds-icon ds-icon--placeholder" /></span></span><span class="ds-icon-block__main"><span class="ds-icon-block__title">Title</span><span class="ds-icon-block__text">text</span></span></span>
```

Styles:

```css
.ds-icon-block {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  box-sizing: border-box;
  gap: 24px; /* --spacing-24 */
  width: 100%;
  min-width: 1344px;
  padding: 24px; /* --spacing-24 */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-icon-block__badges {
  display: flex;
  flex: none;
  gap: 8px; /* --spacing-8 */
}
.ds-icon-block__main {
  flex: 0 1 816px;
  min-width: 0;
}
.ds-icon-block__title {
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.heading.h4-36 — Pragati Narrow 36/32, вага 400 */
  font-size: 36px;
  line-height: 32px;
  font-weight: 400;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
}
.ds-icon-block__text {
  display: block;
  margin-top: 24px; /* --spacing-24 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p3-16 — Archivo 16/20 */
  font-size: 16px;
  line-height: 20px;
  font-weight: 400;
  color: #000000ff; /* --color-text-primary */
}
.ds-icon-block__action {
  display: block;
  margin-top: 24px; /* --spacing-24 */
}
.ds-icon-block--responsive {
  flex-direction: column;
  min-width: 0;
}
.ds-icon-block--responsive .ds-icon-block__main {
  flex: none;
  margin-top: 24px; /* --spacing-24 */
}
```


### Blocks — Outcomes

Dark block holding Outcomes cards

Markup:

```html
<span class="ds-outcomes-block">
  <span class="ds-outcomes-block__title">Success stories shaped by our user experience design agency</span>
  <span class="ds-outcomes-block__cards">
    <span class="ds-outcomes-card">
      <span class="ds-outcomes-card__logo" />
      <span class="ds-outcomes-card__text">Boosted community engagement and increased traffic by 120%.</span>
      <span class="ds-outcomes-card__number">+120%</span>
      <span class="ds-outcomes-card__period">in 4 months</span>
    </span>
    <span class="ds-outcomes-card">
      <span class="ds-outcomes-card__logo" />
      <span class="ds-outcomes-card__text">Improved UX for Peel, an e-commerce analytics app, leading to $5M in funding and acquisition by Shopify.</span>
      <span class="ds-outcomes-card__number">5M</span>
      <span class="ds-outcomes-card__period">in 7 months</span>
    </span>
    <span class="ds-outcomes-card">
      <span class="ds-outcomes-card__logo" />
      <span class="ds-outcomes-card__text">Increased site conversions by 30% and average donations by 18% for one of Ukraine's largest charities.</span>
      <span class="ds-outcomes-card__number">+30%</span>
      <span class="ds-outcomes-card__period">in 4 months</span>
    </span>
  </span>
  <span class="ds-outcomes-block__actions">
    <span class="ds-btn-block">
      <span class="ds-btn-block__text">Real outcomes from complex product challenges</span>
      <span class="ds-btn-block__actions">
        <span class="ds-btn ds-btn--primary is-default">Outcomes</span>
      </span>
    </span>
  </span>
</span>
```

Styles:

```css
.ds-outcomes-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  box-sizing: border-box;
  width: 100%;
  min-width: 1344px;
  padding: 64px 0; /* --spacing-64 */
  border-radius: 8px; /* --radius-8 */
  background: linear-gradient(180deg, #3e4f7fff 0%, #0c0f19ff 30%, #0c0f19ff 65%, #0f9549ff 94%); /* --gradient-horizontal-dark */
  text-align: center;
}
.ds-outcomes-block__title {
  max-width: 1008px; /* TODO: звірити з Figma */
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.heading.h1-80 — Pragati Narrow 80/72, вага 400 */
  font-size: 80px;
  line-height: 72px;
  font-weight: 400;
  letter-spacing: -1.5px;
  color: #ffffffff; /* --color-text-inverse */
}
.ds-outcomes-block__cards {
  display: flex;
  gap: 12px; /* --spacing-12 */
  margin-top: 64px; /* TODO: звірити з Figma */
}
.ds-outcomes-block__actions {
  margin-top: 64px; /* TODO: звірити з Figma */
}
```


### Blocks — Process

One process step: image, title, text, button

Markup:

```html
<span class="ds-process-block ds-process-block--mobile"><span class="ds-process-block__media" /><span class="ds-process-block__main"><span class="ds-process-block__title">Title</span><span class="ds-process-block__text">text</span><span class="ds-process-block__action"><span class="ds-btn ds-btn--secondary is-default">Button label</span></span></span></span>
```

Styles:

```css
.ds-process-block {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  box-sizing: border-box;
  gap: 40px; /* --spacing-40 */
  width: 100%;
  min-width: 1344px;
  padding: 24px; /* --spacing-24 */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-process-block__media {
  flex: none;
  width: 312px;
  height: 175px;
  border-radius: 4px; /* --radius-4 */
  background: repeating-conic-gradient(#f4f4f4 0% 25%, #fbfbfb 0% 50%) 0 0 / 46px 46px;
}
.ds-process-block__main {
  flex: 0 1 648px;
  min-width: 0;
}
.ds-process-block__title {
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.heading.h4-36 — Pragati Narrow 36/32, вага 400 */
  font-size: 36px;
  line-height: 32px;
  font-weight: 400;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
  margin-bottom: 24px; /* --spacing-24 */
}
.ds-process-block__text {
  display: block;
  height: 80px;
  overflow: hidden;
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p3-16 — Archivo 16/20 */
  font-size: 16px;
  line-height: 20px;
  font-weight: 400;
  color: #000000ff; /* --color-text-primary */
}
.ds-process-block__action {
  display: block;
}
.ds-process-block--tab {
  width: 984px;
  min-width: 984px;
}
.ds-process-block--mobile {
  width: 736px;
  min-width: 736px;
}
.ds-process-block--mobile .ds-process-block__media {
  display: none;
}
```


### Blocks — Service

Service offering; wide and narrow layouts

Markup:

```html
<span class="ds-service-block">
  <span class="ds-service-block__main">
    <span>
      <span class="ds-service-block__title">Title</span>
      <span class="ds-service-block__subtitle">subtitle</span>
      <span class="ds-service-block__action"><span class="ds-btn ds-btn--primary is-default">Explore service</span></span>
    </span>
    <span class="ds-service-block__facts">
      <span class="ds-service-block__fact">
        <span class="ds-service-block__fact-label">Outcomes</span>
        <span class="ds-service-block__fact-text">outcomes</span>
      </span>
      <span class="ds-service-block__fact">
        <span class="ds-service-block__fact-label">Deliverables</span>
        <span class="ds-service-block__fact-text">Deliverables</span>
      </span>
    </span>
  </span>
  <span class="ds-service-block__media" />
</span>
```

Styles:

```css
.ds-service-block {
  display: flex;
  gap: 64px; /* --spacing-64 */
  box-sizing: border-box;
  width: 100%;
  min-width: 1344px;
  padding: 24px; /* --spacing-24 */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-service-block__main {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex: 0 1 592px;
  min-width: 448px;
}
.ds-service-block__title {
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.heading.h3-46 — Pragati Narrow 46/40, вага 400 */
  font-size: 46px;
  line-height: 40px;
  font-weight: 400;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
}
.ds-service-block__subtitle {
  display: block;
  margin-top: 24px; /* --spacing-24 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.heading.h6-20 — Archivo 20/24, вага 500 */
  font-size: 20px;
  line-height: 24px;
  font-weight: 500;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
}
.ds-service-block__action {
  display: block;
  margin-top: 16px; /* --spacing-16 */
}
.ds-service-block__facts {
  display: flex;
  gap: 40px; /* --spacing-40 */
}
.ds-service-block__fact {
  flex: 1 1 0;
  min-width: 0;
}
.ds-service-block__fact-label {
  display: block;
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.caption.c1-16 — Pragati Narrow 16/16, uppercase */
  font-size: 16px;
  line-height: 16px;
  font-weight: 400;
  letter-spacing: -0.5px;
  text-transform: uppercase;
  color: #697382ff; /* --color-text-secondary */
}
.ds-service-block__fact-text {
  display: block;
  margin-top: 8px; /* --spacing-8 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p2-18 — Archivo 18/20 */
  font-size: 18px;
  line-height: 20px;
  font-weight: 400;
  color: #000000ff; /* --color-text-primary */
}
.ds-service-block__media {
  flex: 1 1 0;
  min-width: 0;
  height: 360px;
  border-radius: 4px; /* --radius-4 */
  background: repeating-conic-gradient(#f4f4f4 0% 25%, #fbfbfb 0% 50%) 0 0 / 46px 46px;
}
.ds-service-block--narrow {
  flex-direction: column;
  width: 480px;
  min-width: 480px;
}
.ds-service-block--narrow .ds-service-block__main {
  flex: none;
  height: 380px;
  min-width: 0;
}
.ds-service-block--narrow .ds-service-block__facts {
  flex-direction: column;
  gap: 40px; /* --spacing-40 */
}
.ds-service-block--narrow .ds-service-block__media {
  flex: none;
  height: 243px;
}
```


### Blocks — Text

Grid of Text cards

Markup:

```html
<span class="ds-text-block">
  <span class="ds-text-block__title">Subtitle</span>
  <span class="ds-text-block__desc">Title</span>
  <span class="ds-text-block__action"><span class="ds-btn ds-btn--primary is-default">Talk to a strategist</span></span>
  <span class="ds-text-block__cards">
    <span class="ds-icon-block">
      <span class="ds-icon-block__badges">
        <span class="ds-badge">00</span>
        <span class="ds-badge"><span class="ds-icon ds-icon--placeholder" /></span>
      </span>
      <span class="ds-icon-block__main">
        <span class="ds-icon-block__title">Title</span>
        <span class="ds-icon-block__text">text</span>
      </span>
    </span>
    <span class="ds-icon-block">
      <span class="ds-icon-block__badges">
        <span class="ds-badge">00</span>
        <span class="ds-badge"><span class="ds-icon ds-icon--placeholder" /></span>
      </span>
      <span class="ds-icon-block__main">
        <span class="ds-icon-block__title">Title</span>
        <span class="ds-icon-block__text">text</span>
      </span>
    </span>
    <span class="ds-icon-block">
      <span class="ds-icon-block__badges">
        <span class="ds-badge">00</span>
        <span class="ds-badge"><span class="ds-icon ds-icon--placeholder" /></span>
      </span>
      <span class="ds-icon-block__main">
        <span class="ds-icon-block__title">Title</span>
        <span class="ds-icon-block__text">text</span>
      </span>
    </span>
    <span class="ds-icon-block">
      <span class="ds-icon-block__badges">
        <span class="ds-badge">00</span>
        <span class="ds-badge"><span class="ds-icon ds-icon--placeholder" /></span>
      </span>
      <span class="ds-icon-block__main">
        <span class="ds-icon-block__title">Title</span>
        <span class="ds-icon-block__text">text</span>
      </span>
    </span>
    <span class="ds-icon-block">
      <span class="ds-icon-block__badges">
        <span class="ds-badge">00</span>
        <span class="ds-badge"><span class="ds-icon ds-icon--placeholder" /></span>
      </span>
      <span class="ds-icon-block__main">
        <span class="ds-icon-block__title">Title</span>
        <span class="ds-icon-block__text">text</span>
      </span>
    </span>
  </span>
</span>
```

Styles:

```css
.ds-text-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  box-sizing: border-box;
  width: 100%;
  min-width: 1344px;
  padding: 48px; /* --spacing-48 */
  border-radius: 8px; /* --radius-8 */
  background: linear-gradient(180deg, #1e1e1eff 0%, #0f9549ff 45%, #c2cddeff 100%); /* --gradient-horizontal-2 */
  text-align: center;
}
.ds-text-block__title {
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.heading.h2-56 — Pragati Narrow 56/48, вага 400 */
  font-size: 56px;
  line-height: 48px;
  font-weight: 400;
  letter-spacing: -0.5px;
  color: #ffffffff; /* --color-text-inverse */
}
.ds-text-block__desc {
  display: block;
  margin-top: 24px; /* --spacing-24 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p2-18 — Archivo 18/20 */
  font-size: 18px;
  line-height: 20px;
  font-weight: 400;
  color: #ffffffff; /* --color-text-inverse */
}
.ds-text-block__action {
  display: block;
  margin-top: 24px; /* --spacing-24 */
}
.ds-text-block__cards {
  display: flex;
  flex-direction: column;
  gap: 8px; /* --spacing-8 */
  width: 100%;
  margin-top: 72px; /* --spacing-72 */
}
.ds-text-block .ds-icon-block {
  min-width: 0;
}
```


### Blocks — Menu

Full header menu panel

Markup:

```html
<span class="ds-menu"><span class="ds-menu__main"><span class="ds-menu__title">Product design for the AI era: launch new products and build interfaces.</span><span class="ds-menu__columns"><span class="ds-menu__col"><span><span class="ds-menu__caption">Programs</span><span class="ds-menu__links"><span><span class="ds-menu__link-title">Product design and redesign</span><span class="ds-menu__link-desc">Redesign a live product.</span></span><span><span class="ds-menu__link-title">AI product launch</span><span class="ds-menu__link-desc">From stalled pilot to launch.</span></span></span></span></span><span class="ds-menu__col"><span><span class="ds-menu__caption">Programs</span><span class="ds-menu__links"><span><span class="ds-menu__link-title">Product design and redesign</span><span class="ds-menu__link-desc">Redesign a live product.</span></span><span><span class="ds-menu__link-title">AI product launch</span><span class="ds-menu__link-desc">From stalled pilot to launch.</span></span></span></span></span><span class="ds-menu__col"><span><span class="ds-menu__caption">Programs</span><span class="ds-menu__links"><span><span class="ds-menu__link-title">Product design and redesign</span><span class="ds-menu__link-desc">Redesign a live product.</span></span><span><span class="ds-menu__link-title">AI product launch</span><span class="ds-menu__link-desc">From stalled pilot to launch.</span></span></span></span></span></span></span><span class="ds-menu__aside"><span class="ds-menu__aside-title">Latest articles</span><span class="ds-menu__articles"><span class="ds-card-am"><span class="ds-media" /><span class="ds-card-am__title">New Milestone: Our Financial Fund Achieves Growth and Stability</span><span class="ds-btn ds-btn--icon-outline is-default"><span class="ds-icon ds-icon--arrow-up-right" /></span></span><span class="ds-card-am"><span class="ds-media" /><span class="ds-card-am__title">New Milestone: Our Financial Fund Achieves Growth and Stability</span><span class="ds-btn ds-btn--icon-outline is-default"><span class="ds-icon ds-icon--arrow-up-right" /></span></span><span class="ds-card-am"><span class="ds-media" /><span class="ds-card-am__title">New Milestone: Our Financial Fund Achieves Growth and Stability</span><span class="ds-btn ds-btn--icon-outline is-default"><span class="ds-icon ds-icon--arrow-up-right" /></span></span></span></span></span>
```

Styles:

```css
.ds-menu {
  display: flex;
  align-items: stretch;
  box-sizing: border-box;
  gap: 32px; /* TODO: звірити з Figma */
  /* Проєктна ширина десктопної розкладки. У вужчій колонці документації
  приклад не стискається, а прокручується всередині блоку. */
  flex: none;
  width: 1342px;
  padding: 24px; /* --spacing-24 */
  border: 1px solid #d9d9d9ff; /* --border-width-1, --color-border-subtle */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-menu__main {
  display: flex;
  flex-direction: column;
  flex: 1;
  min-width: 0;
}
.ds-menu__title {
  max-width: 600px;
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.heading.h4-36 — Pragati Narrow 36/32, вага 400, трекінг -0.5 */
  font-size: 36px;
  line-height: 32px;
  font-weight: 400;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.ds-menu__columns {
  display: flex;
  gap: 32px; /* --spacing-32 */
  margin-top: auto;
  padding-top: 56px; /* --spacing-56 */
}
.ds-menu__col {
  flex: 1 1 0;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 32px; /* TODO: звірити з Figma — проміжок між групами в колонці */
}
.ds-menu__caption {
  /* block обов'язковий: на рядковому елементі margin-bottom не діє */
  display: block;
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.caption.c1-16 — Pragati Narrow 16/16, uppercase */
  font-size: 16px;
  line-height: 16px;
  font-weight: 400;
  letter-spacing: -0.5px;
  text-transform: uppercase;
  color: #697382ff; /* --color-action-inactive */
  margin-bottom: 20px; /* --spacing-20 */
}
.ds-menu__links {
  display: flex;
  flex-direction: column;
  gap: 16px; /* --spacing-16 */
}
.ds-menu__link-title {
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p2-18 — Archivo 18/20 */
  font-size: 18px;
  line-height: 20px;
  font-weight: 400;
  color: #000000ff; /* --color-action-primary */
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.ds-menu__link-desc {
  margin-top: 4px; /* --spacing-4 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.caption.c2-12 — Archivo 12/12 */
  font-size: 12px;
  line-height: 12px;
  font-weight: 400;
  color: #697382ff; /* --color-action-inactive */
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.ds-menu__aside {
  flex: 0 0 38%; /* TODO: звірити з Figma — ширина блоку статей */
  display: flex;
  flex-direction: column;
}
.ds-menu__aside-title {
  /* працює як flex-елемент, але задаємо явно — щоб не залежало від контексту */
  display: block;
  margin-bottom: 28px; /* --spacing-28 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.heading.h6-20 — Archivo 20/24, вага 500 */
  font-size: 20px;
  line-height: 24px;
  font-weight: 500;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
}
.ds-menu__articles {
  display: flex;
  flex-direction: column;
  gap: 16px; /* --spacing-16 */
}
```


### Layout — Header

Fixed top bar: logo, links, button

Markup:

```html
<span class="ds-header">
  <img class="ds-header__logo" src="/logo/lazarev-logo.svg" alt="LAZAREV.AGENCY" />
  <span class="ds-header-menu">
    <span class="ds-link is-default">Product design</span>
    <span class="ds-link is-default">Agentic websites</span>
    <span class="ds-link is-default">AI visibility</span>
    <span class="ds-link ds-link--plain is-default">Outcomes</span>
    <span class="ds-link ds-link--plain is-default">Cases studies</span>
    <span class="ds-link is-default">About us</span>
  </span>
  <span class="ds-btn ds-btn--primary is-default">Let's talk</span>
</span>
```

Styles:

```css
.ds-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px; /* --spacing-24 */
  width: 100%;
  /* 1344px = 1440 − 48 × 2, тобто хедер має ту саму ширину, що й контейнер
  сторінки. У документації колонка вужча, тому приклад прокручується. */
  min-width: 1344px;
}
.ds-header__logo {
  flex: none;
  height: 32px;
  width: auto;
}
```


### Layout — Footer

Three stacked blocks: contacts, services, legal

Markup:

```html
<span class="ds-footer"><span class="ds-footer__block ds-footer__top"><span class="ds-footer__half"><span class="ds-footer__group"><span class="ds-footer__label">Our location:</span><span class="ds-footer__address">1300 W El Camino Real #100, Mountain View, CA 94040</span></span></span><span class="ds-footer__half"><span class="ds-footer__group"><span class="ds-footer__label">Let's connect:</span><span class="ds-btn ds-btn--primary is-default">Check our latest deck</span></span></span></span><span class="ds-footer__block"><span class="ds-footer__label">Services:</span><span class="ds-footer__cols"><span class="ds-footer__col"><span class="ds-footer__link">Product design for B2C</span><span class="ds-footer__link">Human and agent experience design</span><span class="ds-footer__link">Inbound AI traffic</span><span class="ds-footer__link">Storytelling websites</span><span class="ds-footer__link">Digital transformation services</span><span class="ds-footer__link">AI chatbot development service</span></span><span class="ds-footer__col"><span class="ds-footer__link">Product design for B2B</span><span class="ds-footer__link">Continuous demand generation from SEO and AI</span><span class="ds-footer__link">Agentic website</span><span class="ds-footer__link">AEO discovery</span><span class="ds-footer__link">UI UX consulting</span><span class="ds-footer__link">UX research</span></span><span class="ds-footer__col"><span class="ds-footer__link">Web development</span><span class="ds-footer__link">AI visibility audit</span><span class="ds-footer__link">AEO strategy</span><span class="ds-footer__link">Product redesign</span><span class="ds-footer__link">Generative AI consulting</span><span class="ds-footer__link">Agentic AI services</span></span><span class="ds-footer__col"><span class="ds-footer__link">Web design</span><span class="ds-footer__link">Our approach to SEO and AEO</span><span class="ds-footer__link">Legacy migration</span><span class="ds-footer__link">B2B web design agency</span><span class="ds-footer__link">AI consulting services</span><span class="ds-footer__link">UI UX design services</span></span></span></span><span class="ds-footer__block ds-footer__bottom"><span>©2026 Lazarev | All rights reserved</span><span>Cookie Settings | Privacy Policy</span></span></span>
```

Styles:

```css
.ds-footer {
  display: flex;
  flex-direction: column;
  flex: none;
  gap: 8px; /* --spacing-8 */
  width: 1342px; /* TODO: звірити з Figma — токена ширини немає */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
}
.ds-footer__block {
  box-sizing: border-box;
  padding: 24px; /* --spacing-24 */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-footer__label {
  display: block;
  margin-bottom: 12px; /* --spacing-12 */
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.caption.c1-16 — Pragati Narrow 16/16, uppercase */
  font-size: 16px;
  line-height: 16px;
  font-weight: 400;
  letter-spacing: -0.5px;
  text-transform: uppercase;
  color: #697382ff; /* --color-text-secondary */
}
.ds-footer__top {
  display: flex;
  gap: 56px; /* --spacing-56 */
}
.ds-footer__half {
  flex: 1 1 0;
  min-width: 0;
  display: flex;
  gap: 56px; /* --spacing-56 */
}
.ds-footer__address {
  display: block;
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.heading.h2-56 — Pragati Narrow 56/48, вага 400 */
  font-size: 56px;
  line-height: 48px;
  font-weight: 400;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
}
.ds-footer__group {
  flex: 1 1 0;
  min-width: 0;
}
.ds-footer__socials {
  display: flex;
  flex-wrap: wrap;
  gap: 8px; /* --spacing-8 */
}
.ds-footer__cols {
  display: flex;
  gap: 56px; /* --spacing-56 */
}
.ds-footer__col {
  flex: 1 1 0;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 12px; /* --spacing-12 */
}
.ds-footer__link {
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p4-14 — Archivo 14/16 */
  font-size: 14px;
  line-height: 16px;
  font-weight: 500;
  color: #000000ff; /* --color-text-primary */
}
.ds-footer__bottom {
  display: flex;
  justify-content: space-between;
  gap: 24px; /* --spacing-24 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.caption.c2-12 — Archivo 12/12 */
  font-size: 12px;
  line-height: 12px;
  font-weight: 400;
  color: #000000ff; /* --color-text-primary */
}
```


### Article — Layout

Two columns: 992 body, 336 aside, gap 16

Markup:

```html
<span class="ds-article-grid"><span class="ds-article-grid__main"><span class="ds-article-grid__label">Текст статті</span></span><span class="ds-article-grid__aside"><span class="ds-article-grid__block"><span class="ds-article-grid__label">Зміст</span></span><span class="ds-article-grid__block"><span class="ds-article-grid__label">Поділитися</span></span></span></span>
```

Styles:

```css
.ds-article-grid {
  display: flex;
  align-items: flex-start;
  box-sizing: border-box;
  gap: 16px; /* --spacing-16 */
  width: 100%;
  min-width: 1344px;
}
.ds-article-grid__main {
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  /* 1344 − 16 − 336 = 992: ширина виведена, у макеті її не названо */
  flex: 1 1 auto;
  min-width: 0;
  height: 320px;
  padding: 16px; /* --spacing-16 */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-article-grid__aside {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  flex: none;
  gap: 16px; /* --spacing-16 */
  width: 336px;
}
.ds-article-grid__block {
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  height: 152px;
  padding: 16px; /* --spacing-16 */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-article-grid__label {
  display: block;
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p4-14 — Archivo 14/16 */
  font-size: 14px;
  line-height: 16px;
  font-weight: 500;
  text-align: center;
  color: #697382ff; /* --color-text-secondary */
}
.ds-article-grid--mobile {
  flex-direction: column;
  /* Mob-sm: 430 − 24 × 2 */
  width: 382px;
  min-width: 382px;
}
.ds-article-grid--mobile .ds-article-grid__main {
  width: 100%;
  height: 240px;
}
.ds-article-grid--mobile .ds-article-grid__aside {
  width: 100%;
}
.ds-article-grid--mobile .ds-article-grid__block {
  height: 96px;
}
```


### Article — Typography

h2/h3/h4, lead, body, bullet, number list — each carries its own padding

Markup:

```html
<span class="ds-art-flow"><span class="ds-art-h2">Placeholder title H2</span><span class="ds-art-b1">Placeholder body text</span><span class="ds-art-h3">Placeholder title H3</span><span class="ds-art-b1">Placeholder body text</span></span>
```

Styles:

```css
.ds-art-h1 {
  display: block;
  font-family: "Instrument Serif", Georgia, "Times New Roman", serif; /* --font-instrument */
  /* article.heading.h1-64 — Instrument Serif 64/64, вага 400 */
  font-size: 64px;
  line-height: 64px;
  font-weight: 400;
  letter-spacing: -0.5px;
}
.ds-art-lead {
  display: block;
  padding-top: 24px; /* --spacing-24 */
  padding-bottom: 8px; /* --spacing-8 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* article.lead.lead-24 — Archivo 24/32, вага 500 */
  font-size: 24px;
  line-height: 32px;
  font-weight: 500;
}
.ds-art-b1 {
  display: block;
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* article.body.b1-regular-20 — Archivo 20/28, вага 400 */
  font-size: 20px;
  line-height: 28px;
  font-weight: 400;
}
.ds-art-b1--bold {
  /* article.body.b1-bold-20 — та сама шкала, вага 700 */
  font-weight: 700;
}
.ds-art-b2 {
  display: block;
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* article.body.b2-regular-16 — Archivo 16/20, вага 400 */
  font-size: 16px;
  line-height: 20px;
  font-weight: 400;
}
.ds-art-b2--bold {
  /* article.body.b2-bold-16 — та сама шкала, вага 700 */
  font-weight: 700;
}
.ds-art-link {
  display: block;
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* article.link.link p3 — Archivo 20/28, вага 400, підкреслений */
  font-size: 20px;
  line-height: 28px;
  font-weight: 400;
  text-decoration: underline;
  color: #000000ff; /* --color-action-primary */
}
.ds-art-quote {
  display: block;
  font-family: "Instrument Serif", Georgia, "Times New Roman", serif; /* --font-instrument */
  /* article.quote.quote-40 — Instrument Serif 36/36, вага 400 */
  font-size: 36px;
  line-height: 36px;
  font-weight: 400;
}
.ds-art-h2,
.ds-art-h3,
.ds-art-h4,
.ds-art-lead,
.ds-art-b1,
.ds-art-b2,
.ds-art-link,
.ds-art-bullet,
.ds-art-num {
  max-width: 640px;
}
.ds-art-flow {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  width: 100%;
  color: #000000ff; /* --color-text-primary */
}
.ds-art-h2,
.ds-art-h3,
.ds-art-h4 {
  display: block;
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  font-weight: 400;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
}
.ds-art-h2 {
  /* font.heading.h2-56 — Pragati Narrow 56/48 */
  padding-top: 64px; /* --spacing-64 */
  padding-bottom: 12px; /* --spacing-12 */
  font-size: 56px;
  line-height: 48px;
}
.ds-art-h3 {
  /* font.heading.h3-46 — Pragati Narrow 46/40 */
  padding-top: 48px; /* --spacing-48 */
  padding-bottom: 8px; /* --spacing-8 */
  font-size: 46px;
  line-height: 40px;
}
.ds-art-h4 {
  /* font.heading.h4-36 — Pragati Narrow 36/32 */
  padding-top: 24px; /* --spacing-24 */
  padding-bottom: 8px; /* --spacing-8 */
  font-size: 36px;
  line-height: 32px;
}
.ds-art-bullet,
.ds-art-num {
  display: flex;
  /* flex-start, а не center: текст може бути в кілька рядків */
  align-items: flex-start;
  box-sizing: border-box;
  gap: 8px; /* --spacing-8 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* article.body.b1-regular-20 — Archivo 20/28, вага 400 */
  font-size: 20px;
  line-height: 28px;
  font-weight: 400;
  color: #000000ff; /* --color-text-primary */
}
.ds-art-num__index {
  flex: none;
  color: #0f9549ff; /* --color-icon-brand */
}
```


### Article — Title block

Article header: tag, date, h1, author, reading time

Markup:

```html
<span class="ds-article-title">
  <span class="ds-article-title__meta">
    <span class="ds-tag is-default">AI product design</span>
    <span class="ds-article-title__date">04 May 2026</span>
  </span>
  <span class="ds-article-title__heading">AI product roadmap 2026: how to build one with a training-loop method</span>
  <span class="ds-article-title__author">
    <span class="ds-avatar-info">
      <span class="ds-avatar ds-avatar--m" />
      <span class="ds-avatar-info__text">
        <span class="ds-avatar-info__name">Kyrylo Lazarev</span>
        <span class="ds-avatar-info__job">CEO, Lazarev agency</span>
      </span>
    </span>
    <span class="ds-article-title__time">12 min read</span>
  </span>
</span>
```

Styles:

```css
.ds-article-title {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  width: 100%;
  min-width: 992px;
}
.ds-article-title__meta {
  display: flex;
  align-items: center;
  gap: 16px; /* --spacing-16 */
}
.ds-article-title__date {
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.caption.c1-16 — Pragati Narrow 16/16, uppercase */
  font-size: 16px;
  line-height: 16px;
  font-weight: 400;
  letter-spacing: -0.5px;
  text-transform: uppercase;
  white-space: nowrap;
  color: #bbc2ccff; /* --color-text-tertiary */
}
.ds-article-title__heading {
  margin-top: 16px; /* --spacing-16 */
  font-family: "Instrument Serif", Georgia, "Times New Roman", serif; /* --font-instrument */
  /* article.heading.h1-64 — Instrument Serif 64/64, вага 400 */
  font-size: 64px;
  line-height: 64px;
  font-weight: 400;
  letter-spacing: -0.5px;
  color: #000000ff; /* --color-text-primary */
}
.ds-article-title__author {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 24px; /* --spacing-24 */
  margin-top: 40px; /* --spacing-40 */
}
.ds-article-title__time {
  flex: none;
  /* 4px знизу: час вирівняний по нижньому краю, але трохи піднятий */
  margin-bottom: 4px; /* --spacing-4 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p3-16 — Archivo 16/20 */
  font-size: 16px;
  line-height: 20px;
  font-weight: 400;
  white-space: nowrap;
  color: #000000ff; /* --color-text-primary */
}
```


### Article — Attention block

Callout with a green hairline on the left

Markup:

```html
<span class="ds-attention-block">
  <span class="ds-attention-block__line" />
  <span class="ds-attention-block__text">Insight for consumer mobile AI apps: the activation funnel, in-app agent, retention loop, and storefront belong under one roadmap owner. Teams that split them across separate workstreams ship a product where the onboarding promises things the agent can't deliver, and the storefront surfaces upgrades at the wrong moments.</span>
</span>
```

Styles:

```css
.ds-attention-block {
  display: flex;
  /* stretch (типове значення) розтягує лінію рівно на висоту тексту */
  align-items: stretch;
  box-sizing: border-box;
  gap: 16px; /* --spacing-16 */
  width: 100%;
  /* мірка тексту статті */
  max-width: 640px;
  padding: 16px; /* --spacing-16 */
}
.ds-attention-block__line {
  flex: none;
  width: 1px;
  background: #0f9549ff; /* --color-icon-brand */
}
.ds-attention-block__text {
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* article.body.b1-regular-20 — Archivo 20/28, вага 400 */
  font-size: 20px;
  line-height: 28px;
  font-weight: 400;
  color: #000000ff; /* --color-text-primary */
}
```


### Article — Quote

Serif quote with author

Markup:

```html
<span class="ds-art-quote-block">
  <span class="ds-art-quote">Don't fall into the trap of perspective taking when developing accessible UX solutions. While helpful at first glance, imagining yourself in someone else's shoes leaves too much room for bias.</span>
  <span class="ds-avatar-info">
    <span class="ds-avatar ds-avatar--m" />
    <span class="ds-avatar-info__text">
      <span class="ds-avatar-info__name">Kyrylo Lazarev</span>
      <span class="ds-avatar-info__job">CEO, Lazarev agency</span>
    </span>
  </span>
</span>
```

Styles:

```css
.ds-art-quote-block {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  box-sizing: border-box;
  gap: 32px; /* --spacing-32 */
  width: 100%;
  /* мірка тексту статті */
  max-width: 640px;
  padding-top: 32px; /* --spacing-32 */
  padding-bottom: 32px; /* --spacing-32 */
}
```


### Article — Table

Header row plus data rows, 2px apart

Markup:

```html
<span class="ds-art-table">
  <span class="ds-art-table__row ds-art-table__row--head">
    <span class="ds-art-table__cell">Column title</span>
    <span class="ds-art-table__cell">Column title</span>
    <span class="ds-art-table__cell">Column title</span>
  </span>
  <span class="ds-art-table__row ds-art-table__row--body">
    <span class="ds-art-table__cell">Column text</span>
    <span class="ds-art-table__cell">Column text</span>
    <span class="ds-art-table__cell">Column text</span>
  </span>
  <span class="ds-art-table__row ds-art-table__row--body">
    <span class="ds-art-table__cell">Column text</span>
    <span class="ds-art-table__cell">Column text</span>
    <span class="ds-art-table__cell">Column text</span>
  </span>
</span>
```

Styles:

```css
.ds-art-table {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  gap: 2px; /* --spacing-2 */
  width: 100%;
  /* таблиця йде на всю ширину блоку, без обмеження 640px */
  min-width: 992px;
  margin: 12px 0; /* --spacing-12 */
}
.ds-art-table__row {
  display: flex;
  align-items: stretch;
  box-sizing: border-box;
  /* TODO: звірити з Figma — заокруглення не названо */
  border-radius: 8px; /* --radius-8 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  color: #000000ff; /* --color-text-primary */
}
.ds-art-table__row--head {
  background: #e9e9e9ff; /* --color-gray-100 */
  /* article.body.b2-bold-16 — Archivo 16/20, вага 700 */
  font-weight: 700;
}
.ds-art-table__row--body {
  background: #f4f4f4ff; /* --color-gray-50 */
  /* article.body.b2-regular-16 — Archivo 16/20, вага 400 */
  font-weight: 400;
}
.ds-art-table__cell {
  /* fill: усі колонки ділять ширину порівну, поки не впруться в min або max */
  flex: 1 1 0;
  box-sizing: border-box;
  min-width: 120px;
  padding: 16px; /* --spacing-16 */
  font-size: 16px;
  line-height: 20px;
}
.ds-art-table__cell:first-child {
  min-width: 80px;
  max-width: 208px;
}
```


### Article — Navigation

Table of contents with reading progress

Markup:

```html
<span class="ds-toc">
  <span class="ds-toc__inner">
    <span class="ds-toc__title">Table of contents</span>
    <span class="ds-toc__progress"><span class="ds-toc__progress-bar ds-toc__progress-bar--p25" /></span>
    <span class="ds-toc__links">
      <span class="ds-toc__link is-active">Key takeaways</span>
      <span class="ds-toc__link">What chatbot design means now that the AI does the talking</span>
      <span class="ds-toc__link">5 principles of effective chatbot design for AI-native products</span>
      <span class="ds-toc__link">11 chatbot design best practices for AI-native products</span>
      <span class="ds-toc__link">6 chatbot design mistakes to avoid</span>
      <span class="ds-toc__link">How we design AI-native chatbots at Lazarev.agency</span>
      <span class="ds-toc__link">Build AI chatbots people return to</span>
    </span>
  </span>
</span>
```

Styles:

```css
.ds-toc {
  display: flex;
  box-sizing: border-box;
  width: 336px;
  padding: 32px 24px; /* --spacing-32, --spacing-24 */
  /* TODO: звірити з Figma — фон і заокруглення не названо */
  border-radius: 8px; /* --radius-8 */
  background: #ffffffff; /* --color-background-block */
}
.ds-toc__inner {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  gap: 16px; /* --spacing-16 */
  width: 240px;
  padding: 0 16px; /* --spacing-16 */
}
.ds-toc__title {
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.caption.c1-16 — Pragati Narrow 16/16, uppercase */
  font-size: 16px;
  line-height: 16px;
  font-weight: 400;
  letter-spacing: -0.5px;
  text-transform: uppercase;
  color: #697382ff; /* --color-text-secondary */
}
.ds-toc__progress {
  display: block;
  width: 100%;
  height: 1px;
  background: #cdd4deff; /* --color-gray-300 */
}
.ds-toc__progress-bar {
  display: block;
  height: 1px;
  background: #000000ff; /* --color-background-inverse */
}
.ds-toc__progress-bar--p25 {
  width: 25%;
}
.ds-toc__progress-bar--p60 {
  width: 60%;
}
.ds-toc__links {
  display: flex;
  flex-direction: column;
}
.ds-toc__link {
  position: relative;
  display: block;
  padding: 4px 0; /* --spacing-4 */
  font-family: Archivo, system-ui, -apple-system, "Segoe UI", sans-serif; /* --font-archivo */
  /* font.paragraph.p4-14 — Archivo 14/16 */
  font-size: 14px;
  line-height: 16px;
  font-weight: 500;
  color: #697382ff; /* --color-text-placeholder */
}
.ds-toc__link.is-active {
  color: #000000ff; /* --color-text-primary */
}
.ds-toc__link.is-active::before {
  content: "";
  position: absolute;
  left: -12px;
  top: 10px;
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: #000000ff; /* --color-text-primary */
}
```


### Motion

The only animation in the system: the loading spinner inside a button.

```css
@keyframes ds-btn-spin {
  to {
    transform: rotate(360deg);
  }
}
@media (prefers-reduced-motion: reduce) {
  .ds-btn--icon.is-loading::before {
    animation: none;
  }
}
```


### Shared

Rules used by more than one component.

```css
.ds-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex: none;
  box-sizing: border-box;
  width: 48px;
  height: 48px;
  border: 1px solid #d9d9d9ff; /* --border-width-1, --color-border-subtle */
  border-radius: 12px; /* --radius-12 */
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.caption.c1-16 — Pragati Narrow 16/16, uppercase */
  font-size: 16px;
  line-height: 16px;
  font-weight: 400;
  letter-spacing: -0.5px;
  text-transform: uppercase;
  color: #000000ff; /* --color-text-primary */
}
.ds-card-meta {
  display: flex;
  align-items: center;
  gap: 16px; /* --spacing-16 */
}
.ds-card-date {
  font-family: "Pragati Narrow", "Arial Narrow", Arial, sans-serif; /* --font-pragati */
  /* font.caption.c1-16 — Pragati Narrow 16/16, uppercase */
  font-size: 16px;
  line-height: 16px;
  font-weight: 400;
  letter-spacing: -0.5px;
  text-transform: uppercase;
  color: #bbc2ccff; /* --color-text-tertiary */
}
```


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
