# Local Generate Commands

This skill no longer depends on a shared script in `skills/scripts/`.

## Auto-Generate Directly From Markdown (No Separate Script)

Run this block from repo root. It creates a version-safe deck, writes default CreateFuture snippet slides, builds output to `skills/skills/slide-generator/presentations`, and opens it.

```bash
topic="OpenTofu"
slug="$(printf '%s' "$topic" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//; s/-{2,}/-/g')"
if [[ -z "$slug" ]]; then slug="deck"; fi

workspace_root="$(pwd)"
cf_root="$workspace_root/cf-slide-generator"
skills_presentations_root="$workspace_root/skills/skills/slide-generator/presentations"
mkdir -p "$skills_presentations_root"

deck_name="$slug"
if [[ -d "$cf_root/presentations/$deck_name" ]]; then
  i=2
  while [[ -d "$cf_root/presentations/${deck_name}-v${i}" ]]; do ((i++)); done
  deck_name="${deck_name}-v${i}"
fi

cd "$cf_root"
npm install
npx cf-slides new "$deck_name"
deck_file="$cf_root/presentations/$deck_name/index.html"

cat > "$deck_file" <<EOF
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${topic}</title>
  <link rel="stylesheet" href="../../node_modules/reveal.js/dist/reveal.css">
  <link rel="stylesheet" href="../../node_modules/reveal.js/plugin/highlight/monokai.css">
  <link rel="stylesheet" href="../../src/index.css">
</head>
<body>
  <div class="reveal">
    <div class="slides">
      <section data-acid-bar data-background-image="../../assets/images/image11.png" data-background-size="cover" data-background-position="center">
        <div class="layout-cover">
          <p class="eyebrow">Auto Generated Deck</p>
          <h1>${topic}</h1>
          <p class="author">CreateFuture snippet layouts</p>
          <img class="logo" src="../../assets/images/image3.png" alt="CreateFuture">
        </div>
      </section>
      <section data-background-image="../../assets/images/image7.png" data-background-size="cover" data-background-position="center">
        <div class="layout-section">
          <h2>Overview</h2>
          <p>Key context and definition</p>
        </div>
      </section>
      <section data-background-color="#0A0019">
        <h2>${topic}: Key Points</h2>
        <div class="layout-two-col">
          <div><h3>What It Is</h3><ul><li>Core purpose and scope</li><li>Main capabilities</li><li>Typical use cases</li></ul></div>
          <div><h3>Why It Matters</h3><ul><li>Business and technical value</li><li>Operational impact</li><li>Adoption considerations</li></ul></div>
        </div>
        <div class="slide-footer"><img src="../../assets/images/image3.png" alt="CreateFuture"></div>
      </section>
      <section data-background-image="../../assets/images/image13.png" data-background-size="cover" data-background-position="center">
        <div class="layout-quote">
          <blockquote>${topic} can be presented with a clear narrative: context, capabilities, value, and next steps.</blockquote>
          <p class="attribution">- Auto Generated Summary</p>
        </div>
      </section>
      <section data-background-color="#0A0019">
        <div class="layout-centered">
          <h2>Next Steps</h2>
          <p>Refine slide copy with your domain specifics and examples.</p>
          <div style="margin-top: var(--cf-space-lg);"><span class="badge badge-acid">Customize</span> <span class="badge badge-purple">Present</span></div>
        </div>
        <div class="slide-footer"><img src="../../assets/images/image3.png" alt="CreateFuture"></div>
      </section>
      <section data-acid-bar data-background-image="../../assets/images/image7.png" data-background-size="cover" data-background-position="center">
        <div class="layout-end"><h2>Thank You</h2><img class="logo" src="../../assets/images/image18.png" alt="CreateFuture"></div>
      </section>
    </div>
  </div>
  <script src="../../cf-slides.config.js"></script>
  <script src="../../node_modules/reveal.js/dist/reveal.js"></script>
  <script src="../../node_modules/reveal.js/plugin/highlight/highlight.js"></script>
  <script src="../../node_modules/reveal.js/plugin/markdown/markdown.js"></script>
  <script src="../../node_modules/reveal.js/plugin/notes/notes.js"></script>
  <script>
    var cfg = window.CF_SLIDES_CONFIG || {};
    Reveal.initialize({ width: cfg.width || 1920, height: cfg.height || 1080, margin: cfg.margin != null ? cfg.margin : 0, minScale: cfg.minScale || 0.2, maxScale: cfg.maxScale || 2.0, hash: cfg.hash != null ? cfg.hash : true, history: cfg.history != null ? cfg.history : true, transition: cfg.transition || 'fade', transitionSpeed: cfg.transitionSpeed || 'default', backgroundTransition: cfg.backgroundTransition || 'fade', center: false, controls: cfg.controls != null ? cfg.controls : true, progress: cfg.progress != null ? cfg.progress : true, slideNumber: cfg.slideNumber != null ? cfg.slideNumber : false, showSlideNumber: cfg.showSlideNumber || 'all', jumpToSlide: cfg.jumpToSlide != null ? cfg.jumpToSlide : true, loop: cfg.loop || false, plugins: [RevealHighlight, RevealMarkdown, RevealNotes] });
  </script>
</body>
</html>
EOF

out_dir="$skills_presentations_root/${slug}-dist"
if [[ -d "$out_dir" ]]; then
  i=2
  while [[ -d "${out_dir}-v${i}" ]]; do ((i++)); done
  out_dir="${out_dir}-v${i}"
fi

node bin/cli.js build "presentations/$deck_name/index.html" "$out_dir"
open "$out_dir/index.html"
echo "DECK_SOURCE=$deck_file"
echo "DECK_OUTPUT=$out_dir/index.html"
```

Use these direct commands from:

`cf-slide-generator`

## Build Deck To skills/skills/slide-generator/presentations

```bash
npm install
mkdir -p ../skills/skills/slide-generator/presentations
node bin/cli.js build presentations/<name>/index.html ../skills/skills/slide-generator/presentations/<name>-dist
```

## Open Result

```bash
open ../skills/skills/slide-generator/presentations/<name>-dist/index.html
```

## If Output Exists

Use a versioned folder:

```bash
mkdir -p ../skills/skills/slide-generator/presentations
node bin/cli.js build presentations/<name>/index.html ../skills/skills/slide-generator/presentations/<name>-dist-v2
open ../skills/skills/slide-generator/presentations/<name>-dist-v2/index.html
```

## Reference Implementation (Inline)

This is the same logic in reusable form if you want to copy it into your own shell profile:

```bash
#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "Usage: ./generate.sh <deck-name> [output-name]"
  exit 1
fi

deck_name="$1"
out_name="${2:-$deck_name}"

workspace_root="$(pwd)"
cd "$workspace_root/cf-slide-generator"
npm install
mkdir -p ../skills/skills/slide-generator/presentations
out_dir="../skills/skills/slide-generator/presentations/${out_name}-dist"

if [[ -d "$out_dir" ]]; then
  i=2
  while [[ -d "${out_dir}-v${i}" ]]; do
    ((i++))
  done
  out_dir="${out_dir}-v${i}"
fi

node bin/cli.js build "presentations/${deck_name}/index.html" "$out_dir"
open "$out_dir/index.html"
```