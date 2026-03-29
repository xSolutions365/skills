# React Motion Usage Research Summary

As of March 29, 2026, the strongest recommendation for AI-generated short explainer videos is not to use `Motion` in isolation. The better setup is to use `Motion` for scene-level animation inside a `Remotion` video workflow. That combination fits the actual job: create short React-based videos that explain an article, move through architecture diagrams, highlight stages in an AI SDLC cycle, and render cleanly as a finished video artifact.

## Decision Summary

For this use case, `Motion` should be the animation layer and `Remotion` should be the video-production layer.

`Motion` is the right choice for:

- animating diagram nodes and edges
- sequencing phase-by-phase state changes
- revealing labels and captions
- tracing system flow
- coordinating transitions within React components

`Remotion` is the right choice for:

- timeline-based video composition
- frame-accurate sequencing
- scene duration control
- transitions between scenes
- rendering to video outputs
- assembling reusable explainer-video structures

If the objective is "use a skill that helps AI produce these videos well," the most effective practical stack is:

- `remotion-best-practices`
- `motion`

That pair covers both the video system and the animation grammar.

## What Each Relevant Skill Adds

### 1. `remotion-best-practices` by `remotion-dev/skills`

This is the strongest primary skill for the overall workflow. It is directly aligned with building videos in React and has by far the strongest current adoption signal among the options reviewed.

Relevant strengths:

- Covers animations, transitions, sequencing, text animation, charts, maps, assets, audio, subtitles, and composition management.
- Includes patterns for dynamic metadata, duration calculation, and parameterized compositions.
- Gives the AI a video-native structure instead of treating the work like a normal web UI.

Current signals:

- Weekly installs: `185.7K`
- GitHub stars: `2.4K`
- First seen on `skills.sh`: `Jan 19, 2026`

Install:

```bash
npx skills add https://github.com/remotion-dev/skills --skill remotion-best-practices
```

### 2. `motion` by `hairyf/skills`

This is the best direct `Motion` skill. It is the most relevant skill for the actual animation primitives you care about: variants, layout transitions, scroll/state choreography, `AnimatePresence`, `LayoutGroup`, `useAnimate`, `useScroll`, SVG path animation, and reduced-motion handling.

Relevant strengths:

- Gives the AI precise `Motion` concepts rather than generic animation advice.
- Useful for diagram walkthroughs, stage emphasis, reveal sequences, and flow tracing.
- Well suited to component-level animation patterns inside a Remotion composition.

Current signals:

- Weekly installs: `619`
- GitHub stars: `7`
- First seen on `skills.sh`: `Jan 29, 2026`

Install:

```bash
npx skills add https://github.com/hairyf/skills --skill motion
```

### 3. `ui-animation` by `mblode/agent-skills`

This is a strong companion skill, not a primary one. It is useful when the AI needs better judgment around pacing, easing, motion restraint, accessibility, and performance.

Relevant strengths:

- Covers Framer Motion and spring animation guidance.
- Pushes the AI toward transform/opacity-only motion.
- Enforces `prefers-reduced-motion` and avoids common animation anti-patterns.
- Helps prevent explainer visuals from becoming noisy or overly "UI demo" oriented.

Current signals:

- The page shows a strong adoption profile and broad install base across editors.
- It is materially more adopted than the dedicated `motion` skill, but less directly targeted to your exact use case.

Install:

```bash
npx skills add https://github.com/mblode/agent-skills --skill ui-animation
```

### 4. `create-remotion-geist` by `vercel-labs/skill-remotion-geist`

This is a style-system companion for Remotion. It is useful when you want article explainer videos to look polished, technical, dark, and Vercel-like rather than generic.

Relevant strengths:

- Strong visual system for clean technical explainers.
- Includes scene patterns, typography, color guidance, and spring-based motion utilities.
- Best when the desired outcome is "sharp technical product explainer" rather than "generic diagram animation."

Current signals:

- Weekly installs: `244`
- GitHub stars: `20`
- First seen on `skills.sh`: `Jan 29, 2026`

Install:

```bash
npx skills add https://github.com/vercel-labs/skill-remotion-geist --skill create-remotion-geist
```

### 5. `modern-short-video` by `imaimai17468/modern-short-video-skills`

This is a workflow-oriented companion skill. It is useful when you want the AI to think in terms of short scene stacks, short runtimes, CTA structure, and transition pacing.

Relevant strengths:

- Explicitly extends `remotion-best-practices`.
- Gives the AI a scene-by-scene short-video structure.
- Encourages replacing static screenshots with richer expressions such as charts, maps, and text animation.

Current signals:

- Weekly installs: `220`
- GitHub stars: `6`
- First seen on `skills.sh`: `Jan 27, 2026`

Important limitation:

This skill is oriented toward product-launch and feature videos. It is still useful, but some of its assumptions do not map perfectly to article explainers about system diagrams or lifecycle models.

Install:

```bash
npx skills add https://github.com/imaimai17468/modern-short-video-skills --skill modern-short-video
```

## Secondary Skills Reviewed

These are useful as support skills, but they are not the core recommendation for your video workflow.

### `web-design-guidelines` by `vercel-labs/agent-skills`

Useful for review and UI quality checks, especially accessibility and interface discipline.

- Weekly installs: `209.0K`
- GitHub stars for the parent repo: `24.0K`

This is better for auditing or refining video-related React UI than for generating the video system itself.

### `vercel-react-best-practices` by `vercel-labs/agent-skills`

Useful for React performance, bundle control, and avoiding poor component patterns in animation-heavy code.

- Weekly installs: `259.5K`
- GitHub stars for the parent repo: `24.0K`

This is helpful if the generated video project becomes large or interactive, but it is still secondary to the Remotion and Motion pair.

### `ui-skills` by `ibelick/ui-skills`

Useful as an opinionated frontend constraint set. It explicitly says to use `motion/react` when JavaScript animation is required.

- Weekly installs: `22`
- GitHub stars: `1.1K`

It is more of a UI-quality opinion pack than a dedicated explainer-video workflow.

## Final Recommendations

### Best overall combination

Use this when the goal is article explainers, diagram walkthroughs, or AI SDLC videos:

- `remotion-best-practices`
- `motion`

Why this is the default:

- `Remotion` gives the AI a video-native mental model.
- `Motion` gives the AI better scene choreography.
- Together they cover both composition and animation.

### Best polished technical-brand combination

Use this when the video should look highly polished and intentionally designed:

- `remotion-best-practices`
- `motion`
- `create-remotion-geist`

This is the best fit for architecture explainers, platform demos, and technical article visuals that should feel product-grade.

### Best short-form content combination

Use this when the output should be fast-moving, highly structured, and easy for AI to storyboard:

- `remotion-best-practices`
- `motion`
- `modern-short-video`

Use this with caution for article explainers. The structure is useful, but some of the product-video assumptions may need to be overridden.

### Best review and cleanup combination

Use this when the AI is already generating videos, but you want better discipline in the result:

- `remotion-best-practices`
- `motion`
- `ui-animation`

This helps enforce pacing, restraint, accessibility, and performance.

## What To Install First

If only one skill should be installed, install:

- `remotion-best-practices`

If two skills should be installed, install:

- `remotion-best-practices`
- `motion`

If three skills should be installed for the strongest practical setup, install:

- `remotion-best-practices`
- `motion`
- `create-remotion-geist`

## Recommendation For Your Stated Use Case

For short videos that demonstrate something from an article, such as AI SDLC phases or system-flow diagrams, the final recommendation is:

- Use `Remotion` to structure the video into scenes.
- Use `Motion` inside those scenes to animate stage changes, highlights, path tracing, and diagram emphasis.
- Add `create-remotion-geist` if you want the visuals to feel polished and technical.
- Add `ui-animation` if you want the AI to be more disciplined about pacing and motion quality.

The key architectural decision is that `Motion` should not be treated as the whole solution. It is the animation engine inside the scene. `Remotion` is what turns those scenes into a real video workflow.

## Sources

- `remotion-best-practices`: https://skills.sh/remotion-dev/skills/remotion-best-practices
- `motion`: https://skills.sh/hairyf/skills/motion
- `ui-animation`: https://skills.sh/mblode/agent-skills/ui-animation
- `create-remotion-geist`: https://skills.sh/vercel-labs/skill-remotion-geist/create-remotion-geist
- `modern-short-video`: https://skills.sh/imaimai17468/modern-short-video-skills/modern-short-video
- `web-design-guidelines`: https://skills.sh/vercel-labs/agent-skills/web-design-guidelines
- `vercel-react-best-practices`: https://skills.sh/vercel-labs/agent-skills/vercel-react-best-practices
- `ui-skills`: https://skills.sh/ibelick/ui-skills/ui-skills
- Remotion GitHub repository: https://github.com/remotion-dev/remotion
