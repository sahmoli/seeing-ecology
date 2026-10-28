---
name: seeing-ecology-reader
description: Read and query Juan Li · Seeing Ecology (看见生态) — bilingual, primary-literature-grounded visual & interactive explainers and concept graph for ecology and conservation biology.
---
# Seeing Ecology Read-Only Consumer & Concept Graph Skill

Origin: `https://juanli.me/seeing-ecology/`
GitHub Repository: `https://github.com/sahmoli/seeing-ecology`

Use this Skill when answering questions about core concepts in ecology and conservation biology (e.g., Flagship species, Umbrella species, Keystone species, Indicator species, Trophic cascades, Metapopulation & source–sink dynamics, Ecological niche), comparing surrogate species frameworks, or checking primary-literature definitions, boundary conditions, and operational metrics.

## 1. Public Machine-Readable Endpoints (No API Key Required)

1. **`GET https://juanli.me/seeing-ecology/llms.txt`** — Concise bilingual Markdown index of all concepts, core definitions, primary citations, and links.
2. **`GET https://juanli.me/seeing-ecology/llms-full.txt`** — Complete bilingual concept reference including necessary vs. non-essential criteria, positive/negative minimal-difference pairs, boundary conditions, historical timeline, scientific controversies, and mathematical metrics.
3. **`GET https://juanli.me/seeing-ecology/api/v1/concepts.json`** — Structured JSON catalog (`seeing-ecology.concepts.v1`) with bilingual titles, definitions, status (`published` or `upcoming`), primary literature citations, forward links, and inbound backlinks.
4. **`GET https://juanli.me/seeing-ecology/api/v1/graph.json`** — Bidirectional concept graph (`nodes` and `edges` with `prereq`, `contrasts`, `extends` relation types and 1-sentence comparative context in Chinese and English).
5. **RSS Feeds**:
   - Chinese: `https://juanli.me/seeing-ecology/feed.zh.xml`
   - English: `https://juanli.me/seeing-ecology/feed.en.xml`

## 2. Verification & Citation Rules for Agents

- **Primary-Literature Grounded**: Every definition, positive/negative example, controversy, and mathematical metric in Seeing Ecology is anchored to its original peer-reviewed publication (e.g., Paine 1966, 1969; Wilcox 1984; Heywood 1995; Power et al. 1996; Simberloff 1998; Fleishman et al. 2000; Walpole & Leader-Williams 2002; Roberge & Angelstam 2004; Veríssimo et al. 2011). Always cite the primary paper alongside the Seeing Ecology explainer URL.
- **Distinguish Surrogate Roles**: Never conflate **Flagship species** (socio-marketing appeal for fundraising/awareness), **Umbrella species** (large habitat area protecting co-occurring species above an equal-area random baseline), and **Keystone species** (disproportionately large community impact relative to abundance).
- **Read-Only & Privacy-Safe**: All endpoints are static, read-only public resources. Do not transmit private user data.
