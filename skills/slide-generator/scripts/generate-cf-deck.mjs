#!/usr/bin/env node

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, "..");
const snippetsDir = path.join(rootDir, "snippets");
const presentationsDir = path.join(rootDir, "presentations");

function parseArgs(argv) {
  const out = {};
  for (let i = 2; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg.startsWith("--")) {
      const key = arg.slice(2);
      const value = argv[i + 1] && !argv[i + 1].startsWith("--") ? argv[++i] : true;
      out[key] = value;
    }
  }
  return out;
}

function slugify(input) {
  return String(input || "deck")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .replace(/-{2,}/g, "-") || "deck";
}

function sentenceSplit(text) {
  return text
    .replace(/\s+/g, " ")
    .split(/(?<=[.!?])\s+/)
    .map((s) => s.trim())
    .filter(Boolean);
}

function escapeHtml(text) {
  return String(text)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/\"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function replaceFirstTag(html, tag, value) {
  const re = new RegExp(`<${tag}>[\\s\\S]*?<\\/${tag}>`);
  return html.replace(re, `<${tag}>${value}</${tag}>`);
}

function replaceFirstNthTag(html, tag, n, value) {
  let idx = 0;
  return html.replace(new RegExp(`<${tag}>[\\s\\S]*?<\\/${tag}>`, "g"), (m) => {
    idx += 1;
    if (idx === n) {
      return `<${tag}>${value}</${tag}>`;
    }
    return m;
  });
}

function buildList(items) {
  return items.map((item) => `<li>${escapeHtml(item)}</li>`).join("\n        ");
}

function stripLogoImage(html) {
  return html.replace(/\s*<img\s+class="logo"[^>]*>\s*/g, "\n");
}

function ensureDir(dirPath) {
  fs.mkdirSync(dirPath, { recursive: true });
}

function loadSnippet(name) {
  return fs.readFileSync(path.join(snippetsDir, `${name}.html`), "utf8");
}

function assembleDeck({ title, rawContent }) {
  const lines = rawContent
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);

  const bodyText = lines.join(" ");
  const sentences = sentenceSplit(bodyText);
  const summary = lines[0] || sentences[0] || `${title} overview`;

  // Quote: first line trimmed to 12 words so it doesn't overflow the slide
  const firstLine = lines[0] || sentences[0] || `${title} helps teams move from learning to outcomes.`;
  const quoteWords = firstLine.replace(/[.!?]+$/, "").split(/\s+/);
  const quote = quoteWords.length > 12 ? quoteWords.slice(0, 12).join(" ") + "…" : quoteWords.join(" ");

  // Use lines directly as bullets when content is line-based, otherwise use sentences
  const bullets = (lines.length >= 3 ? lines : sentences.map((s) => s.replace(/[.!?]+$/, ""))).filter(Boolean);

  let cover = loadSnippet("cover");
  cover = cover.replace(/<p\s+class="eyebrow">[\s\S]*?<\/p>/, "");
  cover = cover.replace(/<p\s+class="author">[\s\S]*?<\/p>/, "");
  cover = replaceFirstTag(cover, "h1", escapeHtml(title));
  cover = stripLogoImage(cover);

  let section = loadSnippet("section-divider");
  section = replaceFirstTag(section, "h2", "Overview");
  section = replaceFirstTag(section, "p", escapeHtml(summary));

  function topicName(bullet) {
    const m = bullet.match(/^(.+?)\s+[—–]\s+/);
    return m ? m[1].trim() : bullet.split(/\s+/).slice(0, 3).join(" ");
  }

  const contentSlides = [];
  for (let i = 0; i < bullets.length; i += 6) {
    const chunk = bullets.slice(i, i + 6);
    const leftBullets = chunk.slice(0, 3);
    const rightBullets = chunk.slice(3);

    const first = topicName(chunk[0]);
    const last = topicName(chunk[chunk.length - 1]);
    const slideLabel = first === last ? escapeHtml(first) : `${escapeHtml(first)} — ${escapeHtml(last)}`;

    let twoCol = loadSnippet("two-col");
    twoCol = twoCol.replace(/<p>Content for the (left|right) side\.<\/p>\s*/g, "");
    twoCol = replaceFirstTag(twoCol, "h2", slideLabel);
    twoCol = replaceFirstNthTag(twoCol, "h3", 1, "Key Concepts");
    twoCol = replaceFirstNthTag(twoCol, "h3", 2, "Deep Dive");
    twoCol = replaceFirstNthTag(twoCol, "ul", 1, `\n        ${buildList(leftBullets)}\n      `);

    if (rightBullets.length > 0) {
      twoCol = replaceFirstNthTag(twoCol, "ul", 2, `\n        ${buildList(rightBullets)}\n      `);
    } else {
      // Remove the right column entirely when there's nothing to show
      twoCol = twoCol.replace(/<div>\s*<h3>Deep Dive<\/h3>\s*<ul>[\s\S]*?<\/ul>\s*<\/div>/, "");
    }

    contentSlides.push(twoCol);
  }

  let quoteSlide = loadSnippet("quote");
  quoteSlide = quoteSlide.replace(
    /<blockquote>[\s\S]*?<\/blockquote>/,
    `<blockquote>\n      ${escapeHtml(quote)}\n    </blockquote>`
  );
  quoteSlide = quoteSlide.replace(/<p\s+class="attribution">[\s\S]*?<\/p>/, "");

  let end = loadSnippet("end");
  end = replaceFirstTag(end, "h2", "Thank You");
  end = stripLogoImage(end);

  return [cover, section, ...contentSlides, quoteSlide, end].join("\n\n");
}

function wrapHtml(title, sections) {
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${escapeHtml(title)}</title>
  <style>
    :root {
      --cf-bg: #0a0019;
      --cf-text: #f5f1ff;
      --cf-muted: #d6cdee;
      --cf-acid: #b5ff2f;
      --cf-card: rgba(255,255,255,0.03);
      --cf-line: rgba(255,255,255,0.14);
    }

    * { box-sizing: border-box; }

    html, body {
      width: 100%;
      height: 100%;
      margin: 0;
      padding: 0;
      overflow: hidden;
      color: var(--cf-text);
      background: #05000e;
      font-family: "Avenir Next", "Segoe UI", sans-serif;
    }

    .deck {
      width: 100%;
      height: 100%;
      display: flex;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      scroll-behavior: smooth;
    }

    .deck::-webkit-scrollbar { display: none; }

    section {
      min-width: 100vw;
      height: 100vh;
      padding: clamp(1rem, 2.6vw, 2.5rem);
      scroll-snap-align: start;
      position: relative;
      background-color: var(--cf-bg);
      background-size: cover;
      background-position: center;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    section.has-acid::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 10px;
      background: var(--cf-acid);
    }

    h1, h2, h3 {
      margin: 0 0 0.65rem;
      line-height: 1.14;
      color: var(--cf-text);
    }

    h1 { font-size: clamp(2rem, 5.8vw, 4.8rem); }
    h2 { font-size: clamp(1.6rem, 3.8vw, 3rem); }
    h3 { font-size: clamp(1.05rem, 2vw, 1.45rem); }

    p, li, blockquote {
      color: var(--cf-muted);
      line-height: 1.55;
      font-size: clamp(1rem, 1.8vw, 1.3rem);
      margin: 0;
    }

    ul { margin-top: 0.55rem; }

    .layout-cover,
    .layout-section,
    .layout-end,
    .layout-quote {
      margin: auto 0;
      max-width: 56rem;
    }

    .layout-cover .eyebrow,
    .layout-section p {
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--cf-acid);
      font-size: 0.95rem;
      margin-bottom: 0.6rem;
    }

    .layout-cover .author {
      color: var(--cf-muted);
      margin-top: 0.5rem;
      text-transform: none;
      letter-spacing: 0;
      font-size: 1rem;
    }

    .layout-cover .logo,
    .layout-end .logo {
      margin-top: 1rem;
      max-width: 280px;
      width: 45%;
      min-width: 160px;
    }

    .layout-two-col,
    .layout-two-col-wide-left,
    .layout-two-col-wide-right {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.2rem;
      margin-top: 0.8rem;
    }

    .layout-two-col-wide-left { grid-template-columns: 1.5fr 1fr; }
    .layout-two-col-wide-right { grid-template-columns: 1fr 1.5fr; }

    .layout-two-col > div,
    .layout-two-col-wide-left > div,
    .layout-two-col-wide-right > div {
      border: 1px solid var(--cf-line);
      border-radius: 14px;
      padding: 1rem;
      background: var(--cf-card);
    }

    .layout-quote blockquote {
      font-size: clamp(1.25rem, 3.1vw, 2.25rem);
      line-height: 1.35;
      color: #fff;
      margin-bottom: 0.8rem;
      max-width: 34ch;
    }

    .layout-quote .attribution {
      color: var(--cf-muted);
    }

    .slide-footer {
      margin-top: auto;
      border-top: 1px solid var(--cf-line);
      padding-top: 0.65rem;
      display: flex;
      justify-content: flex-end;
    }

    .slide-footer img {
      width: 120px;
      height: auto;
      opacity: 0.9;
    }

    .nav-controls {
      position: fixed;
      right: 1rem;
      bottom: 1rem;
      z-index: 30;
      display: flex;
      gap: 0.5rem;
    }

    .nav-btn {
      border: 1px solid var(--cf-line);
      border-radius: 10px;
      padding: 0.5rem 0.8rem;
      background: rgba(10, 0, 25, 0.9);
      color: var(--cf-text);
      cursor: pointer;
    }

    .nav-btn:hover { background: rgba(33, 10, 50, 0.95); }

    @media (max-width: 900px) {
      .layout-two-col,
      .layout-two-col-wide-left,
      .layout-two-col-wide-right {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <main class="deck" id="deck">
${sections}
  </main>

  <div class="nav-controls" aria-label="Slide controls">
    <button type="button" class="nav-btn" id="prevBtn">Previous</button>
    <button type="button" class="nav-btn" id="nextBtn">Next</button>
  </div>

  <script>
    (function () {
      const deck = document.getElementById("deck");
      const slides = Array.from(deck.querySelectorAll("section"));

      slides.forEach((slide) => {
        if (slide.dataset.backgroundImage) {
          slide.style.backgroundImage = "url(" + slide.dataset.backgroundImage + ")";
        }
        if (slide.hasAttribute("data-acid-bar")) {
          slide.classList.add("has-acid");
        }
      });

      const width = function () { return window.innerWidth; };
      const clamp = function (value, min, max) { return Math.min(max, Math.max(min, value)); };
      const index = function () { return Math.round(deck.scrollLeft / width()); };

      function go(step) {
        const next = clamp(index() + step, 0, slides.length - 1);
        deck.scrollTo({ left: next * width(), behavior: "smooth" });
      }

      document.getElementById("nextBtn").addEventListener("click", function () { go(1); });
      document.getElementById("prevBtn").addEventListener("click", function () { go(-1); });

      document.addEventListener("keydown", function (event) {
        if (event.key === "ArrowRight" || event.key === "PageDown" || event.key === " ") {
          event.preventDefault();
          go(1);
        }
        if (event.key === "ArrowLeft" || event.key === "PageUp") {
          event.preventDefault();
          go(-1);
        }
      });
    })();
  </script>
</body>
</html>`;
}

function main() {
  const examplesDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../examples");
  if (fs.existsSync(examplesDir)) {
    fs.readdirSync(examplesDir).filter(f => f.endsWith(".md")).forEach(f => fs.rmSync(path.join(examplesDir, f)));
  }

  const args = parseArgs(process.argv);
  const title = String(args.title || args.topic || "Presentation").trim();
  const slug = slugify(args.name || title);

  let rawContent = "";
  if (args["content-file"]) {
    rawContent = fs.readFileSync(path.resolve(String(args["content-file"])), "utf8");
  } else if (args.content) {
    rawContent = String(args.content);
  } else {
    rawContent = title;
  }

  const words = rawContent.trim().split(/\s+/).filter(Boolean);
  const bulletCount = (rawContent.match(/^(?:[-*+]|\d+[.)])\s/gm) || []).length;
  if (words.length < 30 && bulletCount < 5) {
    console.error(
      "INPUT_TOO_SHORT: Provide at least 5 bullet points or ~100 words.\n" +
      "Share one of:\n" +
      "  - 5-10 key points you want covered\n" +
      "  - A short paragraph (~100+ words) on the topic\n" +
      "  - Your audience + goal + duration (e.g. 'senior devs, deep dive, 20 minutes')"
    );
    process.exit(1);
  }

  ensureDir(presentationsDir);

  const outputBase = path.join(presentationsDir, slug);
  const outputDir = outputBase;
  ensureDir(outputDir);

  const sections = assembleDeck({ title, rawContent });
  const html = wrapHtml(title, sections);
  const outFile = path.join(outputDir, "index.html");
  fs.writeFileSync(outFile, html, "utf8");

  console.log(`OUTPUT_HTML=${outFile}`);
}

main();
