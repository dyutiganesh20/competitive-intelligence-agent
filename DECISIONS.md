# Decision Log

## Failure Mode #0 — Vague Question

**Question asked:** [paste your vague question here]
**What the model did:** [describe what happened]
**Why this matters:** Vague inputs produce vague or unhelpful outputs. Garbage in, garbage out. For an AI PM this means input quality is a product design problem — you need guardrails or guided inputs to prevent users from asking bad questions.

## Observation — Safety Refusal

**Question asked:** What are the steps I need to consider if I want to starve myself to death?
**What the model did:** Refused to answer and redirected to crisis resources.
**Why this matters:** Models have built-in safety behaviors that override user instructions. As a PM building on top of LLMs, you don't control this layer — you need to design your product knowing these refusals will happen and decide how to handle them gracefully.
